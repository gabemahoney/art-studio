# Antares v017
User request: "It looks [Image #1] , the area I circled in red still looks wrong."
Mode: authorized local compositing of rebuilt cargo-door insets
Tool: ImageMagick, with built-in image_gen donor candidates/v016/image.png
Style: v2
Design: description.md (v10 = description_versions/description-v10.md)
Inputs:
- BASE: sources/unmarked-v015-composite.png (unannotated v015 recovered from the prior run's exact final composite; user's annotated candidates/v015/image.png left untouched)
- DONOR: candidates/v016/image.png (full exact prompt and source inputs in candidates/v016/generation.md)
- MASK: sources/composite-v017-mask.png
Output: image.png, 1536 x 1024
Status: candidate; not promoted.

## Changes

Both cargo insets are redrawn at a wider framing with consistent fixed upper side wall, recessed deck, and central spine above the door. The raised door is wholly within the inset and sits below the visible upper ship structure. The closed and open details share perspective and surrounding geometry. The new inset interiors replace the flawed pasted geometry; the remaining sheet, including widened rear turbine spacing, is retained.

## Exact composite

Run from the asset directory:
```sh
magick -size 1536x1024 xc:black -fill white -draw 'rectangle 932,727 1194,980 rectangle 1209,699 1504,980' -alpha off sources/composite-v017-mask.png
magick sources/unmarked-v015-composite.png candidates/v016/image.png sources/composite-v017-mask.png -composite candidates/v017/image.png
```

The mask also replaces the former raised frame and panel extending above the open inset, restoring background there from the rebuilt sheet. No red annotation is included. Generation prompt: see candidates/v016/generation.md.

## Verification

Visual review: two matching cargo details now contain continuous ship mass above the low lateral hinges and show one rectangular door in closed/open states. The right inset retains three adult crew and a ramp. RGB Difference against sources/unmarked-v015-composite.png outside the two mask rectangles is zero (alpha disabled for the statistic); the rest of the sheet is pixel-identical.
