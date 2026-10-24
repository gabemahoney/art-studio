# getting-sky v088

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "now try both"

## Sources

| region | from |
|---|---|
| everything | **v076** (v084's base, before the beams) |
| the Antares and her two trails | v076's own pixels through `mask-antares-and-trails.png` (her cutout alpha at +940+470 ∪ blue trail pixels b−r>0.10, b>0.45, dilated 4, blur 2.5), moved down 40 px |
| the area she left | **assets/locations/kalagra-storm-gorge/reference.png** through the same mask, gain-matched to v076's haze on a ring around the mask (R×1.36, G×1.385, B×1.41) |
| four beams | both gunships fire: the lead's two beams as v087, plus the wingman's two as v084 (slope 0.20, 4→340 px); from the LEAD (top) gunship's barrels (`beam-draw.sh`): muzzles (794,309) and (780,318), slope 0.24, 4→340 px, same style as v084 |

Status: awaiting user evaluation

Review: Both gunships firing; each pair straight along its own barrels, same length and style.
