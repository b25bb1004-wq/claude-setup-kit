# Benchmarks

Two parts: free static tests, and a skill-trigger benchmark that calls Claude and spends real usage.

## 1. Static tests (free)

```sh
python -m pytest bench/test_static.py      # or: python bench/test_static.py
```

They check that:
- every skill has valid frontmatter (`scripts/validate_skills.py`);
- the sanitizer finds nothing (`scripts/sanitize.py`; set `SANITIZE_TERMS` to a private term list kept outside the repo to include personal terms);
- `install.sh` and `install.ps1` work in a temporary folder: a dry run writes nothing, a real run copies everything but skips and reports existing items, a rerun copies nothing;
- skills refer only to shipped skills and files;
- every command a skill runs is either a shell basic or named in `requirements.md`;
- the benchmark's own parser and grader behave.

The installer tests are skipped where `bash` or PowerShell is missing.

## 2. Skill-trigger benchmark (spends usage)

`bench/prompts.jsonl` holds 30 prompts. 24 are labelled with the skill that should fire, 6 should fire no skill. Some have a `grader` (a regex the final answer must match), so task success can be checked mechanically.

`bench/run_bench.py` runs each prompt headless with `claude -p --output-format stream-json --verbose` (the last line of that stream is the same result object `--output-format json` prints, and the stream also shows which skills were called). Each prompt runs once in each of two isolated config folders, set through `CLAUDE_CONFIG_DIR`:
- `kit`: an empty config with this kit installed by `scripts/install.sh`;
- `vanilla`: an empty config with nothing added.

Neither config sees your real `~/.claude` (skills, plugins, MCP servers, CLAUDE.md).

### Run it

```sh
# smoke test first: 2 prompts x 2 configs = 4 calls
python bench/run_bench.py --out bench/results/smoke --ids p01,n01 --auth-file ~/.claude/.credentials.json --workdir /path/to/empty-folder

# full run: 30 prompts x 2 configs = 60 calls
python bench/run_bench.py --out bench/results/full --auth-file ~/.claude/.credentials.json --workdir /path/to/empty-folder
```

Options: `--model` (default `haiku`, the cheapest), `--limit N`, `--ids p01,p02`, `--configs kit,vanilla`, `--timeout` seconds per call.

**Auth.** A fresh config folder has no login. Either export `ANTHROPIC_API_KEY` or `CLAUDE_CODE_OAUTH_TOKEN` (from `claude setup-token`), or pass `--auth-file` with your own credentials file. That file is copied into each temporary config folder for the run, deleted afterwards, and never written to the results. On macOS the login lives in the keychain, so use one of the environment variables.

**Workdir.** Claude Code also loads `CLAUDE.md` (and `AGENTS.md`) files from the folders above the working directory. Pick an empty folder with none above it, or both configs will see those instructions and the comparison is skewed.

### Read the report

Each run writes `runs.jsonl` (one row per prompt and config) and `report.md`:

| Column | Meaning |
|---|---|
| Runs / Errors | Calls made; calls that ended with an error (auth, timeout, crash). Fix errors before reading anything else. |
| Trigger accuracy | For labelled prompts: the first skill called is the expected one. For "none" prompts: no skill was called. |
| False fires | Of the prompts that should fire nothing, how many called a skill anyway. |
| Graded success | Of the prompts with a grader, how many answers matched it. |
| Mean wall s | Average wall-clock seconds per call. |
| Tokens | Input + output + cache creation + cache read tokens, summed over the runs. |
| Cost USD | `total_cost_usd` from the result object (an estimate; on a subscription it shows usage, not a bill). |

`skills_available` in `runs.jsonl` shows how many skills each config had; if `kit` is not about 68 higher than `vanilla`, the install did not take.

Vanilla can never fire a kit skill, so its trigger accuracy only counts the "none" prompts. The interesting comparisons are graded success, false fires, and the token and time cost of carrying 68 skill descriptions. Model answers vary run to run: the smoke run fired the expected skill on one attempt and not on another. Repeat the full run two or three times before drawing conclusions.

## Results

- `results/smoke/`: the only run made so far, 2 prompts x 2 configs, to prove the runner works. It is not a benchmark result.
