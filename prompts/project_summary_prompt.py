from langchain.prompts import PromptTemplate

project_summary_prompt = PromptTemplate.from_template("""
You are given summaries of several Java files in a backend project.
Based on these, generate a high-level overview of the project including:
- Its primary purpose
- Its core components
- Testing strategy or mocks/assertions usage
- Anything noteworthy

Summaries:
{summaries}
""")