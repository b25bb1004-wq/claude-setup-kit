---
name: failure-bank-loop
description: Keep every failed task of a model or agent pipeline in a labelled failure bank and learn from it instead of discarding it. Use after any pilot or eval run, before choosing the next change, and when the user says "don't throw away the tasks which went wrong".
---
# Failure bank loop

**Rule:** failed tasks are kept and used to improve the system, never dropped.

1. After a run, write `failures.jsonl`: one line per failed item with the question, reference, answer, a cause label, the source ids AND the source text the system saw (without it a failure cannot be replayed).
2. Use a fixed cause order, for example: checker rejected correct content; reader error with sources present; retrieval missed a source; fetch missed a source; answered an out-of-scope question; abstained but answerable.
3. Count causes first and aim the next change at the biggest one (see `error-breakdown-before-training`). In one case the biggest cause was a checker threshold; freezing a better threshold more than doubled the verified rate on fresh items.
4. Dev items only for choosing levers (retry prompts, lessons, fine-tuning pairs).
5. Freeze the change, run ONCE on fresh items, report both the gain and the failures that remain, and append the new failures to the bank.
6. Thresholds are task specific: an entailment cutoff that suits checking the agent's own cited sentence (e.g. 0.4) is too loose for judging a user's outside claim (0.7 to 0.9). Test each on fresh data.
7. Cheap models can do labour or act as judges on the bank; they never produce the reported number alone.
