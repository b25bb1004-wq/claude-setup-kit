---
name: wsl-memory-cap-restart
description: Raise or change the WSL2 memory cap (.wslconfig) without killing a running GPU chain or losing SSH. Use before any `wsl --shutdown`, .wslconfig edit, Docker Desktop start, or when a task needs more than the default WSL RAM (half of host RAM).
---
# Changing the WSL memory cap safely

- The default cap is 50 percent of host RAM. The setting is `memory=24GB` under `[wsl2]` in `%USERPROFILE%\.wslconfig` (from WSL: `"$(wslpath "$(cmd.exe /c echo %USERPROFILE% | tr -d '\r')")/.wslconfig"`). Back it up first (`.wslconfig.bak-<date>`) and keep existing keys such as `networkingMode=mirrored`.
- It only applies after `wsl --shutdown`, which kills EVERY WSL process (GPU jobs, vLLM, downloads) and any SSH route into WSL. Never run it from inside the SSH session you work in, and never while jobs run. Gate on the chain's finished marker and GPU memory back at baseline.
- If you work remotely, delegate the shutdown to a Claude session on that machine: give it the gating conditions, the verification list and the rollback (restore the .bak), and ask it not to start Docker. Remote Control session names change; list agents first.
- WSL does not restart by itself. A scheduled task that runs a keep-alive script (e.g. starting sshd in WSL every 10 minutes) brings it back; `schtasks /run /tn "<task>"` does it at once.
- Verify after: `free -g` shows the new total, SSH works, `nvidia-smi` sees the card, data folders intact. Background downloads and queued scripts died: relaunch them (HF downloads resume).
- Docker Desktop shares the same WSL2 VM and memory cap; do not start it while a chain runs.
