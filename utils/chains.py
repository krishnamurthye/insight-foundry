from config import  MODEL_NAME, MAX_TOKENS, USE_OPENAI
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence
from langchain.schema.output_parser import StrOutputParser
from prompts.language_prompts import get_code_analysis_prompt

def build_chain(prompt):
    llm = ChatOpenAI(model=MODEL_NAME, temperature=0, max_tokens=MAX_TOKENS) if USE_OPENAI else ChatOllama(model=MODEL_NAME, temperature=0.2)
    return RunnableSequence(prompt | llm | StrOutputParser())

def build_chain_for_language(language):
    return build_chain(get_code_analysis_prompt(language))
