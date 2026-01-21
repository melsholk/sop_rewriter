import re

def minimal_clean(text):
    """Minimal, MVP-grade cleaning for SOP PDF text.

    - Fix hyphenated line breaks (e.g., 'chemi-\ncal' -> 'chemical')
    - Remove 'Page X of Y' artifacts
    - Unwrap line breaks
    - Normalize whitespace
    """
    t = text.replace("-\n", "")
    t = re.sub(r"\bPage\s+\d+\s+of\s+\d+\b", " ", t, flags=re.IGNORECASE)
    t = t.replace("\r", "\n")
    t = re.sub(r"\n+", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t
