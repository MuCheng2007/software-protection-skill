"""Validate this repository's structure and evidence records; no network or dependencies."""
from __future__ import annotations
from datetime import date
from pathlib import Path
from urllib.parse import urlparse, unquote
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter


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
    allowed_hosts = {'bbs.kanxue.com', 'habr.com', 'nac-l.github.io', 'github.com', 'blog.csdn.net', 'overkazaf.github.io', 'dmitrybrant.com', 'www.52hb.com', 'www.52pojie.cn', 'www.chinapyg.com', 'www.ofweek.com', 'vxcall.github.io', 'www.cnblogs.com', 'juejin.cn'}
    for c in cases:
        cid = c['id']
        check('verified' not in c, f'{cid}: ambiguous automatic verified flag')
        check(c.get('patterns_status') != 'unverified-regex', f'{cid}: unreviewed automatic mapping')
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
    supplement = payload.get('supplemental_import')
    if supplement:
        audit_file = root / 'docs/research/supplement-2026-10-15.json'
        check(audit_file.is_file(), 'Supplement audit missing')
        if audit_file.is_file():
            audit = json.loads(audit_file.read_text(encoding='utf-8'))
            records = audit['records']
            check(len(records) == supplement['input_records'], 'Supplement input count mismatch')
            input_ids = [r['input_id'] for r in records]
            check(len(input_ids) == len(set(input_ids)), 'Duplicate supplement input ID')
            aliases = supplement['merged_duplicates']
            new_ids = set(input_ids) - set(aliases)
            check(len(new_ids) == supplement['new_records'], 'Supplement new count mismatch')
            check(new_ids <= set(ids), 'Supplement case missing')
            check(set(aliases.values()) <= set(ids), 'Supplement duplicate target missing')
            sampled = set()
            for record in records:
                check(record['canonical_id'] == aliases.get(record['input_id'], record['input_id']),
                      'Supplement canonical ID mismatch')
                check(re.fullmatch(r'[0-9a-f]{64}', record['source_sha256']) is not None,
                      'Invalid source snapshot digest')
                check(record['source_bytes'] > 0, 'Empty source snapshot')
                check(record['review_status'] in {'sampled_local_body', 'summary_review_only'},
                      'Invalid supplement review status')
                if record['review_status'] == 'sampled_local_body':
                    sampled.add(record['input_id'])
            check(sampled == set(supplement['sampled_local_body']), 'Sample review scope mismatch')
            by_id = {c['id']: c for c in cases}
            for record in records:
                if record['input_id'] in new_ids:
                    check(by_id.get(record['input_id'], {}).get('import_review_status', by_id.get(record['input_id'], {}).get('review_status')) == record['review_status'],
                          'Case review status differs from audit')
        english = (root / 'README.en.md').read_text(encoding='utf-8')
        check(f'**{len(cases)} candidate source records and {len(patterns)} failure patterns**' in english,
              'English README counts do not match evidence')
    reviews = ([payload['full_review']] if payload.get('full_review') else []) + payload.get('update_batches', [])
    covered_ids = []
    for full_review in reviews:
        review_path = root / full_review['report']
        check(review_path.resolve().is_relative_to(root), 'Review path escapes repository')
        check(review_path.is_file(), 'Full review report missing')
        if review_path.is_file():
            review = json.loads(review_path.read_text(encoding='utf-8'))
            reviewed = review['records']
            review_ids = [r['id'] for r in reviewed]
            check(len(review_ids) == len(set(review_ids)), 'Duplicate full review ID')
            check(set(review_ids) <= set(ids), 'Unknown case in review report')
            covered_ids.extend(review_ids)
            check(full_review['records'] == len(reviewed), 'Full review count mismatch')
            check(dict(Counter(r['review_status'] for r in reviewed)) == review['counts'],
                  'Full review scope counts mismatch')
            by_id = {c['id']: c for c in cases}
            reproduced = 0
            for record in reviewed:
                case = by_id.get(record['id'], {})
                check(record['review_status'] in {'source_body_reviewed', 'partial_body_reviewed',
                                                 'header_only_reviewed'}, 'Invalid full review status')
                check(record['review_status'] == case.get('review_status'), 'Latest case review differs')
                check(record['url'] == case.get('url'), 'Review source URL differs')
                check(bool(record.get('finding')) and bool(record.get('evidence')), 'Review evidence missing')
                check(set(record['checked']) == {'source_identity', 'publication_date_basis', 'case_type',
                                                'mechanism_scope', 'pattern_mapping'}, 'Review dimensions missing')
                check(record['mapping_role'] == case.get('mapping_role'), 'Mapping role differs')
                check((record['mapping_role'] == 'none') == (not case.get('patterns')),
                      'Mapping role and patterns disagree')
                check(record['independently_reproduced'] == case.get('independently_reproduced'),
                      'Review reproduction claim differs')
                if record['date_status'] == 'source_date_checked':
                    check(case.get('published_at') is not None, 'Checked date is missing')
                else:
                    check(case.get('published_at') is None, 'Unresolved date claimed as known')
                reproduced += bool(record['independently_reproduced'])
                for evidence in record['evidence']:
                    check(evidence['kind'] in {'provided_text_snapshot', 'public_page_read'},
                          'Unknown source evidence type')
                    if evidence['kind'] == 'provided_text_snapshot':
                        check(re.fullmatch(r'[0-9a-f]{64}', evidence['sha256']) is not None,
                              'Invalid full review source digest')
                        check(evidence['bytes'] > 0, 'Empty review source')
                        check(bool(evidence['line_ranges']), 'Source line references missing')
                        for start, end in evidence['line_ranges']:
                            check(isinstance(start, int) and isinstance(end, int) and 0 < start <= end,
                                  'Invalid source line reference')
                    else:
                        check(bool(evidence['sections']), 'Public-page locator missing')
            check(reproduced == review['runtime_reproductions'], 'Runtime reproduction count mismatch')
    if reviews:
        check(len(covered_ids) == len(set(covered_ids)), 'Case reviewed in multiple active batches')
        check(set(covered_ids) == set(ids), 'Review batches do not cover case IDs exactly')
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
