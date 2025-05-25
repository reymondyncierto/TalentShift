import os
from dotenv import load_dotenv

load_dotenv()

LLM_TEMPLATE = os.getenv("LLM_TEMPLATE")
SYSTEM_CONTENT = os.getenv("SYSTEM_CONTENT")
USER_CONTENT = os.getenv("USER_CONTENT")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", 1000))
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", 0.7))
LLM_TOP_P = float(os.getenv("LLM_TOP_P", 1.0))
