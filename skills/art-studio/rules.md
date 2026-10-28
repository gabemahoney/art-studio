# Generation rules

Mechanics for EVERY image generation, in both skills. `style.md` defines what the
style IS; this file defines how generations run. Read both before any generation.

## Package and output

Every command is told where to work. There is no config file, no environment override
and no default location: a silent fallback is how renders end up somewhere nobody meant.

| | |
|---|---|
| **`--package PKG`** | one project's look and subjects: `style.md`, the anchor, `style_versions/`, `presets.json`, `assets/` |
| **`--output OUT`** | where scene renders are delivered: `OUT/<scene>/vNNN/{image.png, generation.md}` |

- **Asset work writes into the package** (`--asset <type>/<slug>` →
  `PKG/assets/<type>/<slug>/candidates/vNNN/`), because it is changing the package.
- **A scene render never writes into the package.** It reads the style and assets and
  writes only under `OUT`, so one package can feed many output folders — and two repos
  rendering from the same package at once cannot collide. `gen.py` refuses an `OUT`
  that overlaps `PKG`, and refuses `--output` together with `--asset`.
- Text and image sit side by side: each `vNNN/` holds its `image.png` and its
  `generation.md`. Whether either location is in git is the project's business.
- Relative `--attach` and `--mask` paths resolve against the package, then the output
  folder; a path present in both is refused as ambiguous. Receipts write paths as
  `package:<rel>`, `output:<rel>`, or absolute.
- `vNNN` is allocated after a successful response, so a failure leaves no empty folder.

## The One Rule (prevents style drift)

Every image-generation call — new artwork, revisions, and *especially* tiny edits —
must do ALL of these:

1. Attach the current style anchor `ref_images/style_references/canonical_style_reference.png`
   as a style-only input, labeled as such in the prompt — and, with the single
   exception of a masked API call (see *Masked inpainting*), ALWAYS as the FIRST
   attached image, so that "image 1" in any prompt unambiguously means the anchor.
2. Include the full Style Block from `style.md`, verbatim, at the TOP of the prompt.
3. End the prompt with the closing style line exactly as `style.md` states it.
   `style.md` is the single authority for that wording; it is quoted here only by
   reference so the two files cannot drift apart again.
4. Deliver the prompt to the image model **byte-for-byte**. No agent, wrapper or
   tool may paraphrase, "normalize", summarize or expand it on the way.

Style is never inherited from a previous output; it is re-asserted on every call.
If a call skips any part, the result is invalid — regenerate.

### Why #4 exists

Codex CLI's built-in `image_gen` rewrites prompts by default. Its skill doc
(`~/.codex/skills/.system/imagegen/SKILL.md`, step 9) instructs the model to "normalize
it into a clear spec", and session logs confirm it: a nine-word test prompt reached the
tool as a 60-word spec with invented constraints. The One Rule works only if the Style
Block arrives verbatim, so an LLM paraphrasing it in transit defeats the entire
anti-drift mechanism — silently, with no error.

`gen.py --backend codex` defeats this structurally rather than by asking nicely: the
prompt is written to a file, and Codex is told to read it with `fs.readFileSync` inside
its code-mode exec block and pass those bytes straight to the tool argument. The text
goes disk → shell → tool, never through model output tokens, so paraphrasing is
impossible. Verified on a real run: the model's entire output was 313 characters, and the
Style Block appears nowhere in model-authored content.

Consequence for history: `## Exact prompt` in receipts written before 2026-09-28 records
what was handed to Codex, not what the image model saw. Treat those as approximate.

## Image input roles

**Assembly order, because style must dominate:** Style Block FIRST, then the image
roles, then the `TASK:` line, then design text, then layout/scene spec, then the closing
style line LAST — roles go at the top of the prompt *body*, never above the Block. Design wording names materials
and colors, not finish — the Style Block owns finish.

Declare every attached image at the top of the prompt by NUMBER and exactly one
role ("Image 1 is STYLE... Image 2 is IDENTITY...") — position is the only binding
the image model reliably understands; filenames may be added alongside the number
but never replace it:

- **STYLE** — the anchor. "Match this image's rendering technique only. Ignore its
  people, clothing, equipment, and setting."
- **IDENTITY** — an asset's approved `reference.png`, or `sources/` originals for a
  new asset. "Copy this asset's design: face, build, clothing, equipment, colors.
  Ignore this image's rendering."
- **EDIT TARGET** — the image being modified (an approved `reference.png`, or a
  user-designated baseline); what "preserve everything else" refers to. "This is the
  image being modified. Preserve everything the prompt does not change."

Rules:

- Attach the minimum identity image that carries information the design text
  cannot: full source, crop, or nothing (see the `art-studio` skill's escalation
  ladder).
- IDENTITY inputs are approved `reference.png` files or `sources/` originals —
  never an unapproved candidate, except as a user-designated baseline or a crop
  source. Chaining candidate outputs compounds drift.
- Ignore borders, captions, signatures, and screenshot chrome in any reference.

## Reference validation (hard stop)

Before attaching ANY asset's `reference.png` to a generation, validate it:

1. `reference.md` exists beside it and its first line reads "Promoted from
   candidates/vNNN". `gen.py` searches the whole sidecar for `candidates/vNNN` and takes
   the first match anywhere in it, not just on line 1 — so never write another `vNNN`
   path above the provenance line. `promote.py` also writes the
   approval verbatim, the date and an md5, but sidecars predating it are one line
   and remain valid.
2. That `candidates/vNNN/` folder exists and contains `image.png` + `generation.md`.
3. `reference.png` is byte-identical to that candidate's `image.png`
   (`md5 -q` both files and compare).

If ANY check fails, the reference is INVALID — treat the asset as unapproved. Do
not attach it, do not work around it, do not guess. Stop and tell the user exactly
which check failed and which recent candidate could be promoted to fix it. A
reference with no provenance or mismatched bytes is how stale baselines and silent
overwrites sneak in.

## Style versioning procedure

`style.md` is the mutable head revision of the style. Before changing the Style
Block, **either closing style line**, or replacing the anchor image: confirm the current version is frozen in
`style_versions/` (style-v<N>.md + canonical_style_reference-v<N>.png), make the
change, bump the version header, add a changelog line, freeze the new version.
Replacing the anchor image IS a style change. `style_versions/` is read-only
history — never edit or attach from it, and never re-freeze a version to match later
edits. **Only three things are versioned: the Style Block, both closing style lines, and
the anchor image.** Explanatory prose in `style.md` may therefore differ from the frozen
copy without being drift — `gen.py` compares exactly that subset before every call, and a mismatch
there is real. Every `generation.md` records the style
version it ran under and embeds the exact prompt.

## Tooling

The scripts in this skill's `scripts/` folder enforce everything above. Stdlib only — no
venv, no `poetry install`. Run them from anywhere; locations come from the arguments.
Below, `S` is this skill's `scripts/` directory.

### `prompt.py` — assemble the prompt

Emits the sections in the mandated order (Style Block, image roles by number,
design text, scene spec, closing line). Never hand-write a prompt: that is how
the Style Block drifts and the closing line gets paraphrased.

```bash
python3 $S/prompt.py --package PKG \
  --role STYLE:"Match its hand-painted matte rendering only. Ignore its subjects." \
  --role IDENTITY:"Copy this asset's design exactly. Ignore its sheet layout." \
  --task "A single horizontal three-quarter view against a plain background." \
  --design-from assets/<type>/<slug>/description.md --design-section Exterior \
  --spec-file /tmp/framing.txt -o /tmp/prompt.txt
```

`--role` is repeatable and **in attachment order**; image 1 must be STYLE. Omit
the text after the colon to get the standard role wording from this file.

### `gen.py` — generate one candidate

Refuses to run before anything is billed: on any One Rule violation (anchor not first
as STYLE, Style Block not verbatim, no closing style line), on a `reference.png` failing
validation, and on the live anchor differing from its frozen `style_versions/` copy.
**That list goes stale; `selftest.py`'s cases are the authoritative enumeration** —
they also cover the five-attachment cap, a doubled anchor, a dead model, and every mask
guard. One exception to #3: a short list of **legacy closing-line wordings is accepted on
an ordinary call with a warning**, because old receipts used them — but refused outright on
a masked call, where naming "image 1" would point at the picture being repainted.
Allocates `vNNN` only after a successful response, so a failure leaves no empty
folders. Writes `image.png` (raw, frozen), the deliverable,
and a complete `generation.md`.

```bash
python3 $S/gen.py --package PKG --output OUT --scene <slug> \
  --prompt-file /tmp/prompt.txt --preset <name> \
  --attach ref_images/style_references/canonical_style_reference.png:STYLE \
  --attach assets/<type>/<slug>/reference.png:IDENTITY \
  --request "<user's words, verbatim>" --mode "<what this attempt changes>"
```

Use `--asset <type>/<slug>` (and no `--output`) instead of `--scene` for asset candidates, and
`--dry-run` to check invariants for free. `--refinish <vNNN dir>` re-derives a
deliverable from an existing `image.png` without generating anything.

**Presets** name a delivery spec once, in the package's optional `presets.json`:

```json
{"page-float": {"final_size": "1536x1024", "flatten": "#ffffff", "max_mb": 2.5}}
```

A preset also sets the *requested* size to its own
aspect, so the deliverable is full-bleed rather than padded. The deliverable is
always scaled to FIT and padded, never cropped — no hull is ever cut off to
satisfy a box.

### `review.py` — record the assessment
```bash
python3 $S/review.py OUT/<scene>/v002 --review "<what you see, misses included>"
```
Sets the `Review` line `gen.py` leaves as a placeholder. Refuses to
overwrite an existing review without `--replace`.

### The two post-hoc fields

A receipt is frozen history with exactly two exceptions, because both are known
only AFTER the run:

- **`Status`** — owned by `promote.py`, set when the user approves.
- **`Review`** — owned by `review.py`, set once you have looked at the image.

`gen.py` runs before the image exists, so it cannot take the review; it writes
a placeholder. Fill it with `python3 $S/review.py <vNNN dir> --review "..."`. Editing
any other field of a receipt, or editing these two by hand, is still forbidden.

### `promote.py` — approve a candidate

```bash
python3 $S/promote.py OUT/<scene>/v002 --approval "<user's words, verbatim>"
```

Both take the `vNNN` directory's path and read its kind from the path: a `vNNN` under
`candidates/` is an asset candidate, anything else a scene version.

Copies `image.png` to `reference.png` (assets) or `final.png` (scenes), writes the
sidecar recording which `vNNN` it came from, re-verifies byte-identity after the
copy, and updates the candidate's receipt status. Refuses to overwrite an existing
head revision without `--replace`.

## Backends

| | `--backend codex` (default) | `--backend api` |
|---|---|---|
| Pays with | the ChatGPT/Codex subscription | prepaid OpenAI API credits |
| Image model | not exposed by the tool | pinned, e.g. `gpt-image-2.5-sunburst-2026-09-08` |
| Prompt integrity | verbatim via the disk relay | verbatim by construction |
| Requested size | the **shape** is followed, the pixel count is not (asked 1568x896, got 1659x948: exactly 7:4, 2026-10-24) — use `--final-size` for exact pixels | honored |
| Targeted repaint | not possible | **yes — `--mask`, only those pixels regenerate** |

A ChatGPT/Codex subscription does **not** fund API keys; they are separately
billed products. No call has yet completed on this backend, so every cost figure here
is arithmetic, not measurement. The first real call's `Token usage:` receipt line
replaces the estimate with a fact.

#### Masked inpainting

`--backend api --mask PATH` repaints only the masked pixels. The mask is an ordinary
mask — greyscale, **WHITE = the region to repaint**, same dimensions as the EDIT
TARGET attachment. `gen.py` converts it to the API's alpha convention (transparent =
repaint) itself, so **never pre-invert**: backwards repaints everything except the region
you meant, at full cost, and nothing detects it — the only polarity check is a refusal of
an all-black mask plus a warning above 90% coverage.

**A masked call inverts One Rule #1, and it is the only thing that may.**
`/v1/images/edits` applies the mask to the FIRST image in `image[]`, so the EDIT TARGET
must be attached first and the anchor second. With the anchor first the mask lands on the
anchor: you pay, and you get the anchor back with a hole repainted in it, with no error —
the anchor and a scene candidate are both 1536x1024, so the endpoint's dimension check
passes. `check_inputs()` enforces the inversion for masked calls and keeps the normal rule
everywhere else. The Style Block still reaches the model verbatim, and only masked pixels
regenerate, so the target's surrounding pixels carry the rendering.

Build the prompt with `prompt.py --masked`: it puts the EDIT TARGET first and emits
the masked closing style line from `style.md`, which names the anchor by role rather than
by index. `check_prompt()` requires the matching line for the call type and refuses either
mismatch, so a prompt that contradicts its own payload cannot be sent.

**`--quality` defaults to `high`** (`low`/`medium`/`high`/`xhigh`/`max`/`auto`) and is the
cost lever inside the $0.05–0.35 estimate — it reaches the receipt, so say which you
chose when you ask. `--size` must equal the EDIT TARGET's own
dimensions, since the mask is aligned to that
image; it defaults to 1536x1024, which is wrong for portrait and oversized
candidates, so read the real size with `magick identify` and pass it.

The call also fails closed on an alpha-carrying mask, a dimension or `--size` mismatch,
more than one EDIT TARGET, and `--backend codex` (which cannot
inpaint — use Path 3). It prints the share of the frame the mask covers; give that figure
when you ask, so the user sees what they are paying to repaint. The
result is re-encoded: the unmasked area is visually preserved but not byte-identical.

**No masked call has completed here.** The semantics above are from the API reference, not
measurement — verify on the first real call that what comes back is the EDIT TARGET with
the masked region changed, not the anchor.

#### Paid calls need the user's approval, every time

`--backend api` spends prepaid credits. A real call (not `--dry-run`) refuses to run
without `--approved-by "<the user's words>"`: ask first, for that specific call, and pass
their approval verbatim — it is recorded in the receipt. Approval for one call never
covers the next.

The key comes from `OPENAI_API_KEY`, or from `~/.config/art-studio/openai.key` — outside
every repo and every package, so it can never be committed or shipped with one.
**Never put a key on a shell command line** (`echo sk-... > file` writes it into shell
history permanently); a key that has ever appeared in one must be rotated. The real bound
on loss is a project spend cap at OpenAI plus a small balance.

### Codex models

**Availability collapsed over a few hours on 2026-09-30.** Three models stopped being
served to Codex on a ChatGPT account, one after another, each returning:

> The 'gpt-5.6-terra' model is not supported when using Codex with a ChatGPT account.

That is an upstream availability change, not a prompt or tooling fault, and `gen.py`
fails closed on it so a refused call bills nothing. **`gpt-6-astra` is the only model
left that reaches `image_gen`,** and is the default; every dead model is in
`CODEX_MODELS_BROKEN`, so asking for one fails immediately with the reason instead of
burning a call.

| model | reaches `image_gen`? | as of |
|---|---|---|
| `gpt-6-astra` | **yes — current working default** | verified 2026-09-30 |
| `gpt-6-sol` | **no — 400, account not supported** | worked, then broke 2026-09-30 |
| `gpt-5.6-terra` | **no — 400, account not supported** | broke 2026-09-30 |
| `gpt-5.6-luna` | **no — 400, account not supported** | broke 2026-09-30 |
| `gpt-6-luna` | no — returns no image | verified 2026-09-28 |
| `gpt-reserve` | no — returns no image | verified 2026-09-28 |

Because this changed three times in one day, **treat the table as a snapshot.** If a call
returns that 400, that model died too: add it to `CODEX_MODELS_BROKEN`, try another, and
update this table rather than retrying.

**Do not model-shop for savings — there is nothing left to shop for**, and astra was already
dearer than terra (per 1M tokens on 2026-09-28: astra 250 in / 1,250 out against terra's
62.5 / 375; `gen.py`'s header carries sol's). Cost is almost entirely input context anyway: one tool call,
~250–330 output tokens, against a fixed ~28k Codex preamble. Measured swings from 2.8k to
34.8k tokens on identical prompts were **prompt-cache hit rate**, not model or reasoning
effort. **Cached input is much cheaper by an amount never measured on astra** — the only
ratio on record is terra's 10x (62.5 vs 6.25), and terra is dead, so do not quote 10x as
astra's. Run candidates back-to-back to keep that preamble warm; it is worth far more
than model choice ever was.

### Gotchas

- `codex exec`'s `-i/--image` is variadic, so a positional prompt after it is
  swallowed as another filename. Pass the instruction on **stdin**.
- Reference images reach `image_gen` through conversation context, so `-i`
  attachment order is what establishes "image 1". There is no image argument.
- **Never put an API key inside a package or a repo** — see *Paid calls need the user's
  approval*, which owns where the key lives.
