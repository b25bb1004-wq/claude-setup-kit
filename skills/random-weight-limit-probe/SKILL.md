---
name: random-weight-limit-probe
description: Find out whether a model size trains on your GPU, and at what sequence length, without downloading its weights. Use before committing to a bigger base model (9B, 14B, 27B), or when a training run died at an unknown memory edge.
---
# Random-weight limit probe

- Memory and seconds per step depend on shapes, not values. Build a bf16 checkpoint with the real architecture from the repo's `config.json` (respect tied vs untied head; norms = ones, special SSM params = zeros, everything else N(0, 0.02)), shard by shard in a few GiB of RAM, copying only the small config and tokenizer files. A 9B builds in about a minute.
- Then run your real training path on a few dozen real rows (the longest under each cap plus random ones) over a ladder of length caps (e.g. 6144, 4096, 3072), with a stall and peak-memory watchdog, and write a small report. Add rungs around the edge you find.
- Read it carefully: with `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` a job that needs the whole card FAILS fast instead of paging silently; that is the point.
- The probe must include the first `opt.step()` (Adam state). A 9B passed forward+backward at about 10.5 GiB on a 12 GB card and died at the first update. Record the cap where a full run trains cleanly.
- Count the vocabulary: an untied bf16 output layer for a 248k vocab is about 2 GB, so a 4-bit 9B already uses about 7 GiB after load.
- MoE and multimodal wrappers load through `AutoModelForCausalLM.from_config`.
