---
name: fla-kernels-qwen35-training
description: Qwen3.5-style hybrid linear-attention models train slowly in transformers because they fall back to reference kernels. Use when a HF/PEFT training run prints "causal_conv1d ... falling back" or "flash-linear-attention ... falling back", or before launching any such fine-tune.
---
# Faster hybrid linear-attention training without touching the serving venv

**Warning seen:** `chunk_gated_delta_rule is falling back to its reference PyTorch implementation ... install flash-linear-attention`.

**Fix that worked:** install into a SEPARATE folder with no dependencies, and add it to PYTHONPATH only for training:
```
mkdir -p ~/fla_pkg && cd ~/fla_pkg && pip download --no-deps flash-linear-attention fla-core
pip install --no-deps --target ~/fla_site fla_core-*.whl flash_linear_attention-*.whl
PYTHONPATH=.:$HOME/fla_site python -m your_project.train_lora ...
```
Measured on a 2B LoRA run: about 2.3x faster per step (17 s vs 38 s), same loss to 3 decimals, slightly lower peak memory. The first step is slower (kernel compile).

**Do not** `pip install flash-linear-attention` into the main venv with dependencies: it can pull a different torch/triton and break vLLM. `causal-conv1d` needs a CUDA build and was not tried.
**Run vLLM WITHOUT `fla_site`** on the path.
