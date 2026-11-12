---
name: cloud-environment-network-secret
description: Give a Claude cloud session (claude.ai/code) an API key without exposing it. Use when work must move to the cloud and needs a service key, or when the cloud session cannot reach an API host.
---
# Cloud session API keys via Network secrets

**Where:** claude.ai/code > environment selector > Cloud > the environment's gear > "Edit cloud environment". Rows: Network access, Network secrets, Setup script, Environment variables.

**Do**
1. Use **Network secrets**, not Environment variables. The env-variable box warns that anyone using the environment can see the values. A Network secret is injected by a proxy on requests to the host you list; the cloud session never sees the key.
2. Add the secret: type Bearer, Allowed websites = the API host only (check the URL your script calls first, e.g. `grep -o 'https://[^/]*' tools/client.py`), header Authorization, prefix Bearer, value = the key. Listing the host also lets the sandbox reach it (network access is limited by default).
3. The USER pastes the key into the form; agents must not enter keys into forms. If you help, copy it to the clipboard without printing it, and clear the clipboard afterwards.
4. Cloud code must call the host with NO Authorization header of its own; the proxy adds it. Make one tiny test call first and report success without printing headers.

**Limits**
- One secret per host+header. A second key for the same host needs a second environment.
- Save the environment dialog after adding the secret.
- Never put keys in git, notes, env variables, messages or transcripts.
