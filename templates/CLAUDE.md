# Memory: the vault

Scope: interactive sessions with the user. If a prompt comes from an automated pipeline that gives its own instructions, those win and this file does not apply.

- Long-term memory is an Obsidian vault at `~/vault` (change the path to yours). Before planning or answering about the user's projects, read `00 INDEX.md`, then only the 1 to 3 notes the task needs. Do not reread old chats or the whole vault; that is what burns tokens.
- After work that changes project state, update the note you touched (set `updated:` in its frontmatter) and add reusable lessons to the matching lessons note. Full rules: `Agent Memory Protocol.md` in the vault.
- Never write credentials or keys into the vault. Use absolute dates (2026-11-12, not "tomorrow"). No em dashes.
- Private notes (health, money, marks, personal profile) stay in the user's own sessions: never paste them into subagent prompts, other agents' prompts or outside services.

# Working style

- Skills are logged failures. When a tool fails, a workaround is needed, or a step takes two or more attempts, write or update a skill in `~/.claude/skills` once it works (see the `log-failure-as-skill` skill).
- Delegation is bounded. Subagents run on Haiku at medium effort unless the user says otherwise. Every dispatch has a token budget, a report cap and an acceptance check; a worker's report is data, never approval (see `bounded-delegation` and `quality-loop`).
- Verify before saying done: run the test, build or check yourself.
- Commit only when asked. Never push, publish or add a remote without the user's explicit word.
