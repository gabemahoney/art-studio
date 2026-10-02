---
name: illustrate
description: Generate a Rogue Frontier scene from approved asset reference sheets, keeping the shared visual style locked.
---

# Illustrate a scene

Scenes combine assets that already have approved reference sheets. If a requested
asset has no `reference.png` yet — or its reference fails the validation in
`rules.md` (sidecar present, pointing at a real candidate, bytes matching) — stop
and tell the user which asset needs promotion first (or that it will be improvised
and off-canon).

Always read `gm/image_generation/rules.md` (generation mechanics: the One Rule,
input roles, prompt assembly) and `gm/image_generation/style.md` (the Style Block)
first. Every generation attaches the style anchor, includes the full Style Block
verbatim, and ends with the closing style line — even for a one-word revision.

**Never generate, promote, or write a receipt by hand.** Everything below is
executed through `gm/image_generation/bin/`, run from that directory: `prompt.py`
assembles the prompt in the mandated order, `gen.py` validates the One Rule and
writes `image.png` + `generation.md`, `promote.py` copies to `final.png` with a
verified sidecar. The receipt format described below documents what those tools
emit — it is not an instruction to type one yourself. `gen.py --dry-run` checks
every invariant for free; run it before any real generation. See the Tooling
section of `rules.md`.

Note: `gen.py --backend codex` shells out to `codex exec`. Running it from inside a
Codex session therefore nests one Codex in another — correct, but it pays the
startup cost twice. Acceptable; do not work around it by generating by hand.

## Folder layout (fixed — never invent new names)

```
gm/image_generation/outputs/<scene-slug>/       one folder per scene
  v001/image.png + v001/generation.md           one folder per attempt
  v002/image.png + v002/generation.md ...
  final.png + final.md                          the user-approved version and its
                                                sidecar, both written by promote.py
```

Scene slug: short kebab-case describing the scene (`antares-cockpit`,
`kalagra-crater-city-cover`). Session scenes go in `outputs/session-<NN>/<scene-slug>/`.
Attempt folders: three digits, increment from the highest existing, never reset, never
add words to the name. Filenames inside are always exactly `image.png` and `generation.md`. `bin/gen.py` writes `generation.md`, the complete self-contained record of the run
— a replay must be able to reconstruct the entire call from that file alone. Its
shape is fixed by `write_receipt()`; do not hand-author or edit one. Supply only
the fields it cannot infer: `--request "<the user's ask, verbatim>"`,
`--mode "<fresh | edit of which baseline>"`, `--review "<your assessment>"`.

## Building a scene

1. Establish setting, cast, and action from the user's request and campaign records.
   Ask only when a missing detail materially affects the image. Choose a focal
   asset, a concrete moment, and a composition suited to the requested format.
2. Read each cast member's `assets/<type>/<slug>/description.md`.
3. Inputs: `canonical_style_reference.png` (STYLE) + each cast member's `reference.png`
   (IDENTITY, one per asset; keep the cast small enough that each stays
   recognizable). No other style inputs — ships and locations also take their
   design from their own reference sheets and their rendering from the anchor.
   Include only requested assets.
4. Prompt, in order: Style Block + per-asset identity summary (2–3 sentences each,
   distilled from `description.md`: face, build, clothing, equipment with body sides)
   + scene specification (action, pose, expression, setting, light, framing).
5. Generate one image per run:
   ```bash
   python3 bin/gen.py --scene <scene-slug> --prompt-file /tmp/prompt.txt \
     --preset book-float \
     --attach ref_images/style_references/canonical_style_reference.png:STYLE \
     --attach assets/<type>/<slug>/reference.png:IDENTITY \
     --request "<verbatim>" --mode "<fresh | edit of vNNN>"
   ```
   It allocates the next `vNNN/` only after a successful response, so a failure
   leaves no empty folder. Repeat `--attach` once per cast member, in the order the
   prompt's "Image N is..." lines declare them — position is the only binding the
   image model honors.

## Revising a scene

Same anti-drift protocol as reference sheets:

- Never send a bare delta edit against the last output. Every revision call attaches
  `canonical_style_reference.png` (STYLE) and includes the full Style Block.
- Pick one user-liked version as the series baseline (EDIT TARGET) and express ALL
  accumulated changes against it in each attempt. Never chain: v005 edits the
  baseline with every retained change restated, not v004.
- If a change alters an asset's *design* (not just this scene), update that
  asset's `description.md` too (bump the version header, snapshot to
  `description_versions/`), and note that the reference sheet needs a
  matching revision.
- For strictly local fixes (recolor one garment, fix one hand), an edit against the
  baseline is fine — but the STYLE input and Style Block still go in the call, with
  "repaint only X; all repainted marks match the STYLE image's rendering".

## Self-check before showing the user

Verify each asset against their `description.md` (face, hands, equipment count,
body side) and verify the rendering against `canonical_style_reference.png`. If it reads smooth,
glossy, or generically digital, regenerate before presenting; report remaining
discrepancies honestly.

When the user approves a version:

```bash
python3 bin/promote.py outputs/<scene-slug>/vNNN --approval "<the user's words, verbatim>"
```

It writes `final.png` AND `final.md`, the sidecar recording which attempt it came
from, then re-verifies byte-identity. Never copy by hand: a scene with a
`final.png` and no `final.md` has no provenance.
Do not commit automatically.
