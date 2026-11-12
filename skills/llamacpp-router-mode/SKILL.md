---
name: llamacpp-router-mode
description: Run several GGUF models behind one llama-server that loads them on demand, one at a time, on a single 12 GB-class GPU. Use to chat with, benchmark, add, swap or unload local models, and before any GPU job that needs the card free.
---
# llama-server router mode

**Setup that works:** a script starts ONE llama-server on 127.0.0.1:8080 with `--models-preset ~/llm/models.ini --models-max 1 --sleep-idle-seconds 1800`. Models are sections in `models.ini` (e.g. `[coder]`, `[moe-35b]`, `[dense-8b]`) with `model = <path>`, plus `n-cpu-moe = 20` for MoE models, `ngl = 34..36` and `c = 4096` for large dense ones. A global `[*]` section: `ngl 99`, `fa on`, `ctk/ctv q8_0`, `c 8192`, `jinja`. From another machine: `ssh -N -L 127.0.0.1:8080:127.0.0.1:8080 <gpu-host>`, then http://localhost:8080 or POST `/v1/chat/completions` with `"model": "<section name>"`.

**Gotchas that cost time**
- `models.ini` is read at startup only. After adding a model, restart the router (kill the old one by PID); until then requests say `model 'x' not found`.
- Unload without restarting: `POST /models/unload {"model":"name"}`; `GET /models` shows the state. GPU memory drops within a few seconds; read it twice before calling the GPU free.
- Swaps take 10 to 16 s with a warm file cache, about a minute cold. Warm-load with a tiny chat request (`max_tokens` 4).
- Scripts that call the native `/completion` endpoint must send `"model"` in the body in router mode.
- Thinking models answer `''` if `max_tokens` is small: pass `chat_template_kwargs {"enable_thinking": false}` for exams.
- Dense models that spill half their layers to the CPU are slow (32B Q4 about 5 tok/s, 70B IQ2 about 2 tok/s); MoE models with few active params run 16 to 40 tok/s. Speeds drift between runs: re-measure before quoting.
- GPU jobs (vLLM evals, training) need the card free: unload all models first, and tell any other session using the router.
- A second llama-server on another port coexists with the router; kill it by exact PID, never `pkill -f`.
- The web UI is served gzip-only: plain `curl /` returns 415; use `curl --compressed` or a browser.
