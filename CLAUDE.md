# CLAUDE.md

Orientation for working on this project in Claude Code.

## What this is

A read-along audiobook reader for *The Screwtape Letters*. The deliverable is one static HTML file (`dist/screwtape-reader.html`) that is embedded on the Faith Promise Webflow site through an iframe. Audio streams from S3. The page is generated from source text by `build.py`.

## The one rule that matters

`dist/screwtape-reader.html` is generated. Never hand-edit it. Change the inputs and rebuild.

- UI, styling, player behavior: edit `template.html`
- Letter text: edit `sources/letters/chapter_NN.txt`
- Front matter: edit `sources/intro.html` and `sources/preface.html`
- Metadata, order, audio host: edit `sources/book.json`

Then run `python build.py` and verify.

## Build and verify

```
python build.py
```

The build is standard library only. Keep it that way. Do not add dependencies or a package manager.

After building, sanity check:
- 33 chapters total (Introduction, Preface, Letters I through XXXI)
- No form-feed characters in the output
- The file opens and plays in a browser

## How letters are formatted

`format_letter()` in `build.py` parses a clean `.txt`:
- Paragraphs are split on blank lines and rejoined into flowing prose.
- A first line that opens with "MY DEAR" becomes the styled salutation.
- A trailing "SCREWTAPE" with its preceding line becomes the styled signature.

So letter source files stay plain and readable. Do not put HTML in them. The front matter files are the opposite: they are HTML on purpose.

## Voice and style for any human-facing copy

If you write or revise reader-facing prose, such as the Introduction, follow the house style: no em dashes, no "not X but Y" contrast phrasing, no three-word fragment bursts, plain spoken pastoral tone at about a ninth grade reading level. This does not apply to code or to Lewis's own text, which stays as written.

## Open TODOs

1. Two source spots need a print-copy check before fixing. See `CHANGELOG.md`: Letter XX "ratio-circle of the eye" and Letter XVI "other un-essentials".
2. Confirm the S3 audio objects are public read so the live embed plays. The player surfaces a test link when a track fails.
3. Optional: true word-level read-along highlighting would need per-line or per-word timing data, which does not exist yet.

## Deploy

See `README.md`. Short version: build, then either `aws s3 cp` the file to the bucket with `--content-type text/html`, or serve it from GitHub Pages, then iframe it into Webflow.
