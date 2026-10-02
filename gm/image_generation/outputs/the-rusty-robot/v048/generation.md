# the-rusty-robot v048

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "1. The handrails are not symmetrical. Both should go down to the last step. 2. There is a ghost image of the old lantern on the left. It should be removed" / "3. Th overhang under the sign also has a ghost section and is not semmetrical"

## Sources

| region | from |
|---|---|
| the alley corner and the crew (x < 452, y 402-950) | **v005**, x1.055 |
| everything else | v047 |

## The two ghosts were my own mask error

v045's mask ran from y=-60, so its boundary passed straight through the canopy's
left end and the wall lantern. v005 has an ornate hanging lantern there; v042 has a
flat downlight. The feather blended the two into a translucent double image, and
doubled the canopy's stepped end the same way.

Fixed by moving the mask's top edge from -60 to **402**, below the canopy, so both
come wholly from the newer image. Nothing about the crew or the alley changed.

**This is the mask-boundary rule, and I broke it while it was fresh in the skill:
place the boundary in flat, featureless area — never across a real object edge.** The
outside-mask counts were clean on v045 and the ghosts still shipped.

## The two asymmetries

- **Handrails.** The right rail reached the lowest step; the left stopped about three
  steps short, ending in mid-air above a mid-flight post. Both now run unbroken from
  the landing to the lowest step on three posts each, ending at the same step.
- **Canopy.** The left end was a blocky stepped form; the right ran out along a long
  diagonal taper and reached further from the door. The right end is now a mirror of
  the left, both stopping the same distance from the doorway centre.

## Measurements

| | ratio | crew edge energy |
|---|---|---|
| v005 (the target) | 0.2975 | 399.58 |
| v046 | 0.2996 | 399.20 |
| v047 (architecture fix) | 0.3211 | — |
| **v048** | **0.3004** | **399.37** |

v047 drifted brighter again — the ninth time in this scene on an explicit freeze —
but the crew region is replaced wholesale by v005's, so no tonal correction was
needed this time. The lit steps moved only 138.26 to 137.82, so no brightness match
was required either.

## Commands

```bash
magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle -60,402 452,950 18,18" -blur 0x18 -alpha off mask-v005-corner.png
magick v005/image.png -evaluate multiply 1.055 lifted.png
magick lifted.png mask-v005-corner.png -alpha off -compose CopyOpacity -composite layer.png
magick v047/image.png layer.png -compose over -composite image.png
```

## Verification

vs v047: sign **0 px**, far right **0 px**. The canopy/lantern box and the staircase
box both show changes only where the mask's edges cross them; both were inspected at
190% with the boundary invisible, and the lantern is now a single clean downlight
matching the one on the right.

Status: awaiting user evaluation
