---
name: check-vault-before-interpreting
description: Resolve the user's shorthand (tool names, units, project nicknames) from the notes vault and memory before answering. Use whenever a message names something ambiguous, such as a nickname for a tool, a bare number with no unit, or "the other Claude".
---
# Look it up first

- Shorthand bites: a tool nickname was read as a general ML term for two turns; "11gb in one gpu" meant 11 GB of VRAM, not 11B parameters; "the other Claude" meant a specific remote session.
- Procedure: `grep -rniE '<term>' ~/<your-vault>` (quote the pattern; in zsh do not put an unquoted `--include=*.md` after it) and the memory folder; read the 1-3 hits. Only if nothing matches, state your interpretation in one line and answer, or ask.
- When the user says "you remember I told you ..." and neither the vault nor past transcripts hold it, say so plainly. Quote the closest recorded statement and ask which they mean. Never pretend to remember.
- Units: memory sizes are GB or GiB, model sizes are B parameters; restate with both when the number decides a design.
