#!/usr/bin/env python3
"""Convert a Google Scholar exported BibTeX file into Academic Pages markdown files.

Usage:
  python scripts/import_scholar_bibtex.py path/to/scholar.bib _publications

The script will:
  - Parse BibTeX entries
  - Create one markdown file per publication in the target directory
  - Infer publication type (journal vs conference) from 'journal' or 'booktitle'
  - Include citation, authors, year, and links (doi/url) if present

Prerequisites:
  pip install bibtexparser
"""

import sys
import re
from pathlib import Path
from datetime import datetime

try:
    import bibtexparser
except ImportError:
    print("bibtexparser not installed. Run: pip install bibtexparser", file=sys.stderr)
    sys.exit(1)


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text).strip('-')
    return text[:80]


def classify(entry):
    if 'booktitle' in entry:
        return 'conferences'
    if 'journal' in entry:
        return 'manuscripts'
    if entry.get('ENTRYTYPE') in {'book'}:
        return 'books'
    return 'manuscripts'


def build_markdown(entry, collection):
    title = entry.get('title', 'Untitled').replace('{', '').replace('}', '')
    year = entry.get('year', '')
    authors_raw = entry.get('author', '')
    authors = [a.strip() for a in re.split(r'\s+and\s+', authors_raw) if a.strip()]
    doi = entry.get('doi')
    url = entry.get('url') or (f"https://doi.org/{doi}" if doi else '')
    venue = entry.get('journal') or entry.get('booktitle') or ''
    citation = f"{', '.join(authors)}. {title}. {venue} {year}.".strip()

    front_matter = {
        'title': f'"{title}"',
        'collection': 'publications',
        'type': collection,
        'permalink': f"/publications/{slugify(title)}",
        'venue': venue,
        'date': f"{year}-01-01" if year else datetime.utcnow().strftime('%Y-%m-%d'),
        'citation': citation,
    }
    if doi:
        front_matter['doi'] = doi
    if url:
        front_matter['link'] = url

    fm_lines = ['---']
    for k, v in front_matter.items():
        fm_lines.append(f"{k}: {v}")
    fm_lines.append('---\n')
    body = []
    body.append(title)
    body.append('=' * len(title))
    body.append('')
    if venue:
        body.append(f"*{venue}*, {year}.")
    if doi:
        body.append(f"DOI: {doi}")
    if url and (not doi or url != f"https://doi.org/{doi}"):
        body.append(f"Link: {url}")
    body.append('')
    return '\n'.join(fm_lines + body)


def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/import_scholar_bibtex.py path/to/scholar.bib _publications", file=sys.stderr)
        sys.exit(1)
    bib_path = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    if not bib_path.exists():
        print(f"BibTeX file not found: {bib_path}", file=sys.stderr)
        sys.exit(1)
    out_dir.mkdir(parents=True, exist_ok=True)

    with bib_path.open() as fh:
        db = bibtexparser.load(fh)

    created = 0
    for entry in db.entries:
        collection = classify(entry)
        md_content = build_markdown(entry, collection)
        title = entry.get('title', 'untitled')
        slug = slugify(title)
        year = entry.get('year', datetime.utcnow().year)
        filename = out_dir / f"{year}-01-01-{slug}.md"
        if filename.exists():
            # Avoid overwriting; append numeric suffix
            i = 2
            while (out_dir / f"{year}-01-01-{slug}-{i}.md").exists():
                i += 1
            filename = out_dir / f"{year}-01-01-{slug}-{i}.md"
        filename.write_text(md_content)
        created += 1

    print(f"Created {created} publication markdown files in {out_dir}")


if __name__ == '__main__':
    main()
