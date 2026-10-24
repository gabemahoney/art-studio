# the-rusty-robot v080

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User requests verbatim: "no. the top and the bottom should be the same length. the trapezoid is on the sides." / "also we need to fix that weird shadow around the crew" / "also we still need to fix that shadow on the crew AND make the staircase symmetrical AND extend the hand rails all the way down the stairs."

This version addresses the canopy and the crew shadow. Stairs, handrails and the v027
logo follow in the next generation, from this image.

## Sources

| region | from |
|---|---|
| everything else | **v074** |
| the crew | **v005**, unscaled, via `mask-crew-v005-silhouette.png` |
| alley darkening | same three passes as v076, crew excluded |
| canopy, x 398–1046, y 22–500 | **v079** (canopy rebuilt: rectangular front, trapezoid side profile), via `mask-canopy-v079.png` |

The crew mask now follows the right-hand figure's silhouette down to the boot (v076's
mask left a band of v005's dark pillar shadow beside her legs and a dark halo around her
boot on the lit ground — the "weird shadow"):

```bash
magick -size 1536x1024 xc:black -fill white -draw "polygon 0,330 342,330 342,525 348,555 \
  370,568 384,635 384,695 377,728 364,745 360,760 363,795 369,848 360,862 352,875 351,945 \
  346,953 0,953" -blur 0x1.5 -alpha off poly.png
magick -size 1536x1024 xc:black -fill white -draw "rectangle 0,368 1536,1024" -blur 0x12 -alpha off top.png
magick poly.png top.png -compose multiply -composite -alpha off mask-crew-v005-silhouette.png
# crew: v005 through that mask over v074
# darkening, each pass masked by (region x NOT crew):
#   x0.62 polygon 60,0 180,0 180,520 60,520   blur 6
#   x0.84 polygon 180,0 385,0 385,520 180,520 blur 10
#   x0.45 rectangle 205,60 235,170            blur 3
magick -size 1536x1024 xc:black -fill white -draw "rectangle 398,22 1046,500" -blur 0x4 -alpha off mask-canopy-v079.png
# canopy: v079 through that mask over the result
```

v079 vs v076 along the canopy mask's lower seam (y 470–520): mean difference 4/255.

## Measurements (mean luminance 0–255)

| box | v005 | **v080** |
|---|---|---|
| alley far end `120x300+80+60` | 26.9 | **28.3** |
| alley side wall `200x300+180+60` | 37.6 | **36.3** |
| crew `330x500+60+430` | 39.2 | **39.3** |
| lit steps `300x120+700+860` | 131.9 | **130.2** |

Inside the fully-masked crew area: 0 pixels differ from v005.

Status: awaiting user evaluation

Review: Canopy from v079 composited cleanly; crew silhouette mask removes v076's dark halo. Intermediate base for v081.
