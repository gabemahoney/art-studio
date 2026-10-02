# the-rusty-robot v061

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "It is so close but your masking creating an obvious square artifact around the crew. Is this maybe a good use case for the api?"

## Sources

| region | from |
|---|---|
| the alley corner and the crew | **v005**, x1.0629 |
| everything else | v059 |

## No, the API would not have helped

Asked directly, and worth recording because the answer is counter-intuitive:
`--backend api` cannot inpaint here — `gen.py` sends no `mask`, so it is a whole-frame
regeneration on a different backend. It would have repainted the crew, which is the
one thing being preserved, and charged for it. The capability that would help does
not exist in this vault.

## Nor was the artifact an ImageMagick limitation

It was the mask shape. v058-v060 used ONE rectangle with ONE blur applied to all four
edges. When the feather was cut to `0x3` to fix the corner dissolve, the top and
bottom edges went hard too — and those cut across flat wall and flat paving where no
real edge exists. A rectangular mask with uniform treatment produces a rectangular
seam. ImageMagick did exactly what it was told.

**Different edges of one mask need different treatment, and a mask is just an image,
so build it from parts and multiply them together:**

```bash
# soft blob — feathers the top, bottom and left into flat areas
magick -size 1536x1024 xc:black -fill white -draw "rectangle -200,392 620,1000" \
  -blur 0x34 -alpha off soft.png
# hard vertical bound ON the cantina corner, which exists in both images at x=446
magick -size 1536x1024 xc:black -fill white -draw "rectangle -200,-200 446,1224" \
  -blur 0x2 -alpha off halfx.png
# near-hard horizontal bound above v005's ground rubble
magick -size 1536x1024 xc:black -fill white -draw "rectangle -200,-200 1800,946" \
  -blur 0x7 -alpha off halfy.png
magick soft.png halfx.png -compose multiply -composite t.png
magick t.png halfy.png -compose multiply -composite -alpha off mask-v005-corner.png
```

Hard where the boundary follows real geometry; soft everywhere else.

The bottom bound was tuned by measurement, not by eye — y=956 let 2,715 px of v005's
ground rubble through, y=938 cost the boots (mask dropped to 210/255 over them), y=946
gives **0 px of bleed with the boots still at 239/255**.

## Measurements

| | ratio | crew edge energy |
|---|---|---|
| v005 (the target) | 0.2975 | 399.58 |
| **v061** | **0.2980** | **397.49** |

## Verification

vs v059: ground below the boots **0 px**, sign **0 px**, far right **0 px**. The
region above the blob changes by design — that is the soft fade doing its job, and it
lands in flat dark wall where it is invisible.

Status: awaiting user evaluation
