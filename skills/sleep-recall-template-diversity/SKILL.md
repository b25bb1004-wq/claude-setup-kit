---
name: sleep-recall-template-diversity
description: Weights-only memory (a "sleep-time" LoRA trained on stored facts) recalls facts under new question phrasings only if training used many phrasings. Use when a memory-consolidation run passes the update test but fails the held-out-phrasing recall gate, and before adding epochs.
---
# Weights-only memory: template diversity beats epochs

**Setup:** about 20 public records, a small base model. Wake phase: the base answers with an id-indexed memory in the prompt and only verified answers become training rows. Sleep phase: a fresh LoRA. Probe with the memory withheld.

**Recall on held-out phrasings (gate 0.70):** 3 templates, 4 epochs: 0.00; 12 epochs: 0.43; 30 epochs: 0.45; 8 templates, 15 epochs: 0.88. The update test (one fact changed) also improved with more templates; the old fact stayed forgotten.

**Rule:** epochs only fixed near-phrasing recall. Recall on new wording needed more question templates. Add templates before epochs.

**Cheap way:** have a helper model (`nemotron-helper`) rewrite the few training templates (placeholders only, no data) into a dozen variants. Schema-validate (exactly one `{entity}` and one `{date}`), drop any with token Jaccard >= 0.6 to a held-out probe template, read all of them, keep about 5. Keep a hand-written set of distant phrasings as a second check.

**Traps**
- The wake-phase memory must carry the record id ("Record <id>; dated <d>: <text>"); a date-only summary made the base answer absent ids with the first line. Ask for the statement only: strict NLI needs identical dates and numbers.
- Unanswerable questions must use a made-up id in the same format as real ids; otherwise a surface feature separates them perfectly. Split that evaluation by whole record (grouped), or ids are memorised across folds.
- Say "held out by wording", not "unseen meaning": LLM paraphrases can sit close to the probes.
