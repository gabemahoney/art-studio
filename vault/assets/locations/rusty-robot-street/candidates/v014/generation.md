# rusty-robot-street v014

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "Can you try fixing up the dome supports? some are going at random angles." / "you decide. you are learning, and wil update the skills if you learn something useful"

## Sources

| region | from |
|---|---|
| everything | **v010** (approved reference), byte-for-byte outside the mask |
| sky and distant skyline above the far street | **v013** (Codex edit, regular lattice), via `mask-sky-from-v013.png` |

The mask's edges all fall on real boundaries — the near rooftops on the left, the far
bridge along the bottom, the right-hand building's roof — never across open sky:

    polygon 975,0 975,80 1026,78 1082,176 1162,176 1164,246 1211,246 1214,343
            1283,343 1323,467 1493,467 1493,373 1536,360 1536,0   (blur 0x2)

Status: awaiting user evaluation

Review: REJECTED by user: artifact above one of the buildings where the hand-traced mask met a rooftop; v013 whole was preferred.
