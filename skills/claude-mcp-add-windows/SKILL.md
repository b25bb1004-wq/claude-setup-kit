---
name: claude-mcp-add-windows
description: Use when adding an npx-based MCP server with `claude mcp add` on Windows and the stored command shows `D:/ C:/` instead of `/d /c`, or PowerShell says "unknown option '-y'" or "Invalid configuration".
---
# claude mcp add on Windows

**Failure:** from Git Bash, `/d /c` became `D:/ C:/` (MSYS path conversion). From PowerShell 5.1, `--` and JSON quoting broke `mcp add` and `mcp add-json`.

**Fix:** use Git Bash with `MSYS_NO_PATHCONV=1`:
```
MSYS_NO_PATHCONV=1 claude mcp add --scope user <name> -- cmd.exe /d /c npx -y <pkg>@latest
```
Verify the args in `~/.claude.json` (should be `["/d","/c","npx","-y","<pkg>"]`) and that `claude mcp list` shows Connected. If wrong: `claude mcp remove <name> --scope user` and redo.

Note: auto mode may block `claude mcp list`, `claude plugin list` or all-in-one installer commands as self-modification; stop and ask the user to run them.
