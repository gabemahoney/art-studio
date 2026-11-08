# Fixing an existing image

`SKILL.md` covers how images are *made*. This covers how they are *changed*, and its
job is to route a correction to the cheapest tool that can do it. Read it **before**
spending a generation on a fix.

`reference/imagemagick.md` has the commands. `S`, `T`, `PKG` and `OUT` are as in
`SKILL.md`.

## Step 0 — Diagnose before you route

**Magnify the fault to 300–500% and name the actual shape on the canvas**, then route
the fault you can see, not the one you were told about, because the user's words
report a symptom (`SKILL.md` → *Two habits worth building*).

**If the fault is a design fact, the fix must go back into `description.md`.** A pixel
edit teaches the model nothing — the next scene reads the text and repaints the
original error. ImageMagick changes the deliverable; only the text changes what the
asset *is*. Snapshot to `description_versions/` when the design itself moves.

## The four paths, cheapest first

**Credits are the last resort, not one of four equal options.** Work down the list
and stop at the first path that can do the job.

| | path | cost |
|---|---|---|
| 1 | **ImageMagick** — exact, provably zero change outside a mask | free |
| 2 | **Codex regeneration** | subscription |
| 3 | **Generate-and-composite** — one Codex call plus local surgery | subscription |
| 4 | **API inpainting** — the only true targeted repaint here | real money |

### Route by what the change actually is

**ImageMagick can only rearrange pixels that already exist; regeneration invents
them.** Most routing follows from that one line. The table is for the cases where it
does not.

| the change | path | why |
|---|---|---|
| Brightness, contrast, saturation, colour balance | **ImageMagick** | Exact, free, works when Codex is down. Never regenerate or pay for this. |
| Resize, pad, print deliverable | **ImageMagick** (`gen.py --refinish`) | Upscales to ~1.5x are invisible in this flat matte style. |
| Crop, set DPI, shrink an over-budget file | **ImageMagick**, by hand | `--refinish` does none of the three — it only *warns* about size. |
| Wrong aspect ratio came back | **Regenerate**, stating the ratio in the prompt body | `--size` is advisory on Codex; `--refinish` would just pad it. |
| Remove something whose covering texture is flat and adjacent | **ImageMagick** | Clone from the same image. |
| Move a *correct* region from one candidate to another | **ImageMagick** | See `reference/imagemagick.md` → *Transplants between candidates*. |
| Tighter crop from pixels already present | **ImageMagick** | Crop, then upscale. |
| Pose, expression, added objects, architecture, geometry; removing something that reveals structure or that a figure overlaps; any reframe revealing content outside the frame | **Regenerate, then path 3** | Those pixels do not exist — but a regeneration repaints the whole frame, so take only the region you asked for. |
| Wrong, misspelled or badly drawn **text/lettering** | **Regenerate**, then path 3 | ImageMagick cannot author glyphs in style. Fix spelling and typeface in the prompt. |
| A small region regeneration keeps breaking | **Path 3**, then **path 4** | Path 3 is free and usually enough; if its seam cannot be hidden, inpainting is the escalation — ask first. |
| Rendering eroded across passes (facets rounding off) | **ImageMagick transplant** from an un-eroded version | Tonal correction cannot restore crispness; only new pixels can. |
| A detail below ~30 px that will not converge | **Change the gesture** | Orientation is uncontrollable at that size. Pick a shape whose silhouette carries the meaning. |
| Codex returns HTTP 400 | **Path 4 → *The bar*, Codex unavailable** | That model just died; see `rules.md` → *Codex models*. |

## Path 1 — ImageMagick

**Any whole-image operation can be confined to a region** by making an adjusted copy,
giving it the mask as its alpha, and laying it over the original. The recipe,
including the `-alpha off` trap that keeps recurring, is in
`reference/imagemagick.md` → *Confining an operation to a region*.

**Every intermediate goes to `$T`, never the package or the output folder**, except the
one kind listed under *Guardrails*.

**State tonal targets as a ratio** — mean of region A ÷ mean of region B. Ratios
survive rephrasing; "a bit darker" does not. **Record both crop boxes every time you
quote a ratio**, or the number cannot be reproduced; most older receipts omit them,
which is why their measurements are now unusable. Reuse whatever boxes a scene has
already established — its receipts name them — or the series stops being comparable
with its own history.

## Path 2 — Codex regeneration, and its hidden cost

**Every edit pass repaints the entire frame.** "Change only X" is an approximation
recomputed from scratch, so errors accumulate in whatever direction the model's priors
pull — and they accumulate *monotonically*, because the pull is in one direction. A
freeze instruction does not stop it. Shadowed subjects drift brighter pass after pass,
because the model pulls toward legible subjects.

**Re-measure after every pass, and measure two numbers, not one.** Brightness drifts,
and so does rendering: the flat angular facets round off a few percent per generation
— invisible at any single magnification because it is gradual, and compounding into a
visibly softer image over several passes. Edge energy is the second number
(`reference/imagemagick.md` → *Measurement*).

**A tonal correction never restores rendering.** Brightness and crispness are
independent, so an eroded image measures perfectly clean on the ratio alone. Only new
pixels bring crispness back: if edge energy has fallen, composite the region from an
un-eroded version. Noting the drop in a receipt is not fixing it.

**Never enumerate colours inside a freeze instruction.** Naming six coloured garments
while asking to keep "depth of shadow" says *make six things identifiable*, and
brightness wins a little each pass. State the ratio as a number instead.

## Path 3 — Generate-and-composite (inpainting without credits)

**This is the default ending for every regeneration, not a fallback.** Treat the model
as a source of shapes, never of finished frames: regenerate for geometry, then keep
only the shape you asked for.

1. Regenerate normally through `prompt.py` + `gen.py`, aimed at that region.
   Accept that the rest of the frame drifts.
2. Mask **only** the fixed region out of the new candidate.
3. Composite it onto the good baseline.

**Do not wait for a freeze instruction to fail.** Freezes routinely hold — you verify
them, they are intact — while the pass still costs you the picture, because a
regeneration rewrites a large fraction of the frame whether or not your spec mentioned
it. The damage lands in whatever you did not think to name. Take the region and the
rest stays byte-identical; adopt the whole frame and every untouched thing in it
quietly degrades, a little per pass, with nothing to restore it.

The trigger is not "the freeze failed". The trigger is **"I am regenerating."**

Works when the region is interior and its surroundings hide a feathered seam. Fails
when the fix changes a silhouette against a busy background, or must align with
something the new candidate drew differently.

## Path 4 — The paid API, and the bar for spending credits

**Ask the user first, every time** (`rules.md` → *Paid calls need the user's
approval*). One approval is one call, and changing anything needs a fresh one, because
a blanket authorisation is not a yes to a specific call. When you ask, give what you
tried, why the cheaper paths cannot do it, which `--quality` you chose, the mask
coverage `gen.py --dry-run` prints, and the cost as an estimate.

**What this path buys you:** `--mask` sends a mask to `/v1/images/edits` and **only
the masked pixels regenerate**. Codex cannot inpaint; path 3 only approximates it.

```bash
python3 $S/prompt.py --package PKG --masked \
  --role "EDIT TARGET:The image being repaired." \
  --role STYLE:"Match its hand-painted matte rendering only." \
  --task "..." --spec-file "$T/spec.txt" -o "$T/p.txt"

python3 $S/gen.py --package PKG --output OUT --scene <scene> --prompt-file "$T/p.txt" \
  --backend api --approved-by "<the user's words>" \
  --attach <scene>/vNNN/image.png:"EDIT TARGET" \
  --attach ref_images/style_references/canonical_style_reference.png:STYLE \
  --mask OUT/<scene>/masks/fix-the-hand.png --size 1536x1024
```

Copy that invocation's order exactly: the EDIT TARGET goes first, because the endpoint
masks image 1. Pass `--size` as the EDIT TARGET's real size from `magick identify`, not
the 1536x1024 above. Check the mask is WHITE = repaint and not pre-inverted yourself,
because `gen.py` cannot detect polarity and an inverted mask pays to repaint
everything except the region you meant. `rules.md` → *Masked inpainting* has the
reasons and the rest of the guards.

**Try path 3 first** — free, and it hides most seams.

### The bar

Propose credits only if one of these holds. If none does, do not raise it at all — go
back to paths 1–3. Then still ask.

- An **exact native pixel size** is needed and the upscale would exceed ~1.5x.
- A **small region** survived path 3 and its seam cannot be hidden.
- **Codex is genuinely unavailable.** `rules.md` → *Codex models* lists what is left;
  there is currently one working model, so "try another model" is not a step. Retry
  once, check `~/.codex/auth.json` exists, then add the dead model to
  `CODEX_MODELS_BROKEN`, update that table, and say plainly that Codex is down.

**Never for:** tonal or colour work, crops and resizes under ~1.5x, transplants, a
first or second attempt at anything, or framing and composition changes — a mask
cannot help when the whole frame has to move.

## Guardrails

- **Everything already written is frozen** — `image.png`, and any promoted
  `reference.png` or `final.png`. Never edit one in place and never open one in an
  image editor. Annotate a scratchpad copy; correct in a new `vNNN` and promote that,
  with `--replace` if a head already exists.
- **Intermediates go to the scratchpad**, with one exception: a mask that a receipt
  cites (a composite's, or a paid call's `--mask`) is kept beside that scene in the
  output folder — `OUT/<scene>/masks/` — so the receipt stays reproducible.
- **A composite you intend to keep needs its own `vNNN`**, numbered past every existing
  folder and every number in `DELETED.md`, with the image as `image.png` and a
  hand-written `generation.md`, because `promote.py` and `--refinish` read no other
  filenames. **That receipt must open by saying no model was called**
  (`Source: local composite, no generation`), then name the baseline `vNNN`, the donor
  `vNNN` and the commands. Without it, a composite attached to a later generation
  passes the provenance check silently and enters the record as model history.
  Throwaways go to the scratchpad instead.
- **Do not record a local correction with `review.py --replace`.** It overwrites the
  `Review:` line, which by then is the one that caught the fault. Put the note in the
  new candidate's receipt.
- **A damaged candidate is sometimes recoverable — check its receipt.** `git checkout`
  only helps if the folder holding it is in git. What may survive is the `codex source`
  path under `~/.codex/generated_images/` recorded in `generation.md` — but **only
  generated candidates have one. A local composite has no upstream copy and cannot be
  recovered at all.**
- **Never silently substitute a worse fix.** Say what is blocked, and carry on with
  the rest.
