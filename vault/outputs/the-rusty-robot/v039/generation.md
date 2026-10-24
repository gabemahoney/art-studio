# the-rusty-robot v039

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "Perspective is wrong on the side of the Rusty Robot and the alley though. Shouldnnt it go at an angle like this?"
Mode: Path 1 masked tonal correction of v038, which gave the alley its own perspective.

## The fault

Every surface inside the alley was painted as a flat upright band parallel to the
picture plane, with horizontal top and bottom edges. Nothing converged, so the alley
had no depth — a painted backdrop behind the crew rather than a corridor.

The diagnosis that worked: **the alley needs its own vanishing point.** The street
recedes right, toward the distant archway; the alley runs the other way, back and to
the left. Specified as three receding planes — the cantina's side wall and the
opposite flank as trapezoids with top edges sloping down-left and bottom edges up-
left, and the floor's paving joints fanning toward the same point — under one
countable rule: **nothing inside the alley is horizontal.** If an edge in there runs
flat across the picture, it is wrong.

## Correction

v038 came back with the perspective right and the crew bright again at 0.3460.
A masked `-evaluate multiply 0.8597` over the alley restored 0.2976 in one pass.
**Seventh** consecutive regeneration to drift brighter on an explicit freeze.

| | ratio | crew edge energy |
|---|---|---|
| v005 | 0.2975 | 399.58 |
| v037 | 0.2975 | 404.56 |
| v038 | 0.3460 | 393.97 |
| **v039** | **0.2976** | **393.97** |

## Known trade-offs, for the user to judge

- **The framing changed.** v038 pulled the camera back: the cantina is smaller and
  further right, the alley wider, the crew smaller in frame than in v037. This was
  not requested and was not prevented by the spec, which froze lighting and content
  but not camera distance.
- **Edge energy fell** 404.56 to 393.97, a 2.6% loss, the cost of one more full
  repaint.

If the v037 framing is preferred, this cannot be composited back: the perspective
change is global, so the two images no longer describe the same camera.

## Commands

```bash
magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle -80,360 430,1010 36,36" -blur 0x26 -alpha off mask-alley.png
magick v038/image.png -evaluate multiply 0.8597 adjusted.png
magick adjusted.png mask-alley.png -alpha off -compose CopyOpacity -composite layer.png
magick v038/image.png layer.png -compose over -composite image.png
```

Verification: 0 px changed outside the mask in the far right strip and the sign.

Status: awaiting user evaluation
