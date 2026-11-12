---
name: onedrive-chrome-download-queue
description: Download many large zips from an anonymous OneDrive folder through Chrome browser automation and process each on arrival. Use when a dataset of 10+ GB sits in a OneDrive share and curl gets 401/403.
---
# OneDrive folder to disk, one zip at a time

**Setup:** with browser automation connected to Chrome on the target machine, open the share link, open the folder, select ONE row by its left checkbox, click Download, then clear the selection with the "x selected" button at the right of the toolbar. A worker script on the machine waits for each `<name>.zip` to stop growing, then runs the per-file job (under a lock if it uses the GPU).

**Traps (each one cost a download or an hour)**
- Before clicking a row, zoom-check the selected row's NAME and size: the list scrolls after other clicks and rows shift by one. Selecting by a remembered position downloaded the wrong file twice.
- Deselect with the "x selected" button, not by clicking the old checkbox. With several rows selected, Download builds a zip of zips: delete that partial at once.
- After about an hour clicks do NOTHING: the page session expired. Re-open the share link and the folder.
- A click can take 30 to 90 s to show a `.crdownload`; do not re-click (duplicates). Verify with a directory listing.
- Chrome temp files can stall (size frozen) or vanish. A stalled file is dead: delete it and re-request.
- A truncated zip can be saved under the final name. `unzip` fails fast; delete it, or a worker that skips existing files will never process the real one.
- Screenshots time out while a GPU job runs (Chrome renders on the GPU); `find` and JavaScript reads still work.
- Throughput was about 1 to 3 MB/s with two or three downloads at once; plan for many hours on tens of GB.
- Over ssh never `pkill -f name` with the name inside the same command string; use a launcher script file and exact PIDs.
