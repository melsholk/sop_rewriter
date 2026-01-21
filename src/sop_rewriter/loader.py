from langchain_community.document_loaders import PyMuPDFLoader

def load_pdf_as_text(path):
    """Load a PDF and return concatenated text across pages."""
    pages = PyMuPDFLoader(path).load()
    return "\n".join([p.page_content for p in pages])
