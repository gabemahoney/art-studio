# the-rusty-robot (asset) v019

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "Lets try the API key approach using the new skills. Set it up first." / approval: "yes"

## Sources

| region | from |
|---|---|
| everything | **v016**, byte-for-byte outside the mask |
| canopy underside's right end and right fin top | **v018** (masked API inpaint), via `mask-inpaint-from-v018.png` (`tmp/mask-rr-canopy-right.png` blurred 0x1.5) |

```bash
magick v018/image.png mask-inpaint-from-v018.png -alpha off -compose CopyOpacity -composite ip.png
magick v016/image.png ip.png -compose over -composite -alpha off image.png
```

## Verification

Pixels changed vs v016 outside the mask plus a 6 px margin: 0.

Status: awaiting user evaluation

Review: v018's repaired canopy corner on otherwise pixel-identical v016: straight underside edge, flat fin top, matching texture, no visible seam at 200%.
