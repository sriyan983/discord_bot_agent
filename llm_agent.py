import logging
from openai import OpenAI
from prompts import OPS_SYSTEM_PROMPT
import os
from dotenv import load_dotenv  

load_dotenv()
logger = logging.getLogger(__name__)

class OpsLLMAgent:
    def __init__(self):
        api_key = os.getenv("OPEN_API_KEY")
        if not api_key:
            raise ValueError("OPEN_API_KEY not set")

        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"
        self.max_tokens = 300

    def generate_response(self, user_input: str) -> str:
        try:
            messages = [
                {"role": "system", "content": OPS_SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ]

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.4,
                max_tokens=self.max_tokens
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            logger.error(f"LLM error: {e}")
            return (
                "⚠️ I’m unable to analyze this right now. "
                "Please retry or escalate to the operations team."
            )
