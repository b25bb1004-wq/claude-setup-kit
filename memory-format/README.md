# Auto-memory format

Claude Code keeps a per-project auto-memory folder (for example `~/.claude/projects/<project-key>/memory/`). This setup uses a fixed format so memories stay short, findable and linkable. Only the format is shown here; the examples are invented.

## Files

- `MEMORY.md`: the index. One line per memory, loaded into every session, so keep each line short.
- `<slug>.md`: one memory per file, with frontmatter.

## Index line

```markdown
- [Title](slug.md): one-line hook saying when this memory matters
```

Put the most important entries ("START HERE", "CURRENT") in the title so they stand out.

## Memory file

```markdown
---
name: Short title
description: "One sentence: what this memory is and when to read it."
metadata:
  node_type: memory
  type: feedback
---
Body in plain sentences. Absolute dates. Links to related memories or vault notes as [[note name]].
```

`type` is one of:

| type | Holds | Example |
|---|---|---|
| `user` | Who the user is and how they work: role, tools, standing preferences | "Prefers plain-language explanations over jargon." |
| `feedback` | A correction or rule the user gave, so it is not repeated | "Workers run on Haiku at medium effort unless told otherwise." |
| `project` | State of one project: paths, branch, what is done, what is blocked | "Backend migration on branch `x`, not pushed yet." |
| `reference` | Where something lives: a doc, a dashboard, a page id | "Course notes hub page ids for future updates." |

## Rules

- One fact in one place. If a memory and a vault note overlap, the memory points to the note with a [[link]].
- Update or delete a memory when it goes stale; do not add a second one that contradicts it.
- No credentials, no private health, money or marks details.
- Use absolute dates.

See `examples/` for an index and three invented memories.
