# Writing a spec the model obeys

The Style Block and the closing line are handled for you by `bin/prompt.py`. This is
about the part you write: the `--task` line and the `--spec-file` body.

## Replace prohibitions with countable positive statements

**A ban list leaves the model free to satisfy every clause and still be wrong.** Ban
loops, rings, cages and guard plates and you get an L-bracket — because nothing
banned a *bend*. A counted statement of what the thing **is** cannot be gamed that
way.

Three patterns carry most of it.

**Enumerate, do not count.** "Exactly four of them" fails however many times it is
repeated. Describe each one in turn, then close the set: "beyond the fourth the ridge
is empty."

**Point at something already in the frame.** "Turn it away from the camera" is a
direction the model cannot verify against the canvas. "Its front face lies in the
same plane as X, and is foreshortened as hard" is one it can.

**Then bound it with a number.** A referent fixes orientation but not proportion —
specify a facet by width alone and it comes back a tall upright slab. Give the ratio
("2–3x wider than tall") and it resolves.

Prefer one positive sentence to a ban that keeps failing. This succeeds:

> across the whole ground use only THREE OR FOUR flat tones in total, each an
> unbroken field, with NO marking inside any of them; all drawing happens at the
> edges where fields meet

where "do NOT break the ground into chips, facets, dashes, hatching" never does.

**When a prohibition has failed twice, stop adding nouns to the ban list** and write
the positive form with a number in it.

## State the aspect ratio in the prompt body, every time

`--size` is advisory on the Codex backend — it has returned 2:1 when asked for 3:2.
Put the ratio in the spec, and say what it is *not*:

> THE PICTURE MUST BE A 3:2 HORIZONTAL RECTANGLE — exactly one and a half times as
> wide as it is tall, the proportions of a 1536 x 1024 image.

`--size` alone is not a constraint. The prompt is.

## Scale drifts upward every pass

Framing asks are ignored unless the last miss is quantified. Measure the previous
candidate, put the number in the spec, and give the model a tiebreak:

> the last attempt filled 40 percent of frame width; the cap is one fifth. If unsure,
> paint it smaller.

`reference/imagemagick.md` has the measurement commands.

## Budget the five attachment slots

`gen.py` refuses a sixth attachment before anything runs. Left to the backend,
`image_gen` rejects it only after consuming an orchestration turn. Anchor + baseline
+ identities must total five.

**Never stack several multi-view sheets on a SCENE.** With four sheets among five
inputs, a scene imitated the *format* of its inputs and returned a character-design
document. Attach the anchor, the baseline as EDIT TARGET, and **at most one** identity
sheet — a single group lineup beats several individual sheets. Carry the rest of the
cast in text. If an identity input contains lettering, ban reproducing its numbers.

## Attach the minimum identity input

Full source → crop → nothing. Attach the least that carries information the design
text cannot. If a candidate resembles a source's rendering or layout more than the
anchor's, the identity input is dominating: **describe more, attach less.**

## Positional binding only

Images reach the model by attachment order. "Image 1" is a promise about order, not
about a filename, which is why `--role` and `--attach` must be given in the same
sequence. The one exception is a masked API call, where the EDIT TARGET takes image 1
and the anchor follows — build those with `bin/prompt.py --masked`, and see
`reference/fixing-an-image.md`.
