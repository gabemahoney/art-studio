# the-rusty-robot (asset) v021

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "there is a vague light fixture on the bottom of the marquee. We should remove it. The two side lights and one spotlight are sufficeint." / approval: "yes"

## Sources

| region | from |
|---|---|
| everything | **v019**, byte-for-byte outside the mask |
| canopy underside strips, three-quarter view and front elevation | **v020** (masked API inpaint), via `mask-inpaint-from-v020.png` (`tmp/mask-rr-underside-light.png` blurred 0x1.5) |

```bash
magick v020/image.png mask-inpaint-from-v020.png -alpha off -compose CopyOpacity -composite ip.png
magick v019/image.png ip.png -compose over -composite -alpha off image.png
```

Status: awaiting user evaluation

Review: Underside light strip gone in both views. In the three-quarter view the repainted strip is slightly darker than the lit underside just left of it — a faint tonal step at x~497.
