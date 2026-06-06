# Screwtape Reader

A self-contained, read-along audiobook player for *The Screwtape Letters*. One static HTML file holds the whole reader. The audio streams from S3. The page is built from editable source text by a small Python script with no dependencies.

## What is in here

```
screwtape-reader/
  build.py                 The build pipeline (standard library only)
  template.html            The player UI. Edit styling and behavior here.
  sources/
    book.json              Metadata, chapter order, audio host, and the manifest
    intro.html             Front matter: the Introduction (editable HTML)
    preface.html           Front matter: Lewis's Preface (editable HTML)
    letters/
      chapter_01.txt ...   One clean text file per letter (Letters I through XXXI)
    audio_links.csv        Reference list of the original audio filenames and URLs
  dist/
    screwtape-reader.html  The built file you deploy. Generated. Do not hand-edit.
  CHANGELOG.md             Record of the proofreading edits made to the source text
  CLAUDE.md                Orientation for working in Claude Code
```

## Requirements

Python 3.8 or newer. Nothing to install. The build uses only the standard library.

## Build

```
python build.py
```

This reads `sources/book.json`, pulls in each chapter's text, formats the letters, injects everything into `template.html`, and writes `dist/screwtape-reader.html`. To preview, open that file in any browser.

## Editing the content

**A letter.** Open the matching file in `sources/letters/`. These are clean prose: one paragraph per line, a blank line between paragraphs. The first line is the salutation and the closing lines are the signature. The build styles those automatically, so you only edit the words. Run `build.py` when done.

**The Introduction or Preface.** Edit `sources/intro.html` or `sources/preface.html`. These are HTML so the dedication, epigraphs, and signature keep their formatting. You can use `<p>`, `<em>`, `<h3>`, and inline styles.

**Titles, order, audio host, or the eyebrow labels.** Edit `sources/book.json`. Each chapter points to an audio filename and a text file. The full audio URL is `audioBase` plus the filename, so if the files ever move, change `audioBase` once.

After any edit, run `python build.py` and commit the updated `dist/screwtape-reader.html`.

## Deploy

**Option A, S3 (same bucket as the audio).** Upload the built file and set its type so the browser renders it.

```
aws s3 cp dist/screwtape-reader.html \
  s3://faithpromise.org/audio-files/Screwtape\ Letters/screwtape-reader.html \
  --content-type text/html
```

Then embed it in Webflow with an HTML embed element:

```html
<iframe src="https://s3.us-west-2.amazonaws.com/faithpromise.org/audio-files/Screwtape%20Letters/screwtape-reader.html"
        title="The Screwtape Letters"
        style="width:100%;height:85vh;min-height:560px;border:0;border-radius:12px;"
        loading="lazy"></iframe>
```

**Option B, GitHub Pages.** Turn on Pages for this repo and point it at the file, then iframe the Pages URL the same way. See the note below about keeping the repo private.

## Notes

**Audio loading.** The player shows a small "Test the file" link if a track fails to load. If that link opens and plays in a browser tab, the live site is fine. If it returns AccessDenied or NoSuchKey, the S3 objects are not set to public read, which is a bucket policy fix.

**Still to verify against a print copy.** Two spots in the source were left unchanged because correcting them would be a guess. See `CHANGELOG.md` for both. Fix them in the source text and rebuild when confirmed.

**Keep this repo private.** The full text of the book lives in `sources/`, so a public repo would publish it openly. A private repo gives you version history without that exposure.
