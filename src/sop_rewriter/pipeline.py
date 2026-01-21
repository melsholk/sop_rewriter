from dataclasses import dataclass
from .cleaning import minimal_clean
from .loader import load_pdf_as_text
from .template import SOP_TEMPLATE_V1
from .llm import call_openai_chat

@dataclass
class RewriteResult:
    source_path: str
    rewritten_text: str

def build_prompt(cleaned_text: str, template: str = SOP_TEMPLATE_V1) -> str:
    return f"{template}\n\nSOURCE SOP:\n{cleaned_text}"

def rewrite_pdf(path: str, model: str) -> RewriteResult:
    raw = load_pdf_as_text(path)
    cleaned = minimal_clean(raw)
    prompt = build_prompt(cleaned)
    rewritten = call_openai_chat(prompt, model=model)
    return RewriteResult(source_path=path, rewritten_text=rewritten)
