# the-rusty-robot v042

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "Again I think the way v5 drew the alley was great. It angles off the side of the Rusty Robot correctly, they are tucked into it, and it does not take up a lot of the scene. You get a sense of there being an alley without showing anything else beyond it. That was really nice."

## Sources

| region | from |
|---|---|
| everything | v040 (alley rebuilt as v005's narrow slot), tonally corrected |
| the three crew figures | v037 (brightness-matched x0.9850) |

## What the two failed attempts got wrong

v036/v037 built the alley as a coherent space but an *open* one. v038/v039 then gave
it correct perspective and made it worse — a full corridor with visible depth, which
pulled the camera back and let the alley compete with the cantina for the frame.

Both were solving the wrong problem. The user's note names it exactly: v005 gives
"a sense of there being an alley without showing anything else beyond it." The depth
is carried by ONE angled plane — the cantina's side wall turning back from the front
corner — and everything past the crew is flat darkness. Showing the alley destroys
it.

The constraint that worked, stated positively and negatively:

- the gap is about one fifth of the frame's width, and the cantina keeps the rest
- the cantina's side wall is a trapezoid receding back-left from a crisp corner
- a short way past the crew the alley falls to flat darkness: NO far wall, NO back
  door, NO receding floor, NO lit surfaces deeper in, NO light at the far end

v005 was attached as IDENTITY for the alley's shape alone, with its sign, colours,
canopy, staircase, rubble and lighting explicitly excluded.

## Drift, and both corrections

v040 came back with the composition right and both axes drifted: ratio 0.3256 (the
eighth consecutive brightening on an explicit freeze) and edge energy 368.76, a 9%
softening against v037.

| | ratio | crew edge energy |
|---|---|---|
| v005 | 0.2975 | 399.58 |
| v037 | 0.2975 | 404.56 |
| v040 | 0.3256 | 368.76 |
| **v042** | **0.2980** | **404.27** |

Both were repaired locally, no further generation:

1. masked `-evaluate multiply 0.9137` over the alley restored the ratio
2. the crew were transplanted from v037, which aligned at **dx=0 dy=0, RMSE 0.0739** —
   tighter than the v005 transplant at 0.1087, because v040 descends from v037

## Commands

```bash
magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle -80,360 430,1010 36,36" -blur 0x26 -alpha off mask-alley.png
magick v040/image.png -evaluate multiply 0.9137 a.png
magick a.png mask-alley.png -alpha off -compose CopyOpacity -composite l.png
magick v040/image.png l.png -compose over -composite stage1.png

magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle 26,412 396,946 24,24" -blur 0x12 -alpha off mask-crew.png
magick v037/image.png -evaluate multiply 0.9850 d.png
magick d.png mask-crew.png -alpha off -compose CopyOpacity -composite lc.png
magick stage1.png lc.png -compose over -composite image.png
```

## Verification

Pixels changed by the crew transplant: sign `500x380+900+30` **0**, far right
`300x1024+1236+0` **0**, staircase `700x420+380+560` 11,324 — all of it mask feather
at x 380-396, inspected in the composite at 160% with no seam at the boundary.

Status: awaiting user evaluation
