from pathlib import Path
from docx import Document

def save_txt(path, text):
    Path(path).write_text(text, encoding="utf-8")

def save_docx(path, text):
    doc = Document()
    for line in text.split("\n"):
        doc.add_paragraph(line)
    doc.save(path)
