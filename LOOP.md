# LOOP: Claude Setup Kit

## Goal
A local git repo that packages a Claude Code setup (skills, plugins, MCP, subagents, settings, CLAUDE.md template, memory format, vault template, requirements, installers) and is safe to publish: no personal names, paths, hosts, IPs, keys, private projects, marks, health or money details. Local commits only; no remote, no push.

## Checklist
1. Every skill has valid frontmatter `name` (equal to its folder) and `description`. Check: `python scripts/validate_skills.py`.
2. Install scripts run in a temp home without errors, overwrite nothing, and skip and report existing items. Check: dry run, real run, rerun of `install.sh` (temp `HOME`) and `install.ps1` (temp `-Target`), with a pre-existing `CLAUDE.md` and one pre-existing skill folder.
3. Sanitizer has 0 hits. Check: `python scripts/sanitize.py` with the private term list (kept outside the repo) in `SANITIZE_TERMS`.
4. Every file in the README folder map exists. Check: parse the map table and test each path.
5. `DROPPED.md` covers every source skill not shipped. Check: `python scripts/check_coverage.py ~/.claude/skills` with the withheld-name list in `COVERAGE_WITHHELD`.
6. `settings.example.json` is valid JSON. Check: `python -c "import json; json.load(open('settings.example.json'))"`.

## Tasks
- T1 Skills: classify every source skill; ship generic ones after scrubbing, generalise personal ones, drop or merge the rest.
- T2 Docs: `plugins.md`, `mcp.md`, `subagents.md`, `requirements.md`, `settings.example.json`, `templates/CLAUDE.md`.
- T3 Memory format and vault template.
- T4 Scripts: installers, validator, coverage check, sanitizer.
- T5 README, LOOP, checks, commit.

## Budget
About 600k tokens for the whole build. Workers: none used (see log).

## Log
- 2026-11-12: Worker preflight. `agy` smoke test FAILED: the Antigravity CLI is not installed on this machine (only the IDE launcher exists, and nothing in WSL). All labour was done by the orchestrator itself. No text of any kind was sent to an outside service.
- 2026-11-12: T1 done. 70 skills shipped (16 as-is after a light scrub, 54 generalised), 6 own skills dropped or merged, 4 renamed, 26 third-party skills not shipped (licences; reinstall from upstream). One own skill (`install-agent-tools-safely`) was missed in the first pass and added after the coverage check found it.
- 2026-11-12: Repo-local git identity set to a neutral name and a noreply address so commit metadata carries no personal identity.
- 2026-11-12: `agents.md` renamed to `subagents.md`: on a case-insensitive file system Claude Code reads `agents.md` as `AGENTS.md` project instructions.
- 2026-11-12: First sanitizer run: 7 hits (four private project names in `DROPPED.md` skill names, a Windows user path and a WSL user path in two skills, an em dash literal in the sanitizer source). All fixed: names withheld into a list outside the repo, paths rewritten with `%USERPROFILE%`, the em dash built with `chr(0x2014)`.
- 2026-11-12: Checks run: 1 PASS (70 skills, 0 problems); 2 PASS (bash and PowerShell: dry run writes nothing, real run 71 copied and 2 skipped, rerun 0 copied); 4 PASS (20 of 20 paths); 5 PASS (0 not covered); 6 PASS. Item 3: see `SANITIZE.md` from the final run before commit.

## Round 2 (2026-11-12, budget about 400k tokens)

### Goal
Licence, skill review, a benchmark suite, a commit identity with no personal data, a sanitizer pass over the tree and the whole history, then a private GitHub repo.

### Checklist
7. MIT `LICENSE` added; skills with no stated compatible licence are not in the repo; two personal-workflow skills removed and listed in `DROPPED.md`.
8. Skill review: valid frontmatter, no references to files or skills not in the repo, no commands for tools missing from `requirements.md`. Check: `bench/test_static.py`.
9. `bench/` holds static tests, a 30-prompt trigger benchmark runner and a README; one smoke run (2 prompts, both configs) in `bench/results/smoke`.
10. Sanitizer: 0 hits on the tree and on every commit's identity, message and patch.
11. Private GitHub repo created and `main` pushed, only if 10 passes.

### Log
- agy: looked again. No `agy` or `antigravity` on PATH; the IDE folder's `bin` has only the `antigravity-ide` editor launcher (no headless prompt mode); nothing in `~/.local/bin` or WSL. Review done by the orchestrator: script checks in `bench/test_static.py` plus a read of every skill (each was read in full while being generalised in round 1).
- Review fixes: `requirements.md` gained the tools skills actually call (Hugging Face CLI, vLLM, CMake, Jupyter, poppler, Ghostscript, SQLite, graphify, rea-agents, standard Unix tools) and a corrected `agy` row; `parallel-hash-verified-download` now says `pdl.py` is the script you write from its design.
- Third-party skills with unknown upstream (scroll-craft, socratic-tutor, the 5-skill job-seeker pack) were never copied; `DROPPED.md` now marks them "Upstream unknown, reinstall from source". `profile-polish-with-evidence` and `friend-ssh-link` removed (68 skills shipped).
- Licence holder and commit identity: the GitHub login contains the same string as an institute student ID, which is on the scrub list. Putting the login in `LICENSE` or in commit metadata would put that ID in the repo and its history, so the holder is "The claude-setup-kit authors" and the commit identity stays neutral. The user decides whether to accept that or re-author.
- Bench smoke run: first two attempts failed (Python resolved `bash` to the WSL launcher; a comment swallowed the prompt argument). Fixed with `shutil.which` and the prompt on stdin. Third and fourth attempts ran clean: kit has 85 skills available vs 17 for vanilla, so isolation works. In one attempt the kit fired the expected skill and in the other it did not, which shows answers vary between runs.
- Checks: 7 to 9 PASS (7/7 static tests, coverage 0 uncovered, smoke run 0 errors). 10 and 11: see the final report.

## Status
All six checklist items checked by the orchestrator, not by worker claims. Unfinished: nothing in scope. Open decisions for the user are in the final report (licence, unknown upstreams of some third-party skills, whether two personal-workflow skills should be public).
