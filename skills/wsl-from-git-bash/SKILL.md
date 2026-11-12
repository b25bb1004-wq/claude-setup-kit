---
name: wsl-from-git-bash
description: Use when running a command inside WSL from the Windows Bash tool (Git Bash) and it fails with "syntax error near unexpected token" or "C:/Program Files/Git/home/..." paths.
---
# Run WSL commands from Git Bash

**Failure:** `wsl -d <distro> -- bash -lc 'export PATH=$HOME/...; node ...'` broke. Git Bash expanded `$PATH` with Windows entries containing parentheses, and rewrote `/home/...` into `C:/Program Files/Git/home/...`.

**Fix**
1. Prefix `MSYS_NO_PATHCONV=1` so Git Bash stops rewriting paths.
2. Use absolute Linux paths and avoid `bash -lc` with `$VARS`: `MSYS_NO_PATHCONV=1 wsl -d <distro> -- /home/<user>/.local/node/bin/node /home/<user>/app/cli.mjs status`.
3. Pipe output through `tr -d '\0'` (wsl.exe emits UTF-16 for its own messages, e.g. `wsl -l -v`).
4. Find the WSL home first: `MSYS_NO_PATHCONV=1 wsl -d <distro> -- printenv HOME` (the Linux user name often differs from the Windows one).
