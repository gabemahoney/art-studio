# the-rusty-robot v070

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

Supersedes v069. Same two fixes, built the way the skill's Path 3 prescribes instead
of by adopting a whole regenerated frame.

## Sources

| region | from |
|---|---|
| everything | **v067** |
| the stair region only (`mask-stair-region.png`) | v068 |
| the crew figures only, x < 372 (`mask-crew-v005.png`) | v005, x1.0608 |

## Why this replaces v069

v069 took the WHOLE of v068 — a regeneration asked to trim the stair treads — and
then patched the crew back. That is Path 2 plus a repair, not Path 3.

Measured, v067 -> v068 as a whole frame vs. taking only the stair region:

| region | whole regeneration | region only |
|---|---|---|
| crew | 40,630 px changed | **2 px** |
| canopy | 13,742 px | **0** |
| sign | 2,439 px | **0** |
| far right | 8,580 px | **0** |
| whole frame | 15.7% | 4.2% |

The crew degradation the user reported would not have happened at all under Path 3.
No transplant would have been needed; it was repairing damage that the method itself
caused. The same is true of the three passes before it: 39%, 14% and 17% of the frame
changed to fix a canopy edge, two canopy ends and a wall balance.

```bash
# stair region only, out of the regeneration, onto v067
magick -size 1536x1024 xc:black -fill white -draw "rectangle 404,628 1040,980" \
  -blur 0x22 -alpha off mask-stair-region.png
magick v068/image.png mask-stair-region.png -alpha off -compose CopyOpacity \
  -composite lay.png
magick v067/image.png lay.png -compose over -composite base.png

# then the crew, same mask and method as v069
magick v005/image.png -evaluate multiply 1.0608 lifted.png
magick lifted.png mask-crew-v005.png -alpha off -compose CopyOpacity -composite c.png
magick base.png c.png -compose over -composite image.png
```

## Measurements

| | ratio | crew edge energy |
|---|---|---|
| v005 (the referent) | 0.2975 | 399.58 |
| v067 | 0.2978 | 384.99 |
| v069 (superseded) | 0.2975 | 393.11 |
| **v070** | **0.2981** | **393.06** |

Crew box `330x500+60+430` over lit steps `300x120+700+860`.

## Verification

Changed vs v067: sign **0 px**, far right **0 px**, canopy **1,272 px** (the crew
mask's soft top fade landing in flat dark alley wall, as in v061 and v069). The
staircase and the crew change by design. Nothing else in the frame moved.

## The routing gap this exposed

`image-surgery`'s table sent "architecture, geometry" to a bare **Regenerate**, and
Path 3's entry condition read "once a freeze instruction has failed twice". The
freezes here never failed — they were verified intact every pass — so the stated
trigger never fired while the frame drifted anyway. Both have been corrected: the
table now routes geometry to "Regenerate, then Path 3", and Path 3's trigger is now
"I am regenerating", with these numbers as the evidence.

Status: awaiting user evaluation
