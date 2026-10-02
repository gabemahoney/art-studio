# the-rusty-robot v037

Source: local composite, no generation. ImageMagick only; no model was called for
this file and nothing was billed. NOT raw model output.

User request verbatim: "No. The geometry is still bizarre. Sion is standing in front of a shadow that somehow becomes a wall at her feet. The whole alley needs a redo, I am afraid."
Mode: Path 1 masked tonal correction of v036, which was a full alley rebuild.

## Why the alley had to be rebuilt rather than patched

The alley had become a patchwork of four lineages that no longer described the same
space: the crew transplanted from v005, their immediate surroundings from the v027
lineage, and the adjacent architecture from v034. The dark region behind them was a
flat shape rather than a set of surfaces — no floor, no orientable walls — so it
terminated at a hard vertical line at Sion's boots and read as a wall rising out of
the ground in front of her.

Three patches had already failed on this. The fault was not an edge or a value
relationship; it was that the space did not exist. v036 respecified the alley as a
real place — floor continuous with the street and receding, two walls with
convergent edges, depth falling off toward the back — with the rule that **every
dark area must be a surface with an orientation, never a flat shape**. The crew were
repainted with it so their ground contact would be coherent.

## The cost, and the correction

v036 came back with the geometry right, the rendering crisper than any previous
version, and the crew far too bright: ratio 0.3452 against v005's 0.2975. A masked
`-evaluate multiply 0.8619` over the alley mouth restored it in one iteration.

| | ratio | crew edge energy |
|---|---|---|
| v005 | 0.2975 | 399.58 |
| v035 | 0.2901 | 398.60 |
| v036 (rebuild) | 0.3452 | 403.00 |
| **v037** | **0.2975** | **404.56** |

The edge energy is the highest of any version in this scene, including v005 — the
rebuild undid the cumulative softening without a transplant.

## Commands

```bash
magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle -80,350 440,1010 36,36" -blur 0x26 -alpha off mask-alley.png
magick v036/image.png -evaluate multiply 0.8619 adjusted.png
magick adjusted.png mask-alley.png -alpha off -compose CopyOpacity -composite layer.png
magick v036/image.png layer.png -compose over -composite image.png
```

Factor from target / current = 41.75 / 48.44, where the target is v005's ratio
applied to v036's own lit steps. Hit 41.75 first iteration.

## Verification

Pixels changed vs v036 outside the mask: far right `300x1024+1236+0` **0**, sign
`500x380+900+30` **0**, steps and street `400x300+700+700` **0**.

Still to confirm against the user: v036 was a full repaint, so the canopy ends, the
stair flanks and the handrails were all repainted and need re-checking against the
symmetry fixes won in v030-v034.

Status: awaiting user evaluation
