# getting-sky v017

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "yes" (plan: paint the Antares alone at the canyon's angle, paste into the gorge, blend pass)

## Sources

| region | from |
|---|---|
| everything | **assets/locations/kalagra-storm-gorge/reference.png** (approved gorge, v001) |
| the Antares | **outputs/getting-sky-antares-pose/v001** — cut from its flat grey (#6e6e6e) background with `mask-ship-from-pose-v001.png`; a stray third exhaust flame (box 330,135–476,216) removed from the mask; trimmed, scaled to 360x184, placed at +950+560 |

```bash
magick pose.png -fuzz 4% -fill black -opaque 'srgb(110,110,110)' -fill white +opaque black \
  -morphology Open Disk:1 -morphology Close Disk:2 -fill black -draw "rectangle 330,135 476,216" \
  -blur 0x0.7 -alpha off mask.png
magick pose.png mask.png -alpha off -compose CopyOpacity -composite -trim +repage ship.png
magick ship.png -resize 360x ship360.png
magick gorge.png ship360.png -geometry +950+560 -compose over -composite image.png
```

Ship axis (tail→nose) slope ~0.45, matching the gorge floor's line from the bend (~0.46).

Status: awaiting user evaluation

Review: Antares two pods, flying along the gorge line toward lower right, ~23% of frame width, clear air below. Not yet lit or hazed to match the storm.
