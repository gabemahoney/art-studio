# the-rusty-robot v012

User request verbatim: Also, set them back in the alley, dimly lit. Like they were in v5
Mode: Edit off v011. Single change, and the one outstanding since v005: the crew are stepped further back along the alley so the near wall crops more of the nearest figure and they sit behind the building front line, and they are dimmed several steps — Daxus's white jacket to a dim cool grey, Sion's ochre to a deep dull brown, Graxo's cape to near black — reading as dark simplified silhouettes with only a thin cool rim of street spill on a shoulder edge, a cheekbone, Sion's goggles, her cyber arm, Graxo's collar pins and the tip of her pointing hand. Her extended arm and finger are explicitly required to stay readable in silhouette against the lighter street so the gesture is not lost. Poses, identities, the sign, ground and all other lighting frozen.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a0f4b5-85fc-7252-9967-8d0205a66762/exec-5e028252-4978-4ef9-ad94-a91d962cf9cc.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v2
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v2.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v011/image.png
Date: 2026-09-30
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Delivered: image.png itself, 1536x1024, sRGB 8-bit no alpha, 2.10 MB — raw output already meets the delivery spec, so no separate deliverable was written. Place image.png.
Review: The change landed as specified, but it may have overshot the user's actual intent. WHAT CHANGED: the three are stepped further back along the alley, sitting behind the building front line with the near wall cropping more of the nearest figure, and they are correspondingly smaller in frame. They are dimmed several steps — Daxus's off-white jacket now reads a dim cool grey-brown, Sion's ochre a duller brown, Graxo's cape close to black — so they read as dark figures in a slot rather than people standing in the open. The thin cool rim survives on shoulder edges, Sion's goggles and the collar pins, and critically her extended arm and pointing finger still read clearly in silhouette against the lit lane, so the gesture is not lost. The corrected pointing hand from v011 is intact: index alone extended, other three curled into a compact fist, thumb across the front. The contrast the brief wanted is now there — a bright warm doorway across the lane, three dim figures watching it. Everything else held: the sign with its flat stencil emblem, the armoured brow, arched ribbed door, steps, angular lamps, grey ferrocrete with muted teal bands, domed tower, dome underside, distant silhouettes, black alley, clean dusty paving with no rocks. File is 2.10 MB, inside the 2.5 MB book-float budget. CAUTION FOR THE NEXT PASS: the user has since said that "the v5 lighting and postures was ideal", and a side-by-side crop of the crew in v005 against v012 shows v005 is markedly BRIGHTER and warmer than this — full colour on Daxus's white jacket and Sion's ochre, with the group at the alley mouth rather than set back. The user's two instructions are in tension: they asked for the crew set back and dimly lit "like they were in v5", but v005 is in fact the bright, forward version. This candidate delivers the dimming that was asked for literally; if what the user actually wants is v005's warmth and readability at v012's depth, that is a separate middle setting and should be confirmed rather than guessed.

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
Image 2 is EDIT TARGET: The scene baseline: the-rusty-robot v011. Its street, sign, lighting and all three crew poses are correct. Change only how far back in the alley the crew stand and how dimly they are lit.

TASK: A single 3:2 horizontal evening street scene: three dim figures set back in a black alley, one pointing out at the lit door of a cantina whose wall sign reads THE RUSTY ROBOT.

OUTPUT FORM — READ FIRST. Produce ONE single continuous SCENE ILLUSTRATION filling the whole frame. THIS IS NOT A REFERENCE SHEET: no panels, no boxes, no split frames, no borders, no insets, no swatches, no call-outs, no character names and no captions.

THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as wide as it is tall, the proportions of a 1536 x 1024 image. Not a 2:1 banner, not a panorama, not a square.

Image 1 is the STYLE anchor: match its hand-painted matte technique only. Image 2 is the SCENE BASELINE — reproduce it and change only the ONE thing below.

SCENE: "The Cantina," exterior. Evening in the domed city of Kannan. Three travellers confer deep in the shadow of a narrow left-hand alley, across from the lit door of a cantina called The Rusty Robot.

KEEP FROM IMAGE 2 — UNCHANGED: the whole street, its perspective and framing; the sign flat on the wall above the armoured brow with its chipped ivory lettering reading exactly "THE RUSTY ROBOT" in wide squared retro-futuristic capitals and its FLAT STENCIL robot emblem with no shading in it; the hooded lamp above the board; the armoured brow, the round-arched ribbed door, the steps and pipe handrail; the two angular machined lamps and their warm pools on the steps and paving; the grey ferrocrete buildings with their muted teal painted bands and NO red, rust or orange; the domed tower and stepped rooflines; the dome's ribbed underside overhead; the two distant silhouettes; the pitch-black alley with no lights in it; the clean dry dusty paving with no rocks or rubble; and the poses and identities of all three crew — Sion still turned toward the other two with her right arm extended, pointing at the cantina door, her index finger alone extended and the other three curled into a compact fist with the thumb across it; Graxo with his wine-aubergine cape and gold collar pins; Daxus with his glasses, off-white jacket and cross patches. Do not re-frame, do not zoom, do not touch the sign, the ground or anyone's pose.

THE ONE CHANGE — SET THE CREW BACK INTO THE ALLEY AND DIM THEM. In image 2 the three stand close to the street line and are lit at nearly full brightness, so they read as figures standing in the open beside the lane. They should instead be tucked back inside the dark slot, half-swallowed by it.

MOVE THEM DEEPER IN. Step all three further back along the alley, away from the street, so that:
- The alley's near wall overlaps MORE of the nearest figure, cropping further across them than it does now.
- They sit visibly BEHIND the line of the building front, inside the slot rather than at its opening.
- Being further off, they become slightly SMALLER in the frame. Do not enlarge them.
- There is dark alley floor and dark wall visible between them and the street.

DIM THEM DOWN. This is the important half. They are in shadow and almost nothing lights them:
- Every one of their colours drops several steps darker and duller. DAXUS'S off-white jacket is no longer white — it reads as a dim, cool mid-grey, the palest thing among them but far from bright. SION'S ochre jacket becomes a deep, dull brown. GRAXO'S cape goes almost black, its wine colour only just detectable. Their trousers and boots are near-black masses.
- They read mostly as DARK SIMPLIFIED SILHOUETTES: large flat shapes with their internal detail suppressed. Faces are dim, with features barely picked out.
- The ONLY bright marks on them are a THIN COOL RIM of spill light from the street, catching: one edge of a shoulder, a narrow slice of cheekbone, the curve of Sion's ruby goggles, a hard glint along her steel-grey cyber arm, the two small gold pins at Graxo's collar, and the very tip of Sion's pointing hand and forearm as it reaches out toward the lit lane. Nothing else on them catches light.
- Sion's extended arm and pointing finger must stay READABLE in silhouette against the lighter street beyond — that gesture is the point of the picture and must not be lost in the dark.

The contrast is the whole idea: a bright warm doorway across the lane, and three dim figures watching it from a black slot. The cantina entrance stays the brightest thing in the picture by a wide margin.

LIGHT AND COLOUR: unchanged everywhere else — the warm amber pools at the door, the cool grey street, the dry dusty paving, the black alley. No neon, no bloom, no halos, no lens flare, no light rays.

Change nothing else about image 2.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
