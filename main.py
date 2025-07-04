import sys
import os

from config import LOCAL_REPO_PATH, EXTENSION_LANGUAGE_MAP, MODEL_NAME, USE_OPENAI
from utils.file_utils import get_code_files, infer_language_from_path, write_json
from utils.complexity import get_complexity_metrics
from runners.summarize_code import summarize_code
from runners.summarize_project import summarize_project
from utils.git_utils import clone_repo
from utils.ollama_util import stop_ollama_model

def main():
    repo_url = sys.argv[1] if len(sys.argv) > 1 else None
    if repo_url:
        clone_repo(repo_url, LOCAL_REPO_PATH)

    os.makedirs("output", exist_ok=True)

    print(f"Scanning: {LOCAL_REPO_PATH}")
    files = get_code_files(LOCAL_REPO_PATH, EXTENSION_LANGUAGE_MAP.keys())
    results = []

    for path in files:
        print(f"\nProcessing: {path}")
        try:
            with open(path, encoding="utf-8") as f:
                code = f.read()
        except Exception as e:
            print(f"Read error: {e}")
            continue

        if not code.strip():
            print(f"Skipping empty file: {path}")
            continue

        language = infer_language_from_path(path)
        if not language:
            print(f"Skipping unsupported language: {path}")
            continue

        summaries = summarize_code(code, language, path)
        results.append(summaries)

    write_json({"project": "SakilaProject", "files": results}, "output/sakila_summary.json")

    print("\nGenerating project-level summary...")
    project_summary = summarize_project([r["description"] for r in results])
    print(f"\nProject Summary:\n{project_summary}")

    write_json({
        "project": "SakilaProject",
        "summary": project_summary,
        "files": results
    }, "output/sakila_project_summary.json")

    if not USE_OPENAI:
        stop_ollama_model(MODEL_NAME)

if __name__ == "__main__":
    main()
