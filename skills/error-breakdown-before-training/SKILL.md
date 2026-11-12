---
name: error-breakdown-before-training
description: A training round gave no gain, or you are choosing what to train next. Split the model's errors by cause on saved outputs and compare with a trivial heuristic baseline, then pick the fix that targets the largest cause. Use after any failed gate and before any new GPU training run.
---
# Break the errors down before spending GPU hours

**What happened:** a round of training on the model's own correct answers gave zero gain. One CPU-only breakdown of the saved dev outputs showed where the points went, instead of guessing a new recipe.

**Do**
1. Assign each failed task one cause, checked in a fixed order: (a) was the right answer even available (e.g. retrieval recall: is the gold item among the candidates shown?), (b) given it was available, did the model pick it, (c) did it pick it but fail the checker (format, verbatim copy), (d) abstained, (e) impossible.
2. Print the counts on the SAME tasks the gate uses. In our case a large share of tasks were unwinnable by retrieval and about 40 percent of correct picks failed on copying the evidence exactly.
3. Compute a trivial heuristic baseline (e.g. "always answer with retrieval rank 1"). If the model equals the heuristic, it has not learned the task.
4. Count informative training examples (greedy wrong, some sample right). Self-distillation on examples the model already solves teaches nothing and overfits (held-out loss rises).
5. Aim the next fix at the biggest measured cause, not the most fashionable idea.

**Practical notes**
- Run the analysis where the data lives (an ssh heredoc on the training box). Never pipe truncated lines (`cut`) into a JSON parser.
- Read what the model actually saw from the SAVED PROMPT, not from assumed script defaults (e.g. how many candidates were shown vs how many samples were drawn).
- Use DEV only to choose levers; test outputs must not guide design.
- Read about 7 failures by hand. Some "errors" are valid alternatives, so the true ceiling is below 1.
