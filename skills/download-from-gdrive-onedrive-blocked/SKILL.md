---
name: download-from-gdrive-onedrive-blocked
description: Use when a Google Drive or OneDrive share link must be downloaded and curl saves a tiny HTML file, returns 401/403, or a browser download looks stuck. Covers Drive quota pages, ranged downloads, OneDrive anonymous folders and Chrome temp-file sizes.
---
# Dataset downloads from Drive and OneDrive

## Google Drive
- Probe first, download nothing: `curl -s -L -r 0-0 -D - -o /dev/null "https://drive.usercontent.google.com/download?id=<ID>&export=download&confirm=t" | grep -iE "HTTP|content-range|content-disposition"`. `Content-Range: bytes 0-0/<total>` gives the exact size and file name and shows the link is public.
- A real download can still return a 2 KB HTML page ("Quota exceeded ... Too many users have viewed or downloaded this file recently"). Check with `head -c 4 file | xxd` (`3c21 444f` = `<!DO`). Do not loop retries.
- **Ranged workaround:** small range requests (`curl -r 0-16777215`) often return real bytes while the full request gets the quota page. 4 to 16 MiB ranges worked, 32 MiB did not, and after a burst even 16 MiB failed again. A script that appends only chunks of exactly the wanted size that do not start with `<!DOCTYPE`, backs off (60 s, then 600 s) and resumes by file size can crawl through; for popular files it may make almost no progress.
- Fallbacks: the owner or user makes a copy into their own Drive and shares that, or downloads in a normal browser. Use `curl -L -C -` and verify the exact byte size against the probe.

## OneDrive (1drv.ms share links)
- The API share URL returns 401 and `download.aspx` returns 403 to curl (it needs the browser cookie). WebFetch only sees a page shell.
- An anonymous folder opens in Chrome (browser automation). Select exactly one file by its row checkbox and click Download in the top bar. Multi-select makes OneDrive build a zip of zips. See `onedrive-chrome-download-queue` for many files.
- Chrome's `.crdownload` size does NOT grow until the end; the finished file appears minutes later. Do not re-click: each click queues another full download.
- Wait with a file-exists loop, move into the working folder, unzip into a fresh directory, and `cmp` duplicates before deleting.
