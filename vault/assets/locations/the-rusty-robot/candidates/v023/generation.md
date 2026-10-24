# the-rusty-robot (asset) v023

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "can we do one more pass on making the surface underside of the marque look correct? It looks like someone took a smudgetool to the middle." / approval: "Yes. Please be more clear when you are asking for permission."

## Sources

| region | from |
|---|---|
| everything | **v021**, byte-for-byte outside the mask |
| canopy underside, three-quarter view | **v022** (masked API inpaint), via `mask-inpaint-from-v022.png` (`tmp/mask-rr-underside-full.png` blurred 0x1.5) |

```bash
magick v022/image.png mask-inpaint-from-v022.png -alpha off -compose CopyOpacity -composite ip.png
magick v021/image.png ip.png -compose over -composite -alpha off image.png
```

Status: approved and promoted to reference.png on 2026-10-03. User approval: "Probably good enough. Finalize it"

Review: Underside reads as one even concrete slab; straight edges. The fins' tops meet it with a slightly soft edge at 400%.
