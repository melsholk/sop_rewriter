from pathlib import Path
from docx import Document

def save_txt(path: str, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8")

def save_docx(path: str, text: str) -> None:
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    doc.save(path)
