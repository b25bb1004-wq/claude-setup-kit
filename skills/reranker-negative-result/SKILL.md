---
name: reranker-negative-result
description: Read before fine-tuning a cross-encoder reranker on mined hard negatives. A fine-tune on noisy negatives hurt recall and weight interpolation only recovered parity. Use when planning retrieval upgrades.
---
# Reranker fine-tune on mined hard negatives

**Setup:** an off-the-shelf base reranker, listwise cross-entropy with 1 gold + 7 hard negatives taken from the retriever's own candidate lists, 2 epochs (about 10 minutes).

**Result (dev recall@10):** off-the-shelf 0.729; fine-tuned 0.679 (worse, recall@1 also dropped); WiSE-FT weight interpolation at w = 0.3 / 0.5 / 0.7 gave 0.729 / 0.734 / 0.722, all within noise of the baseline.

**Lesson:** when "negatives" can be valid answers (citation and multi-answer tasks), fine-tuning on them teaches noise. Run an error breakdown first (`error-breakdown-before-training`): if retrieval misses are a minority of failures, prefer answer-time selection (`answer-time-selection`), which gave a much larger gain here.

**If retrying:** filter negatives by NLI entailment below 0.2 against the query, and keep the off-the-shelf model as an interpolation anchor.
