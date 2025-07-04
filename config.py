import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # put your key in a `.env` file
#LOCAL_REPO_PATH = "/home//workspace/assesment/SakilaProject"

LOCAL_REPO_PATH = os.environ.get("REPO_PATH", "./repo")
USE_OPENAI = False
MODEL_NAME = "gpt-3.5-turbo" if USE_OPENAI else "codellama"
MAX_TOKENS = 600

EXTENSION_LANGUAGE_MAP = {
    ".py": "Python",
    ".java": "Java",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".go": "Go",
    ".rb": "Ruby",
    ".cpp": "C++",
    ".cs": "C#",
    ".php": "PHP",
    ".rs": "Rust",
    ".kt": "Kotlin",
    ".html": "Html"
}

CHUNK_SIZE = 1024
CHUNK_OVERLAP = 100
