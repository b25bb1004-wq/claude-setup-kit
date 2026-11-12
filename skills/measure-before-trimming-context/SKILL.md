---
name: measure-before-trimming-context
description: Reducing Claude Code token or context overhead (token-optimizer audit, trimming skills, plugins, notes). Use before editing any setup file to save tokens; an estimate was twice the real baseline and a planned trim would have saved only about 500 tokens.
---
# Measure before trimming context

1. Run the token-optimizer measure report and compare its estimate with the real session baseline (one audit estimated 94k against 47k real). Quote both.
2. Compute the real saving before editing: trimming 40 skill descriptions from about 250 to 200 characters saves about 500 tokens, and shorter descriptions risk skills not triggering. Skip tiny wins.
3. Plugin skill listings are usually most of the overhead, but they are cached, so the repeat cost is small. Ask before disabling plugins the user relies on.
4. Run the audit inline. If a skill asks for many parallel subagents, that breaks a bounded-delegation budget; do the measure, backup and report steps yourself.
5. The biggest real win is often a long handoff note read at every session start. Keep the resume note under about 1 KB of current state; move history verbatim to an archive. Split big project notes into a status header plus a log note.
6. A real settings win: `autoCompactWindow` (e.g. 300000) in `~/.claude/settings.json` measurably cut cache-read tokens. Back up settings first.
7. Do not graph whole chat histories with an LLM pass: hundreds of MB cost huge tokens and copy private text. Use AST-based graphing on code repos only.
