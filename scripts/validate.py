"""Validate this repository's structure and evidence records; no network or dependencies."""
from __future__ import annotations
from datetime import date
from pathlib import Path
from urllib.parse import urlparse, unquote
import json
import re
import sys
import xml.etree.ElementTree as ET


def validate(root: Path) -> dict:
    root = root.resolve()
    skill = root / 'skills/software-protection'
    errors: list[str] = []

    def check(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    required = ['README.md', 'LICENSE', 'NOTICE', 'CONTRIBUTING.md', 'CHANGELOG.md',
                'ROADMAP.md', 'assets/hero.svg', 'docs/cases.md', 'docs/github-guide.md',
                'skills/software-protection/SKILL.md',
                'skills/software-protection/references/forum-cases.json']
    for item in required:
        check((root / item).is_file(), f'Missing required file: {item}')
    if errors:
        return {'ok': False, 'errors': errors}

    entry = (skill / 'SKILL.md').read_text(encoding='utf-8')
    front = re.match(r'\A---\n(.*?)\n---\n', entry, re.S)
    check(front is not None, 'Missing skill frontmatter')
    if front:
        # This project uses simple scalar frontmatter, not a general-purpose YAML parser.
        fields = dict(re.findall(r'^([a-z-]+): (.+)$', front.group(1), re.M))
        check(fields.get('name') == 'software-protection', 'Skill name mismatch')
        check(0 < len(fields.get('description', '')) <= 1024, 'Invalid skill description')
        check(fields.get('license') == 'MIT', 'Skill license must match repository')
        check(len(fields) == 3, 'Review newly introduced frontmatter format')

    internal_links = 0
    for p in root.rglob('*.md'):
        if '.git' in p.relative_to(root).parts:
            continue
        text = p.read_text(encoding='utf-8')
        targets = re.findall(r'\]\(([^)]+)\)', text)
        targets += re.findall(r'(?:src|href)="([^"]+)"', text)
        for target in targets:
            if target.startswith(('http://', 'https://', 'mailto:', '#')):
                continue
            clean = unquote(target.split('#')[0].split('?')[0].strip('<>'))
            resolved = (p.parent / clean).resolve()
            check(resolved.is_relative_to(root), f'Link escapes repository: {p.name}: {target}')
            check(resolved.exists(), f'Broken link: {p.relative_to(root)}: {target}')
            internal_links += 1
        check(not re.search(r'\[TODO:|\[FIXME:', text), f'Unfinished scaffold: {p.name}')
        check(not re.search(r'[A-Za-z]:\\Users\\|/Users/', text), f'Local user path: {p.name}')
        check('PRIVATE KEY-----' not in text, f'Private key marker: {p.name}')

    payload = json.loads((skill / 'references/forum-cases.json').read_text(encoding='utf-8'))
    cases = payload['cases']
    ids = [c['id'] for c in cases]
    urls = [c['url'] for c in cases]
    check(len(ids) == len(set(ids)), 'Duplicate case IDs')
    check(len(urls) == len(set(urls)), 'Duplicate source URLs')
    pattern_text = (skill / 'references/failure-patterns.md').read_text(encoding='utf-8')
    patterns = set(re.findall(r'^## (F\d{2}) ', pattern_text, re.M))
    check(set(re.findall(r'\bC\d{2}\b', pattern_text)) <= set(ids), 'Unknown case referenced in patterns')
    allowed_hosts = {'bbs.kanxue.com', 'www.chinapyg.com', 'chinapyg.com', 'www.52hb.com',
                     'www.52pojie.cn', '52pojie.cn'}
    for c in cases:
        cid = c['id']
        for field in ['site', 'title', 'url', 'retrieved_at', 'case_type', 'access',
                      'evidence_summary', 'limitations', 'patterns', 'independently_reproduced']:
            check(field in c, f'{cid}: missing {field}')
        check(re.fullmatch(r'C\d{2,}', cid) is not None, f'Invalid case ID: {cid}')
        parsed = urlparse(c['url'])
        check(parsed.scheme == 'https' and parsed.hostname in allowed_hosts, f'{cid}: review source host')
        check(set(c['patterns']) <= patterns, f'{cid}: unknown failure pattern')
        check(isinstance(c['independently_reproduced'], bool), f'{cid}: invalid reproduction flag')
        if c['independently_reproduced']:
            check(bool(c.get('reproduction_evidence')), f'{cid}: reproduction evidence required')
        if c['case_type'].startswith(('excluded', 'unclassified')) or c['access'] == 'search_excerpt':
            check(not c['patterns'], f'{cid}: insufficient evidence mapped as confirmed mechanism')
        for field in ['published_at', 'retrieved_at']:
            value = c.get(field)
            if value is None:
                continue
            try:
                parsed_date = date.fromisoformat(value)
                if field == 'published_at':
                    check(parsed_date <= date.fromisoformat(c['retrieved_at']), f'{cid}: publication after retrieval')
            except (ValueError, TypeError):
                errors.append(f'{cid}: invalid {field}')

    readme = (root / 'README.md').read_text(encoding='utf-8')
    check(f'**{len(cases)} 条候选资料、{len(patterns)} 类失效模式**' in readme,
          'README counts do not match evidence')
    index = (root / 'docs/cases.md').read_text(encoding='utf-8')
    check(set(re.findall(r'^\| (C\d+) \|', index, re.M)) == set(ids), 'Case index out of sync')
    svg = ET.fromstring((root / 'assets/hero.svg').read_text(encoding='utf-8'))
    check(svg.tag.endswith('svg'), 'Hero is not SVG')
    for el in svg.iter():
        check(not el.tag.endswith(('script', 'foreignObject')), 'Active content in hero')
        check(not any(k.lower().startswith('on') for k in el.attrib), 'Event handler in hero')

    return {'ok': not errors, 'case_records': len(cases), 'failure_patterns': len(patterns),
            'internal_links': internal_links, 'errors': errors,
            'scope': 'Structure/evidence consistency only; not software protection effectiveness.'}


if __name__ == '__main__':
    result = validate(Path(__file__).resolve().parents[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result['ok'] else 1)
