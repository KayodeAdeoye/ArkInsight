import os

from openai import OpenAI

from ai.providers.base import AIProvider


class OpenAIProvider(AIProvider):
    def __init__(self, model: str = "gpt-4.1-mini"):
        self.model = model
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate(self, prompt: str, context: str = "") -> str:
        response = self.client.responses.create(
            model=self.model,
            input=f"{context}\n\n{prompt}",
        )
        return response.output_text