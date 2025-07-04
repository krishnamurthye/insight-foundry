import json

from prompts.project_summary_prompt import project_summary_prompt
from utils.chains import build_chain


def summarize_project(descriptions):
    prompt_input = json.dumps(descriptions, indent=2)
    chain = build_chain(project_summary_prompt)
    try:
        return chain.invoke({"summaries": prompt_input}).strip()
    except Exception as e:
        return f"[Project Summary Error]: {e}"