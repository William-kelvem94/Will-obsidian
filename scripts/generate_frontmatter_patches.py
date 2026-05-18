from pathlib import Path
import yaml
import json

ROOT = Path(__file__).resolve().parents[1]
SNIPPETS = ROOT / 'frontmatter_snippets'
OUT_PATCHES = ROOT / 'frontmatter_patches'
OUT_PATCHES.mkdir(exist_ok=True)

def main(n=100):
    snippets = list(SNIPPETS.glob('*.yaml'))[:n]
    for s in snippets:
        base = s.stem
        # try to find a matching md file by name
        candidates = list(ROOT.rglob(base + '.md'))
        if not candidates:
            continue
        target = candidates[0]
        snippet = s.read_text(encoding='utf-8')
        patch = f"---\n{snippet}---\n\n"
        out = OUT_PATCHES / (target.name + '.patch.md')
        out.write_text(patch, encoding='utf-8')
    print(f'Wrote frontmatter patches to {OUT_PATCHES}')

if __name__ == '__main__':
    main()
