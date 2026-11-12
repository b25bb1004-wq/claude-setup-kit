---
name: oracle-guided-sft-targets
description: Build supervised training targets from an environment's ground truth when self-distillation or rejection sampling gives no gain. Use when designing the next fine-tuning round for a task whose answers can be checked mechanically, and when reporting such a result honestly.
---
# Oracle-guided targets instead of self-samples

**Idea:** if the task has ground truth (e.g. the source a human actually cited), construct the answer the model should have given and keep it only if the SAME checker the exam uses accepts it.

**Recipe**
1. Only use tasks where the gold answer is actually among the candidates shown; otherwise the target teaches something the model could not see.
2. Build the target's supporting part mechanically (e.g. pick the evidence sentence by NLI over the gold source's sentences, length 8 to 40 words, no characters the answer format forbids). Keep that cache separate from the exam's.
3. Re-run the exam's own checks on every target before writing it.
4. Add abstention targets only for tasks where no shown candidate supports the claim (max NLI below 0.5), at a ratio you can measure (start at 0.3 per positive).
5. Train 1 to 2 epochs with a held-out slice (split by task) and watch its loss: if it rises while train loss falls, stop.
6. Gate with a paired bootstrap on dev, plus the subset of dev tasks whose gold item never appears in train (memorisation control).

**Be honest in the write-up:** this is supervised learning from mined ground truth, not self-improvement. Report it separately.

**Leak to avoid:** a retriever fine-tuned on train queries makes train candidate lists look better than dev ones. Cross-fit it (2 folds by a stable hash of the task id) so train candidates come from a model that did not see them.
