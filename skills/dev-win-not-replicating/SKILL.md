---
name: dev-win-not-replicating
description: Read a promotion gate result that passed on dev but fails on the held-out test, and decide what to do next. Use when comparing model sizes or configs on a small dev set, before spending GPU days on a bigger model.
---
# A dev win is a hypothesis

- A dev set of about 400 items gives an interval of roughly +-0.035 on an accuracy-like metric. A +0.043 dev win turned into -0.004 on a test set twice the size. Choosing the config that wins dev inflates dev; report both and trust the test.
- Before concluding "size does not matter", list the confounds: different quantisation (4-bit vs bf16), different epochs. Equalise them before comparing capacity.
- Compare against the untrained baseline on the SAME exam too: a model can gain a lot over its own untrained self and still only tie another trained model.
- Decompose the metric before buying compute (e.g. verified vs gold match vs the retrieval ceiling). The gap between them is label ambiguity plus wrong picks; a human baseline and an error breakdown (`error-breakdown-before-training`) show where the ceiling is.
- Use the test set once per dev-chosen config; log every run.
