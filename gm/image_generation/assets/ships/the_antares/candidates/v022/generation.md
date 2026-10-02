# Antares v022
User request: Its too angular. It does not have the same lines on the cockpit as the 3/4 image in the top left has. It does not have the mild protruberance where the cargo door is. It does not have the small flare and then 90 degree angle where the body meats the turbines. Try again.
Also, in the 3/4 top left image the engines are too far behind the body of the ship (that protruberance). In the heads on view the engines are not blocked by the ship body at all.
Mode: authorized local composite
Tool: ImageMagick, with built-in image_gen donors v020 and v021
Style: v2
Design: description.md (v12 = description_versions/description-v12.md)
Inputs:
- BASE: candidates/v017/image.png
- HERO DONOR: candidates/v020/image.png
- TOP-VIEW DONOR: candidates/v021/image.png
- HERO MASK: sources/composite-v022-hero-mask.png
- TOP MASK: sources/composite-v022-top-mask.png
Output: image.png, 1536 x 1024
Status: candidate; not promoted.

## Changes

The hero turbine placement now exposes the near intake fully clear of the aft side-body protrusion, with both pods following the revised mounting projection. The top outline restores the distinct cockpit shoulders, local cargo-bay projection and stepped body/engine region rather than a straight triangular silhouette. The second top-view attempt reduces the first attempt's larger lobes. Head-on, rear, both side views and both cargo insets are retained from v017.

## Replay

From the asset directory, with a scratch directory already created:
```sh
magick candidates/v017/image.png candidates/v020/image.png sources/composite-v022-hero-mask.png -composite <scratch-directory>/hero.png
magick <scratch-directory>/hero.png candidates/v021/image.png sources/composite-v022-top-mask.png -composite candidates/v022/image.png
```

Masks: hero rectangle 0,0 through 1120,535; top rectangle 1125,15 through 1510,544; white on black, alpha disabled. Exact generation prompts are recorded in v020/generation.md and v021/generation.md.

## Verification

Visual review of the hero intake clearance and the top-view cockpit, cargo housing, and aft body contours. Pixel Difference against v017 outside the two edited view rectangles is checked with alpha disabled. The images remain illustrative projections rather than a validated 3D model.
