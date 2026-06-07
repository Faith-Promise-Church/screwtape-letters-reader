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

### Judgment calls (decided)

- **Letter XXII:** signature `SCREWTAPE, T.E . . . B.S . . . etc.` → `SCREWTAPE, T.E., B.S., etc.` The spaced dots were a scan artifact; fixed to the standard degree punctuation.
- **Letter XXXI:** the editorial gloss `tetter [skin disease]` is kept on purpose as a reader aid, even though it is not in Lewis's text.

### Left unchanged

- **Hyphenation variants** (e.g. `anti-climax`, `un-regularised`, `unselfconscious`, `two-pence`, `birth-right`, `un-rhythmical`, `out-manoeuvred`). Our copy and the online edition disagree on hyphens in a handful of words. Neither source is authoritative on hyphenation, so these were left unchanged.

## Third pass: spacing, line breaks, and PDF artifacts

A mechanical sweep of all 31 letters for odd spacing, broken line wraps,
misplaced punctuation, and invisible import junk. Findings were verified
against the source text, and substantive ones against a clean independent
edition (26reads), before editing.

### Paragraphs rejoined (PDF page-break splits)

The PDF page breaks had left 28 paragraphs split mid-sentence (one or two
per letter), so a single sentence rendered as two paragraphs. Example,
Letter I: `...the bus and the` + `newsboy) was enough...`. Each split was
confirmed continuous against the clean edition and rejoined. The legitimate
paragraph breaks in Letter XXII (`Music and silence...` and the editorial
`[Here the MS. breaks off...]` line) were left as separate paragraphs.

### Broken hyphenated words rejoined

A stray space after a line-break hyphen had split five compounds:

| Letter | Before | After |
|--------|--------|-------|
| VI | `anti- Christian` | `anti-Christian` |
| XXII | `two- faced` | `two-faced` |
| XXIII | `parade- ground` | `parade-ground` |
| XXIV | `over- refined` | `over-refined` |
| XXIX | `self- loathing` | `self-loathing` |

### Punctuation

- **Letter XXVIII:** `you tell me !with glee` → `you tell me with glee`. A stray exclamation mark from the scan (confirmed against a clean edition).
- **Letter XXII:** `...is not music is silence”` → `...silence”.` Restored the missing sentence period.

### Checked and left alone (not errors)

- The comma endings before the signature (e.g. Letter III `...the Enemy's story,` then `Your affectionate uncle`) are authentic; the last line runs into the valediction. Confirmed against the clean edition.
- `a No. 73 bus` (Letter I) and the numbered list `1. 2. 3. 4.` (Letter III) are correct.
- No form-feeds, non-breaking spaces, soft hyphens, zero-width characters, tabs, double spaces, or straight-quote slips remain. Front matter (intro, preface) was clean.

## Player

- Numbering aligned to the letters. Front matter is unnumbered. Letters are numbered 1 through 31 to match Letter I through Letter XXXI.
- Skip controls fixed. The 15 and 30 sit centered inside the circular arrows.
- Audio errors now show a "Test the file" link that opens the actual track URL.
- Layout rebuilt mobile-first with a contents drawer on small screens and a sidebar on wider screens. Intended for an iframe embed.
