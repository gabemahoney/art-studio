# Generation rules

Mechanics for EVERY image generation, in both skills. `style.md` defines what the
style IS; this file defines how generations run. Read both before any generation.

## Where images live

**Text lives in this repo; images live outside it.** Receipts, `description.md`,
sidecars, `style.md` and `bin/` are the written record and belong in git. Images are
large, numerous and regenerable, so they sit in a separate tree configured per project:

| | |
|---|---|
| **repo** | `outputs/<scene>/vNNN/generation.md` |
| **images** | `<IMAGES>/outputs/<scene>/vNNN/image.png` |

Both trees use the **same vault-relative paths**, so a candidate's receipt and its image
are siblings in the vault's layout even though they are in different directories on disk.
`vpath()` in `bin/gen.py` is the only place that decides which root a path belongs to: a
known image suffix goes to `IMAGES`, everything else to the repo, and `tmp/` is always
local scratch.

**One source of truth: the `image-root` file beside this one** — its first non-comment line
is the directory. There is no environment override and no fallback, because three ways to
answer "where are the images" is three ways to disagree, and a silent fallback would
scatter renders into the repo the first time the file went missing. If it is absent, empty,
or names a directory that does not exist, every command stops and says which. Moving the
tree means editing that one line.

Consequences worth knowing:

- **A fresh clone cannot generate until the images tree is present.** `gen.py` hard-stops
  when a `reference.png` fails its provenance check, and that check compares bytes.
- **`git checkout` only recovers an image if the repo holding `IMAGES` tracks it.** See
  the `art-studio` skill's `reference/fixing-an-image.md` → *Guardrails* for what is
  and is not recoverable.
- `vNNN` is allocated from the highest number in **either** tree, so a receipt and an
  unrelated image can never share a folder name.

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
copy without being drift — `bin/selftest.py` compares exactly that subset, and a mismatch
there is real. Every `generation.md` records the style
version it ran under and embeds the exact prompt.

## Tooling

The scripts in `bin/` enforce everything above. Stdlib only — no venv, no
`poetry install`. Run them from this directory.

### `bin/prompt.py` — assemble the prompt

Emits the sections in the mandated order (Style Block, image roles by number,
design text, scene spec, closing line). Never hand-write a prompt: that is how
the Style Block drifts and the closing line gets paraphrased.

```bash
python3 bin/prompt.py \
  --role STYLE:"Match its hand-painted matte rendering only. Ignore its subjects." \
  --role IDENTITY:"Copy this asset's design exactly. Ignore its sheet layout." \
  --task "A single horizontal three-quarter view against a plain background." \
  --design-from assets/<type>/<slug>/description.md --design-section Exterior \
  --spec-file /tmp/framing.txt -o /tmp/prompt.txt
```

`--role` is repeatable and **in attachment order**; image 1 must be STYLE. Omit
the text after the colon to get the standard role wording from this file.

### `bin/gen.py` — generate one candidate

Refuses to run before anything is billed: on any One Rule violation (anchor not first
as STYLE, Style Block not verbatim, no closing style line), on a `reference.png` failing
validation, and on the live anchor differing from its frozen `style_versions/` copy.
**That list goes stale; `bin/selftest.py`'s cases are the authoritative enumeration** —
they also cover the five-attachment cap, a doubled anchor, a dead model, and every mask
guard. One exception to #3: a short list of **legacy closing-line wordings is accepted on
an ordinary call with a warning**, because old receipts used them — but refused outright on
a masked call, where naming "image 1" would point at the picture being repainted.
Allocates `vNNN` only after a successful response, so a failure leaves no empty
folders. Writes `image.png` (raw, frozen), the deliverable,
and a complete `generation.md`.

```bash
python3 bin/gen.py --scene <slug> --prompt-file /tmp/prompt.txt --preset book-float \
  --attach ref_images/style_references/canonical_style_reference.png:STYLE \
  --attach assets/<type>/<slug>/reference.png:IDENTITY \
  --request "<user's words, verbatim>" --mode "<what this attempt changes>"
```

Use `--asset <type>/<slug>` instead of `--scene` for asset candidates, and
`--dry-run` to check invariants for free. `--refinish <vNNN dir>` re-derives a
deliverable from an existing `image.png` without generating anything.

**Presets** name a delivery spec once: `book-float` = 1536×1024 on `#1b1e26`
under 2.5 MB (the 55 mm right-hand float at 708 dpi); `book-float-portrait` =
1200×1500 on the same ground. A preset also sets the *requested* size to its own
aspect, so the deliverable is full-bleed rather than padded. The deliverable is
always scaled to FIT and padded, never cropped — no hull is ever cut off to
satisfy a box.

### `bin/review.py` — record the assessment
```bash
python3 bin/review.py outputs/<scene>/v002 --review "<what you see, misses included>"
```
Sets the `Review` line `gen.py` leaves as a placeholder. Refuses to
overwrite an existing review without `--replace`.

### The two post-hoc fields

A receipt is frozen history with exactly two exceptions, because both are known
only AFTER the run:

- **`Status`** — owned by `bin/promote.py`, set when the user approves.
- **`Review`** — owned by `bin/review.py`, set once you have looked at the image.

`bin/gen.py` runs before the image exists, so it cannot take the review; it writes
a placeholder. Fill it with `python3 bin/review.py <vNNN> --review "..."`. Editing
any other field of a receipt, or editing these two by hand, is still forbidden.

### `bin/promote.py` — approve a candidate

```bash
python3 bin/promote.py outputs/<scene>/v002 --approval "<user's words, verbatim>"
```

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
| Requested size | advisory — the tool picks its own | honored |
| Targeted repaint | not possible | **yes — `--mask`, only those pixels regenerate** |

A ChatGPT/Codex subscription does **not** fund API keys; they are separately
billed products. The account was funded with **$10 on 2026-09-30**; no call has yet
completed on this backend, so every cost figure here is arithmetic, not measurement.
The first real call's `Token usage:` receipt line replaces the estimate with a fact.

#### Masked inpainting

`--backend api --mask PATH` repaints only the masked pixels. The mask is an ordinary
vault mask — greyscale, **WHITE = the region to repaint**, same dimensions as the EDIT
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

Build the prompt with `bin/prompt.py --masked`: it puts the EDIT TARGET first and emits
the masked closing style line from `style.md`, which names the anchor by role rather than
by index. `check_prompt()` requires the matching line for the call type and refuses either
mismatch, so a prompt that contradicts its own payload cannot be sent.

**`--prompt-file -` is refused with `--backend api`**: stdin leaves no file to hash, so the
request could not bind the prompt's content. Write the prompt to a file.

**`--quality` defaults to `high`** (`low`/`medium`/`high`/`xhigh`/`max`/`auto`) and is the
cost lever inside the $0.05–0.35 estimate — it reaches the receipt and the approval
summary, so say which you chose when you ask. `--size` must equal the EDIT TARGET's own
dimensions, since the mask is aligned to that
image; it defaults to 1536x1024, which is wrong for this vault's portrait and oversized
candidates, so read the real size with `magick identify` and pass it.

The call also fails closed on an alpha-carrying mask, a dimension or `--size` mismatch, a
mask outside the vault, more than one EDIT TARGET, and `--backend codex` (which cannot
inpaint — use Path 3). It prints the share of the frame the mask covers and puts that
figure in the approval request, so the user sees what they are paying to repaint. The
result is re-encoded: the unmasked area is visually preserved but not byte-identical.

**No masked call has completed here.** The semantics above are from the API reference, not
measurement — verify on the first real call that what comes back is the EDIT TARGET with
the masked region changed, not the anchor.

#### Paid calls require the user's passphrase

`gen.py` holds no API key and cannot make a paid call. When one is needed it writes
`.api-request` — the exact argv, a human summary, **and an md5 of every file the call
depends on** (prompt file, mask, each attachment) — and fails closed. A file it cannot hash
aborts the request rather than going unbound. Under `VAULT_SELFTEST=1` it adds a `selftest`
marker that `unlock.py` refuses outright, so a request `bin/selftest.py` provoked can never
be approved — never export that variable.

The user then runs `! python3 -I bin/unlock.py`. It prints that request and the command it
will run, **recomputes those md5s and refuses if any file changed** — once before showing
you anything, and **again immediately before launching `gen.py`**, so the interval while you
read the summary and type the passphrase is covered too. Approval binds to content, not to
a path. (A
request with no digests predates the check; `unlock.py` says so rather than failing.) Then
it asks for a passphrase on `/dev/tty`, decrypts `.api-key.enc` in memory, and re-invokes
`gen.py` with `--key-fd`, handing the key down a **pipe** — not argv (visible to `ps`), not
the environment (visible to `ps eww`). The key never touches disk in plaintext.

Setup, once:

```bash
python3 -I bin/seal-key.py   # prompts for the key and a passphrase
rm gpt.key                   # both commands run from vault
```

**Never put a key on a shell command line.** `echo sk-... > gpt.key` writes it into
`~/.zsh_history` permanently — outside the repo, where `.gitignore` and every rule here
is irrelevant, readable by any agent, and already in your backups. That is how the key
in use on 2026-09-30 leaked. **A key that has ever appeared in a shell command must be
rotated, not merely sealed**; `seal-key.py` scans the history files and refuses to
report success if it finds the key it just sealed. Paste it at the `/dev/tty` prompt
instead.

**What these guards can and cannot do.** Every check in `bin/selftest.py` assumes the code
is not hostile: anything able to edit `bin/` can delete the gate, so no guard resists that
access, and one able to write only *data* still hides a key where the search does not look
(see the table below). They exist to catch a rule broken **by accident** — by a future
maintainer or model that did not know it — and to fail loudly rather than silently. The
real bound on loss is a project spend cap at OpenAI plus a small balance.

**Until `gpt.key` is deleted the gate is weak** — the key is readable, so `--key-fd`
proves nothing: any process can supply it without the passphrase. `gen.py` therefore
**refuses `--key-fd` on a real paid call (`--backend api` without `--dry-run`) while
`find_plaintext_keys()` sees any readable key in the vault**,
and `unlock.py` checks the same before prompting, so you are never asked for a passphrase
only to be refused after. That closes the bypass but not the file — a readable key
works against the API directly, with no part of `bin/` involved. **Never create a
plaintext key file, and never use one you find**: report it instead.

What that search sees:

| | |
|---|---|
| **Found** | `*.key`, `*.pem`, `*key.txt`, `*key.json`, `*.secret` — case-insensitive, so `API.KEY` counts while `.env` matches no name pattern — anywhere in the vault, symlinked subtrees included; plus `sk-` strings in the *contents* of text files under 1 MB outside `.git`, `__pycache__`, `node_modules`, `.obsidian` (so a `.env` holding a key IS reported, by content) |
| **Missed** | anything **outside `vault`** — the repo root, `$HOME`, a shell history; a key inside a binary (a `.png`, a zip), appended past 1 MB, or innocuously named under a skipped subtree; and `~/.codex/auth.json`, out of scope by design |

`bin/selftest.py`'s key-read detector has four limits of its own. It cannot see
`args.<attr>` paths, or anything outside `bin/gen.py`. Two more are deliberate, each the
price of a false positive on honest code: a credential token must be punctuated or shouted,
so bare `secret`/`apikey` slips (loosening it lets the receipt's "tokens used" trip); and
`_tokens` is whitelisted for the API's usage fields, which also hides `refresh_tokens`.
**Further Python spellings of a key read are accepted limits, not bugs to chase:** the walk
is good enough for a tripwire, and the real controls are the search above and the
`--key-fd` refusal.

Measured 2026-09-30:

- An agent has no controlling terminal (`/dev/tty` → `Device not configured`), so it
  cannot answer the prompt; piping the passphrase on stdin does not work either.
- A refused unlock leaves `.api-request` in place and spends nothing, and the file is
  consumed *before* the call — a second attempt needs a second approval.
- The pipe handoff works: a piped key returned a clean `401` on a deliberately fake one.

Three things this does **not** defend against, and no local design can:

1. **An agent editing `bin/unlock.py`, or hijacking the interpreter.** User site packages
   are enabled here, so a planted `usercustomize.py` runs on every Python start and can
   capture the passphrase without touching any repo file; `PYTHONPATH` can shadow stdlib
   modules the same way. **This is why both scripts must be run as `python3 -I`** —
   isolated mode disables user site, `usercustomize` and `PYTHONPATH`. Verified:
   `ENABLE_USER_SITE` is `True` normally, `False` under `-I`, and a `PYTHONPATH` stdlib
   shadow is ignored under `-I`.
2. **Key capture after a legitimate unlock.** The call has to happen somehow. The real
   bound on loss is a **project spend cap at OpenAI** plus a small balance — the only
   limit that survives a bug in this code.
3. **The Codex credential.** `~/.codex/auth.json` is a live ChatGPT-account credential at
   rest, and `--backend codex` has no gate at all — it is the documented fallback the
   moment this gate stops an agent. It spends subscription quota rather than prepaid
   balance, so the loss is bounded differently, but it is an ungated spendable
   credential this design does not cover. Known and accepted, not overlooked.

`--approved-by "<the user's words>"` is separate and optional: it records *why* in
the receipt. It is not permission.

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
- **Never create a plaintext key file**, and never use one you find — see *Paid calls
  require the user's passphrase*, which owns this.
