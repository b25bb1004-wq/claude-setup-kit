# Requirements

Versions are what the source machine (Windows 11 with WSL2) had on 2026-11-12. Newer versions should work. Install only what the skills you use need.

## Core

| Tool | Version seen | Install (Windows / macOS) | Needed for |
|---|---|---|---|
| Claude Code | 2.1.322 | `npm install -g @anthropic-ai/claude-code` or the native installer from the Claude Code docs | Everything. |
| Git | 2.55.0 | `winget install Git.Git` / `brew install git` | Version control; Git Bash is the Bash tool on Windows. |
| Node.js | 26.4.0 | `winget install OpenJS.NodeJS` / `brew install node` | `npx`-based MCP servers, the token-optimizer status line. |
| Python | 3.14 (Miniconda) | `winget install Anaconda.Miniconda3` / `brew install python` | Kit scripts, many skills (`python3` on macOS and Linux). |
| uv | 0.11.28 | `winget install astral-sh.uv` / `brew install uv` | Python environments and tools (`uv tool install`). |
| GitHub CLI | 2.96.0 | `winget install GitHub.cli` / `brew install gh` | PRs, issues, private repo access. |

## Optional, by skill

| Tool | Install | Used by |
|---|---|---|
| ffmpeg (9.0 seen) | `winget install Gyan.FFmpeg` / `brew install ffmpeg` | Video and audio skills, the watch plugin. |
| bun | `powershell -c "irm bun.sh/install.ps1 \| iex"` / `brew install oven-sh/bun/bun` | The vercel plugin. |
| WSL2 + Ubuntu 24.04 | `wsl --install -d Ubuntu-24.04` | All `wsl-*` and GPU skills on Windows (`wsl`, `wsl.exe`). |
| Docker Desktop | `winget install Docker.DockerDesktop` | Sandboxed tools (for example Strix). |
| MiKTeX | `winget install MiKTeX.MiKTeX` | `latex-on-windows` (`pdflatex`, `initexmf`). |
| clangd | `winget install LLVM.LLVM` / `brew install llvm` | The clangd-lsp plugin. |
| Obsidian | `winget install Obsidian.Obsidian` / `brew install --cask obsidian` | Browsing the vault (agents edit the files directly). |
| Tailscale | `winget install Tailscale.Tailscale` / `brew install --cask tailscale` | `reach-remote-machine`, `remote-job-launch-and-poll`. |
| restic | `winget install restic.restic` / `brew install restic` | Backups. |
| graphify | `uv tool install graphifyy` (two y's) | Code graphs; see `install-agent-tools-safely`. |
| rea-agents | Runs through `npx -y rea-agents@<version>` (Node.js) | REA MCP server, see `mcp.md`. |
| Codex CLI | `npm install -g @openai/codex` | `delegate-labour`, `codex-health-check`. |
| Antigravity CLI (`agy`) | Separate CLI; install it from the Antigravity docs (the Windows IDE install does not include it) | `delegate-labour`. |
| NVIDIA driver + CUDA 12.8+ (in WSL: driver on Windows only) | NVIDIA website | GPU skills (vLLM, llama.cpp, training); gives `nvidia-smi`. |
| Hugging Face CLI (`hf`) | `uv tool install "huggingface_hub[cli]"` | Model downloads (`hf-download-xet-stall`, `parallel-hash-verified-download`). |
| vLLM | `uv pip install vllm` (Linux or WSL) | `vllm-*` skills, `forced-choice-transfer-eval`. |
| llama.cpp + CMake | `winget install Kitware.CMake` / `brew install cmake`, then build llama.cpp from source | `llamacpp-*` skills. |
| Jupyter | `uv pip install jupyterlab ipykernel nbconvert` | `wsl-torch-cu128-env-setup`. |
| poppler (`pdftoppm`, `pdftotext`) | `brew install poppler` / `winget install oschwartz10612.Poppler` | Lets the Read tool open PDFs; `pdf-to-text-macos`. |
| Ghostscript (`gs`) | `brew install ghostscript` / `winget install ArtifexSoftware.GhostScript` | PDF compression and checks (`pdf-to-text-macos`). |
| SQLite CLI (`sqlite3`) | `brew install sqlite` / `winget install SQLite.SQLite` | `codex-health-check`. |
| Standard Unix tools | Built into macOS, Linux and WSL; Git Bash has most on Windows | `bash`, `ssh`, `rsync`, `curl`, `grep`, `sed`, `perl`, `ps`, `pgrep`, `pkill`, `lsof`, `ip`, `setsid`, `nohup`, `timeout`, `zsh` (`setopt`), `osascript` (macOS only), `schtasks` (Windows only). |

## Check what you have

```sh
claude --version; git --version; node --version; python --version; uv --version; gh --version
```
