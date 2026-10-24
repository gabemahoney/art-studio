# Antares v015

User request: It looks good. One small note we should fix. In the cargo door break out, it shows blue background just above the door. But if you were to view the ship from that angle, you would actually see the top part of the ship above the cargo door, not blue background. It makes it look like the ship is flatter than it truly is.

Also, The front view has the engine turbines very wide apart while the back view has them very close. The back view is wrong. Looking at the 2/3 and top views it does seem like the turbines should be more far apart. Modify the back view.

Mode: user-authorized local image composite
Tool: ImageMagick 7.1.2-27; generated donor from built-in image_gen v014
Style: v2, inherited from the frozen inputs
Design: description.md (v9 = description_versions/description-v9.md)
Inputs:
- BASE and upper-hull geometry: candidates/v013/image.png
- LOCAL DONOR: candidates/v014/image.png (full generation prompt recorded in candidates/v014/generation.md)
- REPLAY SCRIPT: sources/composite-v015.sh
Output: image.png, 1536 x 1024
Status: candidate, not promoted

## Changes

Open cargo detail now shows the existing fixed upper hull behind and above the raised panel. Upper structure is copied from the hero view; the top crop border extends upward 30 pixels to show it. The original raised panel is protected by a polygon mask, retaining its dimensions, angle and low hinge. Crew and ramp remain original.

Rear view uses separated turbines approximately four diameters apart, with the smaller drawing fitting its existing allotted area. Turbine centers are approximately x71 and x364; visible diameters approximately 72 pixels. Central aft hull is reduced to the corresponding local drawing scale, and mounting arms join it to the turbines. Other views keep their prior engine positions and dimensions.

## Exact replay

From the asset directory, create a scratch directory with mktemp -d, then run:
```sh
sh sources/composite-v015.sh <scratch-directory>
```
The output is <scratch-directory>/composite.png. Copy it to a new candidate's image.png. The script records all source crops, resizes, silhouettes, masks, and compositing operations. No new image-generation call was made for this composite; v014's exact prompt is its donor provenance.

## Validation

Visual review: upper-hull mass visible above raised cargo door; widened rear turbine spacing, with preserved ship colors and style. Pixel comparisons against v013 confirm zero difference in the hero, front, top, port and starboard profiles, closed inset, and crew/ramp regions. Rear-mask blur is clipped before x417 to protect the adjacent profile. Candidate remains unpromoted.
