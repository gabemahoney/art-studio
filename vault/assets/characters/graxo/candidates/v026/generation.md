# Graxo v026
User request: v22 facial features look correct. But re-stylize because it became too smooth and detailed. Tell me how you navigate the skills to do so.
Mode: fresh generation, style anchor and description only
Style: v2
Tool: built-in image_gen (model not exposed)
Inputs:
- STYLE: gm/image_generation/ref_images/style_references/canonical_style_reference.png (style v2)
- DESIGN: description.md (v10 = description_versions/description-v10.md)

## Skill route
Repaints v023/v024 insufficient; tight-crop fresh v025 also inherits detailed face rendering. Remove identity input per style-failure ladder. Description carries correct nose and forehead; exact likeness may change. No reference or candidate images attached.

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

Image 1 is STYLE: copy its matte gouache technique, broad flat-brush marks, economical shapes and limited values. Ignore its subjects and setting.

Use case: stylized-concept. Generate a NEW hand-painted gouache character reference sheet with the following design.

# Graxo

**Description version: v10** (2026-09-11)

Height: **6′2″**.

## Appearance

Adult man with a weathered elongated angular face with a longer middle and lower face, prominent long nose with a broad, softly rounded bulbous tip with full nostril wings and a distinct rounded lower silhouette; the tip is distinctly broader than the bridge, proportionate to his long adult face, never spherical or caricatured, tall forehead with a generous exposed brow-to-hairline plane and a loose forelock, heavy brow, clearly readable deep-set eyes with visible light sclera and dark iris/pupil marks, preserved eye shape and spacing, pronounced angular cheekbones and a strong jaw with a rounded chin and curved lower contour. Warm light-to-medium skin, thick dark eyebrows, a regular neatly trimmed dark-brown mustache matching his hair, ending at the mouth corners with no curled ends or handlebar wings; no beard, dark brown hair swept up with a loose forelock. Clearly visible silver-gray hair at both sides and temples. Mature, appraising expression; exact age and eye color unspecified.

## Clothing

Full-width aubergine technical-fabric cape over both shoulders and back, open front, high standing collar and two independent square antique-gold medallion pins, one securing each cape edge; no connecting strap, cord or chain. Long cape extending below the knees. Matte exterior; dusty mauve lining with sparse floral motifs.

Plain dark walnut-brown fitted futuristic vest with asymmetric sealed offset closure, bonded technical panels, clean geometric seams and restrained flush metallic fasteners; no buttons, lapels or floral pattern. Ivory long-sleeved shirt. Compact plum silk ascot, proper knot with broad blades tucked into vest and a sparse muted-gold botanical pattern.

Charcoal trousers, sleek charcoal boots with metal toe and heel caps only; plain leather uppers with no metal at the ankles or boot tops. Charcoal molded holster at anatomical right hip holds one high-tech blaster, wood grip upward/backward, muzzle downward enclosed. Compact diagnostic device on belt and slim metallic scanner on left wrist.

## Character

Spaceship engineer and smuggler with a dandy's attention to dress. Confident, discerning and technically capable; measured posture, alert appraisal and a wry smile.

## Reference sheet

Four full-body views: front, three-quarter, right-side profile facing right and back, at consistent scale. In the right-side profile, draw the cape behind the anatomical right hip and keep the right arm clear so the holstered blaster is unmistakable: visible wood pistol grip, angular receiver and trigger-guard silhouette above the molded holster, with the muzzle enclosed downward. The blaster remains holstered. Four expression portraits below: neutral, wry smile, focused and concerned. Plain gray background, no height chart (the shared crew lineup carries height comparisons).

## Painting

Facial identity is defined by the Appearance section above and must read clearly: visibly elongated middle and lower face, long projecting nose with broad bulbous tip, and regular dark mustache. Simplify the rendering into five to eight broad matte planes per face in total, chunky hair masses, and large quiet cape surfaces; avoid small tessellated facets and excessive surface detail.

Rendered per the shared Style Block in `gm/image_generation/style.md` (canonical_style_reference.png is the style anchor).

Proportions: sturdy legs and moderately broad shoulders, with a sturdy, balanced adult build. Height: 6 feet 2 inches.

## Height presentation

Individual angular sheets use a plain gray background without a height chart. The shared crew lineup carries the height comparison. Stated height: 6′2″.


Landscape sheet, four full-body views above four expression portraits, plain quiet gray background, no text. Use broad flat opaque brushwork throughout. Paint each face in just five to eight big connected planes total, with only small simple eye and mustache marks. Use the specified rounded bulbous nose contour and tall forehead without smooth nose modeling or pinpoint highlights. Broad ochre light stroke, connected umber shadow shape, crisp angular edges. Brushstrokes visibly wide and blunt, with sparse coarse bristle breaks. Cape is big quiet aubergine planes; hair chunky dark masses and broad silver temple strokes. Equipment and trim simplified flat color blocks. No mosaic facets, narrow scratches, gradients, gloss, or dense background texture. Make the result visibly handmade and spare, matching image 1's paint handling.

Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.

## Self-check — partial style improvement, likeness failed
Anchor-only input produces larger quieter matte planes, reduced nose shine and coarser paint handling, though faces still exceed the strict plane limit. Exact v022 likeness is lost: nose tip narrower/less bulbous, facial contour and hairstyle differ, poses and costume details changed. Does not fulfill combined likeness-and-style requirement. Not promoted. Full-sheet repaint preserved likeness but resisted style change; crop preserved detailed rendering; anchor-only improved rendering but lost likeness. All attempts retained for debugging.
