# Generation rules

Mechanics for every image generation. The package's `style.md` defines what the style
is; this file defines how generations run. Read both before any generation.

## Package and output

`SKILL.md` → *Two locations, always given* has the layout. Every command is told where
to work, with no config file, environment override or default location, because a
silent fallback is how renders end up somewhere nobody meant.

- A scene render reads the package and writes only under `OUT`, so one package can
  feed many output folders and two repos rendering from it at once cannot collide.
  `gen.py` refuses an `OUT` that overlaps `PKG`, and `--output` together with `--asset`.
- Relative `--attach` and `--mask` paths resolve against the package, then the output
  folder, and a path present in both is refused as ambiguous. Receipts write paths as
  `package:<rel>`, `output:<rel>`, or absolute.

## The One Rule (prevents style drift)

Every image-generation call — new artwork, revisions, and *especially* tiny edits —
must do ALL of these:

1. Attach the current style anchor `ref_images/style_references/canonical_style_reference.png`
   as a style-only input, labeled as such in the prompt — and, with the single
   exception of a masked API call (see *Masked inpainting*), ALWAYS as the FIRST
   attached image, so that "image 1" in any prompt unambiguously means the anchor.
2. Include the full Style Block from `style.md`, verbatim, at the TOP of the prompt.
3. End the prompt with the closing style line exactly as `style.md` states it; only
   `style.md` holds that wording, so the two files cannot drift apart.
4. Deliver the prompt to the image model **byte-for-byte**. No agent, wrapper or
   tool may paraphrase, "normalize", summarize or expand it on the way.

Style is never inherited from a previous output; it is re-asserted on every call.
If a call skips any part, the result is invalid — regenerate.

### Why #4 exists

Codex CLI's built-in `image_gen` rewrites prompts by default: its skill doc
(`~/.codex/skills/.system/imagegen/SKILL.md`, step 9) tells the model to "normalize it
into a clear spec", and a nine-word test prompt reached the tool as a 60-word spec with
invented constraints. A paraphrased Style Block silently defeats the whole anti-drift
mechanism.

`gen.py --backend codex` prevents this structurally: it writes the prompt to a file and
tells Codex to read it with `fs.readFileSync` and pass those bytes straight to the tool
argument, so the text never passes through model output tokens. A real run confirmed
it: the model's whole output was 313 characters, with no Style Block in it.

`## Exact prompt` in receipts written before 2026-09-28 records what was handed to
Codex, not what the image model saw, so treat those as approximate.

## Image input roles

**Assembly order, because style must dominate:** Style Block first, then the image
roles, the `TASK:` line, design text, layout or scene spec, and the closing style line
last; `prompt.py` builds this order. Roles go at the top of the prompt *body*, never
above the Block. Design wording names materials and colors, not
finish, because the Style Block owns finish.

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
  cannot: full source, crop, or nothing (`reference/writing-prompts.md` → *Attach the
  minimum identity input*).
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

`style.md` is the mutable head revision of the style. **Only three things are
versioned: the Style Block, both closing style lines, and the anchor image**, and
`gen.py` compares exactly those with the frozen copy before every call, so a mismatch
there is real drift while prose may differ freely.

To change any of the three (replacing the anchor counts): confirm the current version
is frozen in `style_versions/` (`style-v<N>.md` + `canonical_style_reference-v<N>.png`),
make the change, bump the version header, add a changelog line, and freeze the new
version. Never edit, attach from or re-freeze anything in `style_versions/`, because
receipts stamped with a version must stay checkable against it.

When you change the closing line, you may list the old wordings under
`## Legacy closing style lines` in `style.md`, one `> ` quote each and below the
closing-line sections, so prompts from older receipts still replay: `gen.py` accepts
them with a warning on ordinary calls and refuses them on masked ones.

## Tooling

The scripts in `scripts/` enforce everything above; `SKILL.md` → *The loop* shows each
call. They are stdlib-only Python, so they need no venv, and take every location from
their arguments, so they run from anywhere.

- **`prompt.py`** emits the sections in the mandated order: Style Block, image roles
  by number, `TASK:`, design text, spec, closing line.
- **`gen.py`** refuses to run, before anything is billed, when the anchor is not image
  1 as STYLE, the Style Block is missing from the prompt, or the closing style line is
  not last; on a `reference.png` failing validation; or on a live style differing from
  its frozen copy. It cannot check that the Block is at the top or that `--role` order
  matches `--attach` order, so `prompt.py` and you own those.
  **`selftest.py`'s cases are the authoritative list of its refusals**, because a list
  here goes stale. `--refinish <vNNN dir>` re-derives a deliverable from an existing
  `image.png` without generating anything.
- **`review.py`** and **`promote.py`** take the `vNNN` directory and read its kind from
  the path: a `vNNN` under `candidates/` is an asset candidate, anything else a scene
  version. Each refuses to overwrite its field or head without `--replace`.

**Presets** name a delivery spec once, in the package's optional `presets.json`:

```json
{"page-float": {"final_size": "1536x1024", "flatten": "#ffffff", "max_mb": 2.5}}
```

A preset also sets the *requested* size to its own aspect, so the deliverable is
full-bleed rather than padded. The deliverable is always scaled to fit and padded,
never cropped, so no subject is cut off to satisfy a box.

### The two post-hoc fields

A receipt is frozen history with two exceptions, because both are known only after
the run: **`Status`**, owned by `promote.py`, and **`Review`**, owned by `review.py`.
Never edit any other field, or these two by hand.

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

Build the prompt with `prompt.py --masked`: it requires the EDIT TARGET as the first
role and emits
the masked closing style line from `style.md`, which names the anchor by role rather than
by index. `check_prompt()` requires the matching line for the call type and refuses either
mismatch, so a prompt that contradicts its own payload cannot be sent.

**`--quality` defaults to `high`** (`low`/`medium`/`high`/`xhigh`/`max`/`auto`) and is the
cost lever inside the $0.05–0.35 estimate, so say which you chose when you ask.
`--size` must equal the EDIT TARGET's own dimensions, because the mask is aligned to
that image; its default (1536x1024, or a preset's size) is wrong for portrait and
oversized candidates, so
read the real size with `magick identify` and pass it.

The call also fails closed on an alpha-carrying mask, a dimension or `--size` mismatch,
more than one EDIT TARGET, and `--mask` with `--backend codex`, which cannot inpaint
(use `reference/fixing-an-image.md` → *Path 3*). It prints the share of the frame the
mask covers; give that figure when you ask, so the user sees what they are paying to
repaint. The result is re-encoded: the unmasked area is visually preserved but not
byte-identical.

**No masked call has completed here.** The semantics above are from the API reference, not
measurement — verify on the first real call that what comes back is the EDIT TARGET with
the masked region changed, not the anchor.

#### Paid calls need the user's approval, every time

`--backend api` spends prepaid credits. A real call (not `--dry-run`) refuses to run
without `--approved-by "<the user's words>"`: ask first, for that specific call, and pass
their approval verbatim — it is recorded in the receipt. Approval for one call never
covers the next.

The key comes from `OPENAI_API_KEY`, or from `~/.config/art-studio/openai.key`. **Never
put a key inside a package or a repo**, so it can never be committed or shipped with one.
**Never put a key on a shell command line** (`echo sk-... > file` writes it into shell
history permanently); a key that has ever appeared in one must be rotated. The real bound
on loss is a project spend cap at OpenAI plus a small balance.

### Codex models

On 2026-09-30 three models stopped being served to Codex on a ChatGPT account within
a few hours, each returning an HTTP 400 such as:

> The 'gpt-5.6-terra' model is not supported when using Codex with a ChatGPT account.

That is an upstream availability change, not a prompt or tooling fault. **`gpt-6-astra`
is the only model left that reaches `image_gen`,** and is the default; every dead model
is in `gen.py`'s `CODEX_MODELS_BROKEN`, so asking for one fails before any call.

| model | reaches `image_gen`? | as of |
|---|---|---|
| `gpt-6-astra` | **yes — current working default** | verified 2026-09-30 |
| `gpt-6-sol` | **no — 400, account not supported** | worked, then broke 2026-09-30 |
| `gpt-5.6-terra` | **no — 400, account not supported** | broke 2026-09-30 |
| `gpt-5.6-luna` | **no — 400, account not supported** | broke 2026-09-30 |
| `gpt-6-luna` | no — returns no image | verified 2026-09-28 |
| `gpt-reserve` | no — returns no image | verified 2026-09-28 |

**Treat the table as a snapshot**, because it changed three times in one day. If a call
returns that 400, that model died too: rather than switching models, follow
`reference/fixing-an-image.md` → *The bar* (Codex unavailable), which ends by moving
it to `CODEX_MODELS_BROKEN` and updating this table.

**Do not model-shop for savings**, because no cheaper working model is left (rates are
in `gen.py`'s header). Cost is almost entirely input context: one tool call of
~250–330 output tokens against a fixed ~28k Codex preamble, and measured swings from
2.8k to 34.8k tokens on identical prompts were prompt-cache hit rate. Run candidates
back-to-back to keep that preamble cached; astra's cached-input discount has never
been measured, so do not quote a ratio for it.

### Gotchas, for anyone changing `gen.py`

- `codex exec`'s `-i/--image` is variadic, so a positional prompt after it is
  swallowed as another filename; `gen.py` passes the instruction on stdin.
- Reference images reach `image_gen` through conversation context, so `-i`
  attachment order is what establishes "image 1".
