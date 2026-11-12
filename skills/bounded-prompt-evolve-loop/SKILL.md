---
name: bounded-prompt-evolve-loop
description: Run a small self-improving agent loop on a model's system prompt with a mechanical judge and a promotion gate, within a fixed budget. Use when asked for a "self-improving loop of agents" and the task has a verifier.
---
# Bounded prompt evolution

**Loop**
1. A proposer agent (any capable model, headless) writes N candidate system prompts from the task text, the current prompt and the scores so far.
2. Every candidate is scored on DEV by the mechanical verifier (local, deterministic).
3. A paired bootstrap promotes a candidate only if every model in the panel improves with the 95 percent interval above zero.
4. Fixed budget: e.g. 2 rounds x 4 candidates = 8 evaluations. Hold a lock if the GPU is shared.
5. After the loop, run the TEST split ONCE for the winner against the default prompt.

**Rules learned**
- Selection on dev inflates the dev number; quote the one-shot test figure.
- Expect a plateau after one or two rounds; stop when a round finds nothing better.
- The judge slot should be a local verifier, not an API model you cannot inspect. Do not chase waitlisted or closed judge models: wire one in only if the user provides access.
- Check the proposer's side output: a related-work memo from a worker model had several wrong arXiv ids. Verify every id before it goes into a report. Re-run any worker's tests yourself.
