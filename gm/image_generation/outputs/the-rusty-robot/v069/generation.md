# the-rusty-robot v069

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "The stair on the right sticks out in front of the right concrete wall, on the left it does not. It should be the same on each. Also, it looks likle between 56 and 57 we degraded the quality of the crew. Can you look into that? The crew should look like they do in 56. You can see in 57 they got blurrier."

## Sources

| region | from |
|---|---|
| everything | **v068** (the generated stair-trim fix) |
| the crew figures only, x < 372 | **v005**, x1.0547 |

## The crew degradation was mine, and the user is right about v056 vs v057

Edge energy on the crew box across the chain:

| | edge | source |
|---|---|---|
| v056 | 399.37 | composite |
| v057 | 390.39 | generated |
| v058 | 400.10 | composite |
| ... | | |
| v063 | 394.10 | composite (tonal only) |
| v064 | 384.28 | generated |
| v065 | 384.76 | composite (tonal only) |
| v067 | 384.99 | composite (tonal only) |

Every generation erodes the crew's facets. Up to v061 every composite **restored**
them, because it transplanted v005's crew pixels wholesale. From v063 I switched to a
tonal-only correction: it fixes the ratio but copies no pixels, so nothing restored
crispness and the loss ratcheted down for four versions.

I switched away from the transplant for a reason — v061's transplant took "the alley
corner AND the crew" (x < 446) and that is what made the alley junction vague, the
fault repaired in v062. The mistake was abandoning the transplant entirely rather
than tightening its mask.

## The fix: transplant the figures, not the corner

Measured first: v005's crew is **pixel-aligned** with v067's at zero offset (best of
117 tested offsets; mean |diff| 5.64 at dx=dy=0, rising at every shift). A column
profile across the robot arm shows v005 and v068 agreeing to within 5 levels out to
x=370, jumping to 13.7 at x=375 and 43.9 at x=415 where v005's pale pilaster sits.

**x=372 is therefore the cut**: the arm's edge, which exists in both images, with
v005's architecture entirely excluded.

```bash
magick -size 1536x1024 xc:black -fill white -draw "rectangle -200,392 520,1000" \
  -blur 0x28 -alpha off soft.png          # feathers top, bottom and left
magick -size 1536x1024 xc:black -fill white -draw "rectangle -200,-200 372,1224" \
  -blur 0x3  -alpha off hardx.png         # hard bound ON the arm edge
magick -size 1536x1024 xc:black -fill white -draw "rectangle -200,-200 1800,946" \
  -blur 0x7  -alpha off hardy.png         # above v005's ground rubble
magick soft.png hardx.png -compose multiply -composite t.png
magick t.png hardy.png -compose multiply -composite -alpha off mask-crew-v005.png

magick v005/image.png -evaluate multiply 1.0547 lifted.png
magick lifted.png mask-crew-v005.png -alpha off -compose CopyOpacity -composite lay.png
magick v068/image.png lay.png -compose over -composite image.png
```

The lift is tuned so the final ratio lands on v005's own 0.2975 rather than computed
once and accepted: part of the measurement box (x 372-390) is v068's, so the
relationship is not linear.

## Measurements

| | ratio | crew edge energy |
|---|---|---|
| v005 (the referent) | 0.2975 | 399.58 |
| v067 (previous) | 0.2978 | 384.99 |
| v068 (raw generation) | 0.2960 | 383.69 |
| **v069** | **0.2975** | **393.11** |

Crew box `330x500+60+430` over lit steps `300x120+700+860`. Edge energy recovered
8.1 points, from 3.7% below v005 to 1.6% below.

## Verification

Changed pixels vs v068: alley corner **0**, lit steps **0**, staircase **0**, sign
**0**, far right **0**, door **0**. At the mask boundary, x=374 changes (the 0x3
feather), x=385 and x=400 are **0** — no v005 architecture crossed.

The soft top fade changes a 40x100 px strip of flat dark alley wall above the crew
(mean 3.8 levels on a wall reading 50). That is the fade doing its job in a flat
area, the same behaviour recorded in v061.

Status: awaiting user evaluation
