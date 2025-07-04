import json
import os

from config import EXTENSION_LANGUAGE_MAP


def get_code_files(base_path, extensions):
    return [
        os.path.join(root, f)
        for root, _, files in os.walk(base_path)
        for f in files if any(f.endswith(ext) for ext in extensions)
    ]

def write_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def infer_language_from_path(file_path):
    for ext, lang in EXTENSION_LANGUAGE_MAP.items():
        if file_path.endswith(ext):
            return lang
    return "Unknown"