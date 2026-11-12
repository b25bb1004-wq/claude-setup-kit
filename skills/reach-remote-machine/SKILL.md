---
name: reach-remote-machine
description: Check whether a remote GPU machine is reachable (over Tailscale or the LAN) before sending heavy jobs, training, or a local model call to it. Use when ssh to the other machine times out or before dispatching remote work.
---
# Reach the remote machine

**Diagnose in one read-only command (from macOS; adapt flags on Linux):**
```
(tailscale status 2>&1 || /Applications/Tailscale.app/Contents/MacOS/Tailscale status 2>&1) | head -8
ping -c 2 -t 3 <REMOTE_IP> | tail -3
nc -z -G 3 <REMOTE_IP> 22 && echo ssh-open || echo ssh-closed
```

**Reading the result**
- "Tailscale is stopped": the user starts it (`! tailscale up` or the app). Do not start it yourself.
- Tailscale up, the remote is listed "offline, last seen Nh ago": the machine is off, asleep or off the network. Nothing to fix locally.
- Ping works, port 22 closed: the SSH server is not running.
- LAN route times out: the DHCP lease probably changed. Ask a session on that machine for `ipconfig`/`ip addr` and update `HostName` in `~/.ssh/config`.

**Notes**
- A Windows box with WSL can appear as two Tailscale nodes (Windows and the WSL distro); know which one runs sshd.
- WSL behind a Windows portproxy needs the proxy rule and the firewall rule; the WSL IP can change after restarts.
- Non-login ssh shells may lack tools on PATH (Node, `nvidia-smi` under WSL is at `/usr/lib/wsl/lib/nvidia-smi`): use absolute paths.
- If Tailscale slows the laptop's internet, prefer a direct LAN alias when both machines share a network, and only start Tailscale when needed.
- Report a failure in two lines and move on; do not loop retries. Copying credentials or testing through a tunnel may be blocked for agents; the user runs those with `!`.
