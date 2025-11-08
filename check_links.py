import os, re
root = r'd:/OneDrive/DEV/exonware/xwsystem'
docs_dir = os.path.join(root, 'docs')
link_pattern = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
missing = {}
for dirpath, _, files in os.walk(docs_dir):
    for fname in files:
        if not fname.lower().endswith('.md'):
            continue
        fpath = os.path.join(dirpath, fname)
        rel_fpath = os.path.relpath(fpath, docs_dir)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        for link in link_pattern.findall(content):
            link = link.strip()
            if not link or link.startswith('#'):
                continue
            lowered = link.lower()
            if lowered.startswith(('http://', 'https://', 'mailto:', 'tel:', 'data:')):
                continue
            if link.startswith('!'):
                continue
            if re.match(r'^[a-z0-9+.-]+:', link, re.IGNORECASE):
                continue
            target = link.split('#', 1)[0]
            if not target or target == '.':
                continue
            if target.startswith('/'):
                full_target = os.path.normpath(os.path.join(root, target.lstrip('/')))
            else:
                full_target = os.path.normpath(os.path.join(dirpath, target))
            if not os.path.exists(full_target):
                missing.setdefault(rel_fpath, set()).add(link)

if not missing:
    print('ALL_LINKS_OK')
else:
    for file, links in sorted(missing.items()):
        print(f'[{file}] missing targets:')
        for link in sorted(links):
            print(f'  - {link}')
