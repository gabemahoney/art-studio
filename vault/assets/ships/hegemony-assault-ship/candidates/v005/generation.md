# hegemony-assault-ship v005

User request verbatim: Also the Hegemony is Black and Red. / Give them a cool logo. Maybe an 8 point +
Mode: Edit off v003: black and red livery, eight-pointed Hegemony star emblem (description v3).
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a10438-5d40-79d0-9fc0-1ff2e690e510/exec-4a95d3ca-ce29-4ca5-8c87-f2b7387111c9.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: assets/ships/hegemony-assault-ship/candidates/v003/image.png
Date: 2026-10-03
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.08 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Black and red livery with an eight-pointed star emblem. Superseded: user chose v004's top-down view as the design authority and wants a line-built emblem, not pointed.

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

TASK: Recolour this reference sheet of the Hegemony assault ship.

SUBJECT DESIGN (description v3, restated so nothing is invented):
The Hegemony's storm-patrol gunship: a two-seat atmospheric interceptor built to hunt
unauthorized flights through Kalagra's planet-wide storm. Two of them chase the
Antares as she climbs out. *(Whole design provisional — first pass.)*

## Exterior

Not an aircraft: a heavy armoured space gunship that hovers and flies on thrusters,
with no wings and no tail fins.

- About half the Antares's length, but bulky and heavy: a thick, blunt armoured hull
  shaped like a flattened hexagonal slab, wider than it is tall, with a blunt angled
  prow — no pointed nose.
- A small armoured cockpit set into the top of the prow: a narrow horizontal slit of
  dark glass under a heavy brow, like a visor in a helmet.
- FOUR stubby round thruster pods, one at each corner of the hull on short
  armoured pylons, each able to swivel; their exhausts glow hard white-blue.
- A blocky gun turret slung under the prow with two heavy laser barrels, and a
  rack of sensor fins and antennas along the spine.
- Thick overlapping armour plates with straight seams, heavy bolts and vent grilles.

## Colour and marking

- The Hegemony's colours are **black and red**. Hull: matte black armour, weathered
  to charcoal grey on exposed edges by sandstorms.
- Blood-red bands around each thruster pod and a red stripe along each flank.
- **The Hegemony emblem**: an eight-pointed star — a bold plus sign with a thinner
  diagonal cross behind it, all eight points sharp — in red, on the top of the hull
  and on each flank. No lettering, numbers or other insignia.

Reproduce image 2, the reference sheet, keeping the ship's shape, the four views and
their layout exactly. Change only its colours and marking:
- The hull is matte BLACK armour, weathered to charcoal grey on exposed edges.
- Blood-red bands around each thruster pod and a red stripe along each flank.
- Add the Hegemony emblem in red: an eight-pointed star — a bold plus sign with a
  thinner diagonal cross behind it, all eight points sharp. Large on the top of the
  hull, smaller on each flank.
- No lettering or numbers.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
