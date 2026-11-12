---
name: tool-gate-and-monitor-traps-windows
description: Use when Write/Bash is blocked by a "Fact-Forcing Gate" hook, Monitor or sleep behaves oddly, or `wsl` commands fail with "execvpe(bash) failed" on a Windows machine running Claude Code.
---
# Claude Code tool traps on Windows

- **GateGuard "Fact-Forcing Gate"** (a plugin hook) blocks the FIRST Bash call of a session and the FIRST Write of each new file. Facts typed in the same turn before the call do not help: the call errors once, then the retry after you state the facts works. For files under `~/.claude/skills` it also wants a real search this turn (Glob or Grep; `cat` in Bash does not count), the harness that loads the file, the behaviour it changes, and the user's instruction quoted. Do the Glob/Grep first, state the facts, then write the full file once. A stub Write is wasted.
- **WSL default distro may be `docker-desktop`**, which has no bash: `execvpe(bash) failed`. Always name the distro: `wsl.exe -d <distro> -e bash -lc '...'`.
- **Heredocs through Git Bash:** prose with apostrophes inside a quoted heredoc that is itself inside a larger quoted command fails with "unexpected EOF while looking for matching quote" and creates nothing. Use the Write tool for any file with prose.
- **Background jobs started with `nohup ... &` inside one `wsl -e bash -lc` call die** when that call returns. Use the Bash tool's `run_in_background: true` with the command in the foreground of that call, or `setsid nohup ... & sleep 3` (see `wsl-detached-gpu-chain`).
- **Monitor runs in Git Bash**, so `~` is the Windows home, not the WSL home. For WSL files call `wsl.exe -d <distro> -e test -f /home/<user>/...` inside the until-loop. Monitors may expire after about 5 minutes; re-arm or check once with a plain command. `sleep N; cmd` chains are blocked.
- Waiting and polling burn tokens: start the job, arm one Monitor, stop talking.
- Edit needs the file read with the Read tool first; reading via `cat` in Bash does not count.
