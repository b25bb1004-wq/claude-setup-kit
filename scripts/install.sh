#!/usr/bin/env bash
# Copy the kit's skills and templates into ~/.claude without overwriting anything.
# Usage: bash scripts/install.sh [--dry-run] [--vault DIR]
#   --dry-run    show what would be copied, change nothing
#   --vault DIR  also copy vault-template/ to DIR (skipped if DIR exists)
# Target: $CLAUDE_HOME if set, else $HOME/.claude
set -euo pipefail

kit="$(cd "$(dirname "$0")/.." && pwd)"
target="${CLAUDE_HOME:-$HOME/.claude}"
dry=0
vault=""
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run) dry=1 ;;
    --vault) vault="${2:?--vault needs a directory}"; shift ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
  shift
done

copied=0; skipped=0
copy_new() { # src dest
  if [ -e "$2" ]; then
    echo "skip (exists): $2"; skipped=$((skipped + 1))
  else
    echo "copy: $2"; copied=$((copied + 1))
    if [ "$dry" -eq 0 ]; then mkdir -p "$(dirname "$2")"; cp -R "$1" "$2"; fi
  fi
}

if [ "$dry" -eq 1 ]; then echo "DRY RUN: nothing will be written"; fi
echo "target: $target"

for d in "$kit"/skills/*/; do
  name="$(basename "$d")"
  copy_new "${d%/}" "$target/skills/$name"
done
copy_new "$kit/templates/CLAUDE.md" "$target/CLAUDE.md"
copy_new "$kit/settings.example.json" "$target/settings.example.json"

if [ -n "$vault" ]; then
  copy_new "$kit/vault-template" "$vault"
fi

echo "done: $copied copied, $skipped skipped"
echo "Next: merge settings.example.json into settings.json by hand, then install plugins (plugins.md) and MCP servers (mcp.md)."
