"""Readers for Instagram's HTML export records."""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

from bs4 import BeautifulSoup


class _Records(HTMLParser):
    """Collect direct children of <main> without loading an entire export into memory."""
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.in_main = False
        self.found_main = False
        self.depth = 0
        self.parts = []
        self.records = []

    def handle_starttag(self, tag, attrs):
        if tag == 'main' and not self.in_main:
            self.in_main = True
            self.found_main = True
            return
        if not self.in_main:
            return
        if self.depth or tag == 'div':
            self.parts.append(self.get_starttag_text())
            if tag not in {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}:
                self.depth += 1

    def handle_startendtag(self, tag, attrs):
        if self.depth:
            self.parts.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if tag == 'main' and not self.depth:
            self.in_main = False
        elif self.depth:
            self.parts.append(f'</{tag}>')
            self.depth -= 1
            if not self.depth:
                self.records.append(''.join(self.parts))
                self.parts = []

    def handle_data(self, data):
        if self.depth:
            self.parts.append(escape(data, quote=False))

    def handle_entityref(self, name):
        if self.depth:
            self.parts.append(f'&{name};')

    def handle_charref(self, name):
        if self.depth:
            self.parts.append(f'&#{name};')


def records(path):
    parser = _Records()
    with Path(path).open(encoding='utf-8') as source:
        while chunk := source.read(65536):
            parser.feed(chunk)
            for record in parser.records:
                yield BeautifulSoup(record, 'html.parser')
            parser.records.clear()
    parser.close()
    if not parser.found_main:
        raise ValueError(f'No <main> element found in Instagram export: {path}')
    for record in parser.records:
        yield BeautifulSoup(record, 'html.parser')


def field_values(node, labels):
    values = []
    for row in node.find_all('tr'):
        cells = row.find_all('td', recursive=False)
        if len(cells) == 2 and cells[0].get_text(' ', strip=True).casefold() in labels:
            values.append(cells[1].get_text(' ', strip=True))
    return values


def profile_from_url(url):
    parsed = urlparse(url)
    if parsed.hostname not in {'www.instagram.com', 'instagram.com'}:
        return None
    parts = [unquote(p) for p in parsed.path.split('/') if p]
    if parts and parts[0] == '_u':
        parts = parts[1:]
    if len(parts) == 1 and parts[0].casefold() not in {'p', 'reel', 'explore', 'accounts'}:
        return parts[0]
    return None


def account_names(path):
    result = set()
    for record in records(path):
        names = field_values(record, {'brukernavn', 'username', 'user name'})
        if not names:
            names = [name for a in record.find_all('a', href=True) if (name := profile_from_url(a['href']))]
        result.update(name.strip() for name in names if name.strip())
    return result


def liked_post_owner(record):
    for heading in record.find_all('h2'):
        title = heading.get_text(' ', strip=True)
        if title.casefold() in {'eier', 'owner'}:
            names = field_values(heading.parent, {'brukernavn', 'username', 'user name'})
            return names[0] if names else None
    # Older exports use the username itself as the record heading.
    heading = record.find('h2')
    if heading and not record.find('table'):
        return heading.get_text(' ', strip=True) or None
    return None


def comments(path):
    for record in records(path):
        for cell in record.find_all('td'):
            label = cell.find(string=True, recursive=False)
            if label and label.strip().casefold() in {'comment', 'kommentar'}:
                content = cell.find('div')
                if content:
                    yield ' '.join(content.get_text(' ', strip=True).split())
