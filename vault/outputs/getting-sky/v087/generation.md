# getting-sky v087

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "can you try one where its the top ship firing instead?"

## Sources

| region | from |
|---|---|
| everything | **v076** (v084's base, before the beams) |
| the Antares and her two trails | v076's own pixels through `mask-antares-and-trails.png` (her cutout alpha at +940+470 ∪ blue trail pixels b−r>0.10, b>0.45, dilated 4, blur 2.5), moved down 40 px |
| the area she left | **assets/locations/kalagra-storm-gorge/reference.png** through the same mask, gain-matched to v076's haze on a ring around the mask (R×1.36, G×1.385, B×1.41) |
| two beams | drawn last from the LEAD (top) gunship's barrels instead (`beam-draw.sh`): muzzles (794,309) and (780,318), slope 0.24, 4→340 px, same style as v084 |

Status: awaiting user evaluation

Review: Top ship fires; beams end well above and ahead of the Antares's far pod, clear of both trails.
