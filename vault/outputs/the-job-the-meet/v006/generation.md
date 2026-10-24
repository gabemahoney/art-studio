# The Job — The Meet v006
User request: make the gloves and the belt black. and make the robes more of a brown color.
Mode: edit of series baseline v001 with accumulated corrections; brown robes, black gloves and belt
Style: v2
Tool: built-in image_gen (model not exposed)
Inputs (ordered):
- STYLE: ref_images/style_references/canonical_style_reference.png (style v2)
- EDIT TARGET: outputs/the-job-the-meet/v001/image.png
- IDENTITY: assets/characters/graxo/reference.png (= graxo/candidates/v024/image.png)
- IDENTITY: assets/characters/daxus/reference.png (= daxus/candidates/v001/image.png)
- IDENTITY: assets/characters/sion/reference.png (= sion/candidates/v001/image.png)
Descriptions: Graxo v10, Daxus v1, Sion v1. Stranger design remains provisional scene-local.
Skill route: illustrate revision from same baseline with accumulated hair/table/gaze/robe corrections; final color instruction supersedes earlier colors.
Status: PROMOTED to final.png 2026-09-30. User approval, verbatim: "yes we need to prompote them too. oops" — retroactive: this candidate had already been placed in the book's PDF by hand, so the approval record was backfilled. This receipt predates the current bin/gen.py format and had no Status line, which is why bin/promote.py could not update it automatically.

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

Image 1 is STYLE: match its matte painted medium and broad brush scale only. Ignore its characters, costumes, and setting. Angular paint edges do NOT mean cubic anatomy or tiled hair.
Image 2 is EDIT TARGET: The Job — The Meet v001. Preserve the four-person cantina negotiation composition and all unchanged character designs.
Image 3 is IDENTITY: approved Graxo v024, facial likeness and costume only; ignore rendering and sheet layout.
Image 4 is IDENTITY: approved Daxus v001, facial likeness and costume only; ignore rendering and sheet layout. Daxus is the bespectacled man at LEFT in image 2.
Image 5 is IDENTITY: approved Sion v001, facial likeness and costume only; ignore rendering and sheet layout. Sion is the woman with red goggles at RIGHT in image 2.

Use case: identity-preserve. Edit the existing cantina meeting, making these four corrections together:
1. Daxus's hair and the unnamed stranger's hair must look like coherent natural hairstyles painted simply. REMOVE the existing checkerboard/cube/tessellated hair pattern completely. Daxus retains his neat side part, closely cropped sides and swept-back voluminous wave. Stranger retains a short dark bob tucked behind the ear. Paint each hairstyle as ONE continuous dark silhouette plus ONE broad restrained lighter sweep following the hair's growth. Smoothly flowing silhouette, broad coherent curved sweep; irregular matte brush edges are fine. Absolutely no cubes, bricks, scales, crosshatching, lattice, diamond tiles, bundles of little blocks, or individual strands. Keep Daxus's face and glasses unchanged.
2. Replace the stained table surface with a mostly CLEAN muted gray metal tabletop. A uniform quiet matte plane with just two or three small edge scuffs is sufficient. Remove the ochre crust, blotches, spilled-liquid marks, mottling, rust patches and stain rings. Preserve table shape, perspective, cups and character hand positions. The room can remain worn; the tabletop has been wiped clean.
3. Redesign ONLY the unnamed stranger's outfit as a fitted utilitarian SCI-FI JUMPSUIT, slate blue-gray, a structured high standing collar rising along the sides of her neck, concealed asymmetric closure, a few broad geometric seam panels and restrained flush fasteners. Long dark charcoal gloves extend to her elbows on BOTH arms, covering all visible fingers and hands completely; preserve a natural expressive open-hand gesture. The gloves are cloth or flexible synthetic material, not armor. No exposed hand skin, no short gloves, no military insignia or faction logos. Read clearly as a futuristic civilian spacer's jumpsuit, not an ordinary jacket, uniform or fantasy tunic. Any lower portion visible must continue as the same one-piece jumpsuit.
4. The unnamed stranger must be LOOKING DIRECTLY AT DAXUS, the glasses-wearing medic at far left. Turn her head and orient her eyes toward his face across the table, with a clear mutual conversational sightline. She is speaking to him. Keep her seated in the foreground on the near side of the table, her face readable in profile/three-quarter profile. Her attention is on the LEFT man, not Graxo in the middle and not Sion on the right. Daxus attends to her.

Preserve Graxo's approved elongated face, full bulbous nose, high forehead, trimmed mustache and silver temples, aubergine cape and brown vest. Preserve Sion's ochre jacket, teal scarf, opaque red goggles, anatomical LEFT metal arm and natural right arm. Preserve Daxus's off-white medical jacket, orange shirt, glasses, scanner and two injector pens. Preserve all four people, their seating, cups, background cantina, ceiling lamp, framing and lighting. No added text, characters, props or panels. Keep everything else identical to the edit target, and keep all repainted areas in the STYLE image's rendering. Broad matte gouache planes with visible restrained brushwork, no glossy digital finish. Hair uses broad organic silhouettes, never tessellated geometric blocks.

FINAL COSTUME OVERRIDE: Replace the stranger's jumpsuit/jacket specification above with classic Princess Leia-style ivory-white science-fiction ROBES. NO cloak, cape, raised hood, beret, hat or teal jumpsuit. A simple high standing neckline, elegant loose one-piece white robe, broad flowing long sleeves, softly draped ivory fabric and a restrained silver belt at the waist where visible. Hood down and out of sight. This is clean understated retro space-opera clothing with broad plain fabric surfaces, no armor, rank insignia, logos, ornate embroidery or medieval trim. Retain her long gloves, now ivory-white to harmonize with the robes, covering both hands and forearms. Her short dark bob and original face remain unchanged; do not replace her identity with an actress or change her hair into side buns. She remains the unnamed adult rebel operative at the foreground table, calmly speaking and looking directly at Daxus on the left. Preserve her open-hand conversational gesture. Keep all crew members, corrected Daxus hair, clean tabletop, cups, cantina lighting and composition. Paint the white robes in broad opaque ivory planes and simple slate-gray shadows matching the STYLE image.

FINAL COLOR CORRECTION, overriding all earlier robe, glove and belt color wording: the unnamed operative's flowing high-neck robes are warm medium BROWN, with muted walnut and umber painted planes, not white or ivory. BOTH long gloves are BLACK, including all fingers, hands and forearms; no white glove areas. Her waist belt is BLACK, including its broad panels and buckle; no silver or ivory belt elements. Preserve the Leia-style robe cut, high neckline, flowing long sleeves, short dark bob, face, seated posture and gaze toward Daxus. No cloak or hood. Keep all other accumulated corrections and every other character unchanged. The brown robes should remain clearly readable against the darker chair and background, with broad matte ochre-brown light planes and deep umber shadows.

Render everything in image 1's exact brush scale: fewest possible flat shapes, no blending, no micro-detail.

## Self-check
Robes now warm brown; visible glove and broad waist belt black. Far hand obscured, so its glove color cannot be independently confirmed. High neckline and flowing sleeves retained, gaze toward Daxus preserved. Crew, clean tabletop and composition visually close to baseline. Matte painted treatment retained. Candidate saved, not finalized.
