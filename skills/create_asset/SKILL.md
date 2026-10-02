---
name: create_asset
description: Create or revise a visual asset (reference sheet) for a Rogue Frontier character, NPC, location, item, or faction, keeping the shared visual style locked.
---

# Create or revise an asset's reference sheet

A reference sheet is the canonical picture of one asset. Later, scenes are built by
combining approved sheets, so the sheet must be on-style and on-design before approval.

Always read `gm/image_generation/rules.md` (generation mechanics: the One Rule,
input roles, prompt assembly) and `gm/image_generation/style.md` (the Style Block)
first. Every generation attaches the style anchor, includes the full Style Block
verbatim, and ends with the closing style line — even for a one-word change.

**Never generate, promote, or write a receipt by hand.** Everything below is
executed through `gm/image_generation/bin/`, run from that directory: `prompt.py`
assembles the prompt in the mandated order, `gen.py` validates the One Rule and
writes `image.png` + `generation.md`, `promote.py` copies to `reference.png` with a
verified sidecar. The receipt and sidecar formats described below document what
those tools emit — they are not instructions to type one yourself.
`gen.py --dry-run` checks every invariant for free; run it before any real
generation. See the Tooling section of `rules.md`.

Note: `gen.py --backend codex` shells out to `codex exec`. Running it from inside a
Codex session therefore nests one Codex in another — correct, but it pays the
startup cost twice. Acceptable; do not work around it by generating by hand.

## Folder layout (fixed — never invent new names)

```
gm/image_generation/assets/<type>/<slug>/     type: characters|npcs|ships|locations|items|factions
  reference.png     The ONLY approved image. All future work starts from this file.
  reference.md      Sidecar written by `bin/promote.py` at promotion. Records
                    "Promoted from candidates/vNNN", the user's approval verbatim,
                    the date, and the md5. Resolves the mutable reference.png to
                    its frozen candidate.
  description.md    Current appearance. Single source of truth for the design.
  description_versions/   Frozen history: description-v1.md, description-v2.md ...
  prompt.md         Reusable plain-English sheet prompt (layout + key constraints).
  sources/          User-supplied original assets, untouched.
  candidates/       Work in progress, one folder per attempt:
                      v001/image.png + v001/generation.md
                      v002/image.png + v002/generation.md ...
```

`description.md` is versioned like `style.md`: it carries a "**Description version:
vN**" header line. EVERY design change bumps the version and snapshots the new file
to `description_versions/description-vN.md` before generating. `description_versions/`
is read-only history — never edit or generate from it directly.

Candidate folders: three digits, always increment from the highest existing number,
never reset, never add words to the name (`v007/`, not `v3-mustache-no-chart-v2/`).
Filenames inside are always exactly `image.png` and `generation.md`. The
`generation.md` is the complete, self-contained record of the run — a replay must be
able to reconstruct the entire call from this file alone, even after later
promotions or style bumps. Mutable paths must be resolved to immutable ones:
`reference.png` is recorded as "reference.png (= candidates/vNNN)" using the
`reference.md` sidecar; the anchor as "canonical_style_reference.png (style vN)".

`bin/gen.py` writes `generation.md`. Its shape is fixed by `write_receipt()`; do
not hand-author or edit one. Supply only the fields it cannot infer:
`--request "<the user's ask, verbatim>"`, `--mode "<fresh | edit of which
baseline>"`, `--review "<your post-generation assessment>"`. Everything else —
style version, resolved frozen paths for every attached input, date, status, and
the exact prompt — is filled in from disk.

The prompt must be rebuildable from the versioned inputs alone: Style Block from
`style_versions/style-vN.md` + design text from `description_versions/description-vM.md`
+ the layout/change request recorded in this file. The embedded prompt is the
assembled result; the versioned files are the parts.

## Creating a new asset

1. Write `description.md` with the user from their input and `sources/`. For people:
   face, build, hair, clothing, equipment (exact counts and body sides), posture.
   For places/objects: form, scale, materials, identifying features. Mark invented
   details as provisional; never invent established canon. Header it
   "**Description version: v1**" and snapshot to `description_versions/description-v1.md`.
2. Layout (unless the user specifies one): people get front, three-quarter, profile,
   and back full-body views at consistent scale plus four expression portraits, neutral
   pose, plain gray background, **no height chart** (the shared crew lineup carries
   height comparisons). Ships and objects: useful orthographic angles and detail
   views with a scale cue. Places: establishing view, alternate angles, details.
3. Assemble the prompt with `bin/prompt.py`: `--role STYLE` first, then
   `--role IDENTITY` for each `sources/` image you attach,
   `--design-from assets/<type>/<slug>/description.md`, and `--spec-file` for the
   layout.
   Attach the MINIMUM identity image that carries information the description
   cannot: a full source when the whole design lives in it, a crop when only one
   feature does, nothing once the description suffices. If a candidate resembles a
   source's rendering or layout more than the anchor's, the identity input is
   dominating — describe more, attach less (see the re-style escalation ladder).
4. Generate:
   ```bash
   python3 bin/gen.py --asset <type>/<slug> --prompt-file /tmp/prompt.txt \
     --attach ref_images/style_references/canonical_style_reference.png:STYLE \
     --attach assets/<type>/<slug>/sources/<file>:IDENTITY \
     --request "<verbatim>" --mode "fresh generation"
   ```
   It allocates the next `candidates/vNNN/` itself — never create one by hand, and
   never pick the number yourself.

## Revising an asset — read this before ANY edit

Style drift happens when you take the last output and send a short delta prompt like
"add a mustache". The edit succeeds but the rendering regresses toward generic digital
illustration, because nothing in the call re-asserted the style. Never do that. Instead:

1. **Update `description.md` first.** Merge the requested change into the design text,
   bump its version header, and snapshot to `description_versions/description-vN.md`.
   The description always reflects what the user wants *now* — and must read as if
   written from scratch: translate relative feedback ("nose more bulbous", "forehead
   slightly taller") into ABSOLUTE wording ("large rounded bulbous nose tip", "tall
   forehead"). Never write deltas like "increase X" or "slightly more Y than before"
   into the description — a fresh generation has no "before". The relative phrasing
   belongs only in the generation prompt when an edit target is attached.
2. **Generate from the approved baseline, with the full prompt.** Before using
   `reference.png`, run the Reference validation in `rules.md` (sidecar → real
   candidate → matching bytes); an invalid reference is a HARD STOP, not a
   baseline. Inputs:
   `canonical_style_reference.png` (STYLE) + `reference.png` (EDIT TARGET / IDENTITY).
   Prompt: Style Block + the change request + all other not-yet-approved changes from
   this revision series, expressed together + "keep everything else identical to the
   edit target, and keep all repainted areas in the STYLE image's rendering".
3. **Never chain candidates.** The edit target is the current baseline, not
   yesterday's attempt — if the user's changes since the baseline are "mustache"
   then "silver temples", the next attempt asks for both, from the baseline. The
   baseline is `reference.png` — UNLESS the user has designated a candidate with
   approving feedback ("v020 is close, just fix X"); a user-designated candidate
   ALWAYS takes precedence over `reference.png`, whether or not one exists, and
   stays the baseline for the whole series until a promotion resets it. Record the
   baseline verbatim as the edit target (candidates are already immutable paths).
4. **Stale-baseline guard.** Before editing `reference.png`, check it is still
   current: if it predates the design by more than one or two description versions,
   or the accumulated unapproved changes exceed two or three discrete items, an
   "edit" of it will behave like a regeneration and lose the style. STOP — tell the
   user which recent candidate best matches the current design and ask them to
   promote it (or designate it as baseline) before continuing.
5. **Multi-character sheets** (e.g. the crew lineup): also attach each depicted
   character's current `reference.png` as an IDENTITY input, per the sheet's
   description. Never repaint a face from text alone.
6. If edits keep failing or the style has already drifted, fall back to a full
   regeneration: same STYLE input, `reference.png` as IDENTITY (design only), full
   description in the prompt, no edit target.
7. Save as the next `candidates/vNNN/` folder.

**Re-style pass (design right, rendering wrong).** When the user designates an
off-style image — often a drifted candidate — as the design authority: copy it into
`sources/` with a name recording its origin (e.g. `design-from-candidate-v008.png`),
sync `description.md` to its design (bump + snapshot), then re-style it. Never
DESIGN-edit an off-style image (e.g. "add a mustache" against it) — a design edit
preserves its rendering, which is the problem.

KNOWN FAILURES: (a) attaching a full off-style sheet as IDENTITY to a fresh
generation makes the model copy its rendering and layout — the identity image
dominates and "ignore its rendering" text loses. (b) fresh text-only generation
holds the style but loses the facial likeness, and may still over-detail from the
model's own reference-sheet prior. Escalation ladder:
1. STYLE-TRANSFER REPAINT (preferred): use the design-correct image as the EDIT
   TARGET with the anchor attached as STYLE, and instruct a TOTAL repaint:
   "Repaint this entire image in the STYLE image's rendering technique — flatten
   all shading into broad opaque angular planes, coarse dry-brush, limited values.
   Change NOTHING else: preserve layout, poses, facial geometry, hair shapes, and
   all clothing/equipment design exactly." The edit pathway preserves geometry
   (likeness survives); the repaint command replaces rendering. If the result is
   still too detailed, retry from the SAME baseline with stronger flattening
   language — never edit the edit.
2. Fresh generation: STYLE anchor + description text only. Style-true rolls;
   likeness from text — works when the description carries the face.
3. Likeness assist for fresh generations: attach a TIGHT FACE CROP (saved to
   `sources/`; `magick in.png -crop WxH+X+Y out.png`, or `sips -c`), never the
   full sheet. Frozen candidates are valid crop sources — cropping is a copy.
4. CONVERGE FROM THE STYLE-TRUE SIDE (when 1–3 all fail): the model gives you the
   design OR the style per call, not both — and small DESIGN edits on a style-true
   image hold the style far better than style repaints hold a design. Designate
   the best style-correct candidate as baseline and fix the design toward the
   description in small describable deltas ("lengthen the face, broaden the nose
   tip"), anchor attached as always, over two or three rounds.
5. Signal-degraded repaint (optional tool for stubborn cases): the repaint fails
   because the edit target's fine rendering is high-signal. Weaken it mechanically,
   not verbally: `magick in.png -resize 25% -posterize 5 -resize 400% out.png`
   flattens the target toward the style while keeping contours — then repaint THAT.
   Save the degraded file to `sources/` and record it as the edit target.
Never attach the full off-style sheet as IDENTITY to a fresh generation.

## Self-check before showing the user

Compare the result against `description.md` (face, hands, equipment count, body side,
clothing) and against `canonical_style_reference.png`'s rendering. If it reads as smooth, glossy,
or generically digital, it failed the style check — regenerate before presenting, and
report any remaining discrepancies honestly.

## Interpreting candidate feedback — close vs. wrong

The user's phrasing selects the generation mode; they never name it:

- **"This is close — just fix X"** (approving tone, small change): the candidate
  they're reacting to becomes the DESIGNATED BASELINE. Edit it: baseline as EDIT
  TARGET, anchor as STYLE, the change stated relatively ("nose more bulbous") —
  relative language works here because the pixels are attached. Later tweaks
  re-edit the SAME baseline with all accumulated changes; never edit an edit.
- **"Wrong / not him / try again"** (rejecting tone): no baseline. Absolutize any
  usable feedback into `description.md` (bump + snapshot) and roll fresh from the
  description. Do not attach the rejected candidate.
- **Style complaints** ("too detailed", "looks like the source"): see the next
  section — diagnose inputs, move down the escalation ladder.
- Ambiguous? Prefer asking "keep this one as the base, or start over?" — one
  question beats a wasted generation.

Every edit pass still obeys the One Rule, and the self-check still applies: if an
edit drifts the rendering, catch it before presenting.

## Reacting to style failures — the user reports problems, not remedies

When the user says a result is off-style ("too detailed", "looks like the source",
"not our style"), do NOT simply re-roll with the same inputs. Diagnose first: read
the failed attempt's `generation.md` and check what was attached. If any identity
image was attached, assume it dominated the rendering and move DOWN the escalation
ladder (full image → crop → none) for the next attempt. Only re-roll with unchanged
inputs when the previous attempt's inputs were already minimal. The user should
never have to say which images to attach or drop — that decision is always yours,
made from the receipt and the ladder.

## Approval

When the user approves a candidate:

1. ```bash
   python3 bin/promote.py assets/<type>/<slug>/candidates/vNNN \
     --approval "<the user's words, verbatim>"
   ```
   It copies `image.png` to `reference.png`, writes `reference.md`, re-verifies
   byte-identity, and updates the candidate's receipt status. It refuses to
   overwrite an existing `reference.png` without `--replace`; pass that only when
   the user approved superseding the current one. NEVER copy these files by hand —
   an unverified promotion produces a `reference.png` that `gen.py` will reject on
   every future generation, from any agent. `description.md` is NOT touched by
   promotion — it holds design only, never status or provenance.
2. Confirm `description.md` and `prompt.md` match the approved image.
3. `candidates/` is permanent history — never delete candidates, even rejected ones
   and even if asked casually; deletion destroys receipts and breaks numbering.
   If the user insists after being warned, record the removed numbers in
   `candidates/DELETED.md` — numbers are NEVER reused, so the next candidate
   continues from the highest number ever used (check `DELETED.md`), not the
   highest surviving folder.

Do not commit automatically.
