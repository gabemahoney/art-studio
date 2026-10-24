# the-rusty-robot v060

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "There is still assymetry and cruft around the overhang that sits above the steps and below the sign."

## Sources

| region | from |
|---|---|
| the alley corner and the crew (x < 446, y 402-950) | **v005**, x1.0629 |
| everything else | v059 |

## The technique that found it

Three earlier passes "fixed" the canopy and the asymmetry survived each time, because
at normal size the two ends look broadly alike. **Cropping both ends and MIRRORING one
before comparing them made it obvious in one look:**

```bash
magick f.png -crop 300x260+300+150 +repage -resize 260% endL.png
magick f.png -crop 300x260+760+230 +repage -flop -resize 260% endR.png   # -flop mirrors
magick endL.png endR.png -background '#555' -splice 14x0 +append cmp.png
```

The left end was TWO large square tiers. The right was four or five small ones plus
short nibs and narrow ledges projecting from the corner and the wall beside it — a
jagged staircase of fragments. Side by side unmirrored, that reads as "similar";
mirrored, it reads as obviously different.

**For any symmetry check, mirror one side and compare directly. Do not judge symmetry
by looking at the whole.**

The fix then used the referent pattern that worked for the handrail: name the correct
side, freeze it, describe how it is built, and make the other match — with a count
("exactly two tiers, not three, not four") and an explicit deletion rule ("if a shape
is smaller than one of the two tiers, it should not be there").

## Measurements

| | ratio | crew edge energy |
|---|---|---|
| v005 (the target) | 0.2975 | 399.58 |
| v058 | 0.2975 | 400.10 |
| **v060** | **0.2979** | **398.11** |

The lift factor was recomputed against v059's own lit steps (140.21), giving 1.0629.

## Commands

```bash
magick -size 1536x1024 xc:black -fill white \
  -draw "rectangle -60,402 446,950" -blur 0x3 -alpha off mask-v005-corner.png
magick v005/image.png -evaluate multiply 1.0629 lifted.png
magick lifted.png mask-v005-corner.png -alpha off -compose CopyOpacity -composite layer.png
magick v059/image.png layer.png -compose over -composite image.png
```

The near-hard `-blur 0x3` cut at x=446 sits on the cantina corner edge that exists in
both images, so the two paintings meet at a real edge instead of cross-dissolving.
Mask coverage over the crew box was asserted at 255 before compositing, after the
`roundrectangle ... 0,0` trap silently produced an empty mask in v058's first attempt.

## Verification

vs v059: sign **0 px**, far right **0 px**. The stairs/door box changes only where
the mask's right edge at x=446 crosses it.

Status: awaiting user evaluation
