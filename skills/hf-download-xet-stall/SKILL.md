---
name: hf-download-xet-stall
description: Hugging Face snapshot_download stuck at 0 bytes with a .incomplete blob and no progress. Use when a model download hangs for minutes.
---
# HF download stalls on the xet backend

**Symptom:** `du` of the cache stays at a few hundred MB, `blobs/*.incomplete` is 0 bytes, the progress bar sits at "15/18 files".
**Fix:** kill the python process by PID and rerun with `HF_HUB_DISABLE_XET=1 HF_HUB_ENABLE_HF_TRANSFER=0` and `max_workers=4`; an 11 GB model then finished in minutes.
**Also:** pipe progress output through `tr "\r" "\n" | grep -v "%|"`, or one `snapshot_download` log can cost 30 KB of context.
If a single connection crawls, see `parallel-hash-verified-download`.
