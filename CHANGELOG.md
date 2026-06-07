# Changelog

## Initial cleanup of the source text

The letter text was extracted from a PDF and carried a few scan artifacts. The edits below are baked into the source files in `sources/`. Lewis's wording was preserved. Only clear scan errors and formatting junk were touched.

### Corrections applied

| Location | Before | After | Reason |
|----------|--------|-------|--------|
| Preface | `disposed or excitable` | `ill-disposed or excitable` | restored a word the scan dropped |
| Letter I | `modem investigation` | `modern investigation` | scan error |
| Letter I | `"true" of "false"` | `"true" or "false"` | scan error |
| Letter III | `himself ,which` | `himself, which` | spacing around comma |
| Letter XVII | `the great, achievements` | `the great achievements` | stray comma removed |
| Letter XIX | `over-weaning` | `overweening` | scan error |
| All 31 letters | one stray page-break character each (32 total) | removed | PDF page break |

## Second pass: checked against an online edition

The full text was compared letter by letter against the copy at
thespiritlife.net (cross-checked against other online editions where a
reading was substantive). That source is faithful on accents but carries
its own scan errors, so each difference was judged on its own, not copied
blindly. The edits below restore Lewis's wording where our copy had lost it.

### Corrections applied (second pass)

| Location | Before | After | Reason |
|----------|--------|-------|--------|
| Letter I | `a trifle naive` | `a trifle naïf` | scan dropped the accent; Lewis's spelling |
| Letter XV | `naively` | `naïvely` | scan dropped the accent |
| Letter XV | `eternity. . .It` | `eternity. . . It` | missing space after the ellipsis |
| Letter XVII | `please . . .all` | `please . . . all` | missing space after the ellipsis |
| Letter XXI | `a time with the friend` | `a tête-à-tête with the friend` | scan mangled the French phrase (confirmed against multiple editions) |
| Letter XXII | `facade` | `façade` | scan dropped the cedilla |
| Letter XXIV | `naivety` | `naïvety` | scan dropped the accent |

### Resolved (the two spots that had needed a print-copy check)

Both were confirmed against the online edition and other sources, then fixed.

- **Letter XX:** `ratio-circle of the eye` → `rôle of the eye`.
- **Letter XVI:** `other un-essentials` → `other unessentials`.

### Still open for a decision

- **Letter XXXI:** our copy carries an editorial gloss, `tetter [skin disease]`, that is not in Lewis's text. It may be a deliberate reader aid. Keep it or drop it.
- **Letter XXII:** the signature reads `SCREWTAPE, T.E . . . B.S . . . etc.` The online edition prints the degrees as `T.E., B.S., etc.` Our spaced dots look like a scan artifact, but the exact punctuation varies by edition, so it was left as is pending a decision.
- **Hyphenation variants** (e.g. `anti-climax`, `un-regularised`, `unselfconscious`, `two-pence`, `birth-right`, `un-rhythmical`, `out-manoeuvred`). Our copy and the online edition disagree on hyphens in a handful of words. Neither source is authoritative on hyphenation, so these were left unchanged.

## Player

- Numbering aligned to the letters. Front matter is unnumbered. Letters are numbered 1 through 31 to match Letter I through Letter XXXI.
- Skip controls fixed. The 15 and 30 sit centered inside the circular arrows.
- Audio errors now show a "Test the file" link that opens the actual track URL.
- Layout rebuilt mobile-first with a contents drawer on small screens and a sidebar on wider screens. Intended for an iframe embed.
