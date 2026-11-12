---
name: reversible-file-tidy
description: Tidy Finder, Desktop, Downloads or home folders for the user ("clean my desktop, organise as per my folders, put garbage away"). Use for any bulk file move; gives a log, an undo script and Trash instead of rm.
---
# Reversible file tidy

1. Survey read-only first: `ls` Desktop, Downloads, Documents and the user's existing top-level folders. Sort into the folders THEY already have; make a new folder only for a clear group.
2. One script (`setopt null_glob` in zsh), a `mv1 SRC DESTDIR` helper using `mv -n` (never overwrite) that skips existing destinations, appends each move to `~/Documents/organize_log_<date>.tsv`, and appends the reverse `mv -n` line to `~/Documents/undo_organize_<date>.sh`.
3. "Garbage" = move to `~/.Trash` (recoverable), never `rm`: installers (.dmg), partial downloads, empty dirs, stubs. Add a time suffix on name collisions.
4. Skipped duplicates: `cmp -s` the two files. Identical: Trash the extra. Different: leave both and tell the user.
5. Ambiguous items (zips, datasets, installers of the user's own apps) are left and listed; ask. Check an installer folder's real contents before judging it.
6. "Important folders on screen" = Finder aliases on the Desktop: `osascript -e 'tell application "Finder" to make new alias file at desktop to POSIX file "<folder>"'`.
7. Repos scattered in the home folder: report copies, branch, commit count and dirty count; do not move them without a go-ahead (notes may hold their paths).
8. Report counts, what was Trashed, what was left, and the undo command.
