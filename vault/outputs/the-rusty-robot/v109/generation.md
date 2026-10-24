# the-rusty-robot v109

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "it looks very good but Sions left foot seem to be IN the wall"

## Sources (layered rebuild per the skill's core rule)

| region | from |
|---|---|
| everything | **v100** (approved v099 + dark window), byte-for-byte outside the mask |
| alley and crew | **v108** (crew painted alone with the lineup attached, pasted into the emptied alley, then one blend pass with the lineup attached), via `mask-alley-and-crew-from-v108.png` (alley polygon 42,440 335,440 345,520 345,930 42,930 ∪ the crew silhouette dilated 4 px) |

Chain: v101 (empty alley) → crew-pose v002 (faces checked) → v106 (paste, 20 px lower than v102) → v108 (blend) → v109 (keep alley region only).

## Verification

Pixels changed vs v100 outside the mask: 0. Faces checked at 200% against the lineup.

Status: awaiting user evaluation

Review: Feet now on the paving in front of the side wall; faces match the lineup; everything outside the alley identical to v100.
