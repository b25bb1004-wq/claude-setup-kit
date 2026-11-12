# Plugins

Taken from `claude plugin list` and `claude plugin marketplace list` on 2026-11-12 (Claude Code 2.1.322). Versions are what was installed then; installing today gets the current version.

## 1. Add the marketplaces

```sh
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin marketplace add addyosmani/agent-skills
claude plugin marketplace add multica-ai/andrej-karpathy-skills
claude plugin marketplace add https://github.com/affaan-m/ECC.git
claude plugin marketplace add miroapp/miro-ai
claude plugin marketplace add DietrichGebert/ponytail
claude plugin marketplace add obra/superpowers-marketplace
claude plugin marketplace add alexgreensh/token-optimizer
claude plugin marketplace add bradautomates/claude-video
```

The built-in `anthropic-plugin-directory` marketplace needs no command.

## 2. Install the plugins (user scope)

| Plugin | Version seen | Command | What it adds |
|---|---|---|---|
| agent-skills | 0.6.13 | `claude plugin install agent-skills@addy-agent-skills` | Engineering workflow skills (spec, plan, build, test, review, ship) and reviewer agents. |
| andrej-karpathy-skills | 1.0.0 | `claude plugin install andrej-karpathy-skills@karpathy-skills` | Coding guidelines against common LLM mistakes. |
| clangd-lsp | 1.0.0 | `claude plugin install clangd-lsp@claude-plugins-official` | C and C++ language server (needs `clangd` on PATH). |
| ecc | 2.2.3 | `claude plugin install ecc@ecc` | Large set of skills, reviewer agents, hooks and a chrome-devtools MCP server. |
| frontend-design | 1.1.1 | `claude plugin install frontend-design@claude-plugins-official` | Visual design guidance for UI work. |
| miro | 2.0.0 | `claude plugin install miro@miro-ai` | Miro board MCP server and skills (needs a Miro login). |
| ponytail | 5.3.2 | `claude plugin install ponytail@ponytail` | "Smallest complete change" coding mode. |
| superpowers | 7.0.1 | `claude plugin install superpowers@superpowers-marketplace` | Process skills: brainstorming, plans, TDD, systematic debugging, verification. |
| token-optimizer | 5.13.57 | `claude plugin install token-optimizer@alexgreensh-token-optimizer` | Context usage dashboard, status line, compaction checkpoints. |
| vercel | 0.50.0 | `claude plugin install vercel@claude-plugins-official` | Vercel skills, agents and MCP server (needs `bun`). |
| watch | 0.2.0 | `claude plugin install watch@claude-video` | Watch videos via captions; optional Whisper fallback with your own key in `~/.config/watch/.env`. |

`cc-plugin-you-should-know@builtin` was also enabled; it ships with Claude Code.

## 3. Plugin settings used

In `settings.json` (see `settings.example.json`):

```json
"pluginConfigs": {
  "ecc": { "hooks_enabled": true, "hook_profile": "minimal" }
}
```

The `minimal` hook profile keeps ecc's hooks light. All hooks in this setup come from plugins; none are hand-written.

## 4. Check

```sh
claude plugin list
claude plugin marketplace list
```

Plugins run code on your machine. Read a plugin's repo before installing it (see `skills/install-agent-tools-safely`).
