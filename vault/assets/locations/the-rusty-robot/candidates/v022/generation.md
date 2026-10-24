# the-rusty-robot v022

User request verbatim: can we do one more pass on making the surface underside of the marque look correct? It looks like someone took a smudgetool to the middle.
Mode: Masked API inpaint off v021: whole canopy underside in the three-quarter view, flat dry-brush concrete, straight edges.
Tool: bin/gen.py, backend=api (OpenAI Images API /v1/images/edits)
Model: gpt-image-2.5-sunburst-2026-09-08 (pinned snapshot)
Parameters: size requested 1536x1024, quality=high, n=1
Prompt integrity: OpenAI Images API, exact prompt bytes sent
Mask: tmp/mask-rr-underside-full.png (white = repainted; only those pixels regenerate)
API approval, verbatim: Yes. Please be more clear when you are asking for permission.
Style: v3
Inputs:
- Image 1 EDIT TARGET: assets/locations/the-rusty-robot/candidates/v021/image.png
- Image 2 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
Token usage: {"input_tokens": 3704, "input_tokens_details": {"image_tokens": 3072, "text_tokens": 632}, "output_tokens": 1372, "output_tokens_details": {"image_tokens": 1372, "text_tokens": 0}, "total_tokens": 5076}
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.87 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Whole three-quarter underside repainted: smudged middle gone, even flat ochre planes, straight front and back edges. Only the masked area is used, in v023. Tokens: 3,704 in.

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

Image 1 is EDIT TARGET: The reference sheet being repaired. Only the masked area changes.
Image 2 is STYLE: Match its hand-painted matte rendering only. Ignore its subjects.

TASK: Repaint one area of this architectural reference sheet of the Rusty Robot cantina.

Repaint ONLY the masked area: the whole underside of the canopy over the door, in the
large three-quarter view. Everything around the mask is final and must join it
seamlessly.

The underside is ONE flat slab of raw board-formed concrete seen from below, painted
in the same hand-painted matte technique as the rest of the building: a few large flat
opaque planes with hard edges and coarse dry-brush texture, matching the concrete of
the canopy's end faces and the walls. It is lit warm ochre by the two door lamps below
— brightest just above the door, falling off evenly to a darker ochre toward both ends
— in at most three flat value steps. No smudged or blurred areas, no gradients, no
light fixture, no glow.

Its FRONT edge, at the bottom of the tilted sign face, and its BACK edge, where it
meets the wall and the tops of the fins, are both single straight lines, continuing
the edges outside the mask at the same angles.

Render everything in the exact brush scale of the style anchor attached to this call: fewest possible flat shapes, no blending, no micro-detail.
