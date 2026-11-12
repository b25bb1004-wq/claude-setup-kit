---
name: dependency-preflight
description: Get third-party model or research code running without relaunching it ten times. Use before running any repo or Hugging Face remote-code model, after the first ImportError, and when a pip install is slow or impossible on the target machine.
---
# Dependency preflight

**Failure:** a demo took eight relaunches, each fixing one missing package.

1. **List every import first.** `grep -rhE "^(import|from) " <repo>/*.py <pkg>/ | sort -u`, then test each module in the target interpreter in ONE loop and print all MISSING at once. Repeat for the packages those packages import.
2. **Do not install into a venv another job uses.** Put extras in a separate folder and run with `PYTHONPATH=~/extras:...` (extras come first on sys.path, so never ship a package that shadows a real one).
3. **Slow target network:** resolve and download on a faster machine. `pip install --target dir --no-deps ...` for pure-python packages; `pip download --platform manylinux_2_28_x86_64 --python-version 3.12 --only-binary=:all: --no-deps` for compiled ones (pick the manylinux wheel that bundles native libs). `pip install --dry-run --report r.json` shows the whole dependency set in one call. Then tar, copy, extract.
4. **Stubs only for modules that are truly never called**, and never for something `transformers` probes (a scipy stub broke it). Prefer a two-line patch of the one file that needs a function.
5. **Check the repo's loader against the installed library version before running.** Remote-code model classes often break across major `transformers` versions; plain weights can usually be loaded by building the model class from the repo's own package and calling `load_state_dict` (check 0 missing, 0 unexpected keys).
6. **Big downloads:** see `parallel-hash-verified-download` and `hf-download-xet-stall`.
7. **Shared GPU:** check free VRAM first; confirm a process exited before resuming another job.
8. **Sanity-check outputs before scoring them.** fp16 autocast once produced constant audio and a speech recogniser "scored" it with hallucinated words. One numpy check (RMS in a sane range, spectral centroid above 200 Hz, no NaN) would have caught it; fp32 fixed it.
9. Never `pkill -f` a pattern that also appears in your own ssh command line (the shell kills itself, exit 255); use exact PIDs.
