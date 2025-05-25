import os
from dotenv import load_dotenv

load_dotenv()

SYSTEM_CONTENT = os.getenv("SYSTEM_CONTENT")
USER_CONTENT = os.getenv("USER_CONTENT")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")
LLM_MAX_TOKENS = int(os.getenv("MAX_TOKENS"))
LLM_TEMPERATURE = float(os.getenv("TEMPERATURE"))
LLM_TOP_P = float(os.getenv("TOP_P"))
