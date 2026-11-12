---
name: gpu-job-preflight
description: Check the GPU and running jobs before launching any GPU job (vLLM eval, llama-server, llama-bench, training), and put timeouts on benchmarks that cross a slow link. Use before every GPU launch on a single consumer card and when a job fails with "CUDA device busy" or hangs while loading weights.
---
# GPU job preflight

**Failures:** (1) a vLLM eval died with "CUDA device busy or unavailable" because a stuck `llama-bench` still held the GPU. (2) An RPC benchmark sat loading weights over an ssh tunnel for about 10 minutes because a large rsync saturated the uplink, and it blocked everything behind it.

**Before launch**
1. `nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader; nvidia-smi --query-compute-apps=pid,used_memory --format=csv`. Under WSL, `nvidia-smi` lives at `/usr/lib/wsl/lib/nvidia-smi` and per-process memory shows N/A, but a listed PID still means something holds the GPU. "Free" = only the desktop's baseline is used.
2. Find holders by PID file or a specific pattern; kill in a SEPARATE ssh call (a `pkill -f` inside the same command line kills the ssh shell, exit 255).
3. One big GPU job at a time on a 12 GB card: stop a local chat server before an eval or training run; restart it after.
4. Anything that moves weights across the network (llama.cpp RPC) needs a hard timeout (`timeout 300 ...`) and must not run while a big transfer saturates the link. Prefer models that fit on one machine.
5. Chain jobs in a script with exit markers per step so one failure does not silently stall the rest (`overnight-gpu-chain`).
6. After any GPU job, confirm memory is back down before the next.
