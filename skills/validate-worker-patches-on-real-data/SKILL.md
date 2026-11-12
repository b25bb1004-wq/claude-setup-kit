---
name: validate-worker-patches-on-real-data
description: Before merging a change proposed by a worker agent, a reviewer agent, or yourself that alters parsing, filtering, cache keys or any rule applied to saved model output, replay old versus new on saved real outputs and count what changes. Use at every merge of worker code into a pipeline.
---
# Replay old vs new on saved real data before merging

**What happened:** a worker's "fix" for loose answer parsing passed its own 24 synthetic tests, but replayed on about 12,000 saved real answers it rejected 28 percent of them (the model copies bracketed ids exactly as shown in its prompt). Merged as is, it would have gutted the training set. The kept fix allowed brackets; it still reclassified 3 to 5 percent, which was written down so old and new numbers are not compared blindly.

**Do, in order**
1. Read the worker's diff yourself, against a snapshot taken before it started (`cp -r` the workspace first).
2. For any rule on model output (parser, span check, filter, scorer): load the saved runs, apply old and new, and print the count of rows whose result differs plus 3 examples. Run it where the data is; never on `cut`-truncated JSON lines (you get "0 rows").
3. For a filter, measure its yield on saved data before wiring it in.
4. A cache-key change invalidates the whole cache. Point the next run at a new cache file instead of discarding the old one.
5. Change the worker's tests to match the decision you made (do not keep tests that encode the behaviour you rejected), run the full suite, and commit worker fixes and your own hardening separately.
6. Worker reports are claims; report numbers from the real repo after merge.

**Reviewer conflicts:** if a reviewer's points conflict with the user's spec, the spec wins. List them as decisions for the user; do not apply them.
