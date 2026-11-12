# Claude Setup Kit

A packaged, public-safe copy of one person's Claude Code setup: 68 skills, the plugin and MCP list, settings, a global instruction template, the auto-memory format and an Obsidian vault template that agents use as long-term memory. Personal names, paths, hosts, keys and private project details have been removed or replaced with placeholders (see `SANITIZE.md`).

## The ideas behind it

**The vault is long-term memory.** Chat history is long and costly to reread, and it disappears on compaction. Instead, every session starts by reading a short index note and then only the one to three notes the task needs. After work, the agent updates the note it touched and stamps `updated:` with an absolute date. A new session can rebuild context from three small files. See `vault-template/`.

**Skills are logged failures.** Most skills here started as something that broke: a command that hung, a flag that silently did the wrong thing, a permission block. Once the fix worked, the lesson became a skill, so no later session pays for the same mistake twice. See `skills/log-failure-as-skill` and `SKILLS.md`.

**Delegation is bounded and checked.** The main session plans and judges; workers do labour. Every dispatch gets a written token budget, a report-size cap and an acceptance check. A worker's report is data, never approval, and nothing is marked passing until the orchestrator runs the check itself. The loop stops on budget, on two rounds without progress, or before anything involving credentials, money or publishing. See `skills/quality-loop`, `skills/bounded-delegation` and `skills/delegate-labour`.

**Haiku workers by default.** Subagents run on Haiku at medium effort unless the user asks for more. A bigger model for every worker burned about 1M tokens in one run and hit the usage limit; small, well-briefed Haiku tasks did the same jobs for a fraction of that.

## Install

1. Install the tools you need: `requirements.md`.
2. Preview, then copy skills and templates into `~/.claude`. Nothing that already exists is overwritten; existing items are skipped and listed.
   - macOS / Linux / Git Bash:
     ```sh
     bash scripts/install.sh --dry-run
     bash scripts/install.sh --vault ~/vault
     ```
   - Windows PowerShell:
     ```powershell
     powershell -ExecutionPolicy Bypass -File scripts\install.ps1 -DryRun
     powershell -ExecutionPolicy Bypass -File scripts\install.ps1 -Vault "$HOME\vault"
     ```
   Set `CLAUDE_HOME` (or `-Target`) to install somewhere other than `~/.claude`.
3. Merge `~/.claude/settings.example.json` into your `settings.json` by hand. It has notes in `_comment` keys and one clearly marked example hook.
4. Install plugins: `plugins.md`. Add MCP servers with your own keys: `mcp.md`.
5. If you skipped `--vault`, copy `vault-template/` somewhere outside your repos and edit the vault path in `~/.claude/CLAUDE.md`.

## Folder map

| Path | What it is |
|---|---|
| `README.md` | This file. |
| `SKILLS.md` | Index of the 68 shipped skills, each marked as-is or generalised. |
| `DROPPED.md` | Skills not shipped, with a reason each (third-party, project-specific, merged). |
| `skills/` | One folder per skill, each with a `SKILL.md`. |
| `plugins.md` | Marketplaces and plugins with exact install commands. |
| `mcp.md` | MCP servers with placeholder keys, plugin-provided servers, claude.ai connectors. |
| `subagents.md` | Where the agent types come from and how workers are used. |
| `settings.example.json` | Example `settings.json`: permissions, plugins, status line, an example hook. |
| `templates/CLAUDE.md` | Generic global instructions that point agents at the vault. |
| `memory-format/README.md` | The auto-memory format: frontmatter types, the `MEMORY.md` index, links. |
| `memory-format/examples/` | An invented index and three invented memories. |
| `vault-template/` | Vault folders, `00 INDEX.md`, the agent protocol, a lessons template, a README. |
| `requirements.md` | Tools with install commands and the versions seen. |
| `scripts/install.sh` | No-overwrite installer for Bash. |
| `scripts/install.ps1` | No-overwrite installer for PowerShell. |
| `scripts/validate_skills.py` | Checks every skill has frontmatter `name` and `description`. |
| `scripts/check_coverage.py` | Checks a skills folder is fully covered by `skills/` plus `DROPPED.md`. |
| `scripts/sanitize.py` | Scans the repo for personal data and secret-like strings; writes `SANITIZE.md`. |
| `SANITIZE.md` | The last sanitizer report. |
| `LOOP.md` | The build checklist and log used to make this kit. |
| `LICENSE` | MIT licence. |
| `bench/README.md` | How to run the static tests and the skill-trigger benchmark, and how to read the report. |
| `bench/test_static.py` | Free static tests: validator, installers, sanitizer, references, required tools. |
| `bench/prompts.jsonl` | 30 labelled prompts for the skill-trigger benchmark. |
| `bench/run_bench.py` | Runs the prompts headless in isolated kit and vanilla configs. |
| `bench/results/smoke/` | The one smoke run (2 prompts x 2 configs) that proves the runner works. |

## Notes

- `templates/CLAUDE.md` is a template. Claude Code may load it as instructions when working inside `templates/`; that is harmless but worth knowing.
- Licensed under MIT (see `LICENSE`). Third-party skills are not included; `DROPPED.md` says where to get them under their own licences.
- Skills mention tools by name (Codex, Antigravity, hosted models). Check each tool's own terms before sending it any data.
