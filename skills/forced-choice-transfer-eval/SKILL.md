---
name: forced-choice-transfer-eval
description: Measure whether a fine-tuned small model transfers to another task without format-following hiding the result. Use before trusting any accuracy from a task the model was not trained on, especially after LoRA on a fixed answer format.
---
# Transfer evals

1. Look at 10 raw outputs BEFORE reading a metric. Adapters trained on one answer format kept writing it on the new task (97 to 99 percent unparseable); the first accuracy table was meaningless.
2. For classification use constrained decoding (vLLM `StructuredOutputsParams(choice=[...])`, older versions `GuidedDecodingParams`) so format is removed from the comparison. Then check your parser accepts the constrained text (ours rejected a valid label because it also wanted evidence indices).
3. Never write a prompt that shows the answer shape as a letter: "answer exactly i or i,j" made models output the letter i. Give a concrete example ("4 or 2,5").
4. Compare to the untrained model with a paired bootstrap on the same task ids. A drop can be real and informative (training data with no negative class made recall of that class fall to about 0).
5. Save a short raw-text field in the results rows from the start.
6. One transfer test can flatter or punish a single adapter; run all of them and report all of them.
