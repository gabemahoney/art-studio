# the-rusty-robot v071

User request verbatim: The stair case is a little too short and steep. The ground is a little too vibrant. Go back and take a look at v5. The stairs were a good length there and the buildings had more variety. Dont use that pastel paint scheme from v5 though
Mode: Edit off v070: staircase rebuilt long and shallow (~10 low treads reaching further into the street); alley buildings varied in width, height, roofline and window pattern while keeping v070's saturated palette.
Tool: bin/gen.py, backend=codex (Codex CLI built-in image_gen; underlying image model not exposed)
Model: gpt-6-astra — orchestrator only; the image model it calls is not exposed
Parameters: size requested 1536x1024
Prompt integrity: codex source /Users/gmahoney/.codex/generated_images/01a1000e-7152-75f0-92d9-02e5aafaddf4/exec-27114f9e-093f-425d-b326-bb6d0ed10f1b.png; prompt relayed from disk via fs.readFileSync into the tool argument (never through model tokens), so the Style Block reached image_gen verbatim
Style: v3
Inputs:
- Image 1 STYLE: ref_images/style_references/canonical_style_reference.png; frozen style_versions/canonical_style_reference-v3.png
- Image 2 EDIT TARGET: outputs/the-rusty-robot/v070/image.png
Date: 2026-10-02
Status: awaiting user evaluation
Output: image.png, 1536x1024 (raw model output, frozen)
Review: pending — record with bin/review.py once you have seen it

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
Image 2 is EDIT TARGET: Reproduce this picture and change only what the spec names.

TASK: A single scene illustration: the exterior of the Rusty Robot cantina at night in the domed city of Kannan.

Reproduce image 2 and change TWO things. Everything else stays exactly as it is.

FIRST: MAKE THE STAIRCASE LONGER AND SHALLOWER.

The flight in image 2 is short and steep: about six tall treads climbing quickly in a
small footprint, so the entrance feels cramped and the steps look more like a ladder
than an approach.

Rebuild it as a long, gentle flight. Count it:

- About TEN treads instead of six.
- Each riser is LOWER — roughly half the height it is now — and each tread is DEEPER,
  so the climb is gradual.
- The flight therefore reaches much FURTHER out from the door into the street, its
  bottom tread landing well forward in the lower third of the picture.
- The flight is also WIDER side to side than it is now, so it reads as a generous
  public stair, not a narrow stoop.
- Both solid side walls extend down with it and finish on the pavement, keeping every
  tread contained between them exactly as they do now. No tread projects past either
  side wall.

The door, its arch and the canopy above do not move or change size. The staircase
grows downward and outward from the threshold, into the street.

SECOND: GIVE THE BUILDINGS ALONG THE ALLEY MORE VARIETY.

The buildings down the right-hand side currently repeat one module: similar widths,
similar heights, the same banding, the same window pattern, over and over. The street
reads as one building copied.

Make them read as MANY SEPARATE BUILDINGS, built at different times by different
hands. Vary, from one to the next:

- WIDTH — some narrow and tall, some broad and squat.
- HEIGHT and ROOFLINE — stepped parapets, plain flat tops, a projecting cornice, a
  setback upper storey. No two neighbours ending at the same height.
- WINDOWS — different sizes, different spacings, different arrangements. Some facades
  with few windows, some with many. Some lit, some dark.
- SURFACE — plain stucco against banded masonry against a facade broken by pilasters.

KEEP THE PALETTE AS IT IS. The current deep, saturated colours are correct: warm
ochres and stone against strong teal accents. Do NOT shift toward pale, chalky or
pastel colours, and do not lighten the facades. Variety here means variety of SHAPE,
HEIGHT, WIDTH and WINDOW PATTERN, with the existing colour range redistributed across
more distinct buildings — not a new or softer colour scheme.

FREEZE EVERYTHING ELSE:

- All four crew members at the left, their poses, faces, clothing and the robot arm.
- The alley corner where the near wall meets the cantina: ONE vertical corner line, the
  near wall one unbroken slab meeting the pavement, one plain buttress on the pavement.
- The canopy: one straight top edge, each end a plain undivided block with a flat end
  face and a downlight beneath.
- The door, its arch and ironwork; the two dark unlit windows, one each side of the
  door; the sign board, its lettering and emblem; the plain wall right of the door.
- The far end of the alley: the lit archway, the distant figures, the domed skyline.
- There are NO handrails anywhere on the steps and none may be added.

LIGHTING IS UNCHANGED. The crew stand in deep shadow and the steps are lit: the crew's
region measures 0.298 times the brightness of the lit steps, and it must still measure
0.298 after this edit. Do not brighten the crew to make them legible.

Render everything in the exact brush scale of image 1, the style anchor: fewest possible flat shapes, no blending, no micro-detail.
