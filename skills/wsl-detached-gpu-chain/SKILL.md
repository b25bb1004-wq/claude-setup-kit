---
name: wsl-detached-gpu-chain
description: Launch a long GPU or eval job inside WSL from a Windows Claude session so it survives the tool call. Use whenever a job in WSL must outlive the shell (training, rollouts, eval chains) and when a background job "vanishes".
---
# Detached WSL jobs

- Call: `wsl -d <distro> -u <user> -e bash -lc 'cd ~/proj && setsid nohup bash scripts/X.sh > ~/logs/X.log 2>&1 & sleep 3; pgrep -af X.sh'`. Without `setsid nohup` and the short `sleep`, the WSL session ends and kills the child.
- Chain steps in one script with a final `echo "$(date -u +%H:%M:%S) <name> finished" | tee -a ~/logs/chain.log` marker; poll the marker, not the process.
- Check the GPU first (`gpu-job-preflight`): one GPU job at a time on a 12 GB card.
- Python heredocs inside `bash -lc`: quote the heredoc (`<<'EOF'`) so `$` is not expanded; pipe through `tr -d '\0'` when output comes back from wsl.exe. For anything with prose, write the script with the file tool instead.
- Reading WSL files from Windows tools: `\\wsl$\<distro>\home\<user>\...` works for Read and Edit.
