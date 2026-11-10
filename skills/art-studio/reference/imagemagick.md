# ImageMagick cookbook

The commands behind `reference/fixing-an-image.md`. `S`, `T`, `PKG` and `OUT` are as in
`SKILL.md`; **every intermediate goes to `$T`, never into the package or the output
folder.**

## Confining an operation to a region

For an image without alpha. On a Layer use *Replacing a region of a Layer*, because
step 3 replaces the image's alpha with the mask.

Make an adjusted copy of the whole image, give it the mask as its alpha, lay it over
the original. Swap line 2's operation for anything at all — tonal, colour, blur,
sharpen.

```bash
SRC=OUT/<scene>/vNNN/image.png

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

### The mask must not carry alpha — the failure that keeps recurring

Masks gain an alpha channel unpredictably: `-blur` always adds one, and the rest
varies. Do not reason about it. **`-alpha off` must appear at least once before the
composite** — at mask creation or in the composite. The recipe above has both,
deliberately.

Omit it from both and the mask is **ignored entirely**: the adjustment lands on the
whole frame *including* the masked region. Inside the mask the result is
indistinguishable from a correct one, because inside is where the adjustment was
supposed to land.

**So checking inside the mask cannot detect this.** Verify by diffing *outside* the
mask, where a correct composite changes 0 pixels and a broken one changes everything.

### A feathered mask lands HIGH of a computed factor

`-evaluate multiply` is exactly linear, but the blurred edge gets only partial
adjustment, so a region measured across the feather reads above target. Measure inside
the fully-white part, or expect one corrective pass.

## Masks

Any `-draw` primitive works; the shape is never the hard part. Build each as
`magick -size <WxH> xc:black -fill white -draw "..." -alpha off $T/mask.png`, where
**`-size` must equal the target image's own dimensions** — a mask of any other size
misaligns silently. Read the real dimensions with `magick identify` rather than
assuming the 1536x1024 below.

```bash
-draw "roundrectangle 0,370 405,915 30,30"      # feather with -blur 0x28
-draw "ellipse 400,500 120,180 0,360"
-draw "polygon 0,42 20,37 35,25 54,21 155,78"   # to follow a real edge

# Ramps fade an adjustment out across the frame. gradient: is ALWAYS vertical, and
# reads 127 at both side edges, so it does nothing to a left/right problem: build it
# tall and rotate. -rotate is CLOCKWISE, so +90 puts white — the part that CHANGES —
# on the right.
magick -size 1536x1024 gradient:white-black             -alpha off $T/mask.png  # DOWNWARD
magick -size 1024x1536 gradient:white-black -rotate -90 -alpha off $T/mask.png  # LEFT
magick -size 1024x1536 gradient:white-black -rotate  90 -alpha off $T/mask.png  # RIGHT
```

`-blur 0xN` sets the feather. **Too hard an edge is the main way these edits get
caught** — N of 20–30 is usually safe over textured ground, more over flat. Lifting
shadows across a large area in a three-or-four-value flat style will posterize; check
for banding at 300%.

**Every coordinate here came from one picture.** Measure your own region and look at
the crop before trusting it — composition shifts between candidates, so a reused box
can silently measure different content.

## Measurement

```bash
magick identify -format '%wx%h  aspect=%[fx:w/h]  %x%U\n' f.png   # size, aspect, density

# mean luminance of a region, 0-255 — the measurement everything else is built on
magick f.png -crop 330x500+60+430 +repage -colorspace Gray \
  -format "%[fx:int(mean*255)]" info:

magick f.png -crop 20x20+230+560 +repage -resize 1x1! \
  -format '%[pixel:p{0,0}]  hex %[hex:p{0,0}]\n' info:          # sample a colour

# edge energy — the SECOND number. Rendering erodes independently of brightness.
magick f.png -crop 330x500+60+430 +repage -colorspace Gray -normalize \
  -morphology Convolve Laplacian:0 -format "%[fx:standard_deviation*1000]" info:

# TRUE count of differing pixels. -precision 10 is REQUIRED — without it %[fx:]
# prints 1.23034e+06 above ~1e6, on exactly the large diffs you care about.
magick a.png b.png -compose difference -composite -colorspace Gray -threshold 0 \
  -precision 10 -format 'differing pixels: %[fx:round(mean*w*h)]\n' info:

magick compare -metric AE   a.png b.png null:   # quantum-scaled, NOT a pixel count:
                                                # use only as a boolean, 0 iff identical
magick compare -metric RMSE a.png b.png null:   # under ~0.01 after a resize
                                                # round-trip is resampling noise
```

**`compare` exits non-zero whenever the images differ.** Under `set -e` or in an `&&`
chain, a working comparison aborts the script. Append `|| true`.

## Tonal and colour operations

```bash
-evaluate multiply 0.74          # scale all values; the precise way to hit a ratio
-brightness-contrast -10x5       # NOT percentages of the mean — a single-digit value
                                 # can move a midtone by a third. Nudge by eye only;
                                 # never use it to hit a measured target.
-gamma 0.9                       # DARKENS midtones; delta scales with the base value
-gamma 1.1                       # BRIGHTENS midtones; neither crushes black or white
-modulate 100,70,100             # brightness,saturation,hue — 70 = desaturate 30%
+level 5%,95%                    # COMPRESSES contrast (-level stretches it); lifts
                                 # blacks, good for haze
```

To hit a measured target use `-evaluate multiply`, factor = `target ÷ current`.

**Avoid `-modulate`'s hue argument for "too magenta".** It rotates *every* hue, so it
drags every other colour along, and the direction is unintuitive — on a `#2D222B`
swatch, `100,100,95` measures `#2D222D`, a barely-visible shift *toward* magenta. Mask
the region and adjust saturation instead.

## Crop, resize, deliverables

`-crop WxH+X+Y` needs `+repage`, or the offset haunts every later operation — an
un-repaged 300x300 crop comes back out of `-flatten` at the original 1536x1024.

```bash
# gen.py's deliverable path: resizes to fit, pads, flattens, checks the size
# budget. It does NOT crop, does NOT set DPI and does NOT recompress.
python3 $S/gen.py --package PKG --refinish OUT/<scene>/vNNN --final-size 2172x1448 \
  --flatten '#ffffff' --max-mb 4

# EVERY command below writes to a NEW path. When the raw output already matches
# --final-size and has no alpha, --refinish writes no file and hands back image.png
# ITSELF — which is frozen history. That is the common case, not the rare one.
magick <in>.png -density 300 -units PixelsPerInch     $T/delivered-300dpi.png
magick <in>.png -colors 128 -define png:color-type=2  $T/reduced.png  # ~half the bytes
magick <in>.png -quality 88                           $T/reduced.jpg  # ~85%, last resort
```

`png:color-type=2` is not optional: `-colors` alone writes an **indexed PNG-8**, not
the truecolor the spec claims. No alpha is involved, so `-alpha off` does nothing
here. `-strip` is not a size fix — nothing on a written deliverable, a few percent on
a raw `image.png`. Reach for `-colors` when a file is over budget.

**DPI verifies in px/cm.** PNG stores density in px/metre, so a successful 300 DPI
stamp reads `118.11 PixelsPerCentimeter` — that *is* 300 DPI. An unstamped PNG prints
`72Undefined`, where `Undefined` means no density, not 72.

## Transplants between candidates

For images without alpha; on a Layer use *Replacing a region of a Layer*, for the same
reason as *Confining an operation to a region*.

Crop the piece, mask it, match its brightness, place it:

```bash
magick donor.png -crop 109x110+29+810 +repage -resize 76x77! $T/piece.png
magick -size 76x77 xc:black -fill white -draw 'ellipse 38,39 37,37 0,360' $T/pmask.png
magick $T/piece.png $T/pmask.png -alpha off -compose CopyOpacity -composite $T/masked.png
magick base.png $T/masked.png -geometry +33+827 -compose over -composite $T/out.png
```

Match the donor's local brightness first, or the transplant reads as a patch.

**The mask boundary is where composites fail.** Diff the region's *edges* against the
baseline, not only the area outside the mask: a boundary crossing a real object edge
imports broken geometry while every outside-mask count still reads 0.

When the base already carries a transplant, subtract that region from the new mask —
multiply by a mask that is BLACK over the region to protect, or you silently overwrite
it:

```bash
magick arch.png protect.png -compose multiply -composite $T/combined.png
```

## Inspection

```bash
# stack two versions at matched scale to compare honestly
magick a.png -resize 760x $T/a2.png && magick b.png -resize 760x $T/b2.png
magick $T/a2.png $T/b2.png -background '#333' -splice 0x6 -append $T/cmp.png
```

Inspect every contested detail at **300–500%** before calling it fixed.

## Layers: alpha-aware recipes

A Layer (`reference/layered-scenes.md`) is an RGBA image, so these keep its alpha.

### Viewing transparency

View a Layer Version or Combined Image over a checkerboard, white and black, cropped to
the contested area and magnified, because a fringe shows only against a contrasting
backdrop and partial transparency only against a pattern:

```bash
F=OUT/<scene>/layers/<layer-id>/vNNN/image.png      # or OUT/<scene>/vNNN/image.png
WH=$(magick identify -format %wx%h "$F")
magick \( -size $WH pattern:checkerboard "$F" -composite \) \
  \( -size $WH xc:white "$F" -composite \) \( -size $WH xc:black "$F" -composite \) \
  -crop 400x300+600+350 +repage -scale 400% -background '#333' -splice 8x0 +append \
  $T/view.png
```

### Measuring alpha

```bash
magick identify -format '%[channels]\n' f.png        # srgba: it has an alpha channel
magick f.png -alpha extract -format 'alpha min %[fx:minima] max %[fx:maxima]\n' info:
magick f.png -alpha extract -threshold 0 -negate \
  -format 'fully transparent: %[fx:mean*100]%%\n' info:
magick f.png -alpha extract -fx 'u>0 && u<1' \
  -format 'partly transparent: %[fx:mean*100]%%\n' info:
```

### Replacing a region of a Layer

This mixes colour and alpha by the mask, premultiplied, so pixels outside the mask stay
unchanged and a feathered edge between two opaque areas stays opaque. Build the mask as
in *Masks*, at the Frame's size, adding `-black-threshold 2%` after `-blur`, because
`layers.py record` counts mask pixels at or below 2% as outside and a blur's faint tail
would make a correct fix warn. `-colorspace sRGB` keeps a grey Layer's colour, and
`-alpha set` gives an image without alpha an opaque one, because `-fx` misreads a
missing alpha channel. Name any `-fx` variable you add with two or more letters, because
single letters such as `m` are channel names.

```bash
START=OUT/<scene>/layers/<layer-id>/vNNN/image.png   # the version being fixed
NEW=OUT/<scene>/layers/<layer-id>/vNNN/image.png     # the donor, e.g. a regeneration
magick \( "$START" -colorspace sRGB \) \( "$NEW" -colorspace sRGB \) \
  \( $T/mask.png -alpha off -colorspace Gray \) -alpha set \
  -fx 'wm=u[2].r; aa=(1-wm)*u.a+wm*v.a; channel(((1-wm)*u.r*u.a+wm*v.r*v.a)/max(aa,1e-9), ((1-wm)*u.g*u.a+wm*v.g*v.a)/max(aa,1e-9), ((1-wm)*u.b*u.a+wm*v.b*v.a)/max(aa,1e-9), 0, aa)' \
  -define png:color-type=6 $T/fixed.png
```

Verify it before recording. `layers.py record ... --mask $T/mask.png --dry-run` warns,
with a count, when any pixel outside the mask changed. This must print 0, or the fix
made opaque content see-through:

```bash
magick $T/fixed.png "$START" "$NEW" -alpha set -fx 'u.a<1 && v.a==1 && u[2].a==1' \
  -alpha off -colorspace Gray -precision 10 \
  -format 'opaque pixels made see-through: %[fx:round(mean*w*h)]\n' info:
```

**Moving or scaling content within a Layer** uses the same recipe. Shift or scale the
whole Layer onto a transparent canvas, then replace the region covering both the old
and the new position, with that image as `NEW`:

```bash
WH=$(magick identify -format %wx%h "$START")
magick -size $WH xc:none "$START" -geometry +30+0 -composite $T/shifted.png
magick -size $WH xc:none \( "$START" -resize 80% \) -geometry +40+20 -composite \
  $T/scaled.png
```

### Grading a Layer

Apply colour operations to the colour channels only, so alpha is untouched:

```bash
magick "$START" -channel RGB -evaluate multiply 0.9 +channel $T/graded.png
```
