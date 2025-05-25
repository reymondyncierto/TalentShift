from openai import OpenAI
from configs.azure_config import AZURE_API_KEY, AZURE_BASE_URL
from configs.llm_config import LLM_TEMPLATE, SYSTEM_CONTENT, USER_CONTENT, OPENAI_MODEL, LLM_MAX_TOKENS, LLM_TEMPERATURE, LLM_TOP_P

class LLMController:
  def __init__(self):
    self.client = OpenAI(
      api_key=AZURE_API_KEY,
      base_url=AZURE_BASE_URL
    )

  def generate_response(self, user_input):
    response = self.client.chat.completions.create(
      model=OPENAI_MODEL,
      max_tokens=LLM_MAX_TOKENS,
      temperature=LLM_TEMPERATURE,
      top_p=LLM_TOP_P,
      messages=[
          {"role": "system", "content": f"{SYSTEM_CONTENT} {LLM_TEMPLATE}"},
          {"role": "user", "content": f"{USER_CONTENT}:{user_input}"},
      ]
    )
    return response.choices[0].message.content.strip() if response.choices else None
