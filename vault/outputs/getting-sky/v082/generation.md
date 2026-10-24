# getting-sky v082

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "lets try only having blasts come from the bottom ship. they come from both turrets at the same time, same length from each turret. they are shooting PAST the Antreas. The beams are red and thicker at the front than they are at the turret origin"

## Sources

| region | from |
|---|---|
| everything | **v076** |
| two beams | drawn with ImageMagick (`beam-draw.sh`) from the wingman's two barrels only — muzzles (546.5,446) and (537.5,456), along the measured barrel axis (slope 0.20), each 950 px long; tapered polygons: crimson glow 3→15 px, red core 1.6→7 px, pale centre line 0.6→2.4 px |
| the Antares, on top | v076's own pixels through `mask-antares-occluder.png` (her cutout alpha at +940+470, eroded 1 px), so the beams pass behind her and emerge beyond her nose |

Status: awaiting user evaluation

Review: User: 'look OK' but beams should paint OVER the Antares, and no darker red at the turret origin (v083).
