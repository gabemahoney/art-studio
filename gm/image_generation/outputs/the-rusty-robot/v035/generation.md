# the-rusty-robot v035

Source: local composite, no generation. ImageMagick only; no model was called for
this file and nothing was billed. NOT raw model output.

User request verbatim: "The side of the alley still blends with the stair case. Thats impossible geometry"
Mode: Path 3. v034 generated from v033 for the corner only; architecture taken,
drift discarded.

## Sources

| region | from |
|---|---|
| canopy, staircase, both flanks, the alley corner | v034 (brightness-matched x0.9928) |
| everything else, including the crew | v033 |

## The fault, and why three passes failed to fix it

The staircase had no thickness on its left side. Its diagonal parapet ran down to
the left and stopped in mid-air, and the pale surface beneath it continued unbroken
into the alley wall — one flat plane serving as both the side of the staircase and
the wall of a building, with no corner anywhere.

Two earlier attempts asked for "separation" and for "a crisp vertical edge" and both
failed, because the missing thing was not an edge: it was a SURFACE. The staircase
needed a side face for the edge to be the boundary *of*.

What worked was counting the planes by value, left to right, and naming what each
one is:

1. alley wall — furthest back, DARKEST, deep cool blue-grey
2. side face of the staircase — in front of it, ONE CLEAR STEP LIGHTER, turned away
   from the doorway lamps; this is the surface that was missing
3. parapet top — LIGHTEST, catching the warm doorway light

plus one vertical edge between 1 and 2, and a cast shadow onto the paving to the
left. Same technique as the ground-texture fix: a counted positive statement of what
is there beats any number of instructions about what should be separated.

## Drift

| | ratio |
|---|---|
| v005 | 0.2975 |
| v033 | 0.2905 |
| v034 | 0.3048 |
| **v035** | **0.2901** |

Sixth consecutive regeneration to drift brighter on a prompt that froze the lighting.

## Mask change

The architecture mask was extended left to x=360 and the crew protection tightened
to x<388 (Sion's arm ends at ~383), so the mask boundary no longer runs through the
new corner edge. In v031 a boundary placed at x=400 cut through this same area and
imported a merge while every outside-mask check read 0. **Diff the mask's edges
against the baseline, not only the area outside it.**

## Verification

vs v033: crew figures `300x480+40+440` **0 px changed**; crew edge energy
398.95 -> 398.60; ratio 0.2901 against v005's 0.2975. The corner was inspected at
150% in the composite, not only in the donor, to confirm the mask boundary did not
re-merge it.

Status: awaiting user evaluation
