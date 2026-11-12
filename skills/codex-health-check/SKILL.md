---
name: codex-health-check
description: Diagnose "Codex keeps failing" by reading the Codex CLI's own log database instead of guessing. Use when Codex tasks error, hang, or the user reports many Codex failures.
---
# Codex health check (read-only)

Codex logs every request to `~/.codex/logs_*.sqlite` (table `logs`: ts, level, target, feedback_log_body, thread_id). Query with `sqlite3 -readonly`:
```
D=~/.codex/logs_2.sqlite
sqlite3 -readonly $D "select level,count(*) from logs where ts>strftime('%s','now','-7 days') group by level;"
sqlite3 -readonly $D "select count(*),level,substr(replace(feedback_log_body,char(10),' '),1,170) from logs where level in ('ERROR','WARN') and ts>strftime('%s','now','-7 days') group by level,substr(feedback_log_body,1,90) order by 1 desc limit 14;"
sqlite3 -readonly $D "select strftime('%m-%d %H:00',ts,'unixepoch','localtime'),count(*) from logs where level='ERROR' and feedback_log_body like '%401%' group by 1;"
codex login status; codex --version
```
The third query shows auth-error episodes by hour. Long WARN lines hide the real message at the END: print `substr(body, length(body)-260)`.

**What real problems vs noise looked like**
- Real: a burst of "401 Unauthorized: invalidated oauth token" (fix: `codex logout && codex login`); intermittent `list_models` timeouts from a flaky network.
- Noise: "unknown feature key in config" (CLI vs app-server version skew), plugin manifest warnings, MCP AuthRequired for plugins you never logged into.
- Quota drain: check which model and effort the default config uses; worker runs should pass both explicitly (`-m <model> -c model_reasoning_effort="medium"`).
- Sandbox: `codex exec -s workspace-write` blocks loopback sockets (`listen EPERM`), so socket tests fail inside Codex; rerun tests outside the sandbox.
- `codex exec` refuses non-git folders unless you pass `--skip-git-repo-check`; a resumed turn (`exec resume`) also needs `--json` if your wrapper parses events, or every reply after a restart looks empty.
- Daemons hold the sqlite files open; stop them by exact PID (never `pkill -f`) before touching `~/.codex` state.

**Clearing Codex memory:** archive first (tar to a dated folder with a MANIFEST), then remove `memories*`, `history.jsonl`, `session_index.jsonl`, `sessions/`, `thread_history_*.sqlite*`. Leave auth, config, AGENTS.md, rules, skills and plugins.
