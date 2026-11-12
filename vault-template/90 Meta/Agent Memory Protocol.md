---
type: protocol
updated: 2026-11-12
---
# Agent Memory Protocol

How any agent (Claude Code, other CLIs, subagents) reads and writes this vault.

1. **Read small.** Read [[00 INDEX]] first, then only the 1 to 3 notes the task needs. Never read the whole vault or old chat transcripts to rebuild context.
2. **Update what you touched.** After work that changes project state, update that note and set `updated:` in its frontmatter. One fact lives in one place; elsewhere, link to it.
3. **Lessons go to a lessons note.** Reusable lessons (what failed, why, the fix) go to the matching lessons note, for example [[Example Project Lessons]], using the template in `90 Meta/Lessons Library/_template.md`.
4. **Privacy.** Automated pipelines and subagents get only the project folder they work on. Personal notes (`50 Life`, health, money, marks, profile) never go into subagent prompts, other agents or outside services.
5. **Hygiene.** No credentials or keys, ever. Absolute dates (2026-11-12, not "yesterday"). No em dashes.
6. **Preferences.** Follow [[Preferences]] for tone and format.
7. **Log.** Add a short entry to the month's log note `01 Log/YYYY-MM` for meaningful work. Closed loops move to its Resolved Loops section. Nothing is deleted; old notes move to `99 Archive`.
8. **New notes.** Put a new note in the folder that fits and add a line for it to [[00 INDEX]] in the same edit.
9. **Git sync.** If the vault is a git repo, stage named paths only (never `git add -A`) and push only when the user says so.
10. **Everything valuable enters the vault.** Decisions, results and plans from a session are written down before the session ends.
11. **Failures become skills.** A failure with a reusable fix becomes a skill in `~/.claude/skills` plus a row in [[Skill Library]].
12. **Attachments travel with notes.** Put files next to the note in a `files/` folder. Anything over 25 MB stays local only; record its path and SHA-256 in a README next to the note.

## Commits
- Commit small, with plain messages that say what changed.
- Optional safety net: a Stop hook that auto-commits the vault folder so a crash never loses notes.

## Wiring
- The global `~/.claude/CLAUDE.md` points agents here (see `templates/CLAUDE.md` in the kit).
- Other CLIs get the same pointer in their own instruction file (for example `AGENTS.md`).
