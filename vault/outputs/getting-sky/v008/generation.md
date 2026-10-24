# getting-sky v008

User request verbatim: The guns shooting out of the ships must just shoot straight... Have them shoot projectiles, show a trail shooting straight out of them. Also, the Antares geometry is incorrect. Right thruster is basically on its nose.
Mode: Fresh: side-on left-to-right chase so guns fire along the flight line; projectile trails; Antares engines at rear. Roll 2 of 2.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a104e5-ed3c-7831-b6af-7291ebf4f28a/exec-0e4e2fa8-3f2e-456b-a6b1-a4833dd0838e.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 IDENTITY: assets/ships/the_antares/sources/hero-crop-from-reference.png
- Image 3 IDENTITY: assets/ships/hegemony-assault-ship/sources/hero-crop-from-reference.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.60 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.  [OVER the 2.5 MB budget — needs recompression]
Review: Same layout, heavier rain/sand, bolts reach past the Antares; Antares engines at rear; gunship designs read.

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
Image 2 is IDENTITY: The Antares. Copy its design exactly; engines at the rear.
Image 3 is IDENTITY: The Hegemony assault ship. Copy its design exactly.

TASK: A single scene illustration: the Antares fleeing two Hegemony assault ships through a storm gorge at night.

ONE single continuous scene illustration, a 3:2 horizontal rectangle. No panels,
borders or text.

Night, in the heart of a planet-wide storm. A narrow gorge between towering black
cliffs; wind-driven sand in grey curtains; lightning in the strip of sky above throws
cold blue-white light on the cliff faces. Dark slate, storm blue and black, with warm
light only from engines and gunfire.

A chase running from LEFT to RIGHT along the gorge, seen from the side and slightly
below:
- The Antares (image 2) on the right, flying RIGHT: her blunt cockpit nose leads at the
  right, her two round engine pods are at her REAR on the left side of her, exhausts
  flaring behind her. Her design exactly as image 2.
- Two Hegemony assault ships (image 3) behind her on the left, also flying RIGHT, one
  higher than the other, noses pointing straight at her.
- Each assault ship fires its two chin guns STRAIGHT AHEAD, along the line it is
  flying: small glowing red projectiles, each with a thin straight streak trailing
  behind it, travelling in straight parallel lines from the gun muzzles toward the
  Antares. Some pass just behind her. No beams, no glow cones, nothing at an angle to
  the guns.
- The ships are small against the cliffs; the gorge and storm dominate.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
