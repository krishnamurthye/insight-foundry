from config import CHUNK_SIZE, CHUNK_OVERLAP
from langchain.text_splitter import RecursiveCharacterTextSplitter

from utils.chains import build_chain_for_language
from utils.extract import extract_json_objects


def summarize_code(code, language):
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_text(code)
    chain = build_chain_for_language(language)
    results = []

    for i, chunk in enumerate(chunks):
        try:
            print(f"\nSummarizing chunk {i + 1}/{len(chunks)}...")
            result = chain.invoke({"code": chunk})
            results.append(result)
        except Exception as e:
            print(f"[Error] Failed summarizing chunk: {e}")

    return extract_json_objects(results)