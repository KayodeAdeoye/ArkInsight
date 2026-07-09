from ai.providers.manual_provider import ManualProvider
from ai.providers.ollama_provider import OllamaProvider
from ai.providers.openai_provider import OpenAIProvider


def get_ai_provider(provider_name: str, model: str = ""):
    if provider_name == "Manual Mode":
        return ManualProvider()

    if provider_name == "Ollama":
        return OllamaProvider(model=model or "llama3.1:8b")

    if provider_name == "OpenAI":
        return OpenAIProvider(model=model or "gpt-4.1-mini")

    raise ValueError(f"Unknown AI provider: {provider_name}")