#!/usr/bin/env python3
"""md2pdf — turn graph pages into corporate PDFs.

    python3 tools/md2pdf.py "legal/articles of association.md" ...
    python3 tools/md2pdf.py -o ~/Desktop/pack legal/*.md

Renders each markdown page as A4 print HTML in the corporate typeface (Play,
Google Fonts) and prints it to PDF through headless Brave/Chrome. Wiki-links and
internal anchors become plain text — a printed page has nothing to click.

Output defaults to ./pdf next to the working directory. --stamp sets the date in
the footer; today by default.
"""
import argparse
import datetime
import html
import os
import re
import subprocess
import sys
import tempfile



PAGES = {}         # normalised page name -> markdown path
TITLES = {}        # markdown path -> (h1 title, {anchor slug: heading text})


def slugify(text):
    """Reproduce the anchor ids the graph renderer builds from a heading."""
    t = re.sub(r'\*\*|__|`|\[\[|\]\]', '', text)
    t = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', t)
    t = t.split('|')[-1] if '|' in t else t
    t = re.sub(r'[^0-9a-zA-Z\s-]', '', t.lower())
    return re.sub(r'-+', '-', re.sub(r'\s+', '-', t.strip())).strip('-')


def build_index(root):
    """Map every markdown page in the tree so footnotes can name their target."""
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for f in files:
            if f.endswith('.md'):
                path = os.path.join(base, f)
                PAGES.setdefault(f[:-3].lower().replace('-', ' '), path)


def headings(path):
    """(title, {anchor: heading}) for a page, read once and cached."""
    if path not in TITLES:
        title, anchors = os.path.basename(path)[:-3], {}
        try:
            first = True
            for line in open(path, encoding='utf-8'):
                m = re.match(r'^(#{1,6})\s+(.*?)\s*$', line)
                if not m:
                    continue
                text = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', m.group(2))
                text = re.sub(r'\*\*|\[\[|\]\]', '', text)
                text = re.sub(r'[\u25b2\u26a0\ufe0f]', '', text).strip()
                if first and len(m.group(1)) == 1:
                    title, first = text, False
                anchors[slugify(text)] = text
        except OSError:
            pass
        TITLES[path] = (title, anchors)
    return TITLES[path]


def resolve(name):
    return PAGES.get(name.lower().replace('-', ' '))


REFS = []          # ordered list of footnote targets for the document being built
REF_INDEX = {}     # target -> footnote number


def words(slug):
    """`8-exit` -> `Exit`, `articles-of-association` -> `articles of association`."""
    t = slug.replace('-', ' ').replace('_', ' ').strip()
    m = re.match(r'^(\d+[a-z]?)\s+(.*)$', t)
    if m:
        return "\u00a7" + m.group(1) + " " + m.group(2)
    return t


def where(url, source=None):
    """Describe a link target the way a reader of paper needs it."""
    if url.startswith('http'):
        return url
    page_part, _, anchor = url.partition('#')
    page_part = page_part.strip('/')
    if page_part.startswith('cyber-valley/cve/'):
        page_part = page_part[len('cyber-valley/cve/'):]

    path = resolve(page_part.rsplit('/', 1)[-1]) if page_part else source
    title, anchors = headings(path) if path else (words(page_part.rsplit('/', 1)[-1]), {})
    section = anchors.get(anchor) or (words(anchor) if anchor else '')

    if not page_part:
        return f"this document, {section}" if section else "this document"
    return f"{title}, {section}" if section else title


SOURCE = [None]    # path of the page being converted, for same-document anchors


def ref(target):
    """Register a footnote and return its number, reusing one per target."""
    key = where(target, SOURCE[0])
    if key not in REF_INDEX:
        REFS.append(key)
        REF_INDEX[key] = len(REFS)
    return REF_INDEX[key]


def note(text, target):
    return f'{text}<sup class="ref">{ref(target)}</sup>'


def inline(t):
    t = html.escape(t)
    t = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', lambda m: note(m.group(2), m.group(1)), t)
    t = re.sub(r'\[\[([^\]]+)\]\]', lambda m: note(m.group(1), m.group(1)), t)
    t = re.sub(r'\[([^\]]+)\]\((#[^)]*|/[^)]*)\)', lambda m: note(m.group(1), m.group(2)), t)
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', lambda m: note(m.group(1), m.group(2)), t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    return t


def row(line):
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    return cells

def convert(md):
    md = re.sub(r'^---\n.*?\n---\n', '', md, flags=re.S)           # frontmatter
    out, lines, i = [], md.split('\n'), 0
    while i < len(lines):
        L = lines[i]
        if re.match(r'^\s*\|', L):
            has_header = i+1 < len(lines) and re.match(r'^\s*\|[\s:|-]+\|?\s*$', lines[i+1])
            head = row(L) if has_header else None
            i += 2 if has_header else 1
            body = [] if has_header else [row(L)]
            while i < len(lines) and re.match(r'^\s*\|', lines[i]):
                body.append(row(lines[i])); i += 1
            out.append('<table>')
            if head:
                out.append('<thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead>')
            out.append('<tbody>')
            for r in body:
                out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>')
            out.append('</tbody></table>')
            continue
        m = re.match(r'^(#{1,6})\s+(.*)$', L)
        if m:
            n = len(m.group(1)); out.append(f'<h{n}>{inline(m.group(2))}</h{n}>'); i += 1; continue
        if re.match(r'^\s*(---|___|\*\*\*)\s*$', L):
            out.append('<hr>'); i += 1; continue
        if L.startswith('>'):
            buf = []
            while i < len(lines) and lines[i].startswith('>'):
                buf.append(lines[i].lstrip('>').strip()); i += 1
            out.append('<blockquote>' + ''.join(
                f'<p>{inline(p)}</p>' for p in '\n'.join(buf).split('\n\n') if p.strip()) + '</blockquote>')
            continue
        m = re.match(r'^\s*([-*+]|\d+\.)\s+(.*)$', L)
        if m:
            ordered = bool(re.match(r'^\s*\d+\.', L)); tag = 'ol' if ordered else 'ul'
            items = []
            while i < len(lines) and re.match(r'^\s*([-*+]|\d+\.)\s+', lines[i]):
                items.append(re.sub(r'^\s*([-*+]|\d+\.)\s+', '', lines[i])); i += 1
            out.append(f'<{tag}>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + f'</{tag}>')
            continue
        if L.strip() == '':
            i += 1; continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(#{1,6}\s|\s*\||>|\s*([-*+]|\d+\.)\s)', lines[i]):
            buf.append(lines[i].rstrip()); i += 1
        if not buf:
            buf.append(lines[i].rstrip()); i += 1
        out.append('<p>' + inline(' '.join(buf)) + '</p>')
    return '\n'.join(out)

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Play:wght@400;700&display=swap');
@page { size: A4; margin: 20mm 18mm 20mm 18mm; }
body { font-family: 'Play', 'Helvetica Neue', sans-serif; font-size: 10.5pt; line-height: 1.5; color: #000; }
h1 { font-size: 16pt; margin: 0 0 4pt; }
h2 { font-size: 12.5pt; margin: 16pt 0 5pt; border-bottom: .5pt solid #999; padding-bottom: 2pt; page-break-after: avoid; }
h3 { font-size: 11pt; margin: 12pt 0 4pt; page-break-after: avoid; }
p { margin: 0 0 6pt; text-align: justify; }
table { border-collapse: collapse; width: 100%; margin: 6pt 0 10pt; font-size: 9.5pt; page-break-inside: auto; }
th, td { border: .5pt solid #666; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #eee; font-weight: bold; }
tr { page-break-inside: avoid; }
blockquote { margin: 6pt 0 8pt; padding: 5pt 9pt; border-left: 2pt solid #666; background: #f6f6f6; }
blockquote p { margin: 0 0 4pt; }
li { margin-bottom: 3pt; }
code { font-family: 'Play', monospace; font-size: 9.5pt; }
hr { border: 0; border-top: .5pt solid #bbb; margin: 10pt 0; }
a { color: #000; text-decoration: none; }
sup.ref { font-size: 7.5pt; line-height: 0; vertical-align: super; padding-left: .5pt; }
.notes { page-break-before: auto; margin-top: 16pt; }
.notes h2 { font-size: 11pt; }
.notes ol { list-style: none; padding-left: 0; font-size: 9pt; column-count: 2; column-gap: 14pt; }
.notes li { margin-bottom: 2.5pt; break-inside: avoid; }
.notes .n { display: inline-block; min-width: 13pt; font-weight: bold; }
.footer { margin-top: 14pt; padding-top: 5pt; border-top: .5pt solid #bbb; font-size: 8pt; color: #555; }
"""



def page(md, title, stamp, source=None):
    SOURCE[0] = source
    REFS.clear()
    REF_INDEX.clear()
    body = convert(md)
    notes = ""
    if REFS:
        rows = "".join(
            f'<li><span class="n">{i}</span> {html.escape(t)}</li>'
            for i, t in enumerate(REFS, 1))
        notes = f'<div class="notes"><h2>References</h2><ol>{rows}</ol></div>'
    return (f"<!doctype html><meta charset='utf-8'><title>{html.escape(title)}</title>"
            f"<style>{CSS}</style>{body}{notes}"
            f"<div class='footer'>PT. Cyber Valley Estate &middot; {html.escape(title)} &middot; {stamp}</div>")


BROWSERS = [
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
]


def browser():
    for b in BROWSERS:
        if os.path.exists(b):
            return b
    sys.exit("no Chromium-based browser found — install Brave or Chrome")


def main():
    ap = argparse.ArgumentParser(description="markdown pages to corporate PDF")
    ap.add_argument("pages", nargs="+", help="markdown files")
    ap.add_argument("-o", "--out", default="pdf", help="output directory")
    ap.add_argument("--stamp", default=None, help="date printed in the footer")
    a = ap.parse_args()

    stamp = a.stamp or datetime.date.today().strftime("%d %B %Y")
    out = os.path.expanduser(a.out)
    os.makedirs(out, exist_ok=True)
    tmp = tempfile.mkdtemp(prefix="md2pdf-")
    exe = browser()
    build_index(os.path.dirname(os.path.abspath(a.pages[0])) or ".")
    build_index(".")

    for src in a.pages:
        name = os.path.basename(src)[:-3]
        html_path = os.path.join(tmp, name + ".html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(page(open(src, encoding="utf-8").read(), name, stamp, src))
        pdf = os.path.join(out, name + ".pdf")
        subprocess.run([exe, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=9000", f"--print-to-pdf={pdf}",
                        "file://" + html_path],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        size = os.path.getsize(pdf) // 1024 if os.path.exists(pdf) else 0
        print(f"{name}.pdf  {size} KB")


if __name__ == "__main__":
    main()
