---
name: bounded-delegation
description: Plan research or labour fan-out so it cannot drain your daily and weekly usage limits. Use before spawning any subagent or external CLI agent job, and when a request names many parallel research tasks (study path, novelty audit, red team, simulations).
---
# Bounded delegation

**Failure that created this rule:** five unbounded research subagents for one request hit the daily and weekly limits, and three of the outputs were lost.

## Rules
1. No unbounded parallel subagent fan-out. Do the thinking and judging inline, one level at a time. If you do run parallel workers (see `quality-loop`), each has a written token budget, a concurrency cap and an acceptance check.
2. Push labour that has acceptance tests to cheaper workers (an external coding CLI, a small model) and second opinions to another vendor's CLI. Launch each detached so the tool call returns.
3. Every job has a brief with a deliverable path, a size cap (report at most 10 lines) and a self-test. Workers write results to disk as they finish, so a limit hit loses nothing.
4. Check `wc -c` before reading any worker output; read with `head` or `grep` first. One 45 KB note once cost a large share of a session limit.
5. One small job per worker at a time. Re-run lost items inline instead of re-spawning the whole set.
6. Use bounded loops for waiting (`for i in $(seq 1 14); do ...; sleep 20; done`); macOS has no `timeout`.
