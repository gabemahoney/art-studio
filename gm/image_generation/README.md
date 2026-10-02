# Image generation — how this directory works

The goal: build approved reference sheets for characters, ships, and objects in one
locked visual style, then compose scenes from those approved references.

## The pipeline

```
style.md  ──────────────┐   Style Block text + canonical_style_reference.png anchor,
                        │   attached to EVERY generation call
assets/<type>/<slug>/ ──┼─► candidates/vNNN/ ─(you approve)─► reference.png
                        │
outputs/<scene-slug>/  ◄┘   scenes built from approved reference.png files
```

## Two kinds of files

Every file here is one of two kinds:

- **Mutable head revisions** — edited or overwritten in place; always hold the
  *current* state: `style.md`, `canonical_style_reference.png`, each asset's
  `description.md`, `prompt.md`, `reference.png` and its `reference.md` sidecar,
  each scene's `final.png`. Generations read and attach these.
- **Frozen revisions** — written once, never modified: everything in
  `style_versions/`, `description_versions/`, `candidates/`, `sources/`, and the
  `vNNN/` scene folders. Every generation receipt resolves the mutable head
  revisions it used to their frozen equivalents, so history survives every edit.

## The files

- **`style.md`** — what the art looks like, and nothing else: the versioned Style
  Block, the anchor declaration, the changelog.
- **`rules.md`** — how generations run: the One Rule (attach the anchor + paste the
  Style Block into every prompt, even tiny edits — this is what stops style drift),
  image input roles, prompt assembly order, style versioning procedure.
- **`ref_images/style_references/canonical_style_reference.png`** — the style anchor. Its
  rendering is copied; its subjects never are.
- **`assets/<type>/<slug>/`** — one folder per character/object:
  - `reference.png` — the approved image, the only one scenes use
  - `reference.md` — one-line sidecar: which frozen candidate the current
    `reference.png` was promoted from
  - `description.md` — current design in words (single source of truth), with a
    version header; every design change is snapshotted to `description_versions/`
  - `prompt.md` — reusable sheet-layout prompt
  - `candidates/vNNN/` — one folder per attempt, each holding `image.png` +
    `generation.md` (the exact prompt and attached inputs)
  - `sources/` — your original uploads
- **`outputs/<scene-slug>/`** — one folder per scene: `vNNN/` attempt folders
  (same `image.png` + `generation.md` shape), `final.png` once you approve one.
- **`bin/`** — the tools that enforce all of the above in code:
  `prompt.py` assembles a prompt in the mandated order, `gen.py` validates the One
  Rule and generates one candidate with a full receipt, `review.py` records your
  assessment on that receipt afterwards, `promote.py` approves a candidate into
  `reference.png` / `final.png` with provenance. Stdlib only; see
  the Tooling section of `rules.md`. Nothing here is generated any other way.
- **`.claude/skills/art-studio`** — the agent workflow that drives `bin/`.
  `.agents/skills/create_asset` and `.agents/skills/illustrate` are the older
  Codex-format versions; they predate `bin/` and still describe the by-hand
  procedure, so `rules.md` and `bin/` win wherever they disagree.

## Requirements

Python 3 (stdlib only — no venv, no `pip install`), plus two external binaries:
ImageMagick (`magick`) for deliverables, and the `codex` CLI for the default
backend. `--backend api` spends prepaid OpenAI credits, which the ChatGPT
subscription does not pay for, and it is gated: `gen.py` holds no key and cannot
make a paid call. The key lives encrypted in `.api-key.enc` and only the user can
unlock it — set it up with `python3 -I bin/seal-key.py`, approve a call with
`python3 -I bin/unlock.py`. See `rules.md`. **Never create a plaintext `gpt.key`;**
it reopens the hole this gate exists to close.

## Reading status from disk

Status is never written down separately — the files are the status:

- An asset is **approved** if and only if `reference.png` exists; `reference.md`
  says which candidate it came from.
- The **latest attempt** is the highest-numbered folder in `candidates/`.
- The **current design** is `description.md`; its header says the version.
- A scene is **done** if and only if `final.png` exists in its folder.
