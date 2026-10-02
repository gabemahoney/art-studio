---
name: image-surgery
description: Decide HOW to make a change to an existing Rogue Frontier image — local ImageMagick arithmetic, a Codex regeneration, a generate-and-composite transplant, or the paid API. Use whenever an approved or candidate image needs a correction, and before spending a generation on it. Covers masked tonal edits, region transplants, measurement, and the narrow bar for spending API credits.
---

# Image surgery

`art-studio` covers how images are *made*; this covers how they are *changed*. Run
everything from `gm/image_generation/`.

## The governing rule

**NEVER SPEND A CREDIT WITHOUT ASKING THE USER FIRST.** `gen.py` holds no key, so a
paid call fails closed and prints what to do — **but that is a mechanism, not an
impossibility.** If you find a key anywhere, in a `*.key` file, a history file or the
environment, **do not use it: say you found it.** **Check the gate is armed before
relying on it** — `bin/selftest.py` warns if any readable key is still in the vault (it
searches by name *and* by content, so an innocuous filename is not safe) or if
`.api-key.enc` is missing.

**Never run `unlock.py` yourself and never pass `--key-fd`** — that is the user's
approval, not yours. One approval is one call; change anything and it needs a fresh
one — a blanket authorisation is not a yes to a specific call. When you ask, give what
you tried, why the cheaper paths cannot do it, and the cost as an estimate. `--approved-by` records
why, not permission. Codex needs none of this.

**Credits are the last resort, not one of four equal options.** Work down this list
and stop at the first path that can do the job:

1. **ImageMagick** — free, exact, provably zero change outside a mask
2. **Codex regeneration** — covered by the subscription
3. **Generate-and-composite** — one Codex call plus local surgery
4. **API inpainting** — real money, but the only true targeted repaint here

## Step 0 — Diagnose before you route

**Magnify the fault to 300–500% and name the actual shape on the canvas before
choosing a path.** The user's words report a symptom, not a diagnosis — "Sion still
has a cape" was a scarf painted as a cowl, and four cape prohibitions failed before
anyone looked. Route the fault you can see.

**If the fault is a design fact, the fix must go back into `description.md`.** A
pixel edit teaches the model nothing: the next scene reads the text and repaints the
original error. ImageMagick changes the deliverable; only the text changes the
canon. Snapshot to `description_versions/` when the design itself moves.

## Route by what the change actually is

**ImageMagick can only rearrange pixels that already exist; regeneration invents
them.** Most routing follows from that one line — the table is for the cases where it
does not.

| The change | Path | Why |
|---|---|---|
| Brightness, contrast, saturation, colour balance | **ImageMagick** | Exact, free, works when Codex is down. Never regenerate or pay for this. |
| Resize, pad, print deliverable | **ImageMagick** (`gen.py --refinish`) | Upscales to ~1.5x are invisible in this flat matte style. |
| Crop, set DPI, or shrink an over-budget file | **ImageMagick**, by hand | `--refinish` does none of the three — it only *warns* about size. |
| Wrong aspect ratio came back | **Regenerate**, stating the ratio in the prompt body | `--size` is advisory on Codex; `--refinish` would just pad it. |
| Remove something whose covering texture is flat and adjacent | **ImageMagick** | Clone from the same image. |
| Move a *correct* region from one candidate to another | **ImageMagick** | See *Transplants*. |
| Tighter crop from pixels already present | **ImageMagick** | Crop then upscale. |
| Pose, expression, added objects, architecture, geometry; removing something that reveals structure or that a figure overlaps; any reframe that reveals content outside the frame | **Regenerate** | Those pixels do not exist. |
| Wrong, misspelled or badly drawn **text/lettering** | **Regenerate**, then Path 3 | ImageMagick cannot author glyphs in style. Fix spelling and typeface in the prompt. |
| A small region regeneration keeps breaking | **Path 3**, then **Path 4** | Path 3 is free and usually enough; if its seam cannot be hidden, inpainting is the escalation — ask first. |
| Rendering eroded across passes (facets rounding off) | **ImageMagick transplant** from an un-eroded version | Tonal correction does not touch it — measured. |
| A detail below ~30 px that will not converge | **Change the gesture** | Orientation is uncontrollable at that size; pick a shape whose silhouette carries the meaning. |
| Codex returns HTTP 400 | **Work the ladder in Path 4** | Astra is already the default, so "try astra" is not a step. Spending is the last rung. |

## Path 1 — ImageMagick

**Every intermediate goes to a scratch directory, never the vault** — `T=$(mktemp -d)`
once per session, and `$T` throughout below. Only two intermediates belong in the vault,
both listed under *Guardrails*.

**Any whole-image operation can be confined to a region** by making an adjusted
copy, giving it the mask as its alpha, and laying it over the original. Swap the
middle line for any operation at all — tonal, colour, blur, sharpen.

```bash
SRC=outputs/<scene>/vNNN/image.png

# 1. Mask: white = change, black = leave. -blur feathers the edge so there is no seam.
magick -size 1536x1024 xc:black -fill white \
  -draw "roundrectangle 0,370 405,915 30,30" -blur 0x28 -alpha off $T/mask.png

# 2. A fully-adjusted copy of the whole image
magick "$SRC" -evaluate multiply 0.74 $T/adjusted.png

# 3. Mask becomes that copy's alpha
magick $T/adjusted.png $T/mask.png -alpha off -compose CopyOpacity -composite $T/layer.png

# 4. Lay it over the original
magick "$SRC" $T/layer.png -compose over -composite $T/corrected.png
```

### The mask must not carry alpha — the one failure that keeps recurring

Masks gain an alpha channel unpredictably — `-blur` always adds one, and the rest
varies. Do not reason about it: **`-alpha off` must appear at least once before the
composite**, at mask creation or in the composite; the recipe above has both
deliberately.

Omit it from both and the mask is **ignored entirely** — the adjustment lands on the
whole frame *including* the masked region. On `the-rusty-robot/v026` (crew
`300x400+40+420`, outside `400x300+900+100`): inside, correct and broken both read
39; outside, correct holds at 79 while broken drops to 59.

**So checking inside the mask cannot detect this** — it looks right. Verify by diffing
*outside*, where a correct composite changes 0 pixels.

### Measure, before and after

```bash
magick identify -format '%wx%h  aspect=%[fx:w/h]  %x%U\n' f.png   # size, aspect, density

# mean luminance of a region, 0-255 — the measurement everything else is built on
magick f.png -crop 330x500+60+430 +repage -colorspace Gray \
  -format "%[fx:int(mean*255)]" info:

magick f.png -crop 20x20+230+560 +repage -resize 1x1! \
  -format '%[pixel:p{0,0}]  hex %[hex:p{0,0}]\n' info:          # sample a colour

# TRUE count of differing pixels. -precision 10 is REQUIRED — without it %[fx:]
# prints 1.23034e+06 above ~1e6, on exactly the large diffs you care about.
magick a.png b.png -compose difference -composite -colorspace Gray -threshold 0 \
  -precision 10 -format 'differing pixels: %[fx:round(mean*w*h)]\n' info:

magick compare -metric AE   a.png b.png null:   # quantum-scaled, NOT a pixel count:
                                                # use only as a boolean, 0 iff identical
magick compare -metric RMSE a.png b.png null:   # under ~0.01 after a resize
                                                # round-trip is resampling noise
# NB: compare EXITS NON-ZERO whenever the images differ. Under `set -e` or in an
# && chain, a working comparison aborts the script. Append `|| true`.
```

**State tonal targets as a ratio** — `mean of region A ÷ mean of region B`. Ratios
survive rephrasing; "a bit darker" does not. **Record both crop boxes every time you
quote one**: only 2 of 60 `the-rusty-robot` receipts did, so most of their numbers can
no longer be checked. That scene's canonical pair is crew `330x500+60+430` over lit
steps `300x120+700+860` — keep those boxes there so the series stays comparable with the
values already in its receipts. Edge energy is its second tracked number and uses the
crew box.

**A feathered mask lands HIGH of a computed factor.** `-evaluate multiply` is exactly
linear, but the blurred edge gets only partial adjustment, so a region measured across
the feather reads above target — 38 where 50 x 0.74 predicted 37. Measure inside the
fully-white part, or expect one corrective pass.

## Path 2 — Codex regeneration, and its hidden cost

**Every edit pass repaints the entire frame.** "Change only X" is an approximation
recomputed from scratch, so errors accumulate in whatever direction the model's
priors pull. Measured on `the-rusty-robot`, across three edits that each explicitly
froze the lighting, the crew's ratio climbed 19% — monotonic, because the model pulls
toward legible subjects.

- **Re-measure after every pass**, and **measure two numbers, not one**: brightness
  drifts, and so does rendering. The flat angular facets round off a few percent a
  pass — 12.8% across five generations, v005 to v028 on the crew box; that span is six
  `vNNN` because v027 is a local composite — invisible at any magnification because it
  is gradual.

  ```bash
  magick f.png -crop 330x500+60+430 +repage -colorspace Gray -normalize \
    -morphology Convolve Laplacian:0 -format "%[fx:standard_deviation*1000]" info:
  ```

  A tonal correction does **not** touch it — the pass that restored the ratio moved
  edge energy 0.1% against that 12.8% loss, so checking only the ratio returns clean
  on a damaged image.
- **Never enumerate colours inside a freeze instruction.** Naming six coloured
  garments while asking to keep "depth of shadow" says *make six things
  identifiable*, and brightness wins a little each pass. State the ratio as a number
  instead.

## Path 3 — Generate-and-composite (inpainting without credits)

Once a freeze instruction has failed twice in a scene, this is the default, not the
exception: regenerate for geometry only, composite for everything else. Treat the
model as a source of shapes, never of finished frames.

1. Regenerate normally through `bin/prompt.py` + `bin/gen.py`, aimed at that region.
   Accept that the rest of the frame drifts.
2. Mask **only** the fixed region out of the new candidate.
3. Composite it onto the good baseline.

Works when the region is interior and its surroundings hide a feathered seam. Fails
when the fix changes a silhouette against a busy background, or must align with
something the new candidate drew differently.

## Path 4 — The paid API, and the bar for spending credits

**The only true targeted repaint here.** `--mask` sends a mask to `/v1/images/edits`
and **only the masked pixels regenerate**. Codex cannot inpaint; Path 3 only
approximates it.

```bash
python3 bin/prompt.py --masked \
  --role "EDIT TARGET:The image being repaired." \
  --role STYLE:"Match its hand-painted matte rendering only." \
  --task "..." --spec-file /tmp/spec.txt -o /tmp/p.txt

python3 bin/gen.py --scene <slug> --prompt-file /tmp/p.txt --backend api \
  --attach outputs/<slug>/vNNN/image.png:"EDIT TARGET" \
  --attach ref_images/style_references/canonical_style_reference.png:STYLE \
  --mask tmp/fix-the-hand.png --size 1536x1024
```

Copy that invocation exactly — **`rules.md` → *Masked inpainting*** has the reasons.
`gen.py` enforces most of it, but **not** the mask's polarity: it refuses an all-black
mask and warns above 90%, so a pre-inverted mask covering 86% sails through and you pay
to repaint everything except the region you meant. Two things the example cannot show
you:

- **the EDIT TARGET goes first** — the one call where the anchor is not image 1, which
  inverts the One Rule
- the mask is a plain greyscale vault mask, **WHITE = repaint**, never pre-inverted,
  and `--size` must equal the EDIT TARGET's real dimensions, not the 1536x1024 above

The result is **re-encoded**: the unmasked area is preserved visually but not
byte-identically, so the AE=0 guarantee does not transfer. **No masked call has
completed here** — check the first one returns the target, not the anchor.

**Try Path 3 first**: free, and it hides most seams.

**The bar — propose credits only if one of these holds.** If none does, do not raise
it at all; go back to Paths 1-3. Then still ask (see *The governing rule*).

- An **exact native pixel size** is needed and the upscale would exceed ~1.5x.
- A **small region** survived Path 3 and its seam cannot be hidden.
- **Codex is genuinely unavailable.** `gpt-6-astra` is both the default and the only
  entry in `CODEX_MODELS_OK`, so there is no second model to try: retry once, check
  `~/.codex/auth.json` exists, then add astra to `CODEX_MODELS_BROKEN`, update
  `rules.md`'s table, and say plainly that Codex is down.

**Never for:** tonal or colour work, crops and resizes under ~1.5x, transplants, a
first or second attempt at anything, or framing and composition changes — a mask
cannot help when the whole frame must move.

Cost is an estimate, ~**$0.05–$0.35 per generation**. `rules.md` records a $10
**deposit**, not a balance — never report it as money remaining.

## ImageMagick competency

### Masks

Any `-draw` primitive works; the shape is never the hard part. Build each as `magick
-size <WxH> xc:black -fill white -draw "..." -alpha off $T/mask.png`, where **`-size` must
equal the target image's own dimensions** — a mask of any other size misaligns silently,
so read them with `magick identify` rather than assuming the 1536x1024 below:

```bash
-draw "roundrectangle 0,370 405,915 30,30"      # feather with -blur 0x28
-draw "ellipse 400,500 120,180 0,360"
-draw "polygon 0,42 20,37 35,25 54,21 155,78"   # to follow a real edge

# ramps fade an adjustment out across the frame. gradient: is ALWAYS vertical, and
# reads 127 at both side edges, so it does nothing to a left/right problem: build it
# tall and rotate. -rotate is CLOCKWISE, so +90 puts white — the part that CHANGES —
# on the right.
magick -size 1536x1024 gradient:white-black            -alpha off $T/mask.png  # DOWNWARD
magick -size 1024x1536 gradient:white-black -rotate -90 -alpha off $T/mask.png  # LEFT
magick -size 1024x1536 gradient:white-black -rotate  90 -alpha off $T/mask.png  # RIGHT
```

`-blur 0xN` sets the feather. **Too hard an edge is the main way these edits get
caught** — N of 20–30 is usually safe over textured ground, more over flat. Lifting
shadows across a large area in a three-or-four-value flat style will posterize; check
for banding at 300%.

**Every coordinate here is from one picture.** Measure your own region and look at the
crop before trusting it — composition shifts between candidates, so a reused box can
silently measure different content.

### Tonal and colour operations

```bash
-evaluate multiply 0.74          # scale all values; the precise way to hit a ratio
-brightness-contrast -10x5       # NOT percentages of the mean: -10x0 took 81 to 56,
                                 # a 31% drop. Nudge by eye; never hit a target.
-gamma 0.9                       # DARKENS midtones; delta scales with the base value
-gamma 1.1                       # BRIGHTENS midtones; neither crushes black or white
-modulate 100,70,100             # brightness,saturation,hue — 70 = desaturate 30%
+level 5%,95%                    # COMPRESSES contrast (-level stretches it); lifts
                                 # blacks, good for haze
```

To hit a measured target use `-evaluate multiply`, factor = `target ÷ current`.

**Avoid `-modulate`'s hue argument for "too magenta".** It rotates *every* hue, so it
drags the ochres and teals along, and the direction is unintuitive — on a `#2D222B`
swatch, `100,100,95` measures `#2D222D` — a barely-visible shift *toward* magenta.
Mask the region and adjust saturation instead.

### Crop, resize, deliverables

`-crop WxH+X+Y` needs `+repage`, or the offset haunts every later operation — an
un-repaged 300x300 crop comes back out of `-flatten` at the original 1536x1024.

```bash
# the vault's deliverable path: resizes-to-fit, pads, flattens, checks the size
# budget. It does NOT crop, does NOT set DPI and does NOT recompress.
python3 bin/gen.py --refinish outputs/<scene>/vNNN --final-size 2172x1448 \
  --flatten '#1b1e26' --max-mb 4

# EVERY command below writes to a NEW path, because when the raw output already
# matches --final-size and has no alpha, --refinish writes no file and hands back
# image.png ITSELF — 193 of 233 candidates at --preset book-float — and that is frozen
# history. (199 are 1536x1024; the 6 with alpha do get a file.)
magick <in>.png -density 300 -units PixelsPerInch     $T/delivered-300dpi.png
magick <in>.png -colors 128 -define png:color-type=2  $T/reduced.png  # median 47%
magick <in>.png -quality 88                           $T/reduced.jpg  # ~85%, last resort
# png:color-type=2 is not optional: -colors alone writes an INDEXED PNG-8, not the
# truecolor the spec claims. No alpha is involved, so -alpha off does nothing.
# -strip is not a size fix: 0% on a written deliverable, median 5.2% on a raw
# image.png (all 233; max 16.3%).
```

**DPI verifies in px/cm.** PNG stores density in px/metre, so a successful 300 DPI
stamp reads `118.11 PixelsPerCentimeter` — that *is* 300 DPI. An unstamped PNG prints
`72Undefined`, where `Undefined` means no density, not 72.

### Transplants between candidates

The technique in `the_antares/sources/composite-v015.sh`:

```bash
magick donor.png -crop 109x110+29+810 +repage -resize 76x77! $T/piece.png
magick -size 76x77 xc:black -fill white -draw 'ellipse 38,39 37,37 0,360' $T/pmask.png
magick $T/piece.png $T/pmask.png -alpha off -compose CopyOpacity -composite $T/masked.png
magick base.png $T/masked.png -geometry +33+827 -compose over -composite $T/out.png
```

Match the donor's local brightness first, or the transplant reads as a patch.

**The mask boundary is where composites fail.** Diff the region's *edges* against the
baseline, not only the area outside the mask: a boundary crossing a real object edge
imports broken geometry while every outside-mask count reads 0. And when the base
already carries a transplant, subtract that region from the new mask — multiply by a
mask that is BLACK over the region to protect:

```bash
magick arch.png protect.png -compose multiply -composite $T/combined.png
```

or you silently overwrite it.

### Inspection aids

```bash
# stack two versions at matched scale to compare honestly
magick a.png -resize 760x $T/a2.png && magick b.png -resize 760x $T/b2.png
magick $T/a2.png $T/b2.png -background '#333' -splice 0x6 -append $T/cmp.png
```

Inspect every contested detail at **300–500%** before calling it fixed.

## Guardrails

- **Everything already written is frozen** — `image.png`, and any promoted
  `reference.png` or `final.png`. Never edit one in place and never open one in an
  image editor; a candidate was annotated in Preview and saved over, destroying it.
  Annotate a scratchpad copy; correct in a new `vNNN` and promote that, `--replace` if
  a head exists.
- **Intermediates go to the scratchpad**, except two that belong in the vault: a mask a
  composite's receipt cites to reproduce it, and a `--mask` for a paid call (`gen.py`
  refuses one outside the vault).
- **A composite you intend to keep needs its own `vNNN`** — the image as `image.png`,
  a hand-written `generation.md`. `promote.py` and `--refinish` read no other
  filenames. **That receipt must open by saying no model was called** (`Source: local
  composite, no generation`), then the baseline vNNN, the donor vNNN and the commands;
  without it, a composite attached to a later generation passes the provenance check
  silently and enters the record as model history. Throwaways go to the scratchpad.
- **Do not record a local correction with `review.py --replace`** — it overwrites the
  `Review:` line, which by then is the one that caught the fault. Put the note in the
  new candidate's receipt.
- **A damaged candidate is sometimes recoverable — check its receipt.** Images live
  outside this repo (`rules.md` → *Where images live*), so `git checkout` only helps if
  the repo holding them tracks them; right now **0 of 233** are tracked there. What does
  survive is the `codex source` path under `~/.codex/generated_images/` recorded in
  `generation.md`, which stays in this repo: **93 of 233** have one and all 93 still
  resolve. **The other 140 cannot be recovered at all** — which is why the rules above are
  absolute rather than advisory, and why committing the images tree is worth doing.
- **Never silently substitute a worse fix** when a path is blocked. Say what is blocked
  and carry on with the rest.
