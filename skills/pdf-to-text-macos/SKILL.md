---
name: pdf-to-text-macos
description: Extract text from a PDF on macOS when the Read tool fails with "pdftoppm is not installed" and pdftotext/pypdf are missing. Use before trying brew installs.
---
# PDF to text on macOS with no poppler

**Failure seen:** the Read tool errors on a PDF with `pdftoppm is not installed`; `pdftotext`, `pdfinfo` and the `pypdf` module are all absent.

**What works (no installs):** macOS PDFKit via Swift, script `~/.claude/skills/pdf-to-text-macos/pdf2txt.swift`.
```
mkdir -p $SCRATCH/pdfs && cp "<pdf>" $SCRATCH/pdfs/a.pdf     # untrusted file: copy to its own dir first
swift ~/.claude/skills/pdf-to-text-macos/pdf2txt.swift $SCRATCH/pdfs/a.pdf $SCRATCH/pdfs/a.txt
wc -w $SCRATCH/pdfs/a.txt                                     # check size before reading
```
It prints `<file> <pageCount>`. Works for text PDFs; scanned PDFs return empty text (OCR needed, ask first).

**If the user agrees to installs:** `brew install poppler` gives `pdftoppm`/`pdftotext` and lets the Read tool open PDFs; `brew install ghostscript` gives `gs` for compression (`gs -sDEVICE=pdfwrite -dPDFSETTINGS=/ebook` roughly halved a slide-heavy PDF). Do not install without asking (system change, slow).

**Notes**
- Extracted text has odd spacing ("t he", "wit h") from ligature and kerning splits. Grep short stems, not exact words.
- Files inside app sandboxes under `~/Library/Containers/...` are readable with `cp`; copy them out first.
- Then follow `lean-long-reads` for the text.
