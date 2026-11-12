---
type: lessons
project: <project name>
updated: YYYY-MM-DD
---
# <Project> Lessons

One entry per lesson, newest first. Keep each entry short enough to read in ten seconds.

## YYYY-MM-DD: <short title of what went wrong>
- **Symptom:** what you saw (error text, wrong number, stalled job).
- **Cause:** why it happened, once known.
- **Fix:** the exact command, setting or change that worked.
- **Rule for next time:** one line an agent can follow without reading the rest.
- **Skill:** link to the skill if it became one, for example `~/.claude/skills/<name>`.

## Example: 2026-11-12: Install script overwrote a customised file
- **Symptom:** a hand-edited CLAUDE.md was replaced by the template.
- **Cause:** the copy step did not check whether the target existed.
- **Fix:** copy only when the target is missing; print "skip" otherwise.
- **Rule for next time:** installers never overwrite; they skip and report.
- **Skill:** none (covered by `archive-before-delete`).
