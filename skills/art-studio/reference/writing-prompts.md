# Writing a spec the model obeys

The Style Block and the closing line are handled for you by `prompt.py`. This is
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

## Give a scene one single-view crop per cast member

Attach the anchor, then one IDENTITY crop per cast member: one full-body view cut from
the approved `reference.png` with ImageMagick (`reference/imagemagick.md` → *Crop,
resize, deliverables*), with no expression portraits, other views or lettering, saved
to the output folder's `sources/`. **Never attach a multi-view sheet to a scene**,
because a scene given four sheets among five inputs once copied their *format* and
returned a character-design page, while in a controlled comparison single-view crops
matched or beat sheets and a lineup on likeness and never did that.

- Pick the view closest to the pose the scene needs, because the model copies the
  crop's stance.
- State relative heights in the spec, because crops carry no scale.
- The five-attachment cap leaves room for four crops beside the anchor, three if a
  baseline rides along as EDIT TARGET; carry anyone beyond that in text.
- Keep the single-image guard in the spec ("one single continuous scene painting, not
  a character sheet; each person appears exactly once"), because it may be doing much
  of the protective work.
- Use a group lineup only when height is the point, and check it against the
  individual sheets, because the scene inherits the lineup's own drift and stiff row.
  If it carries lettering, ban reproducing its numbers.

## Prompt a Layer so it separates

A Layer of a Layered Scene (`reference/layered-scenes.md`) gets its transparency only
from the prompt, because the image tool takes no transparency setting. Build it with
`prompt.py`'s Layer options:

```bash
python3 $S/prompt.py --package PKG --role STYLE: --role PLACEMENT: \
  --layer-name "<layer-id>" --below "<what lies beneath>" --above "<what lies above>" \
  --opaque "<its solid subjects>" --soft "<its glow, flames or haze>" \
  --spec-file "$T/spec.txt" -o "$T/prompt.txt"
```

- `--layer-name`, `--below` and `--above` say the image is one Layer and what lies
  around it, so the model paints only this Layer's subjects.
- `--opaque` and `--soft` add the transparent-background block, which every Layer
  prompt carries, edits included, because the model ignores an EDIT TARGET's alpha and
  otherwise returns the Layer opaque. Only a bottom Layer that fills the Frame omits
  it; `gen.py` warns about any other.
- Name in the spec what not to paint from a PLACEMENT image ("paint none of the rocks
  or ships"), because the model may copy it.
- Say in a lower Layer's spec that it is painted whole where upper Layers will cover it
  ("the whole disc, including where the ships cross it"), because moving an upper
  subject later reveals it.
- Put glow, flames and haze under `--soft`, so the Layers beneath show through them.
  Generate a Layer whose content is light only with `gen.py --emissive`, which repairs
  glow baked onto black. Never mark other Layers emissive, because the repair makes
  opaque content partly transparent.

## Attach the minimum identity input

Full source → crop → nothing. Attach the least that carries information the design
text cannot. If a candidate resembles a source's rendering or layout more than the
anchor's, the identity input is dominating: **describe more, attach less.**
