import os
import anthropic

MODEL = "claude-sonnet-4-6"


class Agent:
    """A single specialized agent backed by Claude."""

    def __init__(self, name: str, role_prompt: str, model: str = MODEL):
        self.name = name
        self.role_prompt = role_prompt
        self.model = model
        self._client = None

    @property
    def client(self) -> anthropic.Anthropic:
        if self._client is None:
            self._client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
        return self._client

    def run(self, task: str, context: str = "") -> str:
        user_content = task if not context else f"Contexto:\n{context}\n\nTarea:\n{task}"
        response = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=self.role_prompt,
            messages=[{"role": "user", "content": user_content}],
        )
        return "".join(block.text for block in response.content if block.type == "text")
