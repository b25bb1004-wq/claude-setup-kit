---
name: gpu-sigstop-pause-hazard
description: Pausing a CUDA training job with SIGSTOP to let another job use the GPU, then resuming it hours later. Use before pausing, resuming or co-locating GPU jobs on a 12 GB-class card; a frozen job that resumed crashed and lost an hour of unsaved progress.
---
# SIGSTOP on a CUDA job is not a safe pause

**What happened:** a LoRA trainer that saved only at epoch end was frozen with SIGSTOP halfway through and held 7.8 GB for 7 hours. After SIGCONT, with a second GPU job frozen beside it, it ran 5 more minutes and died with `CUBLAS_STATUS_INTERNAL_ERROR`. All progress since the start was lost.

**Rules**
1. Never pause a long CUDA job for hours with SIGSTOP. Either let it finish, or checkpoint (save every N steps) and kill it.
2. A stopped process keeps its VRAM and its cached allocator blocks. PyTorch's cache grows to fill free memory (a 0.6B LoRA showed 11.9 GB used), so two jobs plus a stopped one do not fit.
3. Run GPU jobs one at a time. Gate the next job on a done marker (`until [ -f DONE ]; do sleep 30; done`).
4. Trainers that save only at the end must get a `--save-steps` before any long run.
5. After any SIGCONT, check the last 30 lines of the log (`grep -a Error`), not only the step counter.
