# the-rusty-robot v045

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "The composition in v5 was perfect. they were in the right place, right posture, right lighting, the alley was good. Just the ret of the picture, the buildings and stuff was not right" / "Could you isolate the crew in their corner from v5 and rebuild the rest around them?"

## Sources

| region | from |
|---|---|
| the alley corner, the crew, the dark pocket (x < ~452, y < 950) | **v005**, x1.055 |
| everything else — sign, canopy, staircase, street, dome, city | v042 |

## Why this replaced four failed regenerations

v038 through v044 each tried to RE-DESCRIBE v005's alley: first as a coherent space,
then with correct perspective, then as a narrow slot, then as a concealed pocket.
Each attempt improved one property and lost another, and none reproduced it.

The diagnosis that mattered came too late: v005's tuck is three things at once —
foreground masonry OVERLAPPING the nearest figure, a featureless near-black void
behind the group, and rim-only lighting. Any prompt that captures two of the three
still reads wrong.

**When an earlier version already has the thing, transplant it instead of describing
it.** The composite took four commands and reproduced v005 exactly, because it *is*
v005. Four regenerations had failed at the same task.

## Measurements

| | ratio | crew edge energy |
|---|---|---|
| v005 (the target) | 0.2975 | 399.58 |
| v042 | 0.2980 | 404.27 |
| v043 (narrowed + moved) | 0.3320 | 328.92 |
| **v045** | **0.2997** | **399.23** |

v005's region was lifted only 5.5% (`-evaluate multiply 1.055`), a compromise between
preserving its native darkness and hiding the brightness step at the seam. A full
match to v042's alley (x1.1193) overshot to 0.3179 and was rejected — the user had
said v005's lighting was right.

v043's crew could not be transplanted back: the group was told to move, not re-pose,
but the model re-posed them. Best alignment RMSE 0.2569, far above the ~0.11 that
makes a transplant viable.

## Commands

```bash
magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle -60,-60 452,950 20,20" -blur 0x20 -alpha off mask-v005-corner.png
magick v005/image.png -evaluate multiply 1.055 lifted.png
magick lifted.png mask-v005-corner.png -alpha off -compose CopyOpacity -composite layer.png
magick v042/image.png layer.png -compose over -composite image.png
```

The mask stops at y=950, above v005's ground rubble, which the user had removed
earlier in the scene. The paving below the boots comes from v042 and is clean.

## Verification

vs v042: sign `500x380+900+30` **0 px**, far right `300x1024+1236+0` **0 px**,
staircase 49,013 px — the mask's right edge at x=452 crosses the staircase crop,
inspected at 170% with no visible seam; the pillar the nearest figure stands behind
absorbs the boundary.

Status: awaiting user evaluation
