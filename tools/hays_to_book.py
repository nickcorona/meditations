#!/usr/bin/env python3
"""Convert a plain-text copy of the Gregory Hays translation of the Meditations (the
archive.org "FULL TEXT" download, meditations-GeorgeHays_djvu.txt) into book.md, the format
Cue Home reads: "# Book N" headings and one "## N.M" heading per entry.

Usage: python3 tools/hays_to_book.py hays.txt book.md

It finds the twelve books after the introduction, splits each into numbered entries (only
accepting the next number in sequence, or the same number with a letter like 4.49a, so lists
and stray numbers inside an entry don't split it), rejoins lines wrapped by the scan, mends
paragraphs broken across pages, and stops at the Notes. Book 1's entry titles ("MY
GRANDFATHER VERUS") are kept as a short first line.
"""
import re
import sys

ENTRY = re.compile(r'^(\d+)([a-z]?)\.\s*(.*)$')
BOOK = re.compile(r'^Book\s+(\d+)\s*$')
LIST = re.compile(r'^([ivx]+|[a-z])\.\s|^\u2022')  # "i. ...", "a. ...", bullets
END_PUNCT = tuple('.?!:;"”’\'")]>')


def find_books(lines):
    """Index of each "Book N" heading line in the body, in order 1..12, and where the Notes start.
    The contents page writes "Book 1: Debts and Lessons" (with a colon) but also bare "Book 4"
    and up, so the scan starts at the first bare "Book 1" and takes the books in order from there."""
    first = next((i for i, l in enumerate(lines) if l.strip() == 'Book 1'), None)
    if first is None:
        sys.exit('could not find Book 1')
    starts, want = {}, 1
    for i in range(first, len(lines)):
        m = BOOK.match(lines[i].strip())
        if m and int(m.group(1)) == want:
            starts[want] = i
            want += 1
            if want > 12:
                break
    if len(starts) != 12:
        sys.exit(f'found {len(starts)} of 12 books')
    end = next((i for i in range(starts[12], len(lines)) if lines[i].strip() == 'Notes'), len(lines))
    return starts, end


def paragraphs(lines):
    """Wrapped lines -> paragraphs; a blank line ends one. Hyphen and dash line ends join tight."""
    out, cur = [], ''
    for raw in lines:
        line = raw.strip()
        if not line:
            if cur:
                out.append(cur)
            cur = ''
            continue
        if not cur:
            cur = line
        elif cur.endswith(('-', '—')):
            cur = cur + line
        else:
            cur = cur + ' ' + line
    if cur:
        out.append(cur)
    # A page break in the scan splits a paragraph mid-sentence: rejoin when the first part has no
    # closing punctuation and the next starts in lower case.
    merged = []
    for p in out:
        if merged and not merged[-1].endswith(END_PUNCT) and p[:1].islower() and not LIST.match(p):
            sep = '' if merged[-1].endswith(('-', '—')) else ' '
            merged[-1] = merged[-1] + sep + p
        else:
            merged.append(p)
    return merged


def split_book(n, lines):
    entries, cur, expect = [], None, 1
    for line in lines:
        m = ENTRY.match(line.strip())
        if m:
            num, letter = int(m.group(1)), m.group(2)
            if (num == expect and not letter) or (cur and letter and num == expect - 1):
                cur = {'ref': f'{n}.{num}{letter}', 'lines': [m.group(3)]}
                entries.append(cur)
                if not letter:
                    expect = num + 1
                continue
        if cur is not None:
            cur['lines'].append(line)
    out = []
    for e in entries:
        lines = e['lines']
        title = None
        if n == 1:
            # Book 1 entries open with a title in capitals, sometimes over two lines.
            caps = []
            while lines and lines[0].strip() and lines[0].strip() == lines[0].strip().upper() and re.search('[A-Z]', lines[0]):
                caps.append(lines.pop(0).strip())
            if caps:
                title = ' '.join(caps).title()
        paras = paragraphs(lines)
        if title:
            paras = [title + '.'] + paras
        text = '\n\n'.join(p for p in paras if p)
        if text:
            out.append((e['ref'], text))
    return out


def convert(text):
    lines = text.replace('\r', '').split('\n')
    starts, end = find_books(lines)
    md = ['# Meditations, Marcus Aurelius', '',
          'Translated by Gregory Hays. One entry per `## book.section` heading; Cue Home reads through them in order.', '']
    total = 0
    for n in range(1, 13):
        stop = starts[n + 1] if n < 12 else end
        entries = split_book(n, lines[starts[n] + 1:stop])
        md += [f'# Book {n}', '']
        for ref, body in entries:
            md += [f'## {ref}', body, '']
        total += len(entries)
        print(f'Book {n}: {len(entries)} entries', file=sys.stderr)
    print(f'{total} entries', file=sys.stderr)
    return '\n'.join(md)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding='utf-8', errors='replace') as f:
        md = convert(f.read())
    with open(sys.argv[2], 'w', encoding='utf-8') as f:
        f.write(md)
