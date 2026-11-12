---
name: remote-claude-handoff
description: Hand running work to a Claude session on another machine (e.g. a GPU desktop running Remote Control) when your laptop must go offline. Use when the user says to transfer work to the other machine, shut the laptop, or "keep working" while away.
---
# Handing work to another machine's Claude

**Reality check first:** a live local session cannot be moved to the cloud, and a cloud session usually cannot reach a machine on a private LAN. The remote machine keeps running its own jobs; its Claude can supervise them. Say this plainly before the handoff.

**Order**
1. Push the vault, write the current state and lessons into the vault's resume note, and add new skills to the skill library note.
2. Copy new skills to the other machine (`rsync -rt --no-perms --no-owner --no-group` onto a Windows drive path; never `--delete` on its skills folder). Fetch its vault clone rather than pulling blindly: it may hold an unpushed local commit.
3. Message the remote session (Remote Control sessions get renamed: list agents and pick the online idle one). The first line says what the message is. Attachments by `@file` may not arrive, so put the text in the message. Nothing reports back automatically; ask it to write progress into a vault note and commit locally.
4. Tell the user the one command to check on return (e.g. `ssh <host> 'tail <chain log>'`).

**Message contents (self-contained):** running jobs with exact PIDs, log paths, what "healthy" looks like, the open question, the fallback action and who may take it, the rules below, where state lives, what to write back and where.

**Rules to repeat to the remote Claude:** no pushes (commit locally, the user pushes); no `pkill` (exact PIDs); do not edit a script a running bash is reading; the test set was used once and must not be rerun for selection; follow the user's commit-attribution rule; no credentials in notes; private notes never leave the user's own sessions.

**Never ask the peer to do something that was denied in your own session** (permission laundering); route that to the user.
