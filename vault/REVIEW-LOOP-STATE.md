# Review loop state — COMPLETE

**`gate-17` returned `only nits remain` directly after a succinctness pass, which is the
goal's terminating condition.** Seventeen condensation passes, seventeen adversarial
reviews. Its four nits were fixed anyway (two were guards of mine that had gone dead or
unasserted); nothing material was outstanding.

Final: `python3 -I bin/selftest.py` **36/36** (total is derived, so it varies with vault
state — match left against right). image-surgery 3245, art-studio 2455, rules.md 3552,
style.md 994. **$0 spent; zero `backend=api` receipts in the vault.**

Keep this file: the lessons below are not recoverable from the code or git history.

## The goal

Run correctness reviews on the skills until feedback is trivial. Then a succinctness
pass. Then review again until trivial. Keep alternating. **Done when a review comes
back trivial DIRECTLY AFTER a succinctness pass** — not after a correctness fix.

## Phase

**Phase 1 cleared** at 31 bugs — `gate-check` returned `only nits remain`.
**Phase 2 (first succinctness pass) done:** image-surgery 4045 -> 3106 (939 cut),
art-studio 2498 -> 2411, style.md 806 -> 786. Selftest 27/27 throughout.
**Phase 4 (second succinctness pass) DONE** — image-surgery 3192 -> 3088, art-studio
2462 -> 2394. All 25 `magick` recipes re-executed afterwards (0 failures), all
file→section pointers resolve, selftest 29/29. A review of THIS state is what the goal
turns on: trivial here and the loop ends.

Cuts made, for anyone checking I did not lose a fact:
- routing table: three rows justified "those pixels do not exist" separately; merged
  into one row under a stated principle (ImageMagick rearranges, regeneration invents)
- masks: six full `magick` invocations -> the shared skeleton plus the primitives; the
  `-rotate` CLOCKWISE surprise kept verbatim
- the two measurement sections merged; `-metric AE`/RMSE caveats moved inline
- crop/resize: dropped the `-resize` variants a competent reader knows; `-strip` demoted
  to one comment line
- guardrails: "image.png is frozen" and "never hand-edit a promoted head" were the same
  rule twice; merged. Composite-vNNN and its receipt likewise.
- art-studio's four worked examples -> the principle plus two patterns; the L-bracket
  stays because it shows a ban list is defeatable BY CONSTRUCTION
- the cape/scarf story was told in full in BOTH skills. It is image-surgery's (Step 0);
  art-studio now points there.

**Phase 3 CLEARED.** `post-cut-review` returned **only nits remain** after re-checking
12-15; its three nits are also fixed (the five-vs-six generation count, the `-strip`
bound, the changelog's redundant closing line), plus two reflows. An independent
`fresh-eyes-review` is still running on the pre-nit state — wait for it before
condensing, so a material finding does not land mid-condensation. The goal terminates only when a review
comes back trivial DIRECTLY AFTER a condensation pass, so: verdict -> condense again
-> review again. A trivial verdict HERE does not end it; it ends after the NEXT
condensation pass reviews clean.

(historical)**Phase 1 (correctness) — was not clear.** Three reviewers have run; a fourth
(`docs-reviewer-2`) is in flight, instructed to end its report with the literal
phrase **"material bugs remain"** or **"only nits remain"**. That phrase is the gate;
do not advance to Phase 2 on my own judgement.

## Baseline

`python3 -I bin/selftest.py` → **31/31**. Run it before trusting anything below.

| file | words | target after condensation |
|---|---|---|
| `.claude/skills/image-surgery/SKILL.md` | 3166 | ~2700 |
| `.claude/skills/art-studio/SKILL.md` | 2417 | ~2340 |
| `rules.md` | 3002 | (not a target) |
| `style.md` | 927 | (grew by the v2 changelog entry; correct) |

## The condensation plan, already scoped

`rules.md`'s `#### Masked inpainting` section (467 w) **already owns** all six
mechanism facts: the mask convention, the One Rule inversion and why, the
`prompt.py --masked` builder, the unverified status, the `--size` constraint, and the
fail-closed list.

`image-surgery`'s **Path 4 is 811 w and restates every one of them.** Cut it to:
the command, the bar, the Codex-failure ladder, and "try Path 3 first — it is free".
Everything else becomes one pointer to `rules.md`. That is ~400 words from one
section, most of the gap, and a restructure rather than scattered trimming.

Governing principle, learned the hard way today: **one file owns each fact.**
`rules.md` owns mechanics, `image-surgery` owns routing decisions, `art-studio` owns
workflow and points elsewhere, `bin/selftest.py` owns the guard list. A fact stated
twice goes stale in one place — which is how both skills kept describing a lease
design that had been deleted hours earlier.

## Bugs found this loop — all fixed, do not re-fix

1. Mask applied to `image[0]`, which One Rule #1 forced to be the style anchor. Masked
   API calls now invert the order, enforced **by identity, not role**.
2. Approval bound only by path; prompt/mask could be swapped after the user read the
   summary. `.api-request` now records md5s; `unlock.py` refuses on mismatch.
3. "Only after trying gpt-6-astra" was a precondition that cannot fail — astra IS the
   default. Replaced with a four-rung ladder.
4. `--masked` is a `prompt.py` flag only; `gen.py` infers it.
5. `-rotate 90` is CLOCKWISE — the horizontal ramp mask adjusted the wrong side.
6. `%[fx:]` prints scientific notation above ~1e6; needs `-precision 10`.
7. Alpha channels come from antialiased CURVES (`ellipse`) as well as `-blur`.
8. `-strip` in the recompress recipe saves zero bytes; `-colors 128` re-adds alpha
   and only `-define png:color-type=2` prevents it.
9. Five-reference cap was documented but unenforced.
10. `magick compare` exits non-zero when images differ — aborts `set -e` scripts.
11. The stated failure mode for omitting `-alpha off` was BACKWARDS. The mask is
    **ignored**, not inverted: the adjustment hits the whole frame including the
    masked region. Measured — inside the mask correct=37 vs broken=36
    (indistinguishable), outside correct=85 vs broken=63. Checking inside the mask
    therefore cannot detect it. Always diff OUTSIDE.
12. The documented DPI pass rewrote `image.png` IN PLACE. `finish()` returns `raw`
    itself when dimensions already match and there is no alpha, and **193 of 233
    candidates are 1536x1024**, so `out.png` IS `image.png` in the normal case.
    Verified the md5 changes, which hard-fails `validate_reference()` on a promoted
    asset. Recipe now writes to a new path.

**Three of these were found by RUNNING the documented commands, not reading them.**
Any future review of these docs should execute every recipe.

14. **`art-studio` asserted an impossibility that was false, and omitted the
    prohibition that holds.** It said a paid call is impossible because "`gen.py` holds
    no key" — but the gate is `args.key_fd is None`, and `--key-fd 3 3< gpt.key` walks
    past it. The entry-point skill told an agent spending was impossible while saying
    nothing about `--key-fd`, so discovering `gpt.key` reads as finding the supported
    mechanism. Fixed in prose AND in code: `gen.py` now refuses `--key-fd` outright
    while any plaintext `*.key` is in the vault, because a forged approval is
    indistinguishable from a real one. Selftest case is conditional on a plaintext key
    existing, so it does not rot after sealing.
15. The selftest's "reads no key" case was a grep for the literal `gpt.key`, which the
    new guard's explanatory comment false-positived. Replaced with an `ast` walk over
    code only — env lookups of key-like names, literal `*.key` paths — verified 10/10
    against 6 synthetic leaks and 4 benign lookalikes. **A guard whose first failure is
    a comment is a text taboo, not a guard.**

18. **"Candidates are not in git" was false, with two errors of opposite sign.** 57 of
    233 are tracked and `git checkout` restores them BYTE-EXACT; the guardrail called
    the receipt "the only recovery path", which sends an agent past a free exact
    recovery for a quarter of the vault and makes it regenerate a different image. And
    "usually recoverable" is 64%: **83 candidates cannot be recovered by any route** —
    the real reason the surrounding rules are absolute.
    Verified census: 233 candidates / 57 tracked / 93 with a live `codex source` / union
    150 / 83 lost. **I nearly reported the codex route as dead**: my first measurement
    said 0 of 93 resolved, because `(\S+)` swallowed the `;` after `.png`. With
    `(/\S+?\.png)` all 93 resolve. Had I trusted my own number I would have deleted a
    working recovery path from the docs.
    Selftest case 31 recomputes the whole census and fails on drift against all four
    numbers in that paragraph. It caught a bug in itself first (compared `git ls-files`
    output to absolute paths, read 0 tracked; needs `--full-name`).
19. **The condensation DID lose a fact, and this was it.** The collapsed mask skeleton
    said "One `-size`" without saying what it must equal. A wrong-sized mask misaligns
    SILENTLY. Restored with the instruction to read dimensions via `magick identify`
    rather than assume 1536x1024. image-surgery 3088 -> 3162, which is the right trade.

17. **The `ast` key-read check I wrote in finding 15 was weaker than the grep it
    replaced.** `fresh-eyes-review` defeated it nine ways. The one that matters:
    `sorted(ROOT.glob("*.key"))[0].read_text()` — a working plaintext read, the most
    natural way anyone would write it in that file, passing because my exemption
    filtered **by literal value** (`"*.key" not in m`) rather than by use site.
    Its claim that the old grep caught A, B, F, G, H was wrong — measured, the grep
    caught **C, D, I** (substring hits on `OPENAI_API_KEY`) and missed those five, while
    mine missed all eight. Grep 5/10, ast 2/10. The answer was both techniques, not a
    choice: fold concatenations, compare case-insensitively, treat a key-ish literal
    used as a subscript as an env lookup, and exempt the guard's glob by asking whether
    the statement *reads*. Now 10/10 with 0 false positives.
    **Three false-positive classes bit on the way, all mine, all now permanent probes:**
    matching read-ish words against the statement's TEXT (a message saying "ask the user
    to run" counted as `subprocess.run` — 9 hits); walking compound statements (an `if`
    block contains its whole body, so an unrelated message paired with an unrelated
    read); and treating prose as a credential ("tokens used" in the same statement as
    `src.read_bytes()` — a read of an IMAGE). A credential is an identifier: ≤64 chars,
    no whitespace.
    **The check is renamed "gen.py has no obvious key read"** — the old name claimed a
    proof static analysis cannot deliver. Its nine bypasses now run on every selftest,
    and five leaks planted into a copy of `gen.py` are all caught.
    **Lesson: a guard's first version is a hypothesis. Try to defeat it before trusting
    it, and keep the successful attacks as tests.**

16. **Self-found while waiting on the review: the new `--key-fd` guard stranded the
    user.** `unlock.py` showed the summary, took y/N, took the passphrase, decrypted,
    THEN spawned `gen.py`, which refused because `gpt.key` exists — so the user typed
    their passphrase for nothing. `unlock.py` now checks for plaintext `*.key`
    immediately after the `.api-key.enc` check, before any prompt. Verified with a
    synthetic `.api-request` and a dummy (never-decrypted) `.api-key.enc`: refuses
    first, names the file, prints the exact `rm`, exit 1, no passphrase asked. Both
    temp files removed.
    Order of the two early checks is deliberate: missing `.api-key.enc` reports first,
    because the correct sequence is seal, then delete.

13. `rules.md` said "The three dead models are listed in `CODEX_MODELS_BROKEN`" one
    line above a table correctly listing **five**. Found by writing the guard, not by
    reading. Fixed by deleting the count — a number that must be maintained by hand is
    a liability — and selftest case 28 now compares every row of that table against
    `CODEX_MODEL`/`CODEX_MODELS_OK`/`CODEX_MODELS_BROKEN`, and contradicts any count
    word the prose reintroduces. It failed on its first run, which is the point.

**The recurring failure is mine, and it is specific: I write plausible numbers.** In
the edit that FIXED finding 12 — a finding about unsourced measurements — I introduced
three fresh wrong ones (402 words, a 5.5% median, a 13% that contradicted the 12.8%
two lines up). Every figure in these docs must be re-derived at the moment it is
written, from the artefact that actually holds it, and the artefact named in the text.
A number inherited from an earlier paragraph of my own prose is not a measurement.

## Verified figures — do not re-derive

- ratio drift v023→v026: claimed 19%, measured 18.8%
- edge energy v005→v028: claimed 13%, measured 12.8%
- tonal correction's effect on edge energy: claimed 0.1%, measured 0.09%
- all 24 documented `magick` commands execute correctly
- `modulate 100,100,95` on `#2D222B` → `#2D222D` (the doc's `2C212C` was wrong)
- v023→v026 edge energy: −4.0% over three passes (386.7 / 389.9 / 372.3 / 371.0).
  The 12.8% figure is v005→v028 over five — two different series, long conflated.
- `-strip` on raw `image.png`: **census of all 233** — min 0.0%, median 5.2%, p90
  9.6%, max 16.3%, and 32% of files save over 6%. Two independent n=40 samples both
  understated the max (12.9% and 14.4%); the census is the only defensible source. A
  sampled range stated as a hard bound WILL be violated by some file.
- edge energy v005→v028 re-derived independently by a second reviewer: 399.58 → 348.345
  = 12.83%. Holds. And "across five" is correct, not six: v027 is a local composite
  (its receipt opens `Source: local composite, no generation`), so the six-`vNNN` span
  contains five generations. The doc now says so, because a reader who counts folders
  finds six and distrusts the figure.
- the v2 over-delivery: **402 words shipped, 214 declared, +188**, identical across all
  39 affected receipts. Derived from the receipts, the only surviving record, since the
  committed `style.md` predates the Note. **Bound the span from the `Hand-painted flat
  angular` opener to the first `Image N is ` line** — nothing shorter. I twice bounded
  it at the Note's "legitimate art direction" sentence and got 380, missing the two
  lines after it; `selftest.py:209` had 188 right the whole time. 165 receipts carry
  `Style: v2` in all; 39 are the affected subset. **Do not re-derive this from
  `style.md`.**
  The 22 missing words are worth knowing: the shipped Block contained the sentence
  "This note sits outside the Style Block and changes none of its text" — while being
  shipped inside it.
- `gen.py` and `prompt.py` extract both closing style lines identically

## The next condensation pass — the brief the user gave

> "I also wonder, are you encoding TOO much in code? Remember that a model as smart
> as you will be running this."

So the next pass cuts differently from the first. The first removed duplication; this
one removes **instruction a competent reader does not need**: explanations of why an
obvious command works, defensive hand-holding, and prose that restates what the code
already enforces. Keep every *surprise* — `-rotate 90` being clockwise, the mask
inversion, `%[fx:]` scientific notation — because those are the facts a smart model
gets wrong by reasoning correctly from false premises. Cut the rest.

## Where the loop landed (passes 2-6)

Six condensation passes, each followed by an adversarial review:

| pass | net words | material bugs the next review found |
|---|---|---|
| 1 | -939 | 16 |
| 2 | -57 | 2 |
| 3 | -83 | 4 |
| 4 | -68 | 4 |
| 5 | -15 | 6 |
| 6 | -35 | 3 |

**Compression ended at pass 2.** Everything after was a correctness loop wearing a
succinctness loop's clothing, and it was worth running on those terms: it closed a false
all-clear in the gate verdict, seven taint gaps, a key-search hole in the subtree agents
write into most, a frozen-style drift, a documented prompt order that contradicted the
tool, and `.enc` being skipped — the one extension this vault teaches people to use.

**Every one of those was in a guard or a doc I wrote, and not one was found by me.**
`gate-6` on the floor question: "effectively yes", with ~60 words of slack in one place,
which was then cut. Treat the docs as at their floor; run reviews for correctness, not
for length.

## Rounds 10-16: the docs stayed ready; the findings moved to the gate itself

Seven more rounds. **Every round declared all four documents ready**, and freezing the
key-read detector at round 13 (its spellings recorded as accepted limits rather than
chased) is what made room for the findings that mattered:

- the **md5 digest binding existed in no document** — the defence against swapping a
  prompt or mask after the user reads the approval. Its only record was a selftest case
  name.
- the **digest recheck ran before the summary printed**, so the doc's claim that a file
  "cannot be swapped after the summary was read" described the one window it did NOT
  cover. `verify_digests()` now runs twice, the second time just before launch.
- **selftest wrote a structurally real, approvable request** and relied on `unlink()` with
  no `finally`. `gen.py` now stamps a marker under `VAULT_SELFTEST=1` and `unlock.py`
  refuses it.
- `find_plaintext_keys` matched names **case-sensitively**, so `API.KEY` was invisible.
- a bind file that could not be hashed was **silently skipped** while the summary claimed
  every file was bound; now it fails closed.
- digest keys mixed relative and absolute, so `unlock.py` run from another cwd failed
  closed on a readable file; keys are now vault-relative and resolved against ROOT.

**Two regressions of mine were caught by reviewers, not by me**, both in the credential
predicate: a 64-char cap that hid absolute paths (the house idiom), then a token-count
"prose" rule that hid five short shell reads the previous version caught. The second is the
sharpest lesson in the file: **my own probes endorsed the regression because they shared its
blind spot** — the two existing shell probes were 2-3 tokens.

## Round 9: the docs were declared READY

`gate-9`'s verdict: "**`rules.md`, `style.md`, both SKILL.md files — ready.** `bin/selftest.py`
— not ready." All three remaining findings were accidental-path bypasses of the key-read
detector, none in the documentation. That is the first round where the prose was clean.

Fixed: suffix tests other than `==` (`in {...}`, `endswith`, `".key" in p.name`,
`p.match("*.key")` — the last being the idiom `find_plaintext_keys` itself uses); callees
that are methods or lambdas rather than bare names; `READISH` missing bare `read`/`get`.
**43 probes.** Two of my own fixes were dead code until found: the lambda branch sat below
the generic `Assign` branch that swallowed it, and it used `_keyish(_fold(...))` where
`ROOT / "gpt.key"` folds to None — the predicate is now shared by every call-site test.

**The 165/7 receipt figure is correct**, re-verified across all 233 `generation.md` files
in the vault: 165 carry `^Style: v2` as a field, 7 mention it in prose only. `gate-9`
reported 172/4; 172 is 165+7, so that was a substring count. Fifth instrument-vs-doc
conflict of the session and the first where the REVIEWER's instrument was wrong — which
is why the rule is check the instrument, whoever is holding it.

## The threat model, added at round 8 — read this before chasing another bypass

`bin/selftest.py` and `rules.md` now state it: these guards assume the code is **not
hostile**. Anything able to edit `bin/` can delete the gate, so no guard resists that.
They catch a rule broken **by accident**. `gate-8` accepted the model and corrected its
scope: a weaker adversary who can write only *data* still defeats `find_plaintext_keys`
by hiding a key where it does not look (inside a `.png`, under a skipped subtree, past
1 MB), which is why those misses are enumerated rather than glossed.

**The test for whether a finding counts:** could someone write this innocently?
`with open("gpt.key") as f` — yes, real bug. A nested shadowing `def` inside the exempt
function — no, that needs write access to `bin/`, which could just delete the gate.
Without this test the reviews never run out of material and the loop cannot terminate on
its own terms.

## The repeated bug class, which cost five rounds

A guard that skips compound statements must handle EVERY header form. I fixed `for`,
then `with`, then `if`/`while` — three separate rounds, same bug, because each time I
fixed the instance instead of the class. When a guard examines statements, enumerate the
header-bearing node types once: `For`, `AsyncFor`, `With`, `AsyncWith`, `If`, `While`,
comprehensions, `NamedExpr`, `Compare`. It appeared a FOURTH time at round 8 (taint not
surviving `if p.suffix == ".key"`), which is the strongest possible argument for
enumerating the class rather than patching instances.

**Second repeated class, found at round 8:** a guard that compares duplicated code must
compare everything that code DEPENDS on. The byte-identity check on `find_plaintext_keys`
passed while `gen.py`'s `PLAINTEXT_KEY_GLOBS` had been widened and `unlock.py`'s had not —
the likeliest innocent edit in the file, and completely silent. It now compares
`PLAINTEXT_KEY_GLOBS`, `KEY_RE.pattern` and `BINARY_SUFFIXES` too, verified by
reproducing that exact one-sided edit.

## Process failures of mine, worth not repeating

- **`.claude/` has never been added to git** — not ignored, never added. `git ls-files
  .claude/` is empty. The two skills are the main artefact of this work and exist only
  as working files, which also meant a reviewer could not diff the condensation and a
  third of what I asked it to audit was unauditable. Snapshotted to the session
  scratchpad; a commit is the user's call.
- **Reviewer reports truncate before the verdict line.** Four times now. The fix is to
  demand the verdict first and cap the word count, not to re-ask for the whole report.
- **Twice this session a measurement bug of mine nearly rewrote a doc wrongly** — the
  `;`-swallowing regex above, and a 7-failure recipe harness whose failures were all
  missing fixtures and a substring replace mangling `pmask.png`. Both times the docs
  were right and my instrument was wrong. **Check the instrument before the artefact.**

## Unrelated, still open

- Scene 5 is at `outputs/the-rusty-robot/v061`, **not promoted**, and has 0 references
  in `pdf/one-shot.md`.
- The user must seal the API key: rotate first (the current key is in
  `~/.zsh_history`), then `! python3 -I bin/seal-key.py`, then `rm gpt.key`.
  `.api-key.enc` does not exist, so no paid call can run at all right now.
- $0 spent. Zero `backend=api` receipts in the vault.
