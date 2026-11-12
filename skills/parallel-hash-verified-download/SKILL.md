---
name: parallel-hash-verified-download
description: Download multi-GB model weights when a single Hugging Face connection crawls or the internet drops. Use when `snapshot_download` or `hf download` stalls, runs under 1 MB/s, or a model of 10+ GB is needed on a slow link.
---
# Parallel, resumable, hash-verified download

**Symptom:** the Hugging Face CDN gave about 60 KB/s per connection and `snapshot_download` stalled at a few hundred MB. It was per-connection throttling: 8 parallel ranges gave about 3 MB/s, 24 workers about 4 MB/s.

**Downloader design (about 100 lines of Python)**
1. List files from `https://huggingface.co/api/models/<repo>/tree/main` (size and LFS sha256 for each).
2. Fetch each `.safetensors` file in 16 MiB range requests with 24 to 32 threads; write with `os.pwrite` into a pre-sized file.
3. Record finished chunks in `<file>.done`, so resuming = rerunning.
4. Check SHA-256 at the end and delete a mismatching file.
5. Fetch the small files (config, tokenizer) with `snapshot_download(allow_patterns=[...])`.
6. Send the auth header for gated repos from an env var, never a literal.

**Operate**
- The internet also drops: wrap it in a supervisor (`until grep -q DOWNLOAD_OK log; do python pdl.py ...; sleep 60; done`, started with `nohup`).
- `du -sb` on a pre-sized file shows the full size; measure progress with `du -sk` (blocks).
- Never use a third-party mirror without the SHA-256 check.
- Kill a stalled `snapshot_download` by exact PID (`ps -eo pid,args | grep "[s]napshot_download"`), never `pkill -f` over ssh.
- If you only need memory or speed numbers, skip the download: see `random-weight-limit-probe`.
