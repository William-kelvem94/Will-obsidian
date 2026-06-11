"""
Script: scripts/preprocess_multimodal.py
- Percorre o vault, busca assets multimodais referenciados no frontmatter de cada .md.
- Gera multimodal_index.jsonl, listando: {'file':arquivo,'assets':[lista]}
- (Expansão: pode chamar processamento OCR/Caption/Audio etc.)
"""
import yaml
from pathlib import Path
import json
VAULT = Path(__file__).resolve().parents[1]
OUT = VAULT/'multimodal_index.jsonl'
with open(OUT,'w',encoding='utf-8') as idx:
    for f in VAULT.rglob('*.md'):
        if 'node_modules' in str(f): continue
        try:
            with f.open(encoding='utf-8') as fp:
                lines = list(fp)
            if lines and lines[0].strip() == '---':
                fm = []
                for l in lines[1:]:
                    if l.strip() == '---': break
                    fm.append(l)
                meta = yaml.safe_load(''.join(fm)) or {}
                assets = meta.get('assets',[])
                if assets:
                    idx.write(json.dumps({'file':str(f),'assets':assets},ensure_ascii=False)+'\n')
        except Exception: pass
print('multimodal_index.jsonl gerado!')
