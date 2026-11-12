---
name: wsl-torch-cu128-env-setup
description: Use when creating a fresh PyTorch + Jupyter environment for a Blackwell GPU (RTX 50-series) in WSL with uv, or when uv/pip fails with "Failed to download distribution due to network timeout".
---
# PyTorch env for an RTX 50-series card in WSL

- Blackwell cards need a CUDA 12.8+ build: `uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128`, then check `torch.cuda.is_available()`. Do not use a repo's pinned old torch; import only its model files and keep the modern torch.
- Create: `cd <project> && uv venv --python 3.12 .venv && source .venv/bin/activate`.
- Failure: the CUDA wheels (cublas, cudnn, about 3 GB) hit "network timeout ... Try increasing UV_HTTP_TIMEOUT (current value: 30s)". Fix: `export UV_HTTP_TIMEOUT=600` and rerun; uv reuses cached wheels. Run it with `run_in_background: true`, log to a file, end with `echo PIP_DONE`.
- Register a kernel: `python -m ipykernel install --user --name <env> --display-name "<Env name>"`.
- Prove a notebook headless: `jupyter nbconvert --to notebook --execute --ExecutePreprocessor.kernel_name=<env> nb.ipynb --output nb.ipynb`. Serve locally only: `jupyter lab --no-browser --ip=127.0.0.1 --port=8899` in the background.
- Preflight the GPU first (`gpu-job-preflight`): about 1.8 GB used by the Windows desktop with no compute PIDs counts as free.
- Small traps: fvcore `FlopCountAnalysis` must get the `nn.Module` itself; fvcore counts MACs and skips small ops (say so); pandas `to_excel` needs `sheet_name=` as a keyword.
