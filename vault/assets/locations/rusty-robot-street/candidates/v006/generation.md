# rusty-robot-street v006

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "No, the buildings are too varied in height."

## Sources

| region | from |
|---|---|
| x < 800, and the paving below y 890 | **v004** |
| x >= 800, y < 890: buildings to the right, sky, skyline | **v005** (moderate heights), via `mask-buildings-from-v005.png` (polygon 800,0 1536,0 1536,890 800,890, blur 0x5) |

Status: awaiting user evaluation

Review: Right-hand buildings now 3-5 storeys, gentle roofline steps, wall to wall. Faint dome-rib discontinuity at x~800 in the sky. Sign canopy (from v004) has mismatched perspective (user: "mangled").
