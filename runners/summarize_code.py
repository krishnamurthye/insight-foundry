from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP
from utils.chains import build_chain_for_language
from utils.complexity import get_complexity_metrics
from utils.extract import extract_json_objects
import re
import json


def deduplicate_summary(summary):
    lines = re.split(r'[.。!?]\s*', summary)
    seen = set()
    unique_lines = [line for line in lines if line and not (line in seen or seen.add(line))]
    return '. '.join(unique_lines).strip()


def deduplicate_methods(methods):
    seen = set()
    deduped = []
    for method in methods:
        key = (method.get("method_name"), method.get("signature"))
        if key not in seen:
            seen.add(key)
            deduped.append(method)
    return deduped


def summarize_code(code, language, path):
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_text(code)
    chain = build_chain_for_language(language)
    results = []

    for i, chunk in enumerate(chunks):
        try:
            print(f"\nSummarizing chunk {i + 1}/{len(chunks)}...")
            print(f"Chunk preview:\n{chunk[:500]}...")

            result = chain.invoke({"code": chunk})
            print(f"\nRaw LLM Output:\n{result}\n")
            results.append(result)
        except Exception as e:
            print(f"[Error] Failed summarizing chunk {i + 1}: {e}")

    json_blocks = extract_json_objects(results)
    print(f"\nAfter extract_json_objects Output:\n{json_blocks}\n")

    merged = {"file_summary": "", "methods": [], "mocks": [], "assertions": [], "noteworthy": []}
    complexity = []

    try:
        if json_blocks:
            merged = {
                "file_summary": deduplicate_summary(" ".join(
                    str(j.get("file_summary", "")) for j in json_blocks).strip()),
                "methods": deduplicate_methods(sum((j.get("methods", []) for j in json_blocks), [])),
                "mocks": sum((j.get("mocks", []) for j in json_blocks), []),
                "assertions": sum((j.get("assertions", []) for j in json_blocks), []),
                "noteworthy": sum((j.get("noteworthy", []) for j in json_blocks), []),
            }
            print(f"\nMerged Summary: {merged}")

        complexity = get_complexity_metrics(code, language)
    except Exception as e:
        print(f"[Error] Failed while merging or calculating complexity: {e}")

    return {"file": path, "description": merged, "complexity": complexity}
