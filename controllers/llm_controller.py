import openai
from openai import OpenAI
from configs.azure_config import AZURE_API_KEY, AZURE_BASE_URL, AZURE_API_KEY_1
from configs.llm_config import SYSTEM_CONTENT, USER_CONTENT, OPENAI_MODEL, LLM_MAX_TOKENS, LLM_TEMPERATURE, LLM_TOP_P

class LLMController:
  def __init__(self):
    self.api_keys = [AZURE_API_KEY, AZURE_API_KEY_1]
    self.current_key_index = 0
    self.client = self._create_client()

  def _create_client(self):
    return OpenAI(
      api_key=self.api_keys[self.current_key_index],
      base_url=AZURE_BASE_URL
    )

  def generate_response(self, user_input):
    system_message = {
      "role": "system",
      "content": SYSTEM_CONTENT
    }
    user_message = {
      "role": "user",
      "content": f"{USER_CONTENT}:{user_input}"
    }
    messages = [system_message, user_message]

    try:
      response = self.client.chat.completions.create(
        model=OPENAI_MODEL,
        max_tokens=LLM_MAX_TOKENS,
        temperature=LLM_TEMPERATURE,
        top_p=LLM_TOP_P,
        messages=messages
      )
      reply = response.choices[0].message.content.strip()
      return reply

    except openai.RateLimitError:
      print(f"Rate limit exceeded on key {self.current_key_index}. Switching keys...")
      return self._handle_rate_limit(user_input)

    except Exception as e:
      print(f"Unexpected error: {str(e)}")
      return f"Error processing request: {str(e)}"

  def _handle_rate_limit(self, user_input):
    self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)
    self.client = self._create_client()

    if self.current_key_index == 0:
      print(f"All keys rate limited. Wait for refresh...")

    return self.generate_response(user_input)
