---
name: remote-job-launch-and-poll
description: Launch a long job on a remote machine over ssh and watch it without hanging or self-matching. Use when starting training, pip installs or downloads on another machine and polling their logs.
---
# Launch and poll long remote jobs

- **Launch detached:** `ssh -f host 'cd ~/dir && . venv/bin/activate && nohup python x.py > run.log 2>&1 < /dev/null &'` returns at once and the job survives. Alternatively `ssh host '(setsid nohup bash job.sh > /dev/null 2>&1 < /dev/null &); sleep 2; echo launched'`. A plain `nohup cmd &` inside a longer command can hold the ssh session (and the tool call) until timeout.
- **Poll the log, not the process:** `ssh host 'tail -n 5 ~/dir/run.log'`. `pgrep -f "pip install"` inside the same ssh command matches the ssh shell's own command line, so a wait loop never ends. Use `ps | grep "[N]AME"` (bracket trick) or a marker line in the log (`grep -q RESULT`).
- **Bounded waits in one call:** `for i in $(seq 1 14); do ssh host 'grep -q saved log' && break; sleep 20; done` (under the tool time cap), then print the last lines. A foreground `sleep N; check` is blocked by the harness; long waits go in `run_in_background`.
- **Do not block the user:** after launching, say what runs and where the log is; check the first 40 s of the log to catch a broken run early, then poll sparingly.
- **Timed-out compound commands:** if `ssh ... & echo launched; git commit ...` times out, later steps may silently never run. Verify each step afterwards (`git log --oneline -1`, `ls` the output).
- **Slow hybrid-attention models:** warnings that `causal_conv1d` or `flash-linear-attention` are missing mean slow reference kernels (see `fla-kernels-qwen35-training`).
