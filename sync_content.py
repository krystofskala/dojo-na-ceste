# -*- coding: utf-8 -*-
"""
Sync content/*.md files into data/site-content.json and data/aktuality.json.

Workflow:
  1. Edit the .md files in content/pages/ and content/aktuality.md by hand
     (or drop in text you scraped/transcribed yourself from anywhere you like).
  2. Run:  python sync_content.py
  3. Refresh the site in your browser — index.html, historie.html etc. read
     the JSON files directly, so changes show up immediately.

This only ever reads content/*.md and writes data/*.json. It never touches
the live web; you provide the text, this just moves it into the format the
site already knows how to render.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES_DIR = os.path.join(ROOT, "content", "pages")
AKTUALITY_MD = os.path.join(ROOT, "content", "aktuality.md")
SITE_CONTENT_JSON = os.path.join(ROOT, "data", "site-content.json")
AKTUALITY_JSON = os.path.join(ROOT, "data", "aktuality.json")

KEY_RE = re.compile(r"<!--\s*key:\s*(.+?)\s*-->")
SOURCE_RE = re.compile(r"<!--\s*source:\s*(.+?)\s*-->")
LABEL_RE = re.compile(r"<!--\s*([^-].*?)\s*-->")  # first non key/source comment
PHOTO_LINE_RE = re.compile(r'^!\[(.*?)\]\((\S+?)(?:\s+"(.*?)")?\)\s*$', re.M)


def sync_pages():
    if not os.path.isdir(PAGES_DIR):
        print("no content/pages directory, skipping page content sync")
        return []

    entries = []
    for fname in sorted(os.listdir(PAGES_DIR)):
        if not fname.endswith(".md"):
            continue
        page = fname[:-3] + ".html"
        path = os.path.join(PAGES_DIR, fname)
        with open(path, encoding="utf-8") as f:
            text = f.read()

        blocks = [b.strip() for b in text.split("\n---\n")]
        for block in blocks:
            if not block.strip():
                continue
            m_key = KEY_RE.search(block)
            if not m_key:
                continue
            key = m_key.group(1).strip()
            m_source = SOURCE_RE.search(block)
            source_url = m_source.group(1).strip() if m_source else ""

            # label = the first HTML comment that isn't key/source
            label = key
            for line in block.splitlines():
                line = line.strip()
                if line.startswith("<!--") and "key:" not in line and "source:" not in line:
                    lm = re.match(r"<!--\s*(.*?)\s*-->", line)
                    if lm:
                        label = lm.group(1)
                        break

            # body = the block with every HTML-comment line removed (metadata
            # comments can appear anywhere at the top, with or without blank
            # lines between them)
            body_lines = [l for l in block.splitlines() if not re.match(r"^\s*<!--.*-->\s*$", l)]
            body = "\n".join(body_lines).strip()
            body_html = md_to_html(body)

            entries.append({
                "key": key,
                "page": page,
                "label": label,
                "sourceUrl": source_url,
                "text": body_html,
            })

    os.makedirs(os.path.dirname(SITE_CONTENT_JSON), exist_ok=True)
    with open(SITE_CONTENT_JSON, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    print(f"site-content.json: wrote {len(entries)} entries")
    return entries


def sync_aktuality():
    if not os.path.isfile(AKTUALITY_MD):
        print("no content/aktuality.md, skipping aktuality sync")
        return []

    with open(AKTUALITY_MD, encoding="utf-8") as f:
        text = f.read()

    # strip the leading instructional comment block
    text = re.sub(r"^(<!--.*?-->\s*)+", "", text, flags=re.S)

    entries = []
    current_year = None
    posts = re.split(r"\n(?=#{1,2} )", text)
    for chunk in posts:
        chunk = chunk.strip()
        if not chunk:
            continue
        if chunk.startswith("# "):
            current_year = chunk[2:].strip()
            continue
        if not chunk.startswith("## "):
            continue
        first_line, _, rest = chunk.partition("\n")
        date = first_line[3:].strip()
        rest = rest.strip()
        rest = re.sub(r"\n---\s*$", "", rest).strip()

        photo = photo_alt = photo_source = None
        m = PHOTO_LINE_RE.search(rest)
        if m:
            photo_alt, photo, photo_source = m.group(1), m.group(2), m.group(3) or ""
            rest = (rest[:m.start()] + rest[m.end():]).strip()

        entries.append({
            "id": len(entries) + 1,
            "year": current_year,
            "date": date,
            "text": md_to_html(rest),
            "photo": photo,
            "photoAlt": photo_alt,
            "photoSource": photo_source,
        })

    os.makedirs(os.path.dirname(AKTUALITY_JSON), exist_ok=True)
    with open(AKTUALITY_JSON, "w", encoding="utf-8") as f:
        json.dump(entries, f, ensure_ascii=False, indent=2)
    print(f"aktuality.json: wrote {len(entries)} entries")
    return entries


def md_to_html(text):
    """Minimal markdown -> HTML: paragraphs, **bold**, *italic*, [text](url), '- ' lists.
    If the text already looks like HTML (starts with a tag), it's passed through as-is."""
    text = text.strip()
    if not text:
        return ""
    if text.startswith("<"):
        return text

    paragraphs = re.split(r"\n\s*\n", text)
    html_parts = []
    for para in paragraphs:
        lines = [l.strip() for l in para.splitlines() if l.strip()]
        if not lines:
            continue
        if all(l.startswith("- ") for l in lines):
            items = "".join(f"<li>{inline_md(l[2:])}</li>" for l in lines)
            html_parts.append(f"<ul>{items}</ul>")
        else:
            html_parts.append(f"<p>{inline_md(' '.join(lines))}</p>")
    return "\n".join(html_parts)


def inline_md(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"(?<![\w_])_(?!_)(.+?)(?<!_)_(?![\w_])", r"<em>\1</em>", s)
    s = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', s)
    return s


if __name__ == "__main__":
    sync_pages()
    sync_aktuality()
    print("Done. Refresh the site in your browser to see the changes.")
