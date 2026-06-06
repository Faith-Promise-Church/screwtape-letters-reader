#!/usr/bin/env python3
"""
Build the read-along audiobook reader.

Reads:   sources/book.json   (metadata + chapter manifest)
         sources/*.html       (front matter, used verbatim)
         sources/letters/*.txt (one letter each, auto-formatted)
         template.html         (the player UI)
Writes:  dist/screwtape-reader.html

Pure standard library. Run:  python build.py
"""
import json, re, os

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(ROOT, "sources")
TPL  = os.path.join(ROOT, "template.html")
OUT  = os.path.join(ROOT, "dist", "screwtape-reader.html")

# salutation / signature styling for letters
SAL = "letter-spacing:.1em;font-size:.8em;text-transform:uppercase;color:var(--ink-soft);margin-bottom:1.7em"
SIG = "text-align:right;margin-top:2.4em;color:var(--ink-soft);line-height:1.7"

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def format_letter(raw):
    """Turn a clean .txt letter into styled HTML: salutation, paragraphs, signature."""
    raw = raw.replace("\r\n", "\n").replace("\r", "\n").replace("\f", " ").strip("\n")
    raw = re.sub(r" {2,}", " ", raw)
    paras = re.split(r"\n[ \t]*\n", raw)
    paras = [re.sub(r" {2,}", " ", re.sub(r"[ \t]*\n[ \t]*", " ", p)).strip() for p in paras]
    paras = [p for p in paras if p]

    parts = []
    # opening salutation (e.g. "MY DEAR WORMWOOD,")
    if paras and re.match(r"(?i)^my dear\b", paras[0]) and len(paras[0]) < 140:
        parts.append('<div style="%s">%s</div>' % (SAL, esc(paras.pop(0))))
    # closing signature ("Your affectionate uncle" / "SCREWTAPE")
    sig = []
    if paras and paras[-1].strip().upper().rstrip(".") == "SCREWTAPE":
        sig.insert(0, paras.pop())
        if paras and len(paras[-1]) < 90 and re.search(r"(?i)affectionate|uncle|sincerely|truly yours|yours", paras[-1]):
            sig.insert(0, paras.pop())
    for p in paras:
        parts.append("<p>%s</p>" % esc(p))
    if sig:
        lines = []
        for i, s in enumerate(sig):
            if i == len(sig) - 1:
                lines.append('<span style="letter-spacing:.14em;font-size:.92em">%s</span>' % esc(s))
            else:
                lines.append('<span style="font-style:italic">%s</span>' % esc(s))
        parts.append('<div style="%s">%s</div>' % (SIG, "<br>".join(lines)))
    return "\n\n".join(parts)

def main():
    manifest = json.load(open(os.path.join(SRC, "book.json"), encoding="utf-8"))
    base = manifest["audioBase"]

    chapters = []
    for ch in manifest["chapters"]:
        text_path = os.path.join(SRC, ch["text"])
        raw = open(text_path, encoding="utf-8").read()
        text = raw if ch.get("format") == "html" else format_letter(raw)
        entry = {"num": ch.get("num"), "title": ch["title"], "src": base + ch["audio"], "text": text}
        if ch.get("eyebrow"):
            entry["eyebrow"] = ch["eyebrow"]
        chapters.append(entry)

    book = {
        "eyebrow": manifest.get("eyebrow", ""),
        "title": manifest["title"],
        "author": manifest.get("author", ""),
        "chapters": chapters,
    }

    tpl = open(TPL, encoding="utf-8").read()
    start = tpl.index("const BOOK = ")
    end = tpl.index("\n\n/* ============================================================\n   2) PLAYER ENGINE")
    out_html = tpl[:start] + "const BOOK = " + json.dumps(book, indent=2, ensure_ascii=False) + ";" + tpl[end:]

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(out_html)
    print("Built %s  (%d chapters, %.0f KB)" % (os.path.relpath(OUT, ROOT), len(chapters), len(out_html.encode()) / 1024))

if __name__ == "__main__":
    main()
