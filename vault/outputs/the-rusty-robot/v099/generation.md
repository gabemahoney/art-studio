# the-rusty-robot v099

User request verbatim: No it looked better with more. But dont have them all facing the same direction.
Mode: Edit off v096: passersby mixed directions — some away, some toward, a pair talking, one side-on. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1042a-50c1-7121-81ea-a8af97696964/exec-90fa9529-7c02-4f0d-aff1-2c582496b3f8.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v096/image.png
Date: 2026-10-03
Status: approved and promoted to final.png on 2026-10-03. User approval: "v99."
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.95 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Mixed directions, more spread down the street, a talking pair further down; sci-fi silhouettes; framing, crew and cantina held.

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

Image 1 is STYLE: Match this image's rendering technique only. Ignore its people, clothing, equipment, and setting.
Image 2 is EDIT TARGET: This is the image being modified. Preserve everything the prompt does not change.

TASK: Revise the passersby in this street scene.

Reproduce image 2 exactly and change only which way the passersby are walking.
Keep their number, positions, sizes, science-fiction silhouettes and dim lighting.
- About half walk AWAY down the street, backs to us; the others walk TOWARD us, up
  the street, faces in shadow under hoods, collars and helmets.
- One or two pause: one turned side-on to look into a doorway, two standing together
  talking.
The three crew in the alley, the cantina and everything else stay exactly as they
are — the same framing.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
