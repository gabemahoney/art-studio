# the-rusty-robot v090

User request verbatim: 86 was probably the closest. But they are still way too big... I dont think masking or copying is going to work. I think we need to fully regenerate.
Mode: FRESH from the approved street. Old v005 crop dropped (it taught the large size). Crew sized by in-frame referents: plinth at hips, head at the door lamps' bottom, about door height. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10416-0a0b-7192-9bad-fd76d3b86740/exec-dd0a9e91-e227-4b36-80b7-e9f27170711a.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/locations/rusty-robot-street/reference.png; frozen assets/locations/rusty-robot-street/candidates/v013/image.png
- Image 3 IDENTITY: assets/characters/crew-height-lineup/reference.png; frozen assets/characters/crew-height-lineup/candidates/v009/image.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.03 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Crew smaller still, standing in front of the cantina's corner rather than in the alley; framing held.

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
Image 2 is EDIT TARGET: The approved street. Reproduce it exactly and add only the crew.
Image 3 is IDENTITY: The approved crew lineup. Copy their likenesses and clothing only.

TASK: A single scene illustration: the crew, small figures, conferring in the dark alley beside the Rusty Robot cantina, at night inside the domed city of Kannan.

ONE single continuous scene illustration, a 3:2 horizontal rectangle. Not a reference
sheet: no panels, borders, captions, names or numbers.

Image 2 is the approved street. Reproduce it EXACTLY: the same camera and framing, the
Rusty Robot at the same size and position with its full flight of steps, matching side
walls and handrails, its sign and canopy, the alley at the left, the street to the
right, the dome. Do not move the camera or resize anything. Only add the crew.

Image 3 is the approved crew lineup — copy their likenesses and clothing only.

THE CREW ARE SMALL. They stand at the mouth of the alley, beside the cantina's
front-left corner, at the same distance from the viewer as that corner. Size them
against the cantina, which is right next to them:
- The heavy concrete plinth at the bottom of the cantina's corner reaches up to their
  hips.
- The top of Graxo's head, the tallest, is level with the BOTTOM of the cantina's
  door lamps — well below the canopy.
- Above their heads, the dark alley and the shadowed side wall rise a long way: the
  height from their heads up to the canopy is about as tall as they are again.
- Each of them is about as tall as the cantina's arched door.
In previous attempts they came out three times too tall. If unsure, paint them
smaller.

GROUPING AND POSES: a tight huddle in the leftmost part of the picture, shoulder to
shoulder, overlapping. Daxus at the left and Graxo at the back lean in toward the
middle. SION, at the front right of the group, is turned to her left facing Daxus and
Graxo, her goggled face in profile toward them, gesturing with her natural right hand.

LIGHT: they stand in deep shadow inside the alley — dim, muted masses nearly the tone
of the alley wall. Only a thin warm edge of light from the cantina entrance catches
the sides turned toward it: the right edge of Sion's jacket and steel arm, a
cheekbone, the gold pins at Graxo's collar.

DAXUS: broad young man, thin glasses, dark swept-back hair; off-white medical jacket
with red-cross sleeve patches over a burnt-orange shirt, brown cargo trousers, boots.
GRAXO: tallest; long weathered face, mustache, silver temples; long aubergine cape
with two gold pins, walnut vest, plum ascot, charcoal trousers. Only Graxo wears a
cape. SION: slighter young woman, dark hair swept to one side, ruby-red goggles; ochre
jacket, LEFT sleeve absent and a steel cyber arm, slim teal scarf, charcoal trousers.

The lit cantina entrance stays the brightest, warmest thing in the picture.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
