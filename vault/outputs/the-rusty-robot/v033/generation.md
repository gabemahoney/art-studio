# the-rusty-robot v033

Source: local composite, no generation. ImageMagick only; no model was called for
this file and nothing was billed. NOT raw model output.

User request verbatim: "The hand rails should go all the way down the stairs. The overhang is still assymetrical. Also, the edge of the alleyway has now merged with the side of the staircase."
Mode: Path 3. v032 generated from v031 for architecture only; canopy and staircase
taken, drift discarded.

## Sources

| region | from |
|---|---|
| canopy over the door, staircase and both flanks | v032 (brightness-matched x0.9986) |
| everything else, including the crew | v031 |

## What changed

1. **Handrails run the full length.** They previously stopped partway down, ending
   on top of the pier and leaving the lowest steps with no rail. Each rail now runs
   unbroken from the landing to the bottom step on three evenly spaced posts, both
   the same length, both ending at the same step.
2. **Canopy ends now match.** The left end was a blunt two-tier stepped block; the
   right end tapered to a long thin wedge reaching further out. The right end is now
   a copy of the left.
3. **The staircase is separated from the alley wall again.** v030 had merged the
   left pier and the alley wall into one pale grey mass with no boundary, and v031
   inherited it through the architecture mask. Restored as a tonal break — the wall
   behind sits in deeper shadow than the lit face of the pier — not as a drawn line.

Point 3 was a regression this pipeline introduced, not a fault of the original
image: the mask imported a merge the donor had painted. **When compositing a
regenerated region, diff the region's EDGES against the baseline, not just the area
outside the mask.** The outside-mask check was clean every time while this was wrong.

## Drift

| | crew/steps ratio |
|---|---|
| v005 | 0.2975 |
| v031 | 0.2910 |
| v032 | 0.3274 |
| **v033** | **0.2905** |

Fifth consecutive regeneration to drift brighter on a prompt that explicitly froze
the lighting.

## Verification

vs v031: crew figures `300x480+40+440` **0 px changed**, edge energy 399.00 -> 398.95.
The sign region shows 45,652 px changed where the canopy mask overlaps it; compared
side by side the lettering, emblem, lamp, rust and geometry are unchanged — the
difference is repaint mottling, not a regression.

Status: awaiting user evaluation
