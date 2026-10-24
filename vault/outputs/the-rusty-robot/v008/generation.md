# the-rusty-robot v008

User request verbatim: Also there would be no rocks on the ground in a domed city. Some dirt on the road seems likely. but not rocks
Mode: Edit off v007. Single change: all loose rock, rubble, boulders, gravel and angular stone debris deleted from the road, steps, corners and alley, since a city sealed under a dome admits no weather, wind or erosion to wash or blow stone in. Replaced sparingly with what a grubby working street would actually carry — fine drifted dust and dirt along the wall feet and step angles, a little flat litter, scuffed and stained paving, and a thin crack or two with no fragments lifting out. Ground restated as a few large quiet flat planes so the foreground stays calm. Everything else explicitly frozen, including the corrected wall-mounted sign, the teal painted bands, the angular lamps and Sion's corrected stance.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4ac-2519-7f42-95d9-cc3c008c8845/exec-769ab872-95ca-4158-afb0-588e332af744.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v007/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.14 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Rocks removed cleanly. All loose stone, rubble, boulders and gravel are gone from the road, the steps, the corners and the alley, and the lane now reads as a swept, hard-surfaced city street of dry dusty ferroccrete laid out in a few large quiet flat planes, with the teal painted line running across it. What replaced the rubble is appropriate to a sealed dome: soft pale films of drifted dust along the wall feet, a couple of flat litter scraps lying on the paving, and scuffed traffic-worn patches, all low-key. The foreground is calmer than in any earlier pass. Everything else held from v007: the sign flat on the wall above the armoured brow with grey wall all around it and its edges parallel to the wall's horizontal lines, chipped ivory lettering and painted butler-robot emblem on rusted metal, lit only by its hooded lamp, reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals; the armoured brow, arched ribbed door, steps and handrail; the two angular machined lamps with flat downward panels; the grey ferrocrete buildings; the muted teal-green painted bands with no red, rust or orange anywhere on the architecture; the domed tower; the dome's ribbed underside; the two distant silhouettes; the alley and the crew; Graxo's wine-aubergine cape with both gold collar pins; Daxus's likeness and cross patches; Sion's corrected upright stance with her feet close together. File is 2.14 MB, inside the 2.5 MB book-float budget. TWO DISCREPANCIES raised by the user and not yet addressed: (1) small warm WINDOW LIGHTS are visible inside the alley at the far left, which makes the alley read as having lit buildings behind it rather than ending in the blackness the brief calls for; they should be deleted so the slot goes solid dark behind the crew. (2) SION NOW READS TOO CASUAL — the stance correction overshot from hunched into slouching, with her weight cocked and her hand pocketed, so she looks like she is lounging rather than attending to a covert conversation. Also still outstanding from earlier: the crew are lit at close to full value rather than as dark masses in alley shadow.

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

## Note on the Forbidden list

Every item in the Style Block's "Forbidden" line names a **rendering tell**, not a
subject: smooth gradients, airbrush, photographic detail, fine linework,
micro-detail, more than three values, granular noise, polygon mosaics, the polished
modern AI look — and, in that same company, **"neon or rim lighting."**

So "neon" there forbids the *look*: saturated glow, bloom, halo, soft falloff, the
lit-from-within sheen of modern digital art. It does **not** forbid lit signage,
lamps, glowing instruments or electric light as subject matter. The world can have
neon in it; the painting must not be rendered like neon.

A lit sign is therefore fine when it is painted the way this style paints
everything else: flat opaque shapes with hard edges, a bright core and at most one
darker band of the same hue, no glow, no gradient, no rays. Recorded 2026-09-30
after the electric sign in `outputs/the-rusty-robot/`, where reading the ban as a
subject prohibition would have blocked a legitimate art direction.

This note sits outside the Style Block and changes none of its text, so it does not
require a style version bump.

Image 1 is STYLE: Match this image's hand-painted matte rendering technique ONLY. Ignore and do not reproduce its people, clothing, equipment, interior, setting or composition.
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v007, approved by the user. Correct in every respect except for the loose rock and rubble scattered across the street.

TASK: A single 3:2 horizontal evening street scene: a clean dusty ferrocrete lane in a domed city, three travellers conferring in a left-hand alley across from a cantina whose wall sign reads THE RUSTY ROBOT.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE thing below.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers confer in a narrow left-hand alley across from the lit door of a cantina called The Rusty Robot.

IMAGE 2 IS APPROVED AND CORRECT IN EVERY RESPECT BUT ONE. Keep everything else EXACTLY as it is: the street, its perspective and framing; the cantina's flat grey front wall and the SIGN on it, untouched — flat against the wall above the armoured brow with grey wall all around it, its edges parallel to the wall's horizontal lines, chipped ivory lettering and painted butler-robot emblem on rusted dark metal, lit only by its hooded lamp and emitting no light, reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals; the armoured brow; the round-arched ribbed door, steps and pipe handrail; the two angular machined lamps with flat downward-facing lit panels and their warm pools; the weathered GREY FERROCRETE buildings; the MUTED TEAL-GREEN painted bands on walls, parapets, door surrounds and ground, with no red, rust or orange anywhere on the architecture; the domed tower and stepped rooflines; the dome's ribbed underside overhead; the two distant anonymous silhouettes; the alley at the left; the three crew at their current size, positions and poses, including Sion's corrected upright stance with her feet close together and her hand pocketed; Graxo's wine-aubergine cape and gold collar pins; Daxus's likeness and cross patches; and the warm-amber-against-cool-grey light. Do not re-frame, do not zoom, do not move anyone, do not touch the sign.

THE ONE CHANGE — REMOVE THE ROCKS. Image 2 scatters loose broken STONE across the street, the steps and the gutters: angular chunks of rubble, small boulders and piles of stony debris. This is a city sealed under a protective dome, where no weather, wind or erosion reaches the lanes and no rock is washed or blown in. Broken stone does not belong here.

DELETE every piece of it. There are NO rocks, NO boulders, NO stone chunks, NO rubble piles, NO gravel beds, NO chipped masonry fragments and NO angular debris anywhere in the picture — not on the road, not on the steps, not in the corners, not against the walls, and not in the alley.

In their place, leave the ground CLEAN AND FLAT: dry, dusty ferrocrete paving, pale and matte, reading as a few large quiet flat planes with its painted teal markings running across it. The lane should read as a swept, hard-surfaced city street, not as open ground.

What IS plausible, and should replace the rubble sparingly:
- fine DUST and DIRT, drifted into soft pale films along the foot of the walls and into the angles of the steps, and smudged in thin patches across the paving
- a little scattered LITTER — a few flat scraps of paper or packaging, a crushed container, lying flat on the ground
- worn, scuffed and stained patches on the paving where feet and traffic have polished or dirtied it
- a shallow crack or two in the ferrocrete, drawn as a thin line, with NO loose fragments lifting out of it

Keep all of that low-key and flat. It is a grubby working street that someone sweeps occasionally, not a ruin. The foreground in particular should be one of the calmest, emptiest areas in the picture: a broad quiet sweep of dusty paving with very little painted on it.

LIGHT AND COLOUR: unchanged from image 2 in every respect. No neon, no bloom, no halos, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
