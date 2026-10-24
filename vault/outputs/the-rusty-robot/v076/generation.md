# the-rusty-robot v076

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "I want to go back to v5 and start from there. Make the following changes: 1. Make the alley more clearly and plausibly connected to the side of the Rusty Robot. 2. Fix the geometry of the marguee. The left and right sides should be the same shape. 3. Change the lamps to look more modern and sci fi 4. Make the stair case and handrails symmetrical. Do NOT change the crew or the lighting in the alley way itself." — then, on v074: "No you changed the darkness of the alley." — then, on v075: "did the crew change subtley too?"

## Sources

| region | from |
|---|---|
| everything | **v074** (generated off v005: alley side wall, symmetrical canopy, sci-fi lamps, symmetrical stairs) |
| the crew, x < ~392, y ~340–950 | **v005**, unscaled, via `mask-crew-v005-tight.png` (polygon following the right-hand figure's silhouette, blur 0x4, top faded over y 368 with blur 0x12) |
| alley far end, x 60–180, y 0–520 | v074 x0.62, crew excluded |
| alley side wall, x 180–385, y 0–520 | v074 x0.84, crew excluded |
| lit side-wall window, x 205–235, y 60–170 | further x0.45 |

```bash
magick -size 1536x1024 xc:black -fill white \
  -draw "polygon 0,330 342,330 342,505 392,520 392,760 378,780 378,860 362,870 362,950 0,950" \
  -blur 0x4 -alpha off poly.png
magick -size 1536x1024 xc:black -fill white -draw "rectangle 0,368 1536,1024" -blur 0x12 -alpha off top.png
magick poly.png top.png -compose multiply -composite -alpha off mask-crew-v005-tight.png
magick v005/image.png mask-crew-v005-tight.png -alpha off -compose CopyOpacity -composite crew.png
magick v074/image.png crew.png -compose over -composite c.png
# then three darkening passes, each: region mask (blur 6 / 10 / 3) x (negated crew mask),
# magick c.png -evaluate multiply F adj.png; CopyOpacity; compose over.
#   F=0.62 polygon 60,0 180,0 180,520 60,520
#   F=0.84 polygon 180,0 385,0 385,520 180,520
#   F=0.45 rectangle 205,60 235,170
```

## Measurements (mean luminance 0–255)

| box | v005 | v074 | **v075** |
|---|---|---|---|
| alley far end `120x300+80+60` | 26.9 | 43.2 | **28.3** |
| alley side wall `200x300+180+60` | 37.6 | 44.8 | **36.3** |
| crew `330x500+60+430` | 39.2 | 42.8 | **39.1** |
| lit steps `300x120+700+860` | 131.9 | 130.2 | 130.2 |

Crew / lit steps ratio: v005 0.2975, v074 0.329, **v075 0.301**.

## Why v076 supersedes v075

v075's crew mask faded in over y ~373–440, so the top of the tall man's hair was
partly blended with v074's background. v076 moves the fade up: the mask is fully
v005 from y 405 down, above every head. Zero pixels differ from v005 inside the fully
masked crew area (bbox 381x534+0+405). Same darkening passes as v075; measurements
unchanged (far end 28.3, side wall 36.3, crew 39.1).

## Verification

Pixels changed vs v074 at x >= 390: 10,124, all in the feathered edges of the crew and
side-wall masks (x 385–~415; 2,493 of them at x >= 400). Everything right of that is byte-identical to v074.

Status: awaiting user evaluation
