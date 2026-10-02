# the-rusty-robot v065

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "Left arrow: The overhang is a 3d volu,e but the left side of it melds with the face of the building. Right arrow: The overhang still is not symmetrical in its design. The right side, for example, has a horizontal divide that does not exist on the left side. Also, some candle stick looking thins appread to the right of the door that needs to be removed."

## Sources

| region | from |
|---|---|
| everything | **v064** (the generated three-fault fix) |
| crew region, tonal only | v064 x 0.9226 through `mask-crew-tone.png` |

No geometry transplanted. v065 is v064 with one masked brightness correction, the
same procedure as v063 and for the same reason: the generation pass brightened the
crew (0.2977 -> 0.3225) and brightness is arithmetic, so it needs no geometry from
another candidate.

```bash
magick v064/image.png -evaluate multiply 0.9226 adj.png
magick adj.png mask-crew-tone.png -alpha off -compose CopyOpacity -composite lay.png
magick v064/image.png lay.png -compose over -composite image.png
```

## Measurements

| | ratio | crew edge energy |
|---|---|---|
| v005 (the lighting referent) | 0.2975 | 399.58 |
| v063 (previous) | 0.2976 | 394.10 |
| v064 (raw generation) | 0.3225 | 384.28 |
| **v065** | **0.2977** | **384.76** |

Crew box `330x500+60+430` over lit steps `300x120+700+860`.

**Edge energy is now 3.8% below v005** and fell 2.5% in this pass alone, against
0.8% in the pass before. Facet erosion is accelerating; the next correction on this
scene should prefer a local fix over a whole-frame regeneration, or transplant the
crew from an un-eroded version.

## Verification

Changed pixels vs v064 outside the mask: far right `400x300+1100+100` **0**, lit
steps `300x120+700+860` **0**, sign `400x80+560+30` **0**, door wall
`240x230+700+400` **0**.

Frozen regions confirmed intact after the generation: the canopy's straight top
edge, the single alley/cantina corner line with its buttress on the pavement, the
crew poses, the sign and its lettering, the door and steps. No handrails.

Status: awaiting user evaluation
