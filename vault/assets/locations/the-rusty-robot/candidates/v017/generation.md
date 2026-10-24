# the-rusty-robot (asset) v017

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "see this intersection. The marquee line should be straight." [ellipse around the canopy underside where it meets the right fin, three-quarter view]

## Diagnosis

At 500%: the underside's back edge ran straight along the wall and the right fin's top,
then at x~848 turned sharply up toward the canopy's front tip (907,650) — the canopy
ended ~40 px short of the building's right corner (x~890) and hung down in a point
over the fin's side face.

## Sources

| region | from |
|---|---|
| everything | **v016** |
| underside extended to the building corner | flat fill, horizontal gradient #87591f → #755021 (sampled from the underside at x 800–885), via `mask-underside-extend.png` (polygon 775,658 845,662 870,656 906,649 892,677 775,663, blur 0x0.8) |

```bash
magick -size 1536x1024 -define gradient:vector=775,0,906,0 gradient:'#87591f'-'#755021' fill.png
magick fill.png mask-underside-extend.png -alpha off -compose CopyOpacity -composite fl.png
magick v016/image.png fl.png -compose over -composite -alpha off image.png
```

Status: awaiting user evaluation

Review: REJECTED by user: the extended right end of the underside is at the wrong angle and has none of the canopy's painted texture. Cause: slope picked from the local edge, not from the building's perspective; flat gradient fill in a dry-brush style. My own review called it straight at 2x.
