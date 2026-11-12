---
name: vllm-lora-silent-mismatch
description: A LoRA adapter trained with HF/PEFT shows no effect when served with vLLM `--adapter`/LoRARequest, or two different adapters give identical dev numbers. Use before trusting ANY adapter evaluation through vLLM, and whenever a fine-tune "did nothing".
---
# vLLM silently ignored the LoRA adapters

**Symptoms:** two very different adapters gave the same dev scores as the untrained base; each changed exactly the same small set of greedy answers (numeric noise from the LoRA code path, not learning); mean output length unchanged; yet in PEFT the same adapter cut held-out loss by about two thirds. vLLM logged no error.

**Cause:** the adapter was trained on the text-only view of a multimodal model (`base_model.model.model.layers.N...`) but vLLM loaded the multimodal checkpoint (`model.language_model.layers.N...`). The names never matched, so nothing was applied.

**Do, every time**
1. Before any gate, compare the adapter run's outputs with the base run's. If (almost) no answers differ or summary statistics are unchanged, the adapter is not applied.
2. Cross-check one number in a second path (PEFT held-out loss on unseen examples) before believing "no gain".
3. Fix: merge into the ORIGINAL checkpoint with the correct tensor names and serve the merged folder as a normal model (W' = W + alpha/r * B@A in fp32, keep shard names, copy tokenizer and config, assert every adapter pair found its weight). Then evaluate with no `--adapter`.
4. Rename runs made through the broken path (`INVALID_...`) so nobody quotes them.

**Result once merged:** the adapter that had been judged "no gain" gave a large real improvement. A wrong gate can reverse a research conclusion. Log every "no gain" with the evaluation path used.
