# the-rusty-robot v050

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "The handrails are still assymettrical in v48. And the leftside handrail seems to be in the MIDDLE of the stairs case instead of the side."

## Sources

| region | from |
|---|---|
| the alley corner and the crew (x < 452, y 402-950) | **v005**, x1.055 |
| everything else | v049 |

## The fault was placement, not length

Three earlier passes treated this as a LENGTH problem — "both rails should reach the
bottom step" — and each one extended the left rail while leaving it in the wrong
place. The user's second sentence gave the real diagnosis: the left rail was standing
out over the step TREADS, inset from the left side of the flight, with its posts
coming down onto the steps themselves. The right rail was correct all along, running
along the top of the right parapet with its posts on that parapet.

So the instruction that worked was lateral, not longitudinal: move the left rail
sideways onto the top of the left parapet, posts on the parapet and none on a tread,
lowest post landing on the left pier — a mirror of the right. The verifiable
consequence: **the treads are now completely clear between the two rails.**

Another instance of the standing pattern in this scene — the user's words name a
symptom ("not symmetrical"), and the fix only lands once the actual geometric fault
is identified.

## Measurements

| | ratio | crew edge energy |
|---|---|---|
| v005 (the target) | 0.2975 | 399.58 |
| v048 | 0.3004 | 399.37 |
| v049 (rail relocated) | 0.3290 | — |
| **v050** | **0.3029** | **399.24** |

v049 drifted brighter again — the tenth time in this scene on a prompt that froze the
lighting — and again needed no tonal correction, because the crew region is replaced
wholesale by v005's. Lit steps moved 137.82 to 136.66, inside the range where no
brightness match is needed.

## Commands

```bash
magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle -60,402 452,950 18,18" -blur 0x18 -alpha off mask-v005-corner.png
magick v005/image.png -evaluate multiply 1.055 lifted.png
magick lifted.png mask-v005-corner.png -alpha off -compose CopyOpacity -composite layer.png
magick v049/image.png layer.png -compose over -composite image.png
```

## Verification

vs v049: sign **0 px**, far right **0 px**. The canopy/lantern box changes only where
the mask's top edge crosses it at y=402, below the canopy — the lantern itself is
untouched and remains v042's single clean downlight.

Status: awaiting user evaluation
