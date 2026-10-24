# Antares v019
User request: Looks good. I believe the top down view iss till incorrect. Those wings are too wide in the center. I do not see that protrusion in the mid section when lookg at the other angles. It looks instead like the ship is more of a triangle or "flying V". Can you revise the top down view?
Mode: user-authorized local composite
Tool: ImageMagick, with built-in image_gen donor candidates/v018/image.png
Style: v2
Design: description.md (v11 = description_versions/description-v11.md)
Inputs:
- BASE: candidates/v017/image.png (user-designated baseline)
- TOP-VIEW DONOR: candidates/v018/image.png
- MASK: sources/composite-v019-mask.png
Output: image.png, 1536 x 1024
Status: candidate; not promoted.

## Change

Replace only the upper-right top projection. Its outer hull now tapers continuously from the aft region toward the cockpit, without the midship wings and squared lateral tabs. The engine pods retain their outboard aft positions. All other sheet views and cargo insets come unchanged from v017.

## Exact replay

From the asset directory:
```sh
magick -size 1536x1024 xc:black -fill white -draw 'rectangle 1125,15 1510,544' -alpha off sources/composite-v019-mask.png
magick candidates/v017/image.png candidates/v018/image.png sources/composite-v019-mask.png -composite candidates/v019/image.png
```

The exact generation prompt is recorded in candidates/v018/generation.md. There is no new generation prompt for this composite.

## Verification

Visual inspection: triangular tapered top planform, no central wing-like protrusions; nose points down, engines remain outboard at the aft end. RGB Difference outside rectangle 1125,15–1510,544 is zero against v017.
