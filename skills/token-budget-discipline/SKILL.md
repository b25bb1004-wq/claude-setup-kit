---
name: token-budget-discipline
description: Keep an interactive session cheap. Use at the start of every session with a user who cares about usage limits, before any multi-step job, and whenever the user mentions usage, limits or "conserve tokens". Treat it as the default mode, not a request.
---
# Token discipline

**What burned the budget, and the rule that replaces it**
1. Full-file rewrites of large artifacts (each Write of a 60 to 100 KB file is 20 to 30k output tokens). RULE: write a page once; change it with small Edit calls plus a republish.
2. Retry chains: eight relaunches of one demo, each fixing one missing import. RULE: after the first failure run a preflight that finds ALL problems at once (`dependency-preflight`). Three failed attempts at the same job: stop and report the cause.
3. Monitors and polling that wake the model per event. RULE: one background job, one check at the end; stop monitors you no longer need.
4. Searches and reads: dozens of web searches, huge files, repeated skill loads. RULE: grep for the lines you need; batch searches in one turn; load a skill once.
5. Screenshots after every edit. RULE: one look per breakpoint, after the last edit.
6. Long status messages. RULE: one or two lines while working; the final reply says what is done, what is not, and the one decision needed.
7. Speculative extra work nobody asked for. RULE: do the asked thing; offer the extra in one line.

**Gates**
- Before a multi-step job, estimate the number of tool calls; if above about 10, say so and ask once (unless the user handed over the goal with freedom).
- When the user reports usage above 50 percent, stop background work that wakes you, finish what is in flight, write state to the vault, and suggest /clear.
- Prefer one compound Bash call over several, Edit over Write, and head/grep/cut over cat.
- Delegate labour with a brief and a self-test (`bounded-delegation`), and read only the report.
