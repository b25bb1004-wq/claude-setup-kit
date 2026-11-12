---
name: study-artifact-handbook
description: Build a study or explainer artifact (HTML page) the user will accept, and check it properly before publishing. Use whenever the user asks for an "artifact so I can study", a pipeline or paper explainer page, or rejects a page design.
---
# Study artifact handbook

(The first two designs were rejected before this one was accepted.)

**Design:** a typographic handbook. No cards, rounded boxes, pills or tab rail. One accent colour, hairline rules, a left index rail that becomes a sticky top bar under 900 px, one continuous document with scroll-spy, a tick strip for progress. Fonts that worked: Archivo (headings), IBM Plex Sans, IBM Plex Mono labels, Instrument Serif italic for one headline word. Light and dark tokens on `:root`. Use `<details>` only for answers and deep dives.

**Content order:** (1) background topics from the basics, each with an intuition, a "for us" line, papers and a self-check; (2) the route chosen and why the others lose; (3) papers adopted and rejected, each with a reason and an evidence tag; (4) the final pipeline from basics: one worked example traced through every block, then per block intuition, what happens, example, papers, what breaks; (5) strategy threaded through, not a table of ideas. Always give an everyday picture first; "explained normally" was rejected.

**Check once, properly**
- A local file without a viewport meta shows the desktop layout in phone emulation. Test a copy with `<meta name=viewport content="width=device-width,initial-scale=1">` prepended.
- In chrome-devtools MCP, navigating to the same URL with a new hash does NOT reload; use a reload with `ignoreCache`.
- Overflow probe: report `innerWidth`, `documentElement.scrollWidth`, and every element with `scrollWidth > clientWidth` whose overflow-x is visible.
- CSS grid trap: items with an explicit row but auto column are placed first and can squeeze other cells; give every child an explicit column on mobile.

**Publishing:** edit the file and republish the same path to keep the URL. Do not change sharing; tell the user if it is shared by link.

**Cost lesson:** rewriting a 60 to 100 KB HTML file several times costs 20 to 30k output tokens each. Write the page once, then use small Edit calls plus a republish; batch searches; one screenshot per breakpoint.
