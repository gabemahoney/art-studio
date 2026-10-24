# the-rusty-robot v082

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User requests verbatim: "also we still need to fix that shadow on the crew AND make the staircase symmetrical AND extend the hand rails all the way down the stairs." / "can you bring back the robot logo from v27 as well"

## Sources

| region | from |
|---|---|
| everything at x >= ~396 | **v081** (stairs, handrails, v027 robot emblem; canopy carried from v080) |
| x < 396: crew, alley, near wall | **v080** (crew from v005 via silhouette mask, darkened alley), via `mask-left-from-v080.png` |

```bash
magick -size 1536x1024 xc:black -fill white -draw "rectangle 0,0 396,1024" -blur 0x3 -alpha off mask-left-from-v080.png
magick v080/image.png mask-left-from-v080.png -alpha off -compose CopyOpacity -composite left.png
magick v081/image.png left.png -compose over -composite image.png
```

v080 vs v081 along the seam (20x1024 strips at x 400 and 430): mean difference 4.3 and
5.1 /255. The seam falls on the cantina's front-left pillar edge.

## Measurements (mean luminance 0–255)

| box | v005 | **v082** |
|---|---|---|
| alley far end `120x300+80+60` | 26.9 | **28.3** |
| alley side wall `200x300+180+60` | 37.6 | **36.3** |
| crew `330x500+60+430` | 39.2 | **39.3** |
| lit steps `300x120+700+860` | 131.9 | **129.8** |

Inside the fully-masked crew area (`v080/mask-crew-v005-silhouette.png` at 100%):
0 pixels differ from v005.

Status: awaiting user evaluation

Review: CORRECTED after user review; my first review overclaimed. MISSES: (1) canopy is a plain rectangular box — its visible left end face is a perspective parallelogram, not the requested trapezoid side profile (shallow top, deep bottom); (2) dark halo around the crew remains: v005's crew carry their own dark background and dark ground, which end in a hard edge against v074/v081's lit ground and pillar; (3) stairs not symmetrical: right side wall has an extra low ledge carrying the handrail that the left side does not have; (4) the flight is skewed relative to the facade and sits ~80 px right of the door's centre; (5) handrails stop ~3 treads above the bottom. LANDED: v027 robot emblem.
