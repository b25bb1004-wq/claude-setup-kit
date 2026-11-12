---
name: overnight-gpu-chain
description: Run a multi-stage GPU pipeline unattended (train, evaluate, retrain, test) so the card never idles while you sleep. Use when more than two GPU jobs depend on each other, or the user says to keep working overnight.
---
# Resumable overnight chain

**Pattern**
- One driver script, launched detached: `ssh -f host 'cd proj && nohup bash scripts/overnight.sh > log 2>&1 < /dev/null &'`.
- Every stage is a function run by `stage NAME fn`, which logs BEGIN/END with the exit code, re-reads a plain `VAR=value` env file (so you can change learning rate or ratios between stages without restarting), and checks a `STOP` file so you can halt cleanly. A failed stage never stops the chain.
- Every stage skips work whose output already exists (`metrics.json`, `train_log.json`, `model.safetensors`), so rerunning the driver resumes.
- Wait on ARTIFACTS, not PIDs: `until [ -f out/train_log.json ]; do sleep 30; done` (a PID check can match its own shell).
- Small helpers: one script per single eval, one report script that writes a markdown table with gates.

**Before chaining:** smoke-test each new script on a tiny slice so the 3 a.m. failure is not a typo. Run the held-out TEST only once, for configs chosen on dev, and report every config that ran.

**Operate:** poll with bounded loops under the tool time cap, read the chain log, update the vault at milestones. GPU stages run one at a time; light CPU work can overlap.

## Editing or restarting a running driver
- `rsync` replaces a file by rename, so a RUNNING bash keeps executing the OLD content. Restart the driver (stages are resumable). Child scripts called fresh each stage DO pick up edits.
- `nohup bash x.sh &` leaves TWO processes (the `bash -c` wrapper and the real one). Kill both by exact PID (`ps -eo pid,ppid,lstart,args | grep "[x].sh"`) before relaunching, or two drivers will hit the GPU together.

## Flaky internet
- Set `HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1` in unattended chains whose models are cached.
- Supervise downloads with a retry loop (`parallel-hash-verified-download`) and guard training with a log-silence watchdog (kill by exact PID after 300 s of silence, 1200 s before the first line).
- A chain you must pause for a higher-priority job gets a STOP file it checks in its wait loops, not a kill.
