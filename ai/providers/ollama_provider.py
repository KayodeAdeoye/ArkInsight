import requests

from ai.providers.base import AIProvider


class OllamaProvider(AIProvider):
    def __init__(self, model: str = "llama3.1", base_url: str = "http://localhost:11434"):
        self.model = model
        self.base_url = base_url.rstrip("/")

    def generate(self, prompt: str, context: str = "") -> str:
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": f"{context}\n\n{prompt}",
                "stream": False,
            },
            timeout=120,
        )
        response.raise_for_status()
        return response.json().get("response", "")