# the-rusty-robot v054

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "lets remove the handrails. its too complicated"

## Sources

| region | from |
|---|---|
| the alley corner and the crew (x < 452, y 402-950) | **v005**, x1.055 |
| everything else | v053 |

## Why they were removed

Five passes failed to make the pair symmetrical, each failing differently:

1. v030 — both rails stopped partway down; extended them.
2. v047 — the left still stopped short; treated as a LENGTH fault, extended again.
3. v049 — treated as a POSITION fault and moved the left rail ONTO the parapet. This
   was backwards: it put the rail on the crest of a sloping wall, above head height,
   where nobody on the flight could reach it.
4. v051 — the user identified the real geometry: the RIGHT rail was correct all
   along, posts on the treads at hand height. The left came down to match.
5. v054 — the user called it: not worth more passes. Both removed.

The cost of the detour was eleven regenerations in this scene. The transferable
rule, written up in the v052 receipt: **when one half of a symmetrical pair is
already correct, freeze it by name and describe it as the referent** — "the right one
is correct, do not change it, here is how it is built, make the left match it."
"Make them symmetrical" does not say which side is right, and produced three
different wrong arrangements.

A second rule worth keeping: a detail that has failed three passes is a candidate for
DELETION, not a sixth attempt. The staircase reads better without the rails than it
did with either wrong arrangement.

## Measurements

| | ratio | crew edge energy |
|---|---|---|
| v005 (the target) | 0.2975 | 399.58 |
| v052 | 0.3038 | 399.25 |
| v053 (rails removed) | 0.3250 | — |
| **v054** | **0.3019** | **399.38** |

The removal was clean: steps run as unbroken bands, parapet crests are bare, pier
caps are whole, and there are no stubs, sockets, bolt plates or orphaned post
shadows.

## Commands

```bash
magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle -60,402 452,950 18,18" -blur 0x18 -alpha off mask-v005-corner.png
magick v005/image.png -evaluate multiply 1.055 lifted.png
magick lifted.png mask-v005-corner.png -alpha off -compose CopyOpacity -composite layer.png
magick v053/image.png layer.png -compose over -composite image.png
```

## Verification

vs v053: sign **0 px**, far right **0 px**. Crew edge energy 399.38 against v005's
399.58; ratio 0.3019 against 0.2975.

Status: awaiting user evaluation
