---
name: report-pdf-reportlab
description: Build a crisp, human-looking results PDF (and optionally a matching shareable Claude Docs page) with reportlab. Use when the user wants a report for a professor or team: benchmarks, tables, a short chart.
---
# Results PDF that looks written by a person

- **Scope first.** Feedback after a full report: "just performance, simple and crisp". Default to ONE page: title line, one sentence of setup, one table per result family, one sentence of reading under each. Drop methodology, caveat sections and side experiments unless asked. Keep a long version as `-detailed.pdf`.
- **Tone:** first person plural, plain sentences, no bullet-heavy AI patterns, no em dashes, no "key takeaways". Numbers with units; say what a measure means in half a sentence.
- **Honesty in a short report:** if a number is unsettled, show the range in the cell instead of a caveat section. Never drop a result because it is unflattering.
- **Setup:** `python3 -m venv $S/venv && $S/venv/bin/pip install reportlab pypdfium2`. Use a serif with lining numerals for text (e.g. Charter; on macOS `/System/Library/Fonts/Supplemental/Charter.ttc`, subfontIndex 0 roman, 1 italic, 2 bold italic, 3 bold) and a sans for tables. Georgia is wrong for numbers (old-style figures). Never use unicode sub/superscripts.
- **Layout:** A4, 2.2 cm margins, platypus; tables `hAlign="LEFT"`, dark header row, zebra rows, thin rules; headings `keepWithNext=1`; wrap a heading plus its table in `KeepTogether`; footer with title and page number.
- **Check:** render with pypdfium2 (`d[i].render(scale=1).to_pil().save(png)`) and look at every page; `pdftotext` to confirm no leftover placeholders ("...", "running").
- **Builders live in the session scratchpad;** the content tables live in the vault note, so the report can be rebuilt from the note.
- **Shareable version:** a Claude Docs page via the Artifact tool's Docs type, filled section by section. It starts private; the user decides on sharing. Keep the fuller version there and the PDF short.
