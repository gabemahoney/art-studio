# the-rusty-robot v025

User request verbatim: Looking great. Bring back the robot sign image from v20
Mode: Edit off v024. Single detail change: the sign's robot emblem restored to the treatment it had in v020. Comparison of the two at magnification shows the difference precisely — v020 painted it as a SOLID FILLED silhouette of chipped ivory with the eyes and bow tie as dark cut-outs punched through, reading as a bold poster-like stencil, whereas v024 drew it as thin OUTLINE line-art with the rusted board showing through the head and body. Now specified as solid masses filled edge to edge with the board showing only through the small cut-outs, kept flat with no shading or volume and chipping to rust as the only variation, at its current size and position. Everything else frozen, including the board, the lettering, the lighting, the crew and Graxo's shortened nose.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f571-f5b0-7712-995e-646c7f5d4f0d/exec-8a5ef4c3-3719-4710-b092-5c407f30618a.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v024/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 1.95 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: Robot emblem restored to the v020 treatment. It is now a bold SOLID FILLED stencil — head, body, shoulders and arms painted as solid masses of chipped ivory, with the dark rusted board showing through only as cut-outs for the two round eyes, the bow tie and a couple of button marks. v024 had drawn it as thin outline line-art with the board showing through the whole figure, which read weak and delicate; comparing the two at magnification made the difference plain. It stays flat with no shading or volume, chipping to rust is the only variation, and its size and position beside the lettering are unchanged. Everything else held: camera, framing, lighting, the three crew with Graxo's shortened nose, the sign board and its lettering, the armoured brow, the industrial angular lamps, the grey ferrocrete with teal bands, the clean dry paving with no rocks, the dome and the alley. File is 1.95 MB. OUTSTANDING, raised by the user: a TRIANGULAR WEDGE sits at the foot of the stairs on the LEFT, a sloping ramp-like element running diagonally from the pavement up to the lowest step. The right-hand side of the same stair run terminates in a plain squared block with no such wedge, so the two sides do not match and the element reads as an unexplained architectural oddity. Confirmed on a magnified crop. Also still outstanding and unaddressed: the crew's luminance ratio sits at 0.38 against v005's 0.33, having drifted when the lamp fittings were swapped in v024.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v024. Correct in every respect except that the sign's robot emblem is drawn as thin outline line-art instead of a solid filled stencil.

TASK: A single 3:2 horizontal evening street scene: the approved cantina picture with its sign's robot emblem repainted as a bold solid filled stencil.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE small thing below.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers stand in the shadow of an alley at the left, conferring, across from the lit door of a cantina called The Rusty Robot.

IMAGE 2 IS APPROVED AND CORRECT IN EVERY RESPECT BUT ONE DETAIL ON THE SIGN. Keep absolutely everything else exactly as it is: the camera, framing and composition; the lighting, with its warm golden pool across the entrance, steps and paving and the cool blue-grey shadow elsewhere; the three crew at their exact positions, sizes, postures and depth of shadow, and every part of their clothing, equipment and faces including Graxo's shortened nose; the SIGN BOARD itself, flat on the wall above the armoured brow with wall visible all around it, its edges parallel to the wall's horizontals, its dark rusted metal surface, its small thickness and cast shadow, and the hooded lamp above it; the LETTERING, reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals of flat chipped ivory, at its current size and position; the armoured brow, the round-arched ribbed door, the steps and handrails; the INDUSTRIAL ANGULAR LAMPS with their flat downward-facing lit panels; the GREY FERROCRETE buildings with their MUTED TEAL painted bands; the domed tower, the dome overhead, the distant figures, the alley; and the CLEAN DRY PAVING with its drifted dust and no rocks, rubble or gravel. Do not re-frame, do not zoom, do not move anyone, do not change any lighting, do not alter the lettering or the board.

THE ONE CHANGE — MAKE THE ROBOT EMBLEM A SOLID FILLED SILHOUETTE. On the sign beside the lettering is a painted butler-robot. In image 2 it is drawn as thin OUTLINE LINE-ART: narrow ivory strokes tracing the robot's edges, with the dark rusted board showing through its head, body and shoulders. That is too weak and delicate.

Repaint it as a BOLD SOLID STENCIL, filled in:
- The robot's HEAD, BODY, SHOULDERS and ARMS are painted as SOLID MASSES of flat chipped ivory, completely filled edge to edge. The rusted board does NOT show through them.
- It reads as one strong, graphic, poster-like silhouette — the kind of shape a sign painter would cut from a stencil and spray — not as a drawing made of lines.
- The only places the dark board shows through are the small CUT-OUTS within that solid mass: the two round EYES, the BOW TIE at its collar, and a couple of small marks for buttons. Those read as dark holes punched in a filled shape.
- The silhouette itself: a rounded dome head with a small nub or antenna on top, two round eyes, a stiff collar, a bow tie, and a simple squared body with shoulders.
- Keep it FLAT: no shading, no rounding, no gradient, no highlight and no sense of volume anywhere inside the ivory. The form is described by its outline and its cut-outs alone.
- The only variation within the ivory is WEAR: flat, hard-edged flecks and patches where the paint has chipped away to show rust beneath, as elsewhere on the sign.

Keep the emblem at its current SIZE and POSITION beside the lettering, and keep the warm wash from the hooded lamp falling across the board as it already does.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
