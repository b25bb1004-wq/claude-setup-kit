---
name: lean-long-reads
description: Read long documents, PDFs or tool output without burning tokens. Use when a file or tool result is over about 10k words or a result says "Output too large ... saved to".
---
# Lean long reads

1. **Size first.** `wc -w file` before reading. Under about 4k words: read whole. Over: plan the read.
2. **Read in line ranges.** `sed -n 440,760p file | cut -c1-220`. Avoid `head -c 60000` on a huge file: output over about 40 KB is saved to a file and only a short preview comes back, so you pay twice.
3. **Order of value.** Read the original source in full (problem statements, specs). For third-party analyses, read the headings (`grep -o '#\{3,6\} [^|]\{3,90\}'`) and the closing recommendations only, and check them against the original. Analyses can be wrong (one misstated the point weights).
4. **Skip appendices** (sampling protocols, consent templates, glossaries) until a task needs them; note that they were skipped.
5. **One read, one summary.** Write the digest to the vault note right away so the file is never reread.
6. **Parallel independent reads** go in one response.
7. If the Read tool refuses a PDF, use `pdf-to-text-macos` (macOS) or `pdftotext`.
