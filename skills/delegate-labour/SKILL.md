---
name: delegate-labour
description: Hand well-specified, testable labour (scripts, downloads, profiling, boilerplate, tests) to an external coding agent CLI (Codex, Antigravity `agy`, Gemini CLI) to save Claude tokens. Use when a task has a clear brief and acceptance tests; keep design, review and gate-critical code on Claude.
---
# Delegate labour to other agents

**Why:** Claude usage is the scarcest budget; labour with a clear brief can go elsewhere.

## Workers (check what is installed: `which codex agy gemini`)
- **Codex CLI**, non-interactive: `codex exec -C <dir> -m <model> -c model_reasoning_effort="medium" -s workspace-write --skip-git-repo-check -o <report_file> "<prompt>"`. Always pass the model and effort explicitly; the config default may be an expensive model.
- **Antigravity CLI `agy`**, headless: `agy -p "<prompt>" --model <id> --output-format text` (also `--mode plan|accept-edits`, `--add-dir`, `--effort`). List models with `agy models`. Do not use `--dangerously-skip-permissions` unless the user says so. Short inline questions worked better than "do this brief file" for agy.
- **Gemini CLI**: similar headless use.
- Preflight every worker with a one-line smoke test ("reply with OK") before giving it real work; if it fails, do the labour yourself and note it.

## Protocol
1. Claude writes `briefs/<id>.md` with the deliverable, files it may touch, and acceptance tests.
2. Run the worker detached (background), cwd = the workspace, prompt = "Do briefs/<id>.md".
3. The worker writes `reports/<id>.md` (max 10 lines). Claude reads ONLY that report plus the diff of gate-critical files.
4. Claude runs the tests itself; never trust "passed" without running them.

**Launch notes:** a background launcher's "completed" notice fires when the shell exits, not when the worker finishes; check the process and the report file. Some CLIs need a git workspace or a flag to skip that check.

**Never delegate:** design decisions, reading that needs judgement, correctness review of gate-critical code, anything involving private notes.
**Privacy:** workers are other vendors' models. Send only public or already-scrubbed text; no credentials in prompts (keys via env vars); never copy a private repo into a worker workspace without the user's explicit approval.
**Routing:** log which worker did what and how it went, so routing improves over time.
