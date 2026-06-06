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

### Left unchanged, needs a print-copy check

These look wrong but the correct reading is a guess, so they were left as is. Confirm against a print edition, then fix the source and rebuild.

- **Letter XX:** `ratio-circle of the eye`. Appears garbled. Likely "role of the eye".
- **Letter XVI:** `other un-essentials`. Possibly "unessentials" or "non-essentials".

## Player

- Numbering aligned to the letters. Front matter is unnumbered. Letters are numbered 1 through 31 to match Letter I through Letter XXXI.
- Skip controls fixed. The 15 and 30 sit centered inside the circular arrows.
- Audio errors now show a "Test the file" link that opens the actual track URL.
- Layout rebuilt mobile-first with a contents drawer on small screens and a sidebar on wider screens. Intended for an iframe embed.
