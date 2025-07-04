from langchain.prompts import PromptTemplate

from config import EXTENSION_LANGUAGE_MAP


def get_code_analysis_prompt(language: str):
    return PromptTemplate(
        input_variables=["code"],
        template=f"""
You are a code analysis assistant. Analyze the following {language} code and return ONLY a valid JSON object with the following structure.
Do NOT include any additional commentary or formatting like markdown.

Expected JSON format:
{{{{
  "file_summary": "One-line summary of what the file does (include both technical and business-level insights if possible).",
  "methods": [
    {{{{
      "method_name": "methodName",
      "signature": "full method signature",
      "description": "What this method does (only key methods, not every method).",
      "complexity": "cyclomatic complexity estimate (optional)"
    }}}}
  ],
  "mocks": ["list any mocks used"],
  "assertions": ["list any assertions used"],
  "noteworthy": [
    "Mention boilerplate code",
    "Code quality issues (long methods, duplication, etc.)",
    "Spelling mistakes in identifiers or comments",
    "Security concerns (e.g., use of weak encryption, SQL injection, hardcoded secrets)",
    "Performance bottlenecks",
    "Refactoring suggestions (e.g., simplify conditionals, better naming)"
  ]
}}}}

Code:
{{{{code}}}}
"""
    )

