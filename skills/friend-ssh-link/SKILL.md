---
name: friend-ssh-link
description: Set up, use and fully tear down a temporary SSH link to a collaborator's laptop so their Claude and yours can work on a shared task. Use only when the user asks and the collaborator consents; includes the Windows traps and the permission-classifier blocks.
---
# Temporary SSH link to a collaborator's machine

**Rules**
- The collaborator consents and does their own steps (give them a prompt for their Claude).
- One dedicated key pair per task: `ssh-keygen -t ed25519 -N "" -C task-name -f ~/.ssh/<task>_ed25519`.
- Their `authorized_keys` line starts with `restrict,pty`. Only one shared folder is touched.
- Nothing from your private notes or other keys crosses.
- At the end the key, helper script and known_hosts entries are deleted, and the collaborator removes the key line and files.

**Windows hosts**
- Default ssh shell is `cmd`: no `;` (use `&` or `&&`), `cd /d "%USERPROFILE%\shared-task"`, quote usernames with spaces (`"first last"@host`). `scp file "user@host:shared-task/"` works (relative paths start in their home folder).
- Admin accounts need the key in `C:\ProgramData\ssh\administrators_authorized_keys` (fix permissions with icacls).
- Allow port 22 for the local subnet only, network profile Private. A timeout later usually means they switched sshd off, not a fault.

**Test order:** `nc -vz host 22`; compare the fingerprint they quote (`ssh-keygen -lf key.pub`); a read-only command (`whoami`, list the folder, `where claude`); then `claude -p "task"` in the folder. Always use `-i key -o IdentitiesOnly=yes -o IdentityAgent=none -o UserKnownHostsFile=<own file> -o ForwardAgent=no`.

**One-way:** the link only reaches them. For replies use a mailbox file in the shared folder.

**Classifier blocks seen (do not route around; ask the user for a permission rule or to run the command with `!`):** creating a helper script that connects with the key ("Unauthorized Persistence"), starting a hub bound to a LAN address ("Expose Local Services"). Never expose a service on the LAN that can reach private workspaces.

**Teardown checklist:** stop anything you started by PID; delete invites, helper dir, key pair and known_hosts; delete files copied to their folder (or tell the user the collaborator must); ask them to remove the authorized_keys line and turn sshd off.
