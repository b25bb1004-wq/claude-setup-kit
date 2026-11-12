---
name: obsidian-open-vault-windows
description: Use when registering an existing folder as an Obsidian vault on Windows from a script (the obsidian:// URI says "Vault not found", or Obsidian opens a Welcome or throwaway vault).
---
# Open an existing folder as an Obsidian vault (Windows)

**Failure:** the obsidian:// URI gave "Vault not found", and a first launch overwrote obsidian.json and created a throwaway "Obsidian Vault" folder. Typing a path into the folder picker with SendKeys opened Downloads instead (and created Downloads/.obsidian).

**Fix**
1. Stop Obsidian (`Stop-Process`) so it cannot overwrite the config. Back up `%APPDATA%\obsidian\obsidian.json`.
2. Add `"<16 hex id>":{"path":"C:\\...\\vault","ts":<ms>,"open":true}` under "vaults"; remove "open" from the other vaults; write UTF-8 without BOM.
3. Launch Obsidian.exe. It opens the vault marked open. Check the window title "... - <vault> - Obsidian" (`Get-Process obsidian`).
4. If the first launches only show the "Quick start" screen, a pending update may be applying: stop, relaunch once, then redo step 2.
5. Do not drive the folder picker with SendKeys. Delete any stray `.obsidian` folder or throwaway vault it made.
6. Check `git status`: Obsidian touches tracked `.obsidian/graph.json` and `core-plugins.json`; report, do not commit blindly.
