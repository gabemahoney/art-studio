# the-rusty-robot v092

User request verbatim: v89 looks really good. Can we tuck them a little more into the alleyway and darken the lighting on them a bit>
Mode: Edit off v089 (user-designated), short spec: crew tucked further into the alley, darker. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10419-cbf3-7140-97b4-50385723711f/exec-f4f54706-815d-4d6b-9ea8-5b63ee2f0f49.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v089/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.02 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Short-spec edit off v089: crew pulled deeper into the alley and smaller, darker; Sion's arm still catches light.

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
Image 3 is IDENTITY: The crew, for their likenesses and clothing only.

TASK: Revise this scene: the crew conferring in the dark alley beside the Rusty Robot cantina.

Reproduce image 2 exactly and change only two things about the three crew:
- Move them a little further back into the dark alley, so they are tucked inside it
  beside the cantina's side wall rather than at its mouth. Keep their size, grouping
  and poses.
- Darken the light on them: they stand in the alley's shadow, dim and muted, with only
  a thin warm edge of light from the cantina entrance on the sides facing it.
Everything else stays exactly as it is.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
