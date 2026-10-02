# Graxo v018
User request: That nose is cartoonish. Too much.
Mode: edit of user-selected candidates/v015/image.png with cumulative eye, forehead and holster-view constraints
Style: v2 (current block embedded below)
Tool: built-in image_gen
Inputs (ordered):
- STYLE: ref_images/style_references/canonical_style_reference.png (style v2)
- EDIT TARGET: candidates/v015/image.png
- DESIGN: description.md (v7 = description_versions/description-v7.md)

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

Use case: precise-object-edit.
Image 1 is STYLE: match its rendering technique only. Ignore its people, clothing, equipment, and setting.
Image 2 is EDIT TARGET: Graxo v015, the user-selected baseline with correct likeness and readable eyes. Preserve all unchanged details exactly and keep all repainted areas in the STYLE image's rendering.

FULL DESIGN:
# Graxo

**Description version: v7** (2026-09-11)

Height: **6′2″**.

## Appearance

Adult man with a weathered elongated angular face with a longer middle and lower face, prominent long nose with a moderately full, naturally rounded bulbous tip with full nostril wings; the tip is a little broader than the bridge, proportionate to his long adult face, never spherical or caricatured, slightly taller forehead (a subtle increase in brow-to-hairline distance, preserving the forelock), heavy brow, clearly readable deep-set eyes with visible light sclera and dark iris/pupil marks, preserved eye shape and spacing, pronounced angular cheekbones and a strong jaw with a rounded chin and curved lower contour. Warm light-to-medium skin, thick dark eyebrows, a regular neatly trimmed dark-brown mustache matching his hair, ending at the mouth corners with no curled ends or handlebar wings; no beard, dark brown hair swept up with a loose forelock. Clearly visible silver-gray hair at both sides and temples. Mature, appraising expression; exact age and eye color unspecified.

## Clothing

Full-width aubergine technical-fabric cape over both shoulders and back, open front, high standing collar and two independent square antique-gold medallion pins, one securing each cape edge; no connecting strap, cord or chain. Long cape extending below the knees. Matte exterior; dusty mauve lining with sparse floral motifs.

Plain dark walnut-brown fitted futuristic vest with asymmetric sealed offset closure, bonded technical panels, clean geometric seams and restrained flush metallic fasteners; no buttons, lapels or floral pattern. Ivory long-sleeved shirt. Compact plum silk ascot, proper knot with broad blades tucked into vest and a sparse muted-gold botanical pattern.

Charcoal trousers, sleek charcoal boots with metal toe and heel caps only; plain leather uppers with no metal at the ankles or boot tops. Charcoal molded holster at anatomical right hip holds one high-tech blaster, wood grip upward/backward, muzzle downward enclosed. Compact diagnostic device on belt and slim metallic scanner on left wrist.

## Character

Spaceship engineer and smuggler with a dandy's attention to dress. Confident, discerning and technically capable; measured posture, alert appraisal and a wry smile.

## Reference sheet

Four full-body views: front, three-quarter, right-side profile facing right and back, at consistent scale. In the right-side profile, draw the cape behind the anatomical right hip and keep the right arm clear so the holstered blaster is unmistakable: visible wood pistol grip, angular receiver and trigger-guard silhouette above the molded holster, with the muzzle enclosed downward. The blaster remains holstered. Four expression portraits below: neutral, wry smile, focused and concerned. Plain gray background, no height chart (the shared crew lineup carries height comparisons).

## Painting

Facial identity is defined by the Appearance section above and must read clearly: visibly elongated middle and lower face, long projecting nose with broad bulbous tip, and regular dark mustache. Simplify the rendering into a few broad matte planes per facial region, chunky hair masses, and large quiet cape surfaces; avoid small tessellated facets and excessive surface detail.

Rendered per the shared Style Block in `gm/image_generation/style.md` (canonical_style_reference.png is the style anchor).

Proportions: sturdy legs and moderately broad shoulders, as shown in reference.png. Height: 6 feet 2 inches.

## Height presentation

Individual angular sheets use a plain gray background without a height chart. The shared crew lineup carries the height comparison. Stated height: 6′2″.


CUMULATIVE CHANGES FROM IMAGE 2:
NOSE: a restrained natural adjustment. Keep the long bridge, existing nose length and adult facial proportions. Make the tip only about 15 percent fuller/wider than image 2, with slightly fuller nostril wings smoothly integrated into the existing silhouette. It is a naturally fleshy nose tip, NOT a separate round ball. No spherical knob, drooping pear, oversized bulb, cartoon nose, red tint or pinpoint shine. The user rejected a previous 40-percent enlargement as cartoonish; aim much closer to the original here. Show this modest fullness in all views using flat angular paint, not rounded glossy modeling.
EYES: preserve image 2's exact eye shapes, spacing, gaze and expressions. Keep visible small ivory sclera and dark iris/pupil marks beneath the brows. Do not simplify eyes away into black slits or empty shadow triangles. Maintain the same recognizable face.
FOREHEAD: a subtly taller forehead, a small increase in brow-to-hairline distance, keeping the forelock and silver temples.
HOLSTER: replace ONLY the third full-body view with a RIGHT-FACING right-side profile (nose points toward the right edge of the sheet). Show anatomical right hip closest to viewer, cape swept behind that hip and arm clear. One sci-fi blaster pistol remains holstered muzzle-down, wood grip angled backward and angular metal receiver plus trigger guard visibly above holster lip. It should unmistakably read as a holstered pistol. No extra weapon. Keep front, three-quarter, back and four expression portraits otherwise unchanged.
Preserve all clothing, colors, proportions, equipment counts, sheet layout and gray background.

Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.

## Review
Nose fullness reduced markedly from v017 to a more natural proportion. Eyes remain readable in portraits. Right-facing profile restored with pistol grip and receiver visible; holster geometry has an extra upright brown element and is not fully clean. Forehead increase remains subtle. Existing faceted texture persists. Not promoted.
