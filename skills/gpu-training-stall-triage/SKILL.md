---
name: gpu-training-stall-triage
description: Decide whether a long GPU training job is slow or hung when its log stops advancing. Use when a step counter has not moved for several expected step intervals but the process and GPU look busy.
---
# Slow or hung? (QLoRA on a 12 GB consumer card)

**Symptom seen:** log every 10 steps at about 70 s/step, then no new line for 35+ minutes. Process alive at 97 percent CPU, GPU 100 percent util, VRAM pinned near the limit, power only about 50 W.

## Checks, cheapest first (read-only)
1. Log cadence: `stat` the log, compare mtime with the last step; compute when the next line was due from the previous gaps.
2. Who owns the GPU: `nvidia-smi --query-compute-apps` and `ps --sort=-rss` for stragglers (an orphan vLLM EngineCore, a second driver).
3. Power vs util: real training draws well above 100 W on such a card. 100 percent util at about 50 W with VRAM constant near the limit means spinning or spilling into system memory (WDDM fallback under Windows/WSL), not working.
4. CPU ticks rising (`/proc/PID/stat` fields 14+15) mean a busy-wait; they do not prove progress.
5. Wait one more expected interval before acting.

**If still silent:** kill the training process by exact PID (not pkill). Retry with a shorter `--max-len`, a smaller accumulation, and a heartbeat print every step. Logging every 10 steps is too coarse for a 70 s step.

## Root cause in the case above: memory blow-up on the longest example
- `peft.prepare_model_for_kbit_training` casts every bf16 parameter to fp32 (a tied 248k-vocab embedding alone is about 2.4 GiB). SDPA cannot use flash attention in fp32, so attention falls to the math kernel and materialises fp32 [heads, L, L] matrices in backward. Peak grows with L squared; the longest example needed far more than the card, so the driver paged to system memory and crawled.
- Warning sign: the allocator warns ONCE ("allocation failed with OOM") and then stays silent; the stall begins when the shuffled order reaches the longest example. Reproduce the order with the same seed to find that step.
- **Prevention:** (1) log a heartbeat per example with its length and peak allocated memory, and fit peak against length in the first minute; (2) run one forward+backward+optimizer step on the LONGEST example before the loop; (3) set `--max-len` from that fit; (4) watchdog: no heartbeat for 300 s (1200 s before the first line) means kill by exact PID.
- **Better recipe:** skip `prepare_model_for_kbit_training`; `requires_grad_(False)` on all params, `gradient_checkpointing_enable(use_reentrant=False)`, `enable_input_require_grads()`, `torch.backends.cuda.enable_math_sdp(False)` to fail fast; keep bf16 so flash attention is used. The longest example then fit at about a third of the memory and ran faster.

## Watchdog and allocator traps
- `nvidia-smi` "memory used" is NOT what a job needs: PyTorch's caching allocator grows to whatever is free. A "kill above 11.7 GB" rule killed healthy runs. Use heartbeats, a wall-time cap and the job's own `torch.cuda.max_memory_allocated()` (print it at exit with `atexit`; SIGKILL skips atexit).
- `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` makes a job that needs about the whole card fail FAST (internal assert or "device not ready") under WSL2; the default allocator spills silently instead. Use the variable on purpose for limit probes; unset it to learn the true peak of a job that does not fit.
- A memory probe must include the optimizer step: Adam allocates its state on the first `opt.step()`. A probe that passed forward+backward died at the first update. Leave 0.5 GiB margin or use paged/8-bit Adam, a lower LoRA rank, or CPU offload.
