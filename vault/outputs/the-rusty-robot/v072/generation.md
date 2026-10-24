# the-rusty-robot v072

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "The stair case is a little too short and steep. The ground is a little too vibrant. Go back and take a look at v5. The stairs were a good length there and the buildings had more variety. Dont use that pastel paint scheme from v5 though"

## Sources

| region | from |
|---|---|
| everything | **v071** (generated: long shallow staircase + varied alley buildings) |
| the crew figures only, x < 372 | **v005**, x0.9720, via `mask-crew-v005.png` |
| the paving, desaturated 14% | v071 itself, via `mask-ground.png` |

## What the user asked for, and what was measured

**Stairs.** v070 had six tall treads in a small footprint. v071 rebuilds the flight
with about eleven low treads, wider and reaching much further into the street, both
side walls running down to the pavement with every tread contained between them.

**Building variety.** v005 was the referent, but only for VARIETY — the user
explicitly rejected its pastel palette. Measured: v005's alley buildings carry a
wider hue spread (67.1 vs 61.7) at much lower saturation (28.6% vs 39.0%) — that
lower saturation IS the pastel. The spec therefore asked for variety of width,
height, roofline and window pattern while keeping v070's saturated palette, and
named the pastel direction as forbidden.

**Ground.** Measured before touching it: v070 58.8% saturation against v005's 45.2%.
Desaturating the paving by 14% through a feathered mask lands it at 46.3%.

## Why the crew came from v005 again

v071's generation pushed the crew ratio to 0.3441, its largest jump yet. Everything
else in v071 was checked BY EYE, not by pixel count — the canopy, sign, door and the
two dark windows all survived intact, so the 16-40% "changed" readings in those boxes
were repaint and sub-pixel shift, not damage. The crew was the only regression, and
transplanting restores crispness that a tonal correction cannot.

```bash
magick v005/image.png -evaluate multiply 0.9720 lifted.png
magick lifted.png mask-crew-v005.png -alpha off -compose CopyOpacity -composite c.png
magick v071/image.png c.png -compose over -composite crew-done.png

magick -size 1536x1024 xc:black -fill white -draw "rectangle -200,845 1800,1224" \
  -blur 0x55 -alpha off mask-ground.png
magick crew-done.png -modulate 100,86,100 g.png
magick g.png mask-ground.png -alpha off -compose CopyOpacity -composite gl.png
magick crew-done.png gl.png -compose over -composite image.png
```

The crew lift was tuned AFTER the ground pass, not before: the lit-steps box sits
inside the ground mask, so desaturating it moves the ratio's denominator.

## Measurements

| | ratio | crew edge energy | ground saturation |
|---|---|---|---|
| v005 (the referent) | 0.2975 | 399.6 | 45.2% |
| v070 (previous) | 0.2981 | 393.1 | 58.8% |
| v071 (raw generation) | 0.3441 | 386.0 | 52.7% |
| **v072** | **0.2966** | **390.1** | **46.3%** |

Crew box `330x500+60+430` over lit steps `300x120+700+860`; ground box
`600x180+500+840` measured as HSL saturation.

## Verification

Changed vs v071 outside the crew and the ground: sign **0 px**, door **0 px**, far
alley **0 px**, canopy **484 px** (the crew mask's soft top fade in flat dark wall).

Status: awaiting user evaluation
