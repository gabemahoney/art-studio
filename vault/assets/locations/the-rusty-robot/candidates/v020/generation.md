# the-rusty-robot v020

User request verbatim: there is a vague light fixture on the bottom of the marquee. We should remove it. The two side lights and one spotlight are sufficeint.
Mode: Masked API inpaint off v019: remove the glowing strip in the canopy underside, three-quarter view and front elevation.
Tool: bin/gen.py, backend=api (OpenAI Images API /v1/images/edits)
Model: gpt-image-2.5-sunburst-2026-09-08 (pinned snapshot)
Parameters: size requested 1536x1024, quality=high, n=1
Prompt integrity: OpenAI Images API, exact prompt bytes sent
Mask: tmp/mask-rr-underside-light.png (white = repainted; only those pixels regenerate)
API approval, verbatim: yes
Style: v3
Inputs:
- Image 1 EDIT TARGET: assets/locations/the-rusty-robot/candidates/v019/image.png
- Image 2 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
Token usage: {"input_tokens": 3634, "input_tokens_details": {"image_tokens": 3072, "text_tokens": 562}, "output_tokens": 1372, "output_tokens_details": {"image_tokens": 1372, "text_tokens": 0}, "total_tokens": 5006}
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.92 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Glowing strip in the canopy underside removed in both views; underside now plain ochre concrete. Only the masked strips are used, in v021. Tokens: 3,634 in (3,072 image), 1,372 out.

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

TASK: Repair two small areas of this architectural reference sheet of the Rusty Robot cantina.

Repaint ONLY the two masked strips: the underside of the canopy above the door, in
the large three-quarter view and in the front elevation. Everything around the masks
is final and must join them seamlessly.

Remove the glowing light strip set into the canopy's underside. The underside is
plain flat concrete, painted with the same dull warm ochre dry-brush texture as the
rest of the underside beside the masks, lit only by the reflected warmth of the two
door lamps below — no bright band, no fixture, no glow, nothing set into it. Its back
edge, where it meets the wall, stays one straight line, continuing the edge outside
the mask at the same angle.

Render everything in the exact brush scale of the style anchor attached to this call: fewest possible flat shapes, no blending, no micro-detail.
