---
name: skill-vault-checkpoint
description: Reminder to save skills and vault notes. Use at the end of every task, after any tool failure or step that took 2+ attempts, after a permission block, after any hard or long task, and after any breakthrough (a result, trick or approach that finally worked or beat the baseline). Triggers the skill write-up and the vault update before you reply "done".
---
# Skill and vault checkpoint

Run this checklist before telling the user a task is finished, and right after any failure:

1. **Did anything fail, get blocked, or take 2+ attempts?** Yes: follow `log-failure-as-skill` (a short generalised skill in `~/.claude/skills/<name>/SKILL.md`, then a row in the vault's skill library note). A permission block counts: store what was blocked and how the user unblocked it.
2. **Was the task hard or long, or did something finally work?** Store the reusable method as a skill even if nothing failed, and record what made the difference (the insight, the setting, the numbers).
3. **Vault:** update the note the work touched (set `updated:` in its frontmatter), add one dated line to the month's log note, add any new note to the INDEX, then commit (named paths only). No credentials, absolute dates, no private notes.
4. **Multi-task sessions:** when the user is away or several tasks ran, write one short report per task in the vault (`Asked / Did and worked / Failed or blocked / Open items`) plus an index note, so the user can read what happened without the chat.
5. **Peers:** if another Claude session works with you, tell it what changed so its vault clone stays level.

Do not skip this because the task "was simple"; forgetting means rediscovering the fix later.
