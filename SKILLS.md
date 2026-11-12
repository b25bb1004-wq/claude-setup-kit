# Skills index

68 skills: 16 shipped as-is after a light scrub, 52 generalised (personal paths, names and project details replaced with placeholders). Skills not shipped are listed in [DROPPED.md](DROPPED.md).

Most of these began as a logged failure: something broke, the fix was found, and the lesson was written down so the next session does not repeat it (see `log-failure-as-skill`).

| Skill | Status | What it is for |
|---|---|---|
| [answer-time-selection](skills/answer-time-selection/SKILL.md) | generalised | Pick the final answer from k sampled answers with a frozen scoring rule (verifier share, entailment, retrieval rank) instead of greedy decoding. |
| [archive-before-delete](skills/archive-before-delete/SKILL.md) | generalised | Clean up vaults, folders or notes when the user says "clear", "gone", "garbage" or "get rid of". |
| [bounded-delegation](skills/bounded-delegation/SKILL.md) | generalised | Plan research or labour fan-out so it cannot drain your daily and weekly usage limits. |
| [bounded-prompt-evolve-loop](skills/bounded-prompt-evolve-loop/SKILL.md) | generalised | Run a small self-improving agent loop on a model's system prompt with a mechanical judge and a promotion gate, within a fixed budget. |
| [check-vault-before-interpreting](skills/check-vault-before-interpreting/SKILL.md) | generalised | Resolve the user's shorthand (tool names, units, project nicknames) from the notes vault and memory before answering. |
| [claude-mcp-add-windows](skills/claude-mcp-add-windows/SKILL.md) | as-is | Use when adding an npx-based MCP server with `claude mcp add` on Windows and the stored command shows `D:/ C:/` instead of `/d /c`, or PowerShell says "unknown option '-y'" or "Invalid configuration". |
| [cloud-environment-network-secret](skills/cloud-environment-network-secret/SKILL.md) | generalised | Give a Claude cloud session (claude.ai/code) an API key without exposing it. |
| [codex-health-check](skills/codex-health-check/SKILL.md) | generalised | Diagnose "Codex keeps failing" by reading the Codex CLI's own log database instead of guessing. |
| [delegate-labour](skills/delegate-labour/SKILL.md) | generalised | Hand well-specified, testable labour (scripts, downloads, profiling, boilerplate, tests) to an external coding agent CLI (Codex, Antigravity `agy`, Gemini CLI) to save Claude tokens. |
| [dependency-preflight](skills/dependency-preflight/SKILL.md) | generalised | Get third-party model or research code running without relaunching it ten times. |
| [dev-win-not-replicating](skills/dev-win-not-replicating/SKILL.md) | generalised | Read a promotion gate result that passed on dev but fails on the held-out test, and decide what to do next. |
| [download-from-gdrive-onedrive-blocked](skills/download-from-gdrive-onedrive-blocked/SKILL.md) | generalised | Use when a Google Drive or OneDrive share link must be downloaded and curl saves a tiny HTML file, returns 401/403, or a browser download looks stuck. |
| [error-breakdown-before-training](skills/error-breakdown-before-training/SKILL.md) | generalised | A training round gave no gain, or you are choosing what to train next. |
| [eval-harness-sanity-check](skills/eval-harness-sanity-check/SKILL.md) | as-is | Before trusting or waiting on any benchmark or scoring script (MMLU letter scoring, HumanEval, pass rates), run it on 10 to 25 items and check the score is plausible. |
| [failure-bank-loop](skills/failure-bank-loop/SKILL.md) | generalised | Keep every failed task of a model or agent pipeline in a labelled failure bank and learn from it instead of discarding it. |
| [fla-kernels-qwen35-training](skills/fla-kernels-qwen35-training/SKILL.md) | as-is | Qwen3.5-style hybrid linear-attention models train slowly in transformers because they fall back to reference kernels. |
| [forced-choice-transfer-eval](skills/forced-choice-transfer-eval/SKILL.md) | generalised | Measure whether a fine-tuned small model transfers to another task without format-following hiding the result. |
| [gpu-job-preflight](skills/gpu-job-preflight/SKILL.md) | generalised | Check the GPU and running jobs before launching any GPU job (vLLM eval, llama-server, llama-bench, training), and put timeouts on benchmarks that cross a slow link. |
| [gpu-sigstop-pause-hazard](skills/gpu-sigstop-pause-hazard/SKILL.md) | as-is | Pausing a CUDA training job with SIGSTOP to let another job use the GPU, then resuming it hours later. |
| [gpu-training-stall-triage](skills/gpu-training-stall-triage/SKILL.md) | generalised | Decide whether a long GPU training job is slow or hung when its log stops advancing. |
| [handle-permission-blocks](skills/handle-permission-blocks/SKILL.md) | generalised | What to do when the permission classifier denies an action (credential leakage, exfiltration, self-modification, exposing services, auto-mode bypass). |
| [hf-download-xet-stall](skills/hf-download-xet-stall/SKILL.md) | as-is | Hugging Face snapshot_download stuck at 0 bytes with a .incomplete blob and no progress. |
| [install-agent-tools-safely](skills/install-agent-tools-safely/SKILL.md) | generalised | Install third-party Claude Code skills, plugins, MCP servers and CLIs (Context7, Graphify, Strix, REA, Magic MCP) without letting their installers edit your CLAUDE.md or hooks. |
| [latex-on-windows](skills/latex-on-windows/SKILL.md) | generalised | Compile LaTeX (resume, report) on Windows with MiKTeX. |
| [lead-part-strategy](skills/lead-part-strategy/SKILL.md) | generalised | Decide which part of a multi-part competition to lead with, using the problem statement's own scoring, pros and cons, rivals, and cheap pilots. |
| [lean-long-reads](skills/lean-long-reads/SKILL.md) | as-is | Read long documents, PDFs or tool output without burning tokens. |
| [llamacpp-router-mode](skills/llamacpp-router-mode/SKILL.md) | generalised | Run several GGUF models behind one llama-server that loads them on demand, one at a time, on a single 12 GB-class GPU. |
| [llamacpp-split-inference](skills/llamacpp-split-inference/SKILL.md) | generalised | Build and run llama.cpp across two machines (e.g. |
| [log-failure-as-skill](skills/log-failure-as-skill/SKILL.md) | as-is | After a tool failure or a hard step that took 2+ attempts to solve, write the fix down as a short generalised skill so it is not rediscovered. |
| [mac-shell-gotchas](skills/mac-shell-gotchas/SKILL.md) | generalised | Fix the macOS and zsh traps that break background jobs, rsyncs, process checks and python installs on a Mac. |
| [measure-before-trimming-context](skills/measure-before-trimming-context/SKILL.md) | generalised | Reducing Claude Code token or context overhead (token-optimizer audit, trimming skills, plugins, notes). |
| [nemotron-helper](skills/nemotron-helper/SKILL.md) | generalised | Use a cheap hosted LLM (e.g. |
| [obsidian-open-vault-windows](skills/obsidian-open-vault-windows/SKILL.md) | as-is | Use when registering an existing folder as an Obsidian vault on Windows from a script (the obsidian:// URI says "Vault not found", or Obsidian opens a Welcome or throwaway vault). |
| [onedrive-chrome-download-queue](skills/onedrive-chrome-download-queue/SKILL.md) | generalised | Download many large zips from an anonymous OneDrive folder through Chrome browser automation and process each on arrival. |
| [oracle-guided-sft-targets](skills/oracle-guided-sft-targets/SKILL.md) | generalised | Build supervised training targets from an environment's ground truth when self-distillation or rejection sampling gives no gain. |
| [overnight-gpu-chain](skills/overnight-gpu-chain/SKILL.md) | generalised | Run a multi-stage GPU pipeline unattended (train, evaluate, retrain, test) so the card never idles while you sleep. |
| [parallel-hash-verified-download](skills/parallel-hash-verified-download/SKILL.md) | generalised | Download multi-GB model weights when a single Hugging Face connection crawls or the internet drops. |
| [pdf-to-text-macos](skills/pdf-to-text-macos/SKILL.md) | as-is | Extract text from a PDF on macOS when the Read tool fails with "pdftoppm is not installed" and pdftotext/pypdf are missing. |
| [prior-art-audit](skills/prior-art-audit/SKILL.md) | generalised | Check whether a research or competition idea is already published before claiming novelty, with cheap verified citations. |
| [product-red-team-panel](skills/product-red-team-panel/SKILL.md) | generalised | Red-team a PRODUCT (its demos, numbers, claims, code, PDF), not just the idea, with a fixed panel of adversarial personas, and turn every objection into the failure bank. |
| [quality-loop](skills/quality-loop/SKILL.md) | generalised | Orchestrator-led build loop. |
| [random-weight-limit-probe](skills/random-weight-limit-probe/SKILL.md) | generalised | Find out whether a model size trains on your GPU, and at what sequence length, without downloading its weights. |
| [reach-remote-machine](skills/reach-remote-machine/SKILL.md) | generalised | Check whether a remote GPU machine is reachable (over Tailscale or the LAN) before sending heavy jobs, training, or a local model call to it. |
| [remote-claude-handoff](skills/remote-claude-handoff/SKILL.md) | generalised | Hand running work to a Claude session on another machine (e.g. |
| [remote-job-launch-and-poll](skills/remote-job-launch-and-poll/SKILL.md) | generalised | Launch a long job on a remote machine over ssh and watch it without hanging or self-matching. |
| [remotion-promo-taste](skills/remotion-promo-taste/SKILL.md) | as-is | Make a promo or edit video with Remotion that does not look AI-generated. |
| [report-pdf-reportlab](skills/report-pdf-reportlab/SKILL.md) | as-is | Build a crisp, human-looking results PDF (and optionally a matching shareable Claude Docs page) with reportlab. |
| [reranker-negative-result](skills/reranker-negative-result/SKILL.md) | generalised | Read before fine-tuning a cross-encoder reranker on mined hard negatives. |
| [reversible-file-tidy](skills/reversible-file-tidy/SKILL.md) | generalised | Tidy Finder, Desktop, Downloads or home folders for the user ("clean my desktop, organise as per my folders, put garbage away"). |
| [skill-vault-checkpoint](skills/skill-vault-checkpoint/SKILL.md) | generalised | Reminder to save skills and vault notes. |
| [sleep-recall-template-diversity](skills/sleep-recall-template-diversity/SKILL.md) | generalised | Weights-only memory (a "sleep-time" LoRA trained on stored facts) recalls facts under new question phrasings only if training used many phrasings. |
| [store-secret-from-clipboard](skills/store-secret-from-clipboard/SKILL.md) | generalised | The user puts an API key on the clipboard and says not to paste it in chat. |
| [study-artifact-handbook](skills/study-artifact-handbook/SKILL.md) | generalised | Build a study or explainer artifact (HTML page) the user will accept, and check it properly before publishing. |
| [token-budget-discipline](skills/token-budget-discipline/SKILL.md) | generalised | Keep an interactive session cheap. |
| [tool-gate-and-monitor-traps-windows](skills/tool-gate-and-monitor-traps-windows/SKILL.md) | as-is | Use when Write/Bash is blocked by a "Fact-Forcing Gate" hook, Monitor or sleep behaves oddly, or `wsl` commands fail with "execvpe(bash) failed" on a Windows machine running Claude Code. |
| [uav-geoloc-zero-shot-baseline](skills/uav-geoloc-zero-shot-baseline/SKILL.md) | generalised | Use when benchmarking place-recognition or cross-view CNNs (ResNet, MixVPR, CAMP) zero-shot on UAV-to-satellite datasets (AnyVisLoc, UAV-VisLoc) and reporting recall plus distance bands. |
| [validate-metric-on-human-ratings](skills/validate-metric-on-human-ratings/SKILL.md) | generalised | Before trusting any automatic quality metric or judge (TTS MOS, pronunciation, similarity), search for a public corpus of real human ratings and test against it. |
| [validate-worker-patches-on-real-data](skills/validate-worker-patches-on-real-data/SKILL.md) | generalised | Before merging a change proposed by a worker agent, a reviewer agent, or yourself that alters parsing, filtering, cache keys or any rule applied to saved model output, replay old versus new on saved real outputs and count what changes. |
| [vault-edit-safely-windows](skills/vault-edit-safely-windows/SKILL.md) | as-is | Use when editing a notes vault (or any git repo) from the Windows Bash tool and git shows a file as "Binary", a push is rejected, or `git stash pop` conflicts. |
| [verify-before-commit-push](skills/verify-before-commit-push/SKILL.md) | generalised | Guard commits and pushes against broken output and wrong attribution. |
| [vllm-lora-silent-mismatch](skills/vllm-lora-silent-mismatch/SKILL.md) | generalised | A LoRA adapter trained with HF/PEFT shows no effect when served with vLLM `--adapter`/LoRARequest, or two different adapters give identical dev numbers. |
| [vllm-run-crash-cleanup](skills/vllm-run-crash-cleanup/SKILL.md) | generalised | A vLLM job (rollout, eval, benchmark) crashed, hung, or looks "running" with a traceback in its log. |
| [web-animation-integration-gotchas](skills/web-animation-integration-gotchas/SKILL.md) | as-is | Bugs that appear when several workers' animation files (GSAP, cursors, canvas) are integrated into one page, and how to check motion in a throttled test browser. |
| [web-research-sweep](skills/web-research-sweep/SKILL.md) | as-is | Run a broad literature, model and vendor sweep (papers, open models, licences, prior art) cheaply and honestly. |
| [wsl-detached-gpu-chain](skills/wsl-detached-gpu-chain/SKILL.md) | generalised | Launch a long GPU or eval job inside WSL from a Windows Claude session so it survives the tool call. |
| [wsl-from-git-bash](skills/wsl-from-git-bash/SKILL.md) | as-is | Use when running a command inside WSL from the Windows Bash tool (Git Bash) and it fails with "syntax error near unexpected token" or "C:/Program Files/Git/home/..." paths. |
| [wsl-memory-cap-restart](skills/wsl-memory-cap-restart/SKILL.md) | generalised | Raise or change the WSL2 memory cap (.wslconfig) without killing a running GPU chain or losing SSH. |
| [wsl-torch-cu128-env-setup](skills/wsl-torch-cu128-env-setup/SKILL.md) | generalised | Use when creating a fresh PyTorch + Jupyter environment for a Blackwell GPU (RTX 50-series) in WSL with uv, or when uv/pip fails with "Failed to download distribution due to network timeout". |
