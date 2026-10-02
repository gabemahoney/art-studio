# the-rusty-robot v029

Source: local composite, no generation — ImageMagick only. No model was called for
this file and nothing was billed. This is NOT raw model output.

User request verbatim: "Make the staircase symmetrical." and "somethign happened on
the rendering between v5 (left) and v28(right). The characters look more blurry,
less sharp, in the later version."

Mode: Path 3 (generate-and-composite) for the stairs, plus a Path 1 transplant for
the crew. Three sources, each contributing the one thing it does best.

## Sources

| region | from | why |
|---|---|---|
| everything not listed below | v027 | corrected crew/alley lighting (ratio 0.2972) |
| the staircase and both flanks | v028 | the only version with symmetric flanks |
| the three crew figures | v005 | the only version with un-eroded edge rendering |

v028 was generated from v027 for the stair geometry alone; its lighting drifted
(0.2972 to 0.3312) and its crew softened further, so only its stairs were taken.

## Two independent drifts, both measured

**Brightness** — crew/steps luminance ratio. Crops: crew `330x500+60+430`, lit steps
`300x120+700+860`.

| v005 | v023 | v026 | v027 | v028 | v029 |
|---|---|---|---|---|---|
| 0.2975 | 0.314 | 0.3737 | 0.2972 | 0.3312 | **0.2906** |

**Edge rendering** — contrast-normalised Laplacian standard deviation on the crew
crop, higher = crisper. This one is NOT fixed by tonal correction and had not been
tracked before v029.

| v005 | v023 | v026 | v027 | v028 | v029 |
|---|---|---|---|---|---|
| 399.58 | 386.67 | 371.03 | 371.38 | 348.35 | **399.00** |

Each regeneration rounds off the flat angular gouache facets the Style Block
requires. Thirteen percent of the edge energy was lost between v005 and v028, and no
prompt instruction had asked for it.

## Commands

```bash
# 1. stairs from v028, brightness-matched to v027 on the lit steps
magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle 400,440 1180,1012 30,30" -blur 0x24 -alpha off mask-stairs.png
magick v028/image.png -evaluate multiply 1.0118 donor-matched.png
magick donor-matched.png mask-stairs.png -alpha off -compose CopyOpacity -composite L1.png
magick v027/image.png L1.png -compose over -composite stage1.png

# 2. crew figures from v005. Bottom edge stops at y=948, above the rubble line:
#    v005 still has the ground rocks the user had removed, and they must not return.
magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle 26,408 400,948 24,24" -blur 0x10 -alpha off mask-crew.png
magick v005/image.png mask-crew.png -alpha off -compose CopyOpacity -composite L2.png
magick stage1.png L2.png -compose over -composite image.png
```

No brightness rebalance was needed for the crew: v005 reads 39.24 against the
baseline's 40.25.

## Verification

Pixels changed, counted with `-compose difference -composite -colorspace Gray
-threshold 0`:

- ground strip below the boots `420x60+20+975`: **0** — no rubble returned
- sign and upper right `500x380+900+30`: **0**
- far right strip `300x1024+1236+0`: **0**
- entire top strip `1536x380+0+0`: **0**

The sign, its lettering, the buildings, the dome, the street and the distant figures
are byte-identical to v027.

Status: awaiting user evaluation
