---
name: llamacpp-split-inference
description: Build and run llama.cpp across two machines (e.g. Apple Metal plus a CUDA box) with RPC, fetch GGUF files, and estimate tokens/s. Use for any local-LLM speed test, a 70B split, speculative decoding or llama-bench work.
---
# llama.cpp split inference

- **Build only what you need:** `cmake --build build --target llama-server llama-cli llama-bench ggml-rpc-server -j 6`. The RPC server target is `ggml-rpc-server`, NOT `rpc-server` ("No rule to make target"). CUDA builds need `export PATH=/usr/local/cuda/bin:$PATH`.
- **Launch detached over ssh:** see `remote-job-launch-and-poll`.
- **Downloads:** fetch big GGUFs on the machine with the fastest internet (`curl -L -C - -o file URL`, resumable), then `rsync -a --progress` over the LAN. A bad URL returns a 29-byte "401" file: check size and `curl -sIL` first. Not every quantiser publishes every model; confirm the repo exists.
- **Estimate, then measure:** a simple estimator from model size, each tier's memory bandwidth and network latency is optimistic. A real two-machine RPC split lost about 50 percent of decode speed. Calibrate with `llama-bench` `tg128`.
- **MoE on a 12 GB GPU:** start with `--n-cpu-moe 28` and lower it until VRAM is about 11 GB (e.g. `--n-cpu-moe 20`: about 37 tok/s for a 35B with few active params). Weights that fit on one machine should not be split over RPC.
- **RAM matters for CPU-offloaded layers:** check whether XMP/EXPO is enabled; DDR5 running at its fallback speed costs real tokens/s.
- **WSL memory cap** defaults to half of host RAM; raising it needs `wsl --shutdown` (see `wsl-memory-cap-restart`).
- **Shell traps:** zsh does not word-split `$var` (use arrays or `${=var}`); macOS has no `setsid` (`setsid nohup ... &` silently does nothing there; use `nohup bash -c '...' < /dev/null > /dev/null 2>&1 &`). Always `ls -la` the target 5 s later to confirm bytes are arriving.
- `pkill -f`/`pgrep -f` inside an ssh command string matches the ssh shell itself (exit 255): kill in a separate call or use PID files.
- MMLU letter scoring: see `eval-harness-sanity-check`.
