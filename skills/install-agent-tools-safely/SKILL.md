---
name: install-agent-tools-safely
description: Install third-party Claude Code skills, plugins, MCP servers and CLIs (Context7, Graphify, Strix, REA, Magic MCP) without letting their installers edit your CLAUDE.md or hooks. Use when asked to "download" or "get" a GitHub agent tool.
---
# Installing agent tools

1. **Verify provenance first.** PyPI or npm metadata must link to the official GitHub repo (`curl https://pypi.org/pypi/<pkg>/json`, `npm view <pkg> repository.url`). Beware lookalike names (graphify is published as `graphifyy`, two y's).
2. **Prefer the narrow install:** `claude plugin marketplace add <owner/repo>` then `claude plugin install <name>@<marketplace>`; `claude mcp add --scope user <name> -- npx -y <pkg>`; `uv tool install <pkg>`.
3. **Do not run all-in-one `setup` or `install` commands** (for example `graphify install`, `rea-agents setup`). They edit `~/.claude/CLAUDE.md`, settings.json hooks and other agents' configs. Copy the bundled SKILL.md into `~/.claude/skills/<name>/` instead. The permission layer may block such a command as self-modification; the user then runs it with `!` or adds a Bash rule.
4. **Keys:** MCP servers that need an API key (for example 21st.dev Magic) need the user's own key. Never take one from a web page; never write it to notes, git or messages.
5. **Dual-use tools** (Strix pentest agent, REA reverse engineering): install only; run them against targets you own or are authorised to test. Strix needs Docker and an LLM key.
6. Verify with `claude plugin list` and `claude mcp list`, then save any lesson (`skill-vault-checkpoint`).

## Worked recipes
- REA without its setup command: `claude mcp add --scope user rea -- npx -y rea-agents@<version> mcp`, then `npm pack rea-agents@<version>`, extract, and copy `package/skills/reverse-engineer-anything/` to `~/.claude/skills/`.
- Moving an MCP server with a key from project to user scope without printing the key: read it into a shell variable with a small script, run `claude mcp add --scope user ... --header "x-api-key: $key"`, `unset key`, then `claude mcp remove <name> --scope local` from that project folder.

## Traps
- If a placeholder such as `<KEY>` is pasted literally into `--header`, the config silently stores the placeholder and the tool fails. Re-run with the real key.
- Git Bash on Windows rewrites `/path`-style args (for example Context7's `npx` args): prefix `MSYS_NO_PATHCONV=1`.
- Installers that edit CLAUDE.md, settings or other agents' configs get a self-modification block: use the manual command and tell the user what was skipped (see `handle-permission-blocks`).
