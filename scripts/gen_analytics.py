"""
Script: scripts/gen_analytics.py
Exemplo inicial – hiper básico:
Percorre todos os arquivos do vault, agrupa e conta por tags, gera summary de tópicos/áreas mais frequentes.
Pode ser expandido com Dataview CSV export, integração com charts, tracking web etc.
"""
import yaml
from pathlib import Path
from collections import Counter

stat = Counter()
VAULT = Path(__file__).resolve().parents[1]
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
            tags = meta.get('tags',[])
            for tag in tags: stat[tag] +=1
    except Exception: pass
with open(VAULT/'ANALYTICS.md','a',encoding='utf-8') as out:
    out.write('\n# Analytics Summary - update\n')
    for tag, qtd in stat.most_common():
        out.write(f'* {tag}: {qtd} notas\n')
print('Analytics summary appended!')
