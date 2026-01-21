# GenAI SOP Rewriter (MVP)

A minimal, GitHub-ready project that rewrites existing SOP PDFs into a standardized SOP template using an LLM.

**Use case:** Convert messy/legacy SOPs into a consistent, audit-friendly first draft.  
**Important:** Output is **draft-only** and requires engineer review.

## What this project does
1. Loads SOP PDFs
2. Applies *minimal* text cleaning (hyphenation fix, remove `Page X of Y`, unwrap line breaks)
3. Sends cleaned text to an LLM with a strict SOP template
4. Saves rewritten SOPs as `.txt` and `.docx`

## Quickstart (local)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Set your API key
cp .env.example .env
# edit .env to add OPENAI_API_KEY=...

# Run the CLI
python -m sop_rewriter.cli --inputs data/sample_inputs --outputs outputs --model gpt-4o-mini
```

## Quickstart (Colab)
Open `notebooks/SOP_MVP_clean.ipynb`.

## Repository layout
- `src/sop_rewriter/` : reusable code (cleaning, loading, prompting, writing outputs, CLI)
- `notebooks/`        : Colab-friendly notebook
- `data/sample_inputs/` : put SOP PDFs here (excluded from git by default)
- `outputs/`          : generated files (excluded from git)

## Notes on safety and compliance
- This is a drafting tool. It can reformat and rewrite content, but must not be treated as regulatory approval.
- You should validate that no requirements are dropped and that no new requirements are invented.

## License
MIT (edit as you prefer).
