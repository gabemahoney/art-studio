# the-rusty-robot v058

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "and can you now make the top corners of the overhang (above the door, below the sign) symmetrical?" / "I think the masking is creating ghosting. See this circled area. Its like the geometry of the alley and the geometry of the cantina are doing a dissolve into each other. Instead of being a proper geometry."

## Sources

| region | from |
|---|---|
| the alley corner and the crew (x < 446, y 402-950) | **v005**, x1.0549 |
| everything else | v057 |

## The ghosting was the mask, and the user diagnosed it correctly

Every composite from v045 onward used a mask with a **36-pixel feather running
vertically through the cantina's corner**. That corner is a real architectural edge,
and it is painted differently in v005 than in the later versions. Feathering across
it did not blend two tones — it cross-dissolved two different GEOMETRIES, so the
alley wall and the cantina wall faded through each other instead of meeting.

The fix is the mask-boundary rule applied properly. Measuring per-column vertical
edge strength in the band x 360-560 found a strong edge at **x=446 in BOTH images** —
the same corner. Cutting there with a near-hard boundary (`-blur 0x3` instead of
`0x18`) makes the two paintings meet AT a shared real edge rather than dissolving
across it.

**Where a mask boundary must cross a real edge, put it exactly on an edge that
exists in both images and cut nearly hard. Feather is for flat areas only.**

## ImageMagick trap found here

`-draw "roundrectangle X1,Y1 X2,Y2 0,0"` draws **nothing at all** — a zero corner
radius silently produces an empty mask. The first attempt at this composite was
therefore byte-identical to its base, and only a measurement caught it: the ratio and
edge energy came back as the base's values rather than v005's. Use
`-draw "rectangle ..."` for square corners.

## Canopy top corners

v057 rebuilt the canopy's right TOP corner to match the left: each now steps down
toward the wall in exactly two square tiers, same depth and height, no diagonals or
chamfers. The canopy's ends, depth, vents, trim and downlights were frozen.

## Measurements

| | ratio | crew edge energy |
|---|---|---|
| v005 (the target) | 0.2975 | 399.58 |
| v056 | 0.2979 | 399.37 |
| **v058** | **0.2975** | **400.10** |

An exact match on the ratio, and edge energy slightly above v005's own. The lift
factor was recomputed against v057's lit steps (139.15) rather than carried over.

## Commands

```bash
magick -size 1536x1024 xc:black -fill white \
  -draw "rectangle -60,402 446,950" -blur 0x3 -alpha off mask-v005-corner.png
magick v005/image.png -evaluate multiply 1.0549 lifted.png
magick lifted.png mask-v005-corner.png -alpha off -compose CopyOpacity -composite layer.png
magick v057/image.png layer.png -compose over -composite image.png
```

## Verification

vs v057: sign **0 px**, far right **0 px**. The corner was inspected at 200% in the
composite: a single crisp vertical edge between the dark alley pillar and the lit
cantina wall, with no dissolve.

Status: awaiting user evaluation
