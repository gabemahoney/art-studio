# rusty-robot-street v011

User request verbatim: Can you try fixing up the dome supports? some are going at random angles.
Mode: Masked API inpaint off v010: dome lattice in the sky above the far street, regular meridians and rings.
Tool: bin/gen.py, backend=api (OpenAI Images API /v1/images/edits)
Model: gpt-image-2.5-sunburst-2026-09-08 (pinned snapshot)
Parameters: size requested 1536x1024, quality=high, n=1
Prompt integrity: OpenAI Images API, exact prompt bytes sent
Mask: tmp/mask-street-dome.png (white = repainted; only those pixels regenerate)
API approval, verbatim: yes
Style: v3
Inputs:
- Image 1 EDIT TARGET: assets/locations/rusty-robot-street/candidates/v010/image.png
- Image 2 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
Token usage: {"input_tokens": 3692, "input_tokens_details": {"image_tokens": 3072, "text_tokens": 620}, "output_tokens": 1372, "output_tokens_details": {"image_tokens": 1372, "text_tokens": 0}, "total_tokens": 5064}
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.11 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Masked inpaint: dome lattice now regular — meridians fanning from one point overhead, evenly spaced ring arcs, uniform thickness; the stray thick vertical support is gone. Only the mask is used, in v012.

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

Image 1 is EDIT TARGET: The street view being repaired. Only the masked area changes.
Image 2 is STYLE: Match its hand-painted matte rendering only. Ignore its subjects.

TASK: Repair the dome lattice in the sky of this street illustration.

Repaint ONLY the masked area: the night sky and the city dome's structural ribs above
the far end of the street. Everything around the mask is final and must join it
seamlessly — the ribs continue into the unmasked sky at the same positions and angles.

The dome is one huge regular geodesic lattice seen from below, close overhead:
- MERIDIAN ribs: thick dark bands that all converge toward a single point high above
  the top of the picture, so they fan out evenly as they come down — like the spokes
  of an umbrella seen from beneath.
- RING ribs: thick dark bands crossing the meridians as smooth concentric arcs, evenly
  spaced, each curving the same way.
- Every rib is the same thickness, straight-sided, and meets its neighbours at a clean
  crossing. No rib runs at an odd angle, stops short, or crosses another diagonally.
Deep night blue between the ribs, painted flat with dry-brush texture.

Render everything in the exact brush scale of the style anchor attached to this call: fewest possible flat shapes, no blending, no micro-detail.
