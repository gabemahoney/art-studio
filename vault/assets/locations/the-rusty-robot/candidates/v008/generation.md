# the-rusty-robot (asset) v008

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "also fix the lettering so its on the same plane as the marquee"

## Sources

| region | from |
|---|---|
| everything | **v007** |
| sign board, three-quarter view | `sources/sign-board-flat-from-v082.png`, perspective-warped onto the canopy's front face |
| lamp hood on the canopy | v007 again, over the warped board, via `mask-lamp-hood.png` |

The canopy's front face in v007's three-quarter view, measured by eye on a gridded
crop: TL (305,331), TR (862,454), BR (881,573), BL (189,546). Its side edges lean
outward as they descend; v007's board leaned inward, which is why it read as off the
plane. The new board's corners are bilinear points of that quad at u 0.10–0.96,
v 0.04–0.96, so its edges follow the face and it fully covers v007's board.

```bash
magick sources/sign-board-flat-from-v082.png -alpha set -background none -mattecolor none \
  -virtual-pixel transparent -define distort:viewport=1536x1024+0+0 \
  -distort Perspective "0,0 357,352 748,0 840,454 748,230 853,567 0,230 262,540" +repage warp.png
magick -size 1536x1024 xc:black -fill white -draw "polygon 540,355 655,358 652,402 545,398" \
  -blur 0x1 -alpha off mask-lamp-hood.png
magick v007/image.png mask-lamp-hood.png -alpha off -compose CopyOpacity -composite hood.png
magick v007/image.png warp.png -compose over -composite hood.png -compose over -composite -alpha off image.png
```

## Verification

Pixels changed vs v007 outside the board quad `355,350 842,452 855,569 260,542`: 1.

Status: awaiting user evaluation

Review: REJECTED by user ('v8 looks horrible', 'the 3/4 view has the sign completely messed up'). The perspective-warped board reads as a pasted, slanted decal. Do not build on it.
