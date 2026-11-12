---
name: log-failure-as-skill
description: After a tool failure or a hard step that took 2+ attempts to solve, write the fix down as a short generalised skill so it is not rediscovered. Use at the end of any task where a workaround was needed.
---
# Turn failures into skills

**Trigger:** a command or tool errored and a workaround was needed, a step took 2+ attempts, or the user corrected your approach.

**Do (cheaply, once, at task end)**
1. `ls ~/.claude/skills` for an existing skill that fits. Update it instead of adding a duplicate.
2. If new, create `~/.claude/skills/<kebab-name>/SKILL.md` with frontmatter `name` and a `description` that says WHEN to use it (the trigger words matter more than the summary).
3. Body: the exact error text, what worked (copy-pasteable command), what not to do, the date seen. Under 40 lines. Keep helper scripts in the same folder.
4. Generalise: name the class of problem ("no poppler"), not the one file.
5. Never write credentials or private notes into a skill.
6. Add a row for it in the vault's skill library note, and tell the user in one line which skill was added or updated.
