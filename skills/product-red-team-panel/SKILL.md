---
name: product-red-team-panel
description: Red-team a PRODUCT (its demos, numbers, claims, code, PDF), not just the idea, with a fixed panel of adversarial personas, and turn every objection into the failure bank. Use before any external showing (professor, investor, hackathon), after a big change, or when asked to "challenge" or "stress test" the product.
---
# Product red-team panel

Adapted from multi-agent "seed, personas, simulate, report, interview" workflows; no extra software needed.

1. **Seed:** collect claims and evidence, not the pitch. List every claim as one line with its evidence file ("verified correct 0.43 on fresh items, one run, LLM-written questions").
2. **Personas** (fixed panel, one prompt each): sceptical professor (is the test valid?), investor (is this a product, what is the moat, what does a user pay for?), working user (does it save time, does it lie?), citation or output auditor (find a fabricated or mis-attributed output that got through), data-leak reviewer (private data, keys, web access defaults), competitor (why not the obvious existing tool?), operations engineer (does it run without your special hardware?).
3. **Attack:** each persona must try to break a specific claim using only evidence in the repo and name the file or number it used. No generic criticism. Run real probes where cheap: a fake citation, an out-of-scope question, a two-source question, a prompt-injection sentence inside an input document.
4. **Report:** one table per persona: claim attacked, result (held / broke / unknown), evidence path, fix proposal. Rank by damage to the product, not by cleverness.
5. **Interview:** re-ask a persona about its worst finding before accepting it; drop objections that rely on facts not in the evidence.

**Rules**
- Every finding that broke goes into `failures.jsonl` with cause `product_challenge:<persona>` and is replayed after the fix (`failure-bank-loop`). Wrong objections are kept, marked `rejected` with the reason.
- The persona that proposes a fix does not grade it; rerun the probe on fresh items and report both outcomes.
- Cheap or local models can play personas; you chair. Never send private notes or keys to any persona.
- Output: a one-page report; numbers only where they decide something.
