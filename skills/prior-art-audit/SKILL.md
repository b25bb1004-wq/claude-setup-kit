---
name: prior-art-audit
description: Check whether a research or competition idea is already published before claiming novelty, with cheap verified citations. Use before scoring novelty, naming a lead contribution, writing a "what is new" section, or trusting another agent's literature claims.
---
# Prior-art audit

(A first novelty judgement was overrated until 13 targeted searches found the collisions.)

1. **Read the rubric first.** What earns novelty points (e.g. "meaningful adaptation" vs "new insight in depth"; a clear negative result may count), and which side criteria (efficiency, latency) are credited.
2. **Search the claim, not the topic.** One web search per claim, phrased as the sentence you would put in the report; several searches in one turn. Expect recent preprints that collide.
3. **Verify ids and read abstracts cheaply:** `curl -s -L "https://export.arxiv.org/api/query?id_list=ID1,ID2,...&max_results=100"` (use https and -L; plain http returned nothing and made every id look fake). Parse `<title>`, `<published>`, `<summary>` with Python. 70 ids fit in one call; sleep 3 s between calls.
4. **Tag every claim** `[abs]` abstract read, `[search]` summary only, `[mem]` unchecked, and keep a `refs_verified.txt`. "None found" means searches, not a literature review; say so.
5. **Catch other agents' misquotes:** a worker model cited a number for the wrong experimental condition. Open the abstract before repeating any number.
6. **Re-score novelty after the search and recompute weighted tables by script.** Hand arithmetic slipped three times; `python3 -c` the weights.
7. **Output:** claim | nearest prior art with id and date | what is left for us | level. When the method space is crowded, reframe the contribution as a controlled study or a protocol insight.
