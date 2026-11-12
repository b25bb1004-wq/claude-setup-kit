---
name: vllm-run-crash-cleanup
description: A vLLM job (rollout, eval, benchmark) crashed, hung, or looks "running" with a traceback in its log. Use to find out if it is really dead, free the GPU by exact PID, and relaunch; also for context-length crashes on a few huge prompts.
---
# vLLM run crashed but the GPU is still held

**Symptoms:** the log ends with `VLLMValidationError: ... maximum context length is 6144 tokens ... prompt contains at least 6145 input tokens`; the launcher says the process is still running; `nvidia-smi` shows most of the card used.
**Why:** one over-long prompt kills the generate call, but the main python process may hang, and the child `VLLM::EngineCore` is re-parented to PID 1 and keeps the GPU after the parent dies.

**Do**
1. Look at the log tail, not at `pgrep`. `pgrep -f <module>` over ssh matches the ssh shell's own command line and always says "running". Use `ps -eo pid,etime,cmd | grep "[p]ython -m <module>"` and `ps -eo pid,ppid,cmd | grep "[E]ngineCore"`.
2. Kill by exact PID (`kill <python pid> <EngineCore pid>`), wait about 7 s, then check `nvidia-smi --query-gpu=memory.used` is back near the desktop baseline. Never `pkill -f`.
3. Fix the cause instead of only raising `--max-model-len` (the next crash was a prompt one token over the new limit). Tokenize the rendered prompts, skip those over `max_model_len - 256`, print and record the count (e.g. `skipped_too_long` in metrics.json).
4. Relaunch detached (`ssh -f host 'cd ... && nohup python ... > log 2>&1 < /dev/null &'`) and read the first 80 s of the log to confirm the fix took.
5. Run `gpu-job-preflight` first if anything else (a llama-server router) could hold the card.

**Adapters:** `enable_lora=True, max_lora_rank=<r>` must be set; also see `vllm-lora-silent-mismatch`.
**After killing an eval by PID** to free the GPU for something else, also kill the orphan EngineCore and wait until memory is back to baseline; record the killed run so it can be rerun.
