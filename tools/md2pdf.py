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


def inline(t):
    t = html.escape(t)
    t = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', t)          # [[slug|text]] -> text
    t = re.sub(r'\[\[([^\]]+)\]\]', r'\1', t)                      # [[text]] -> text
    t = re.sub(r'\[([^\]]+)\]\((#[^)]*|/[^)]*)\)', r'\1', t)       # internal links -> text
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2">\1</a>', t)
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
        if re.match(r'^\s*\|', L) and i+1 < len(lines) and re.match(r'^\s*\|[\s:|-]+\|?\s*$', lines[i+1]):
            head = row(L); i += 2; body = []
            while i < len(lines) and re.match(r'^\s*\|', lines[i]):
                body.append(row(lines[i])); i += 1
            out.append('<table><thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in head) + '</tr></thead><tbody>')
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
.footer { margin-top: 14pt; padding-top: 5pt; border-top: .5pt solid #bbb; font-size: 8pt; color: #555; }
"""



def page(md, title, stamp):
    return (f"<!doctype html><meta charset='utf-8'><title>{html.escape(title)}</title>"
            f"<style>{CSS}</style>{convert(md)}"
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

    for src in a.pages:
        name = os.path.basename(src)[:-3]
        html_path = os.path.join(tmp, name + ".html")
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(page(open(src, encoding="utf-8").read(), name, stamp))
        pdf = os.path.join(out, name + ".pdf")
        subprocess.run([exe, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=9000", f"--print-to-pdf={pdf}",
                        "file://" + html_path],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        size = os.path.getsize(pdf) // 1024 if os.path.exists(pdf) else 0
        print(f"{name}.pdf  {size} KB")


if __name__ == "__main__":
    main()
