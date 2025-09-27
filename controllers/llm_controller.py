import os
from openai import OpenAI
from configs.llm_config import SYSTEM_CONTENT, USER_CONTENT, OPENAI_MODEL, LLM_MAX_TOKENS, LLM_TEMPERATURE, LLM_TOP_P

class LLMController:
  def __init__(self):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
      raise ValueError("No OpenAI API key found. Set OPENAI_API_KEY in your environment.")

    self.client = OpenAI(api_key=api_key)

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

      # response.choices is expected; handle gracefully if structure differs
      content = None
      if hasattr(response, 'choices') and len(response.choices) > 0:
        choice = response.choices[0]
        # newer SDKs may store the message in choice.message
        if hasattr(choice, 'message') and hasattr(choice.message, 'content'):
          content = choice.message.content
        # fallback to 'text' property if present
        elif hasattr(choice, 'text'):
          content = choice.text

      if content is None:
        return ""  # empty reply if structure unexpected

      return content.strip()

    except Exception as e:
      return f"Error processing request: {str(e)}"
