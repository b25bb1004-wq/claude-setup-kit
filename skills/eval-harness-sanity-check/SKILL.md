---
name: eval-harness-sanity-check
description: Before trusting or waiting on any benchmark or scoring script (MMLU letter scoring, HumanEval, pass rates), run it on 10 to 25 items and check the score is plausible. Use when a score looks absurdly low or high, or before launching a long eval.
---
# Sanity-check an eval harness first

**Failure:** MMLU on a strong 35B model scored 1 percent while the same script gave about 66 percent on an 8B. Cause: the scorer did `tok in "ABCD"` on a stripped token. The big model's first token was a newline, `"\n".strip()` is `""`, and the empty string is a substring of every string, so the newline always "won". Two wasted runs.

**Do**
1. Run the first 10 to 25 items and print raw prediction, gold and top candidates for 3 of them before the full run.
2. A score near 0 or near chance (25 percent for 4 choices) on a clearly good model is a harness bug until proven otherwise. Do not wait for the full run.
3. Compare against a known baseline model through the same script, and keep its numbers on file.
4. Scorers: never use `x in "ABCD"` for membership; use `x in set("ABCD")` or `x and x in L`. Widen the logprob window (e.g. `n_probs` 300) when the first token may be whitespace or a thinking tag. Strip, then require non-empty.
5. Keep the original scorer file; write the fixed copy under a new name and note the change, so earlier numbers stay comparable.
6. Run long evals detached with a done-marker and look at the log tail after about 40 s, not blindly at the end.
