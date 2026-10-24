# getting-sky v086

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "84 is good. can we move the Antares a little lower down so its fore jet engine trail is not obscured by the laser?"

## Sources

| region | from |
|---|---|
| everything | **v076** (v084's base, before the beams) |
| the Antares and her two trails | v076's own pixels through `mask-antares-and-trails.png` (her cutout alpha at +940+470 ∪ blue trail pixels b−r>0.10, b>0.45, dilated 4, blur 2.5), moved down 40 px |
| the area she left | **assets/locations/kalagra-storm-gorge/reference.png** through the same mask, gain-matched to v076's haze on a ring around the mask (R×1.36, G×1.385, B×1.41) |
| two beams | redrawn last, identical to v084 (`beam-draw.sh`: wingman barrels, slope 0.20, 4→340 px) |

Status: awaiting user evaluation

Review: User found white cruft right of the Antares: the gorge fill (gain-matched gorge) was much brighter than v076's darkened rock where her nose used to be, plus a haze halo carried by the over-dilated mask. Fixed in v089.
