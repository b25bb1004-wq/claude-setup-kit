---
name: web-animation-integration-gotchas
description: Bugs that appear when several workers' animation files (GSAP, cursors, canvas) are integrated into one page, and how to check motion in a throttled test browser. Use when building or reviewing a scripted or cursor-driven web page, splitting text into letters, animating charts, or screenshotting motion.
---
# Web animation integration gotchas

## Bugs seen, each with its fix
- **Gradient headline goes invisible after letter splitting.** `background-clip: text` on the heading does not paint through `display: inline-block` children. Put the gradient, `background-clip: text` and transparent fill on each `.letter`. Do not set `will-change: transform` on them.
- **Split letters break words mid-word.** Every inline-block letter is a break opportunity. Wrap each word's letters in `span.word { display: inline-block; white-space: nowrap }`.
- **Bars vanish after the chart animation.** `clearProps: 'all'` removes the whole inline style, including custom properties such as `--w` that carry the bar width. Clear only what the tween set (`clearProps: 'transform'`).
- **Phone page gets a sideways scroll from cursors.** `position: fixed` elements moved past the right edge widen the layout viewport on mobile. Put them in a fixed, inset 0 layer with `contain: strict`.
- **Killed tweens never resolve.** `gsap.killTweensOf` does not fire `onComplete`, so an awaited tween promise hangs. Never await across a reset; block the rebuild control while a run is active.
- **Stale continuations after a skip.** A `.then` attached to an animation still runs after the run was stopped. First line of every continuation: return if the run was stopped.
- **Everything hidden if the engine fails.** Hide content only under a class that JS adds when motion is on, and give every run a `finally` that shows all content. Add a short safety net that unhides if the engine is not ready.
- **Display fonts with a letter-like zero** are wrong for email addresses and numbers; use the text face there.

## Checking motion through chrome-devtools MCP
- The automated browser often runs at about 4 fps and clamps `setTimeout` to 1 s (window occluded), so GSAP time crawls. After load run `gsap.ticker.lagSmoothing(0)`, then wait with an async `evaluate_script` and screenshot.
- Per-frame lerps and trail fades still look wrong at 4 fps. Do not judge pacing or smoothness there; say so and let a human look at 60 fps.
- Reduced motion: patch `window.matchMedia` with a `navigate_page` `initScript`.
- Phone: `emulate` takes the string form `390x844x2,mobile,touch`. Check `document.documentElement.scrollWidth` against `innerWidth`.
- Wait for a state class (`.built`) in a polling `evaluate_script` rather than guessing sleep times; return log lines and counts as data, then take one screenshot.

## Parallel build pattern that worked
Write one spec with a fixed DOM contract (ids, classes, data attributes) and the `window.*` API of each file, then let one worker per file write against the contract at the same time. The orchestrator fixes one-line CSS integration issues itself; each real defect goes back as an exact, numbered fix list.
