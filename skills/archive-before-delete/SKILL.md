---
name: archive-before-delete
description: Clean up vaults, folders or notes when the user says "clear", "gone", "garbage" or "get rid of". Use before any delete or move of user files; vague wording usually means archive or hide, and untracked files deleted by mistake are gone for good.
---
# Archive before delete

1. Treat "organise, never delete" as the default. Words like "gone", "clear the garbage" or "stop it popping up" mean hide or archive unless the user says delete or trash. If unsure, ask ONE question with options (junk only / archive / delete) before touching files.
2. Delete only provable junk: `.DS_Store`, `._*` resource forks, empty dirs, zero-byte stubs, scratch dirs. Check each with `ls` or `cat` first.
3. Gitignored or untracked files are NOT in git, so deleting them cannot be undone. List `.gitignore` entries and `git status --ignored` before any removal; move those files, never `rm` them.
4. Order for git moves: `git mv` first, delete junk after. Deleting tracked files first makes `git mv` of the parent fail ("bad source"); recover with `git rm -r --cached <junk>` and retry.
5. To hide without deleting in an Obsidian vault: move to `99 Archive/`, add it to `.obsidian/app.json` `{"userIgnoreFilters": ["99 Archive/"]}`, and drop it from the index note. Wikilinks still resolve by name.
6. Passing mentions in important notes stay; ask before scrubbing them.
7. Tell the user exactly what was and was not touched (`git status`, `ls`), because they may fear something important was removed.
