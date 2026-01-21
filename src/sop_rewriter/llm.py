import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass
class LLMConfig:
    model: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

def call_openai_chat(prompt, model):
    """Call OpenAI chat completions. Requires OPENAI_API_KEY env var."""
    from openai import OpenAI
    client = OpenAI()
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a careful chemical engineering documentation assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )
    return resp.choices[0].message.content
