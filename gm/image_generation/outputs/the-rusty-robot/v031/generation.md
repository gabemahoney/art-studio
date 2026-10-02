# the-rusty-robot v031

Source: local composite, no generation. ImageMagick only; no model was called for
this file and nothing was billed. NOT raw model output.

User request verbatim: "Stairs are still not symmetrical. Nor is the overhang below the sign."
Mode: Path 3. v030 was generated from v029 for the architecture only; its canopy and
stair flanks are taken, its drift is discarded.

## Sources

| region | from |
|---|---|
| canopy over the door, staircase and both flanks | v030 (brightness-matched x1.0156) |
| everything else, including the crew | v029 |

## What was actually asymmetric

v028 made the flanks the same *kind* of structure, and I wrongly called that done.
Five specific differences remained, and naming them individually is what fixed them —
asking for "symmetry" in general had not:

Canopy: the left end's outer corner was cut back on a diagonal chamfer with a
stepped bracket beneath; the right end was a plain blunt slab with neither.

Stair flanks: (1) the right pier had a chamfered cap, the left a plain flat top;
(2) an extra lower block stood beyond the right pier with no counterpart on the
left; (3) the bottom step projected further past the right pier than the left.

## Drift, and why only two regions were taken

| | crew/steps ratio | crew edge energy |
|---|---|---|
| v005 | 0.2975 | 399.58 |
| v029 | 0.2906 | 399.00 |
| v030 | 0.3176 | 396.69 |
| **v031** | **0.2910** | **399.00** |

v030 drifted brighter again (0.2906 to 0.3176) on a prompt that explicitly froze the
lighting — the fourth time in this scene. Its architecture was wanted; nothing else
was.

## Commands

```bash
# architecture mask: canopy + stairs, MINUS the crew, so the v005 transplant in v029
# is never overwritten
magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle 240,110 1010,392 24,24" \
  -draw "roundrectangle 400,430 1200,1012 30,30" -blur 0x20 -alpha off arch.png
magick -size 1536x1024 xc:white -fill black \
  -draw "roundrectangle 0,396 408,1000 24,24" -blur 0x18 -alpha off nocrew.png
magick arch.png nocrew.png -compose multiply -composite -alpha off mask-architecture.png

magick v030/image.png -evaluate multiply 1.0156 d30.png
magick d30.png mask-architecture.png -alpha off -compose CopyOpacity -composite l30.png
magick v029/image.png l30.png -compose over -composite image.png
```

## Verification

Pixels changed vs v029:

- crew figures `300x480+40+440`: **0** — edge energy held at exactly 399.00
- ground below the boots `420x60+20+975`: 2335, all of it street inside the stair
  mask; no rubble returned
- far right strip `300x1024+1236+0`: 485, mask-feather overlap only

Status: awaiting user evaluation
