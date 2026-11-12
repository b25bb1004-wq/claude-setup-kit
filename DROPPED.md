# Skills not shipped

Every folder in the source `~/.claude/skills/` that is not in `skills/` is listed here with a one-line reason. `scripts/check_coverage.py` checks this file against a skills folder.

## Own skills: dropped or merged

| Source skill | Reason |
|---|---|
| commit-attribution-check | Merged into `verify-before-commit-push`; the original held a personal name and email. |
| gdrive-ranged-download | Merged into `download-from-gdrive-onedrive-blocked`. |
| soup-cli-gotchas | Specific to one personal fork of a CLI. |
| (withheld 1) | Instructions for one private project tool; not reusable. Name withheld because it names the project. |
| (withheld 2) | Project state for one competition track, not a skill. Name withheld. |
| (withheld 3) | Controls one private multi-agent setup; its reusable Codex flag lessons moved into `codex-health-check`. Name withheld. |

Withheld names are kept in a private list outside the repo; `scripts/check_coverage.py` reads it from the `COVERAGE_WITHHELD` environment variable (one folder name per line).

## Own skills: shipped under a new name

| Source skill | Shipped as | Why |
|---|---|---|
| (withheld 4) | product-red-team-panel | Project name removed from the skill and its folder name. |
| pc-claude-handoff | remote-claude-handoff | Machine-specific name removed. |
| reach-pc-tailscale | reach-remote-machine | Host and network names removed. |
| latex-on-windows-pc | latex-on-windows | Machine-specific name removed. |

## Third-party skills (install from upstream instead)

These were installed from other authors. They are not copied here because of licences and because upstream versions change. Reinstall them from their source.

| Source skill | Origin | How to get it |
|---|---|---|
| composition-patterns | Vercel agent skills | Install the `vercel` plugin (see plugins.md) or Vercel's agent-skills repo. |
| react-best-practices | Vercel agent skills (MIT) | Same as above. |
| react-view-transitions | Vercel agent skills (MIT) | Same as above. |
| web-design-guidelines | Vercel agent skills | Same as above. |
| writing-guidelines | Vercel agent skills | Same as above. |
| vercel-optimize | Vercel | Same as above. |
| higgsfield-brandkit | Higgsfield skills pack | Account-specific; comes with the Higgsfield connector or its skills pack. |
| higgsfield-faceless-video | Higgsfield skills pack | Same as above. |
| higgsfield-generate | Higgsfield skills pack | Same as above. |
| higgsfield-marketplace-cards | Higgsfield skills pack | Same as above. |
| higgsfield-product-photoshoot | Higgsfield skills pack | Same as above. |
| higgsfield-soul-id | Higgsfield skills pack | Same as above. |
| higgsfield-video-explainer | Higgsfield skills pack | Same as above. |
| higgsfield-websites | Higgsfield skills pack | Same as above. |
| higgsfield-youtube-thumbnail | Higgsfield skills pack | Same as above. |
| graphify | PyPI package `graphifyy` | `uv tool install graphifyy`, then copy its bundled SKILL.md (do not run its installer, see `install-agent-tools-safely`). |
| ui-ux-pro-max | Third-party UI/UX skill | Install from its upstream repo. |
| reverse-engineer-anything | npm `rea-agents` | `npm pack rea-agents@<version>` and copy `package/skills/reverse-engineer-anything/`. |
| scroll-craft | Third-party release | Upstream source not recorded; find the original before reinstalling. |
| llm-judge | Third-party (MIT) | Install from its upstream repo. |
| job-seeker-helper | Job-seeker skill pack | Upstream source not recorded. |
| cover-letter | Job-seeker skill pack | Upstream source not recorded. |
| interview-coach | Job-seeker skill pack | Upstream source not recorded. |
| job-application-tracker | Job-seeker skill pack | Upstream source not recorded. |
| resume-optimizer | Job-seeker skill pack | Upstream source not recorded. |
| socratic-tutor | Third-party | Upstream source not recorded. |

## Folders that are not skills

| Folder | Reason |
|---|---|
| learned | Empty folder used by a plugin for auto-learned notes. |
| synced | Built-in skills synced from claude.ai; they arrive with the account. |

Hidden folders (for example a `.trash` folder of archived skills) are skipped by the coverage check.
