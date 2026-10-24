# When the image comes out wrong

Three separate questions, in this order:

1. **Which image do I edit from?** → *Choosing the baseline*
2. **Why did this one fail?** → *Diagnosing a style failure*
3. **The design is right but the rendering is wrong** → *The escalation ladder*

If the fault is small and local and the picture is otherwise good, you may not need
a generation at all — see `reference/fixing-an-image.md` first.

## Choosing the baseline

The baseline is `reference.png` **unless the user has designated a candidate**, which
they do by approving one while asking for a change. They never name the mode, so their
phrasing selects it:

- **"This is close — just fix X"** (approving) → that candidate becomes the
  **designated baseline**. It outranks `reference.png`, whether or not one exists, and
  stays the baseline for the whole series until a promotion resets it. Edit it, and
  state the change *relatively* ("nose more bulbous") — relative language works here
  because the pixels are attached.
- **"Wrong / not him / try again"** (rejecting) → no baseline. Absolutize any usable
  feedback into `description.md` (bump + snapshot) and roll fresh. Do not attach the
  rejected candidate.
- **Ambiguous?** Ask: "keep this one as the base, or start over?" One question beats a
  wasted generation.

Record the designation in `--mode` so the receipt says what this attempt was edited
from.

### Never chain candidates

The edit target is the current baseline, not yesterday's attempt. If the changes since
the baseline are "mustache" and then "silver temples", the next attempt asks for
**both**, from the baseline. Editing an edit compounds drift in whatever direction the
model's priors pull.

### The stale-baseline guard

Before editing `reference.png`, check it is still current. If it predates the design
by more than one or two description versions, or the accumulated unapproved changes
exceed two or three discrete items, an "edit" will behave like a regeneration and lose
the style.

**Stop.** Name the recent candidate that best matches the current design and ask the
user to promote or designate it before continuing.

## Diagnosing a style failure

When the user says a result is off-style — "too detailed", "looks like the source",
"not our style" — **do not re-roll with the same inputs.**

Read the failed attempt's `generation.md` and check what was attached. If any identity
image was attached, assume it dominated the rendering and move DOWN the ladder for the
next attempt: full image → crop → none. Only re-roll unchanged when the previous
inputs were already minimal.

The user reports problems, not remedies. Which images to attach or drop is always your
decision, made from the receipt — they should never have to say.

## The escalation ladder — design right, rendering wrong

The two obvious approaches each fail in a known way, which is why the ladder exists:

- A full off-style sheet attached as IDENTITY makes the model copy its **rendering and
  layout**. The image dominates and "ignore its rendering" loses.
- A text-only generation holds the style but loses the likeness, and over-details from
  the model's own reference-sheet prior.

Work down from 1 and stop at the first rung that works.

**1. Style-transfer repaint (preferred).** Design-correct image as EDIT TARGET, anchor
as STYLE, and command a TOTAL repaint:

> Repaint this entire image in the STYLE image's rendering technique — flatten all
> shading into broad opaque angular planes, coarse dry-brush, limited values. Change
> NOTHING else: preserve layout, poses, facial geometry, hair shapes, and all
> clothing/equipment design exactly.

The edit pathway preserves geometry, so the likeness survives, while the repaint
command replaces the rendering. If the result is still too detailed, retry **from the
same baseline** with stronger flattening language — never edit the edit.

**2. Fresh generation.** STYLE anchor plus description text only. Works when the
description carries the face.

**3. Likeness assist.** Attach a TIGHT FACE CROP, saved to `sources/`, never the full
sheet:

```bash
magick in.png -crop WxH+X+Y +repage out.png
```

Cropping is a copy, so frozen candidates are valid crop sources. **`+repage` is not
optional** — without it the offset is frozen into a `sources/` file you will then
attach.

**4. Converge from the style-true side.** When 1–3 all fail. The model gives you the
design OR the style per call, not both — and small *design* edits on a style-true
image hold the style far better than style repaints hold a design. Designate the best
style-correct candidate as the baseline and fix the design toward the description in
small describable deltas ("lengthen the face, broaden the nose tip"), over two or
three rounds.

**5. Signal-degraded repaint.** For stubborn cases. The repaint fails because the edit
target's fine rendering is high-signal, so weaken it mechanically rather than verbally:

```bash
magick in.png -resize 25% -posterize 5 -resize 400% out.png
```

That flattens it toward the style while keeping contours. Repaint THAT — save the
degraded file to `sources/` and record it as the edit target in the receipt.

### The re-style pass, when the user hands you a drifted candidate

When the user designates an off-style image as the *design* authority: copy it into
`sources/` under a name recording its origin (`design-from-candidate-v008.png`), sync
`description.md` to its design (bump + snapshot), then re-style it with the ladder
above.

**Never DESIGN-edit an off-style image** — "add a mustache" against it preserves its
rendering, which is the problem you are trying to remove.

## Self-check before showing the user

Compare the result against `description.md` — face, hands, equipment count, body
side, clothing — and against the anchor's rendering. If it reads smooth, glossy, or
generically digital, it failed the style check: regenerate before presenting, and
report any remaining discrepancy honestly.
