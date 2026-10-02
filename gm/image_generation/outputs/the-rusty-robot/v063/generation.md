# the-rusty-robot v063

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "Where the alley meets the building the geometry gets kind of vague. We need to tight this up. And the overhang below the sign still has strange outcroppings on the top that need to be remove."

## Sources

| region | from |
|---|---|
| everything | **v062** (the generated geometry fix) |
| crew region, tonal only | v062 x 0.9301 through `mask-crew-tone.png` |

No geometry was transplanted. v063 is v062 with one masked brightness correction.

## Why a tonal pass and not a transplant

v062 fixed both faults the user named but brightened the crew, as every edit pass on
this scene has: ratio 0.2980 -> 0.3199, the documented pull toward legible subjects.

v061 solved that by transplanting v005's crew. **That transplant is what made the
alley junction vague in the first place** — v005 and v059 draw architecturally
different corners (different steps, different pilaster widths, and v005 has the
handrail the user had removed), so the hard seam at x=446 spliced two buildings
together. Repeating it would have re-imported the fault this pass exists to fix.

Brightness is arithmetic, so it needs no geometry from anywhere.

```bash
magick -size 1536x1024 xc:black -fill white -draw "rectangle -200,392 470,1000" \
  -blur 0x34 -alpha off mask-crew-tone.png
magick v062/image.png -evaluate multiply 0.9301 adj.png
magick adj.png mask-crew-tone.png -alpha off -compose CopyOpacity -composite lay.png
magick v062/image.png lay.png -compose over -composite image.png
```

The factor is `target / current` = (0.2975 x 140.41) / 44.91. The crew measurement
box lies entirely inside the mask's solid white, so the feather did not land high and
one pass was enough.

## Measurements

| | ratio | crew edge energy |
|---|---|---|
| v005 (the lighting referent) | 0.2975 | 399.58 |
| v061 (previous) | 0.2980 | 397.49 |
| v062 (raw generation) | 0.3199 | 394.40 |
| **v063** | **0.2976** | **394.10** |

Crew box `330x500+60+430` over lit steps `300x120+700+860`.

## Verification

Changed pixels vs v062 outside the mask: far right `400x300+1100+100` **0**, lit steps
`300x120+700+860` **0**, sign `400x80+560+30` **0**, right paving `500x200+1000+820`
**0**, door `200x300+600+300` **0**. Edge energy moved 0.08%, consistent with a tonal
pass not touching rendering.

Status: awaiting user evaluation
