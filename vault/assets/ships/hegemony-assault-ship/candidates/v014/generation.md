# hegemony-assault-ship v014

User request verbatim: ver good. now do the same with the side view. It has no front thrusters.
Mode: Masked API off v013: side elevation rebuilt with both near-side pods.
Tool: bin/gen.py, backend=api (OpenAI Images API /v1/images/edits)
Model: gpt-image-2.5-sunburst-2026-09-08 (pinned snapshot)
Parameters: size requested 1536x1024, quality=high, n=1
Prompt integrity: OpenAI Images API, exact prompt bytes sent
Mask: tmp/mask-as-side.png (white = repainted; only those pixels regenerate)
API approval, verbatim: ver good. now do the same with the side view.
Style: v3
Inputs:
- Image 1 EDIT TARGET: assets/ships/hegemony-assault-ship/candidates/v013/image.png
- Image 2 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
Token usage: {"input_tokens": 3693, "input_tokens_details": {"image_tokens": 3072, "text_tokens": 621}, "output_tokens": 1372, "output_tokens_details": {"image_tokens": 1372, "text_tokens": 0}, "total_tokens": 5065}
Date: 2026-10-03
Status: approved and promoted to reference.png on 2026-10-03. User approval: "approved."
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.84 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Masked API off v013: side elevation now shows both near-side pods (front beside the cockpit, back at the tail), both aft, same size and height; flank star; turret barrels forward. Other views preserved visually. 1 API call.

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

Image 1 is EDIT TARGET: The reference sheet. Only the masked area changes.
Image 2 is STYLE: Match its hand-painted matte rendering only. Ignore its subjects.

TASK: Rebuild the side view of this ship reference sheet.

This is a reference sheet of one ship on a plain mid-grey background. The three-
quarter view (left), the top-down plan view (middle right) and the head-on front view
(lower right) are correct and stay exactly as they are. Repaint only the masked area:
the SIDE ELEVATION at upper right.

Rebuild the side elevation strictly from the correct views: the ship seen exactly
side-on from its left, nose to the left, the same length as the top-down view, low and
squat as in the front view. Show BOTH near-side thruster pods — the front pod beside
the cockpit and the back pod at the tail — each on its short pylon, both pointing
straight back with their exhausts glowing behind them, the same size, at the same
height. The chin turret's two barrels point forward under the nose. Same black armour,
red bands and red line-built star (on the flank) as the other views. Plain mid-grey
around it. No text.

Render everything in the exact brush scale of the style anchor attached to this call: fewest possible flat shapes, no blending, no micro-detail.
