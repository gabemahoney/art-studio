# Fixing an existing image

Routes a correction to the cheapest tool that can do it. Commands are in
`reference/imagemagick.md`.

## 1. Diagnose

Zoom the fault to 300–500% and name the actual shape on the canvas. The user's words
describe a symptom: a garment reported as "the wrong jacket" is often the right jacket
painted badly.

If the fault is in the design itself, update `description.md` too — a pixel fix
changes this image, but the next generation reads the text.

## 2. Pick a path

| | path | cost |
|---|---|---|
| 1 | ImageMagick | free |
| 2 | Regeneration | subscription |
| 3 | Regenerate, then composite the fixed region onto the original | subscription |
| 4 | Masked inpainting via the API | paid credits |

ImageMagick rearranges pixels that already exist; regeneration invents new ones.

| the change | path |
|---|---|
| Brightness, contrast, saturation, colour balance | 1 |
| Resize, pad, deliverable (`gen.py --refinish <vNNN dir>`) | 1 |
| Crop, DPI, shrink an over-budget file | 1 |
| Remove something over flat, adjacent texture | 1 |
| Move a correct region from one candidate to another | 1 (transplant) |
| Wrong aspect ratio | 2, with the ratio stated in the prompt body |
| Pose, expression, added objects, geometry, revealing what's behind something | 2, then 3 |
| Wrong or badly drawn lettering | 2, then 3 |
| A small region that keeps breaking | 3, then 4 |
| Rendering softened over several passes | 1 — transplant from an earlier, crisper version |
| A detail under ~30 px that won't come out right | change the design to a shape whose silhouette reads |

## Path 1 — ImageMagick

Confine any whole-image operation to a region with a mask (recipe in
`imagemagick.md`). Keep intermediates in a scratch directory.

State tonal targets as a ratio — mean of region A ÷ mean of region B — and record the
crop boxes with the number so it can be reproduced.

## Path 2 — Regeneration

Every pass repaints the whole frame, even when the prompt says "change only X", and
errors accumulate in one direction (likenesses drift, distinguishing features fade,
subjects in shadow get brighter, crisp edges
soften). After each pass, measure brightness and edge energy for the regions that
matter. A tonal fix restores brightness but not crispness; only new pixels restore
crispness.

## Path 3 — Regenerate and composite

The default ending for every regeneration aimed at one region (see *The core rule* in
`SKILL.md` — every pass repaints the whole frame):

1. Regenerate, aimed at the region, with the reference of every asset in frame attached.
2. Mask just the fixed region and composite it onto the last approved image.

Mask edges must follow real boundaries in the picture (see *Masks and composites* in
`SKILL.md`). Save a kept composite as its own `vNNN` with a hand-written
`generation.md` that opens `Source: local composite, no generation` and names the base,
the donor, the mask and the commands.

## Path 4 — Paid masked inpainting

Only the masked pixels regenerate. Use it when regeneration keeps getting a region
wrong, and ask the user every time (see *Backends and cost* in `SKILL.md`). Works best
on a single surface whose mask edges sit on real boundaries.

```bash
python3 bin/prompt.py --masked \
  --role "EDIT TARGET" --role STYLE \
  --task "..." --spec-file $T/spec.txt -o $T/p.txt

python3 bin/gen.py --scene <slug> --prompt-file $T/p.txt --backend api \
  --attach outputs/<slug>/vNNN/image.png:"EDIT TARGET" \
  --attach ref_images/style_references/canonical_style_reference.png:STYLE \
  --mask tmp/mask.png --size <WxH of the edit target> \
  --approved-by "<the user's yes, verbatim>"
```

- The EDIT TARGET goes first here — the API applies the mask to the first image.
- The mask is greyscale, same size as the EDIT TARGET, **white = repaint**. `gen.py`
  converts it to the API's format.
- The mask must be inside the project folder (`tmp/` is fine).
- Run `--dry-run` first, then ask; `gen.py` refuses a paid call without `--approved-by`.
- The unmasked area comes back re-encoded; paste the masked region back onto the
  original to keep the rest byte-identical.
