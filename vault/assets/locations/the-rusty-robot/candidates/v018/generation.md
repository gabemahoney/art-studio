# the-rusty-robot v018

User request verbatim: Lets try the API key approach using the new skills. Set it up first.
Mode: Masked API inpaint off v016: canopy underside's right end and the right fin's top, straight back edge, matching texture.
Tool: bin/gen.py, backend=api (OpenAI Images API /v1/images/edits)
Model: gpt-image-2.5-sunburst-2026-09-08 (pinned snapshot)
Parameters: size requested 1536x1024, quality=high, n=1
Prompt integrity: OpenAI Images API, exact prompt bytes sent
Mask: tmp/mask-rr-canopy-right.png (white = repainted; only those pixels regenerate)
API approval, verbatim: yes
Style: v3
Inputs:
- Image 1 EDIT TARGET: assets/locations/the-rusty-robot/candidates/v016/image.png
- Image 2 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
Token usage: {"input_tokens": 3788, "input_tokens_details": {"image_tokens": 3072, "text_tokens": 716}, "output_tokens": 1372, "output_tokens_details": {"image_tokens": 1372, "text_tokens": 0}, "total_tokens": 5160}
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.91 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: First masked API call here; it worked as documented: the EDIT TARGET (v016) came back with only the masked region repainted, not the anchor. Canopy underside's back edge now one straight line to the building corner, the right fin stops flat against it, texture matches the rest of the underside. Outside the mask the image is re-encoded (mean difference 3.4/255 vs v016); v019 restores those pixels exactly. Tokens: 3,788 in (3,072 image), 1,372 out.

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

TASK: Repair one small area of this architectural reference sheet of the Rusty Robot cantina.

Repaint ONLY the masked area: the right-hand end of the canopy's underside and the top
of the right corner fin below it, in the large three-quarter view on the left of the
sheet. Everything around the mask is final and must join it seamlessly.

The canopy's underside is ONE flat concrete plane, painted with the same warm ochre
dry-brush texture as the underside to the left of the mask, with the same broken
pigment and the same lighting from the door lamps below.

- Its BACK edge, where the underside meets the building's front wall and the top of
  the right fin, is ONE STRAIGHT LINE: it continues the edge already visible to the
  left of the mask at exactly the same angle, all the way to the building's right
  corner. It does not bend, step or dip where it crosses the fin.
- Its FRONT edge is the bottom of the tilted sign face, already visible above the
  mask; the underside fills the space between the two edges.
- At the building's right corner the canopy ends in a clean square corner: the
  underside's back edge meets the corner, and the canopy's right end rises from there
  to the tip of the sign face. Nothing hangs below the back edge.
- The right fin below rises straight up and stops flat against that straight edge,
  its lit front face and its darker side face continuing exactly as below the mask.

Render everything in the exact brush scale of the style anchor attached to this call: fewest possible flat shapes, no blending, no micro-detail.
