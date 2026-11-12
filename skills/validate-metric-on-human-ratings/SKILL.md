---
name: validate-metric-on-human-ratings
description: Before trusting any automatic quality metric or judge (TTS MOS, pronunciation, similarity), search for a public corpus of real human ratings and test against it. Use when building an evaluator where only synthetic checks are available.
---
# Validate on real human ratings, not only synthetic degradations

**What happened:** a speech-naturalness judge looked good on physics-defined degradation ladders (noise, reverb, clipping): Spearman about 0.75, pair accuracy 0.95. On a public corpus of real native-listener ratings, the same experts scored 0.05 to 0.14 in one language and 0.4 to 0.66 in another. In the first language no acoustic expert could tell real recordings from TTS, while listeners rated real speech far higher.

**Rules**
1. Search for human-rated corpora first (one web search plus `HfApi().list_datasets(search=...)`). Ungated datasets download in minutes.
2. Controlled degradations prove an expert is monotone in a physical factor. They do not prove agreement with people. Report both, labelled differently.
3. Compute the human ceiling (split-half Spearman over raters) before judging a score.
4. Check the corpus before blaming the judge: look at anchor clips and per-system means per rating file; panels differ.
5. Evaluate fusion with leave-one-text-out AND leave-one-system-out; the second is the honest test for unseen systems.
6. Metrics trained on signal quality miss pronunciation and prosody. Add a real-vs-synthetic probe and phone-level experts.
