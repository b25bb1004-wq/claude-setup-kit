---
name: vault-edit-safely-windows
description: Use when editing a notes vault (or any git repo) from the Windows Bash tool and git shows a file as "Binary", a push is rejected, or `git stash pop` conflicts.
---
# Edit and push a vault safely on Windows

**Failures:** a typed backslash-zero in a shell heredoc became a real NUL byte, so git showed a note as binary; `git stash` before staging hid my own edits and the pop conflicted; a push was rejected because another machine had pushed.

**Rules**
1. Write or edit notes with the file tools (Write/Edit). If a script must write special bytes, build them explicitly (`bytes([92,48])`), never by typing a backslash-zero.
2. Check before committing: `grep -c -a -P '\x00' file` must print 0.
3. Order: edit, `git add <only your files>`, commit, `git pull --rebase --autostash`, push. Never `git stash` your own uncommitted edits before staging them.
4. Keep tool-made files (e.g. Obsidian's `.obsidian/graph.json`) out of the commit unless told.
5. Keep the file's line endings (detect `\r\n` first) so diffs stay small.
