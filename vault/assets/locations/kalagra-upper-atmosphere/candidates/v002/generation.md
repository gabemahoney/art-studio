# kalagra-upper-atmosphere v002

User request verbatim: I think we need to try changing the scene. Try a scene where they are flying in the planets upper atmosphere, with the storm and the planet below?
Mode: Layer 1 for the new concept: empty upper atmosphere over the storm. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a109c7-8906-7902-abd1-f79823f3a8c5/exec-bd036bc9-6814-483b-a139-e2bdcbd45069.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
Date: 2026-10-04
Status: approved and promoted to reference.png on 2026-10-04. User approval: "v2"
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.51 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: Same layout, warmer browner storm, yellow lightning, star with flat ray burst; more stars.

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

Image 1 is STYLE: Match its hand-painted matte rendering only. Ignore its subjects.

TASK: A single illustration of Kalagra's upper atmosphere above the storm.

SUBJECT DESIGN (description v1, restated so nothing is invented):
The edge of space above Kalagra, where the Antares climbs out of the storm in
"Getting Sky". *(Provisional throughout.)*

- High above the planet: the sky deep blue-black overhead, thinning to a band of pale
  blue atmosphere glowing along the curved horizon.
- Kalagra below: a bleak rocky world, its curve visible, mostly hidden under the
  planet-wide storm — a vast spiral of churning grey-brown cloud with lightning
  flickering inside it, the storm front a dark wall rolling across the surface.
- The searing blue star low on the horizon, throwing hard cold light across the cloud
  tops.
- A few stars in the black above.
- No ships, vehicles or structures.

ONE single continuous illustration, a 3:2 horizontal rectangle. No text or frames.
Empty sky and planet only — no ships.

The view from high in the upper atmosphere, looking out and down: the planet's curved
horizon sweeps across the picture on a diagonal, lower left to middle right. Below it
the storm fills the lower half — huge churning cloud bands with lightning inside them.
Above, the sky darkens from a thin glowing band of atmosphere into blue-black space.
The blue star sits low near the horizon at the right. Leave open sky across the
middle and upper part of the picture, where a chase will fly.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
