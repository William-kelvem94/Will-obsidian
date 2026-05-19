"""
Script: scripts/enrich_frontmatter.py

Percorre todos os arquivos .md do vault. Se não houver frontmatter, ou se campos obrigatórios estiverem ausentes, gera um arquivo de patch YAML mínimo para ser aplicado no arquivo correspondente (pasta frontmatter_patches/). NÃO altera arquivos diretamente, respeitando revisão manual.

Recomenda-se execução periódica ou após grandes inserções. Campos obrigatórios: title, tags, nivel, fonte, updated, backlinks, assets, referencias, sensivel.
"""
import yaml
from pathlib import Path
from datetime import date
import os

TEMPLATE = {
    'title': None,
    'tags': [],
    'nivel': 'intermediário',
    'fonte': '',
    'updated': str(date.today()),
    'backlinks': [],
    'assets': [],
    'referencias': [],
    'sensivel': False
}

VAULT = Path(__file__).resolve().parents[1]
PATCHES = VAULT / 'frontmatter_patches'
PATCHES.mkdir(exist_ok=True)

def get_frontmatter(fpath):
    try:
        lines = list(Path(fpath).open(encoding='utf-8'))
        if lines[0].strip() == '---':
            fm_lines = []
            for l in lines[1:]:
                if l.strip() == '---':
                    break
                fm_lines.append(l)
            return yaml.safe_load(''.join(fm_lines))
    except Exception:
        return None
    return None

def gen_patch(fpath, missing_fields):
    patch = {**TEMPLATE, 'title': Path(fpath).stem}
    for k in patch:
        if k not in missing_fields:
            patch[k] = None
    patch_path = PATCHES / f'{Path(fpath).stem}.patch.yaml'
    with open(patch_path, 'w', encoding='utf-8') as out:
        yaml.dump({k: patch[k] for k in missing_fields}, out, allow_unicode=True)


def main():
    for f in VAULT.rglob('*.md'):
        if f.parts[0] == 'node_modules':
            continue
        fm = get_frontmatter(f)
        if not fm:
            # Ausente frontmatter, sugere todos
            gen_patch(f, list(TEMPLATE.keys()))
        else:
            missing = [k for k in TEMPLATE if k not in fm]
            if missing:
                gen_patch(f, missing)

if __name__ == '__main__':
    main()
