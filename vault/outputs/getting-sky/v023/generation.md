# getting-sky v023

Source: local composite, no generation. ImageMagick only; nothing was billed.
NOT raw model output.

User request verbatim: "oh wait there is a 3rd engine fire coming out the back. not connected to an engine"

## Sources

| region | from |
|---|---|
| everything | **v021** (blend pass off v017) |
| band along the stray spine trail | **v017** (same gorge, no trails), haze-matched, via `mask-stray-trail.png` (line 520,342 → 1062,566, width 44, blur 0x8) |

The blend passes (v018–v022) all invented a third exhaust from the Antares's raised
spine. The band over that trail is filled from v017, the pre-blend composite of the
same approved gorge, with v021's sand veil reproduced by a linear tone match measured
on a parallel strip (line 520,292 → 1000,490, width 30): gain 0.888, offset R +6.6%,
G +7.2%, B +8.0%.

```bash
magick v017.png -evaluate multiply 0.888 -channel R -evaluate add 6.6% \
  -channel G -evaluate add 7.2% -channel B -evaluate add 8.0% +channel v17haze.png
magick v17haze.png mask-stray-trail.png -alpha off -compose CopyOpacity -composite st.png
magick v021.png st.png -compose over -composite -alpha off image.png
```

Status: awaiting user evaluation

Review: User: engines not symmetrical — the far (right) pod sits too far forward. Inherited from the isolated pose painting (getting-sky-antares-pose v001).
