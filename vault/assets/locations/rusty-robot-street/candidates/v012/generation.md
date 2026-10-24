# rusty-robot-street v012

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "Can you try fixing up the dome supports? some are going at random angles." / approval: "yes"

## Sources

| region | from |
|---|---|
| everything | **v010** (approved reference), byte-for-byte outside the mask |
| sky above the far street | **v011** (masked API inpaint), via `mask-inpaint-from-v011.png` (`tmp/mask-street-dome.png` blurred 0x2) |

Status: awaiting user evaluation

Review: REJECTED by user ('That masking did not work'): the mask's bottom edge was a straight line across open sky, so ribs and a spire broke along it and the blur smeared it.
