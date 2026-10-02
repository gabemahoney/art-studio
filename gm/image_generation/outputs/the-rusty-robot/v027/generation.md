# the-rusty-robot v027

Source: local composite, no generation — ImageMagick only, no model was called and
nothing was billed. This is NOT raw model output.

Baseline: v026/image.png (unmodified; this is a masked tonal correction of it)
Donor: none
User request verbatim: "bro also look at how the crew have different lighting than the rest of the scene in v5 / can u not see that? They are in the shadows."
Mode: masked tonal correction of the crew/alley region to restore v005's shadow
depth, after three regeneration passes drifted it brighter. Regeneration was the
wrong tool — see the image-surgery skill, Path 1: tonal changes are arithmetic.

## Measurements

Ratio = mean luminance of crew `330x500+60+430` over lit steps `300x120+700+860`.

| | crew | steps | ratio |
|---|---|---|---|
| v005 (the look the user approved) | 39.24 | 131.90 | 0.2975 |
| v026 (after drift) | 50.45 | 135.00 | 0.3737 |
| v027 (this file) | 40.13 | 135.00 | **0.2972** |

Drift across v023→v026 was 0.31→0.37, roughly 19%, despite every pass explicitly
freezing the lighting.

## Commands

```bash
magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle -80,340 470,1010 40,40" -blur 0x30 -alpha off mask.png
magick v026/image.png -evaluate multiply 0.7962 adjusted.png
magick adjusted.png mask.png -alpha off -compose CopyOpacity -composite layer.png
magick v026/image.png layer.png -compose over -composite image.png
```

Factor derived as target ÷ current = 40.17 ÷ 50.45. Hit 40.13 on the first
iteration; no corrective pass needed. The mask extends well past the measurement
crop on all sides so the feather falls outside it.

The mask is kept beside this file as `correction-mask.png`.

## Verification

Pixels changed outside the mask, counted with
`-compose difference -composite -colorspace Gray -threshold 0`:

- far right `600x1024+936+0`: **0**
- sign / upper right `500x300+900+40`: **0**

The sign, the buildings, the street, the dome and the distant figures are
byte-identical to v026. Only the alley and the crew in it changed.

Status: awaiting user evaluation
