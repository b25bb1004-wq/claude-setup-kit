---
name: mac-shell-gotchas
description: Fix the macOS and zsh traps that break background jobs, rsyncs, process checks and python installs on a Mac. Use before launching a detached job, an rsync, a process search or a pip install on macOS.
---
# macOS and zsh traps

- **No `setsid` on macOS.** Detach with `nohup ./job.sh < /dev/null > job.out 2>&1 &` (a `setsid` launch fails silently). On Linux hosts `setsid` exists: `ssh host '(setsid nohup job.sh > /dev/null 2>&1 < /dev/null &); sleep 2; echo launched'`.
- **No `timeout` binary** (exit 127). Use `perl -e 'alarm N; exec @ARGV' cmd ...` or a background job with a PID.
- **`rsync` is openrsync:** no `--append-verify`. Use `rsync -a --partial -e "ssh -o BatchMode=yes -o ServerAliveInterval=30"` inside a retry loop (Wi-Fi drops it). It first re-reads the half already sent (looks stalled), then sends the rest.
- **zsh does not word-split variables:** `for p in $pids` loops once over the whole string. Use `${=pids}` or an array; same for option lists (`ssh $=O host`).
- **zsh expands unquoted globs in arguments:** `grep -rn pat . --include=*.md` fails with "no matches found"; quote it (`--include='*.md'`).
- **BSD sed:** `sed -i` needs `-i ''`; otherwise it eats the expression ("unterminated substitute pattern"). Prefer a small `python3 -` edit for multi-line changes.
- **Process searches:** a tunnel started as `ssh -o ... -N -R ...` does not match `grep "ssh -N"`. Use `ps aux | grep "[s]sh .*-R"` or `lsof -iTCP -sTCP:LISTEN`. Never declare a tunnel dead from one grep.
- **`pgrep -f`/`pkill -f` inside your own command matches your own shell** (exit 144 locally, 255 over ssh; the rest never runs). Use the bracket trick (`ps -axo pid,command | awk '/[j]obname/{print $1}'`) and kill exact PIDs, or use PID files.
- **Pause a transfer:** `kill -STOP <rsync pid>` then `kill -CONT` frees the link without losing progress.
- **Waiting:** a foreground `sleep N` is blocked by the harness. Use `until <check>; do sleep 20; done` with `run_in_background: true`.
- **System python lacks most packages:** make a venv in the session scratchpad (`python3 -m venv $S/venv && $S/venv/bin/pip install reportlab pypdfium2`). Homebrew tools live in `/opt/homebrew/bin`.
- **Detach remote jobs** with `ssh -f host 'nohup cmd > log 2>&1 < /dev/null &'`; a plain `ssh host 'cmd &'` can hang.
- When giving the user `! ssh ... 'cmd'` lines, double-check the closing quote.
