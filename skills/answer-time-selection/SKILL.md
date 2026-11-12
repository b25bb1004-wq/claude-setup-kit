---
name: answer-time-selection
description: Pick the final answer from k sampled answers with a frozen scoring rule (verifier share, entailment, retrieval rank) instead of greedy decoding. Use when a model with a mechanical checker has sampled rollouts and you want a fair test-time gain without retraining; also the protocol for reporting it.
---
# Answer-time selection

**Rule:** score each candidate answer with a weighted sum, for example
`w_vote*vote_share + w_ver*verified_share + w_ent*best_entailment + w_rank*(-log(rank+1))`, and return the top one.

## Protocol (keeps the number honest)
1. Choose the weights by k-fold cross-validation on DEV only (a small grid, e.g. 3x3x3x4).
2. Freeze the weights, apply them ONCE to TEST, and compare with greedy using a paired bootstrap on the same items.
3. Report it as test-time search (k samples plus a verifier). No gold labels are used at answer time and no weights change.
4. If "verified" uses the same checker the selector optimises, also report a metric the selector cannot see (e.g. gold match). Gains on the shared checker are inflated.

## What we learned
- Only the checker signals (verified share, entailment) carry the gain. Majority vote alone and retrieval rank alone gave nothing.
- Gains grow with k but cost k+1 generations: measure k = 0, 1, 2, 4, 8 on dev and stop where the curve flattens.
- Compare the selector with the any-of-k ceiling (is ANY sample correct?). If selection is close to that ceiling, improve the candidates, not the selector.
- Selection gains were the same order as fine-tuning gains and the two stacked; a smaller untrained model with selection could match a trained one with greedy. Report both so readers can see the trade.
