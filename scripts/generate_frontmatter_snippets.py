from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]

def top_md_files(n=100):
    files = [p for p in ROOT.rglob('*.md') if p.is_file()]
    # prioritise hubs and top-level INDEX.md, then size
    def score(p):
        name = p.name.lower()
        s = p.stat().st_size
        if 'index' in name or 'skill' in name or 'master' in name:
            s += 10**7
        return s
    return sorted(files, key=score, reverse=True)[:n]

def snippet_for(p):
    slug = '/'.join(p.parts[-3:])
    front = {
        'title': p.stem,
        'id': slug,
        'type': 'note',
        'tags': [],
        'status': 'draft',
        'description': '',
        'created': '',
        'updated': '',
        'publish': False,
        'embedding_ignore': False,
    }
    return yaml.safe_dump(front, allow_unicode=True)

def main():
    out = ROOT / 'frontmatter_snippets'
    out.mkdir(exist_ok=True)
    for p in top_md_files(100):
        s = snippet_for(p)
        name = p.stem + '.yaml'
        (out / name).write_text(s, encoding='utf-8')
    print(f"Wrote frontmatter snippets for top 100 files into {out}")

if __name__ == '__main__':
    main()
