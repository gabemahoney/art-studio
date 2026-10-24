# getting-sky v083

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "they look OK but they should paint OVER the Antares so it looks like they are going OVER it. Also, they should not be a darker red at the turret origin"

## Sources

| region | from |
|---|---|
| everything | **v076** |
| two beams | drawn with ImageMagick (`beam-draw.sh`) from the wingman's two barrels only — muzzles (546.5,446) and (537.5,456), along the measured barrel axis (slope 0.20), each 950 px long; tapered polygons, one colour from origin to tip: red glow (35% alpha) 4→16 px, solid red core #f23024 2.2→7 px, pale centre line 1→2.4 px |

Status: awaiting user evaluation

Review: User: 'also not working'. Next: beams short of the Antares (v084) and detached from the turret (v085).
