# Vault template

A starting folder for an Obsidian vault that agents use as long-term memory. Copy it somewhere outside your repos (for example `~/vault`), open it in Obsidian if you like, and point your `~/.claude/CLAUDE.md` at it (see `../templates/CLAUDE.md`).

## Why a vault

Chat transcripts are long and expensive to reread. A vault of short notes, each holding one fact in one place, lets a new session rebuild context by reading three small files instead of a whole history.

## How agents use it

1. **Read `00 INDEX.md` first, then only the 1 to 3 notes the task needs.** The index lists every note with a one-line hook, so the agent can pick without opening everything.
2. **Update the note after work.** When work changes a project's state, the agent edits that project's note and sets `updated:` in the frontmatter to today's date.
3. **Write lessons to a lessons note.** Each project has a `<Project> Lessons` note. Each entry gives the symptom, cause, fix and a one-line rule (template: `90 Meta/Lessons Library/_template.md`). Lessons that apply everywhere also become a skill in `~/.claude/skills`.
4. **Use absolute dates.** Write 2026-11-12, never "today" or "next week"; notes are read months later.
5. **Keep private notes private.** Personal notes are never attached to subagent prompts or sent to outside services.
6. **No credentials.** Keys and tokens never go in the vault.

The full rules are in `90 Meta/Agent Memory Protocol.md`.

## Folders

| Folder | Holds |
|---|---|
| `00 Now` | This week: active work, open loops. |
| `01 Log` | Monthly log notes `YYYY-MM`. |
| `10 Projects` | One note per project plus its lessons note. |
| `20 Career` | Applications, profile drafts. |
| `30 Study` | Courses and exams. |
| `40 Learning` | Self-study and reading notes. |
| `50 Life` | Personal notes (private). |
| `90 Meta` | The protocol, preferences, lessons library, skill library, mirrors of agent and skill files, plans. |
| `99 Archive` | Finished or dropped work. Nothing is deleted. |

The `.gitkeep` files only keep empty folders in git; delete them once a folder has notes.

## Editing on Windows

Obsidian keeps files open; agents should edit notes with their file tools, not shell redirection (see the `vault-edit-safely-windows` and `obsidian-open-vault-windows` skills).
