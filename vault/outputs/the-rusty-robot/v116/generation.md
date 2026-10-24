# the-rusty-robot v116

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "Can you try one where she is doing the pointing pose again? Like in v5?"

## Sources (layered rebuild per the skill's core rule)

| region | from |
|---|---|
| everything | **v100** (approved v099 + dark window), byte-for-byte outside the mask |
| alley and crew | **v114** (crew painted alone with the lineup attached, pasted into the emptied alley, then one blend pass with the lineup attached), via `mask-alley-and-crew-from-v114.png` (alley polygon 42,440 335,440 345,520 345,930 42,930 ∪ the crew silhouette dilated 4 px) |

Chain: v101 (empty alley) → crew-pose v002 → crew-pose v003 (Sion pointing, as v005) → v113 (paste) → v114 (blend) → v116 (keep alley region only).

## Verification

Pixels changed vs v100 outside the mask: 0. Faces checked at 200% against the lineup.

Status: approved and promoted to final.png on 2026-10-05. User approval: "v116"

Review: Sion points at the men as in v005; feet on the paving; faces match the lineup; 0 px changed outside the alley vs v100.
