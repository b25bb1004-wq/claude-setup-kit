---
name: web-research-sweep
description: Run a broad literature, model and vendor sweep (papers, open models, licences, prior art) cheaply and honestly. Use when asked to "scan everything" on a technical topic.
---
# Web research sweep

1. **Batch in parallel.** 8 to 10 web searches in one response, grouped by theme. Search first, then fetch only the 5 to 8 most important primary sources.
2. **Snippets are not facts.** Search summaries misstate numbers, dates and licences and often say "not found". For anything you will rely on (licence, languages supported, results) fetch the primary page: arXiv `abs/` pages, Hugging Face model cards, GitHub READMEs. Fetch prompts ask for specific fields and a word limit ("licence, languages, params, under 150 words").
3. **Tag every claim** in the notes: `[fetched]`, `[search]`, `[memory-verify]`. Never state a `[search]` or `[memory]` number as established.
4. **Vendor and blog pages are marketing.** Prefer papers and model cards; note "single-author preprint, unreviewed" when true.
5. **Do not limit the sweep to the local framing.** Search the general architecture literature too, not only the narrow niche named in the request.
6. **If the user rejects a fetch,** stop and wait; they may widen scope or approve later.
7. **Write the dossier as you go:** one hub note plus one note per part in the vault, with evidence tags, failure modes, open questions and a compute section. Read a source once.
8. **Record gaps:** list what was not scanned.
See also `lean-long-reads` and `prior-art-audit`.
