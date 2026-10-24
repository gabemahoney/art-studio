# hegemony-assault-ship v013

User request verbatim: The 2/3 and side views are incorrect geometry and the symbols is wrong on the 2/3 view. The front and topdown views are correct. Why dont you just totally remove the 2/3 view (mask it out) and rebuild it from scratch using the topdown and front views as the guide.
Mode: Masked API off v009, attempt 1: everything except the top-down and front views repainted; three-quarter and side views rebuilt from them.
Tool: bin/gen.py, backend=api (OpenAI Images API /v1/images/edits)
Model: gpt-image-2.5-sunburst-2026-09-08 (pinned snapshot)
Parameters: size requested 1536x1024, quality=high, n=1
Prompt integrity: OpenAI Images API, exact prompt bytes sent
Mask: tmp/mask-as-rebuild.png (white = repainted; only those pixels regenerate)
API approval, verbatim: approved paid / Why dont you just totally remove the 2/3 view (mask it out) and rebuild it from scratch using the topdown and front views as the guide. / do that until the model gets it right
Style: v3
Inputs:
- Image 1 EDIT TARGET: assets/ships/hegemony-assault-ship/candidates/v009/image.png
- Image 2 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
Token usage: {"input_tokens": 3805, "input_tokens_details": {"image_tokens": 3072, "text_tokens": 733}, "output_tokens": 1372, "output_tokens_details": {"image_tokens": 1372, "text_tokens": 0}, "total_tokens": 5177}
Date: 2026-10-03
Status: approved and promoted to reference.png on 2026-10-03. User approval: "ver good."
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.76 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Masked API off v009, attempt 1. Three-quarter and side views rebuilt from the top and front views: pods as two mirrored pairs all pointing aft, star centred on the hull top between cockpit and turret, squat side profile. Top and front views preserved. Composite onto v009 tried and discarded: the background grey differs, leaving a halo around the kept views; v013 whole is better. Tokens 3,805 in.

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

Image 1 is EDIT TARGET: The reference sheet. Its top-down and front views are correct; only the masked area changes.
Image 2 is STYLE: Match its hand-painted matte rendering only. Ignore its subjects.

TASK: Rebuild two views of this ship reference sheet.

This is a reference sheet of one ship on a plain mid-grey background. Two of its views
are correct and stay exactly as they are: the TOP-DOWN plan view (middle right, nose
to the left) and the HEAD-ON front view (lower right). Repaint only the masked area:
the empty grey, and two new views built strictly from those two correct views.

1. LEFT HALF, large: a THREE-QUARTER VIEW of the same ship from in front, above and to
   its left, in flight. Every part matches the top-down and front views: the same hull
   outline, cockpit, chin turret with two barrels, spine details, and the four
   thruster pods as two mirrored pairs — each pair the same size, at the same height,
   equally far from the centreline, all four pointing straight back with their
   exhausts glowing behind the ship. The red Hegemony star sits exactly where it is in
   the top-down view: on the centreline of the hull top, centred between the cockpit
   and the turret, lying flat on the hull in its perspective.
2. UPPER RIGHT: a SIDE ELEVATION, nose to the left, the same length as the top-down
   view, its profile matching the front view's height: low and squat. One near pair of
   pods visible, pointing back.

Same black armour, red bands and red line-built star as the correct views. Plain
mid-grey everywhere else. No text.

Render everything in the exact brush scale of the style anchor attached to this call: fewest possible flat shapes, no blending, no micro-detail.
