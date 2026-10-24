# the-rusty-robot (asset) v016

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "Except...the right side of the bottom of the marquee looks weird. Its not a straight line nere the right columns"

## Sources

| region | from |
|---|---|
| everything | **v014** (v012 + v013's emblem) |
| canopy underside's right end and right end face, three-quarter view | **v015**, via `mask-canopy-right-from-v015.png` (polygon 640,640 868,640 868,560 950,560 950,730 640,730, blur 0x3; stops below the emblem so v014's emblem is kept) |

```bash
magick v015/image.png mask-canopy-right-from-v015.png -alpha off -compose CopyOpacity -composite cr.png
magick v014/image.png cr.png -compose over -composite -alpha off image.png
```

Status: awaiting user evaluation

Review: Underside's back edge now straight past the right fin; emblem with two eyes intact; everything else is v012. Three storeys (description says four) — user accepted the sheet as "the one".

## Incident, 2026-10-03

`image.png` was annotated (red ellipse) and saved over by the user. Restored by
re-running the two commands above; the restored file differs from the annotated one
only in the ellipse's box (147x68+725+633).
