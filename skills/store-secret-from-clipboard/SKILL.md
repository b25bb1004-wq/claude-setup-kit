---
name: store-secret-from-clipboard
description: The user puts an API key on the clipboard and says not to paste it in chat. Use to move it into a mode-600 file (Windows or WSL) without ever printing it, and to avoid the one-element-array bug that once wrote a single character.
---
# Secret from clipboard to file, never echoed

1. Never `echo`, `cat` or `set -x` the key or its file; check with `ls -l` (size) and one API call instead. A shell error once printed a key into a transcript (it had to be rotated).
2. The clipboard may hold a whole page snippet (e.g. 26 lines with a curl example), not just the key. Do not show it. Describe it structurally (line count, contains a token, distinct count) and extract the key with a regex.
3. PowerShell trap: `$m = [regex]::Matches(...) | ... | Sort-Object -Unique` with ONE result returns a string, so `$m[0]` is its first character (the file came out as `KEY=n`). Wrap in `@(...)`. Sanity check: the new file's size should equal a known-good key file's size.
4. Compare against an existing key without printing (`$m -contains $k1`), so a "new" key is not the old one pasted again.
5. Write via a temp file (UTF-8, no BOM), copy it to `~/.config/<service>/keyN.env`, `chmod 600`, delete the temp, null the variables.
6. Verify by calling the API once and report only OK or the HTTP code (401 = wrong key, 503 = transient). Key files stay out of git and the vault.
