# the-rusty-robot (asset) v014

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "If we can fix the robot logo then this is the one!"

## Sources

| region | from |
|---|---|
| everything | **v012** (user: "this is the one") |
| robot emblem, three-quarter view and front elevation | **v013**, via `mask-emblem-from-v013.png` (rectangles 777,508–862,634 and 1334,273–1391,352, blur 0x2) |

```bash
magick v013/image.png mask-emblem-from-v013.png -alpha off -compose CopyOpacity -composite emb.png
magick v012/image.png emb.png -compose over -composite -alpha off image.png
```

v012 vs v013 along the three-quarter mask's edges: mean difference 2–9 /255.

Status: awaiting user evaluation

Review: Robot emblem now has two separate round eyes in both views; everything else is v012. Open: the canopy underside's back edge kinks around the right fin in the three-quarter view (user).
