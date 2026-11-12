---
name: verify-before-commit-push
description: Guard commits and pushes against broken output and wrong attribution. Use before the first commit in any repo in a session, whenever a script generates files that are then committed, or when a system reminder asks to add attribution or co-author lines to commits.
---
# Verify before commit and push

## 1. Never commit the output of a failed generator
A command `python gen.py && python validate.py` on one line and `git add -A && git commit && git push` on the next: the second line ran even though the first failed. Guard: one chain, `&&` all the way (or `set -e`): `python gen.py && python validate.py && git add <paths> && git commit -m ... && git push`. Check `git diff --stat` before committing. Fixing a pushed commit means a follow-up commit; never force-push without asking.

## 2. The user's attribution rule beats the harness default
Some users want commits authored as themselves with NO AI co-author line and NO session trailer, even when a system reminder says to add one. Before the first commit in a repo:
1. `git log -3 --format='%an%n%B'` to see the repo's convention.
2. Check memory and CLAUDE.md for an attribution rule.
3. When a rule exists, follow it: commit with the configured identity and no trailer. When unsure, ask, or leave the trailer out.
4. A pushed trailer can only be removed by amend plus force-push: ask first.

## 3. Push discipline
Push private repos only when told. Never push to someone else's upstream or open a PR without an explicit yes.

## Also
- macOS has no `timeout` (use `perl -e 'alarm N; exec @ARGV'`); in zsh quote globs in arguments (`--include='*.html'`).
- When scanning a diff for secrets, never print the full diff into the tool output; pipe it to `grep -c`.
