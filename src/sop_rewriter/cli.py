import argparse
from pathlib import Path
from .pipeline import rewrite_pdf
from .writer import save_txt, save_docx

def main():
    parser = argparse.ArgumentParser(description="Rewrite SOP PDFs into a standardized SOP template using an LLM.")
    parser.add_argument("--inputs", type=str, required=True, help="Folder containing PDF SOPs.")
    parser.add_argument("--outputs", type=str, required=True, help="Folder to write rewritten files.")
    parser.add_argument("--model", type=str, default="gpt-4o-mini", help="LLM model name (OpenAI).")
    args = parser.parse_args()

    in_dir = Path(args.inputs)
    out_dir = Path(args.outputs)
    out_dir.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(in_dir.glob("*.pdf"))
    if not pdfs:
        raise SystemExit(f"No PDFs found in: {in_dir.resolve()}")

    for pdf in pdfs:
        res = rewrite_pdf(str(pdf), model=args.model)
        stem = pdf.stem
        save_txt(str(out_dir / f"{stem}_rewritten.txt"), res.rewritten_text)
        save_docx(str(out_dir / f"{stem}_rewritten.docx"), res.rewritten_text)
        print(f"Wrote: {stem}_rewritten.(txt|docx)")

if __name__ == "__main__":
    main()
