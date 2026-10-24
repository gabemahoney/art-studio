# the-rusty-robot v105

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "Ok. Now try this with the characters at the cantina"

## Sources (layered rebuild per the skill's core rule)

| region | from |
|---|---|
| everything | **v100** (approved v099 + dark window), byte-for-byte outside the mask |
| alley and crew | **v103** (crew painted alone with the lineup attached, pasted into the emptied alley, then one blend pass with the lineup attached), via `mask-alley-and-crew-from-v103.png` (alley polygon 42,440 335,440 345,520 345,905 42,905 ∪ the crew silhouette dilated 4 px) |

Chain: v101 (empty alley) → crew-pose v002 (faces checked) → v102 (paste) → v103 (blend) → v105 (keep alley region only).

## Verification

Pixels changed vs v100 outside the mask: 0. Faces checked at 200% against the lineup.

Status: awaiting user evaluation

Review: User: 'very good' but Sion's foot appears to be in the wall (feet on the wall/paving line). Redone 20 px lower in v109.
