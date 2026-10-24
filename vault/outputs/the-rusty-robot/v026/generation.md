# the-rusty-robot v026

User request verbatim: This triangular element is out of place. It does not exist on the other side of the stairs.
Mode: Edit off v025. Single architectural change: the sloping triangular wedge at the left foot of the stair flight removed, since the right-hand flank terminates in a plain squared block and the mismatch read as an unexplained oddity. The left flank is rebuilt as a matching squared cheek wall with a flat top and vertical faces, with all diagonals, slopes, ramps and slanted edges explicitly banned at the foot of the stairs on both sides, and the two sides required to read as a matching pair allowing only for perspective foreshortening. Treads, handrails, flight width and step positions frozen, as are the lighting, the crew, the sign with its solid filled emblem, the lamps, the buildings and the paving.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f574-221d-7fd3-bcd4-15c92868282c/exec-8cbc9a38-7085-4a70-92a7-7832eab922c2.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v025/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.91 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Wedge removed cleanly. The sloping triangular ramp at the left foot of the stair flight is gone, and the left flank now terminates in a plain squared cheek wall with a flat top and vertical faces, matching the squared block on the right. No diagonal, slope or slanted edge remains at the foot of the stairs on either side, the treads run cleanly to the block, and the two flanks read as a matching pair allowing for perspective. Treads, handrails, flight width and step positions are unchanged. Everything else held: camera, framing, the three crew and their postures, Graxo's shortened nose, the sign with its dark rusted board, chipped ivory lettering reading exactly "THE RUSTY ROBOT" and its bold solid filled robot emblem with cut-out eyes and bow tie, the armoured brow, the industrial angular lamps, the grey ferrocrete with teal bands, the clean dry paving, the dome and the alley. File is 1.91 MB, inside the book-float budget. CUMULATIVE LIGHTING DRIFT — THE ONE SERIOUS ISSUE. Mean luminance of the crew region against the lit steps region has crept upward on every pass since the v005 branch: v005 and the branch point v023 both sit at 0.33 and 0.34, then v024 at 0.38, v025 at 0.40 and now v026 at 0.42. That is roughly a 24 percent brightening of the crew relative to the lit area across three edits, none of which requested any lighting change and each of which explicitly froze it. The cause appears to be that "reproduce image 2 and change only X" is not perfectly lossless on values — each regeneration re-paints the whole picture and the shadowed figures drift a little lighter each time. This matters because the crew's depth of shadow is the single element the user has corrected most often in this scene, and v023 had it correct. It should be pulled back to about 0.33 in a dedicated pass that changes nothing else, and any future edits to this scene should re-measure it afterwards rather than assuming a freeze instruction held.

## Exact prompt

Hand-painted flat angular matte gouache illustration in the manner of late-1970s
TSR tabletop-RPG interior art (Star Frontiers, early Dungeons & Dragons) — poster
paint, not digital illustration. Build every form from a few large flat opaque
color planes with hard edges. Plane edges are straight or crisply angled —
chiseled, polygonal shapes, never soft rounded blobs; shadow meets light in a
straight angular seam. HARD LIMITS: a face is five to eight flat planes
total; any surface gets at most three value steps; shadow is one darker flat
plane, never a gradient or blend. Hair is one or two chunky painted masses —
silhouette only, zero strands. Fabric folds are a few straight angular strokes.
Equipment, trim, patterns and fasteners are simplified blocks of color — details
suggested, never drawn. Muted palette: slate blue-gray, warm ochre, ivory,
brick-red accents. Coarse dry-brush edges and broken pigment on large areas;
large areas stay quiet and under-detailed. When in doubt, paint LESS: fewer
shapes, fewer details, flatter.

Forbidden: smooth gradients, airbrush or glossy digital shading, photographic
detail or realistic skin, fine linework or fine hair strands, surface
subdivisions or micro-detail, more than three values on any surface, neon or rim
lighting, uniform granular noise, dense tiny facets or polygon mosaics, and the
polished modern AI character-sheet look.

## Note on the Forbidden list

Every item in the Style Block's "Forbidden" line names a **rendering tell**, not a
subject: smooth gradients, airbrush, photographic detail, fine linework,
micro-detail, more than three values, granular noise, polygon mosaics, the polished
modern AI look — and, in that same company, **"neon or rim lighting."**

So "neon" there forbids the *look*: saturated glow, bloom, halo, soft falloff, the
lit-from-within sheen of modern digital art. It does **not** forbid lit signage,
lamps, glowing instruments or electric light as subject matter. The world can have
neon in it; the painting must not be rendered like neon.

A lit sign is therefore fine when it is painted the way this style paints
everything else: flat opaque shapes with hard edges, a bright core and at most one
darker band of the same hue, no glow, no gradient, no rays. Recorded 2026-09-30
after the electric sign in `outputs/the-rusty-robot/`, where reading the ban as a
subject prohibition would have blocked a legitimate art direction.

This note sits outside the Style Block and changes none of its text, so it does not
require a style version bump.

Image 1 is STYLE: Match this image's hand-painted matte rendering technique ONLY. Ignore and do not reproduce its people, clothing, equipment, interior, setting or composition.
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v025. Correct in every respect except for an asymmetric triangular wedge at the left foot of the stairs.

TASK: A single 3:2 horizontal evening street scene: the approved cantina picture with its stair flanks rebuilt as a matching pair of squared blocks.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE small thing below.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers stand in the shadow of an alley at the left, conferring, across from the lit door of a cantina called The Rusty Robot.

IMAGE 2 IS APPROVED AND CORRECT IN EVERY RESPECT BUT ONE PIECE OF ARCHITECTURE. Keep absolutely everything else exactly as it is: the camera, framing and composition; the lighting, with its warm golden pool across the entrance, steps and paving and the cool blue-grey shadow elsewhere; the three crew at their exact positions, sizes, postures and depth of shadow, and every part of their clothing, equipment and faces including Graxo's shortened nose; the SIGN flat on the wall with its dark rusted board, its chipped ivory lettering reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals, and its BOLD SOLID FILLED robot emblem with the eyes and bow tie as dark cut-outs; the hooded lamp above the board; the armoured brow; the round-arched ribbed door; the STEPS themselves and their pipe handrails; the two INDUSTRIAL ANGULAR LAMPS with flat downward-facing lit panels; the GREY FERROCRETE buildings with their MUTED TEAL painted bands; the domed tower, the dome overhead, the distant figures, the alley; and the CLEAN DRY PAVING with its drifted dust and no rocks, rubble or gravel. Do not re-frame, do not zoom, do not move anyone, do not change any lighting, do not touch the sign.

THE ONE CHANGE — REMOVE THE TRIANGULAR WEDGE AT THE FOOT OF THE STAIRS. At the LEFT-HAND side of the flight of steps, where the stairs meet the pavement, there is a sloping TRIANGULAR WEDGE: a ramp-like diagonal mass running up from the ground to the lowest tread, forming a long slanted edge against the side of the stair.

The RIGHT-HAND side of the same flight has no such thing — it ends in a plain squared block. The two sides therefore do not match, and the wedge reads as an unexplained oddity.

DELETE the wedge. Rebuild the left side of the stair so that it MIRRORS the right:
- The left flank of the steps now ends in a PLAIN SQUARED BLOCK of the same grey ferrocrete — a simple rectangular cheek wall with a flat level top and vertical faces, exactly the kind of squared termination the right-hand side already has.
- There is NO diagonal, NO slope, NO ramp, NO triangular face and NO slanted edge anywhere at the foot of the stairs on either side.
- The treads run cleanly to that squared block, and the block meets the pavement in a straight horizontal line.
- Make the two sides of the stair read as a MATCHING PAIR: the same squared form, the same height and the same proportions on the left as on the right, allowing only for the natural difference in how perspective foreshortens the nearer and farther sides.

Keep the handrails, the number of treads, the width of the flight and the position of the steps exactly as image 2 has them. The ground in front of the new block is the same clean dry dusty paving, with the warm lamplight falling across it as before.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
