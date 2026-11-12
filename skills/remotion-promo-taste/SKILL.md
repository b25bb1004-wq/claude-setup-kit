---
name: remotion-promo-taste
description: Make a promo or edit video with Remotion that does not look AI-generated. Use for any short promo, reel or title film; it holds the art direction rules, a sound design recipe and the render-and-check loop that worked.
---
# Promo video that reads as designed, not generated

**What read as AI (feedback: "too much AI"):** neon cyan and magenta, glowing text, RGB-split slams, perspective grids, vignette plus scanlines, bouncy springs, everything centred, a generic EDM loop.

**What worked:** an editorial spec-sheet direction.
- Flat paper (#eeeae1) and ink (#0f0f0e) alternating by scene, ONE signal-orange accent (#ff4b14) used sparingly.
- Helvetica Neue bold for statements, a serif italic for one emphasis word, a mono face for labels; left-aligned type on a 96 px margin; small chrome (scene label, timecode, 2 px progress line).
- Text rising out of overflow masks (cubic ease-out, 7 to 14 frames), no overshoot; technical line drawings via `pathLength={1}` dash offsets; data-shaped visuals instead of decoration.
- Film grain: `ffmpeg -f lavfi -i "color=c=0x808080:s=512x512,noise=alls=40:allf=u"` as a tiled PNG with multiply/screen blend at 5 to 8 percent.
- Hard cuts only, on a beat grid: 90 bpm at 30 fps = 20 frames per beat, scenes of 2 to 9 beats.

**Content rule:** spectacle, not test numbers; show the good parts; every claim still true (do not imply something is fast if it is not; avoid numbers you cannot defend).

**Setup:** `npm i remotion @remotion/cli react react-dom typescript @types/react`, `src/index.ts` (registerRoot), `src/Root.tsx` (Composition 1920x1080, 30 fps). `npx tsc --noEmit -p .` before rendering; `npx remotion render src/index.ts Promo out/p.mp4 --codec h264 --crf 17` (about 40 s for 28 s of video).

**Sound (numpy, no samples):** a script writing a stereo WAV to `public/`, used via `<Audio src={staticFile("x.wav")} />`: a thock (sine 140 to 50 Hz, 160 ms + click) on every cut, a sub kick every 2 beats, rising ticks per element, 6 ms noise clicks while text types, plucks on beats with a short noise-convolved reverb, one long impact on the final cut, a 55 Hz drone bed. Check levels with `ffmpeg -i out.mp4 -af volumedetect -vn -f null -` (peak about -1 dB).

**Check loop:** render, extract one mid-animation and one end-state frame per scene (`ffmpeg -ss T -i out.mp4 -frames:v 1 -vf scale=800:-1 f.png`), look at them, fix collisions, re-render. Keep the previous version.
**Fonts:** system fonts only; avoid Georgia for numbers (old-style numerals make "0" read as "o").
