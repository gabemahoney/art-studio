# the-rusty-robot v052

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "The rightside handrail is correct. It sits in the steps but directly on the side. The left hadnrail is wrong. It sits up high on the parapet where it could not be reached."

## Sources

| region | from |
|---|---|
| the alley corner and the crew (x < 452, y 402-950) | **v005**, x1.055 |
| everything else | v051 |

## I had the fix backwards in v049

Four passes failed on this rail, and the third of them actively made it worse.

- v047: treated it as a LENGTH fault, extended the left rail downward.
- v049: treated it as a POSITION fault and moved the left rail ONTO the left parapet.
  **This was backwards.** It put the rail on the crest of a sloping wall, above head
  height for anyone on the flight — a rail nobody could reach.
- v051: the user supplied the correct reading. The RIGHT rail was right all along:
  posts standing on the step TREADS near the edge, rail at hand height above the
  stone. The left rail had to come DOWN off the parapet onto the treads to match.

The lesson is not about handrails. **When one side of a symmetrical pair is correct,
freeze it explicitly and describe it as the referent** — "the right rail is correct,
do not change it, here is how it is built, make the left match" — rather than
describing the desired end state in the abstract. Three passes of "both rails should
be symmetrical" produced three different wrong arrangements, because "symmetrical"
does not say which side is right.

The verifiable test: a person standing on any step can reach either rail, and the
parapet crests are bare stone.

## Measurements

| | ratio | crew edge energy |
|---|---|---|
| v005 (the target) | 0.2975 | 399.58 |
| v050 | 0.3029 | 399.24 |
| v051 (rail relocated) | 0.3368 | — |
| **v052** | **0.3038** | **399.25** |

v051 drifted brighter — the eleventh time in this scene on an explicit freeze — and
again needed no correction, the crew region being replaced wholesale by v005's. Lit
steps 136.27, within the no-match range.

## Commands

```bash
magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle -60,402 452,950 18,18" -blur 0x18 -alpha off mask-v005-corner.png
magick v005/image.png -evaluate multiply 1.055 lifted.png
magick lifted.png mask-v005-corner.png -alpha off -compose CopyOpacity -composite layer.png
magick v051/image.png layer.png -compose over -composite image.png
```

## Verification

vs v051: sign **0 px**, far right **0 px**. Crew edge energy 399.25 against v005's
399.58, ratio 0.3038 against 0.2975.

Status: awaiting user evaluation
