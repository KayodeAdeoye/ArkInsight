from ai.providers.base import AIProvider


class ManualProvider(AIProvider):
    def generate(self, prompt: str, context: str = "") -> str:
        return (
            "Manual Mode is enabled. "
            "No AI response was generated. "
            "User must complete this step manually."
        )