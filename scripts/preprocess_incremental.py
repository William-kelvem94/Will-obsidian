"""
Script: scripts/preprocess_incremental.py - Indexação incremental

Para cada arquivo .md em Will-obsidian:
- Calcula hash SHA1 apenas do conteúdo relevante (ignora modificação de mtime).
- Se mudou desde último preprocess, executa preprocess_file (ou pipeline desejado) apenas para ele.
- Atualiza preprocess_manifest.json com hash e data de cada arquivo.
- Gera um preprocess_incremental.jsonl com chunks novos/atualizados.

Para uso em CI, CRON ou rodadas rápidas.
"""
import hashlib
import json
from pathlib import Path
from scripts.preprocess_poc import process_file

VAULT = Path(__file__).resolve().parents[1]
MANIFEST = VAULT / 'preprocess_manifest.json'
OUT = VAULT / 'preprocess_incremental.jsonl'

try:
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
except Exception:
    manifest = {}
with OUT.open('w', encoding='utf-8') as out:
    for f in VAULT.rglob('*.md'):
        if 'node_modules' in str(f):
            continue
        data = f.read_text(encoding='utf-8')
        h = hashlib.sha1(data.encode('utf-8')).hexdigest()
        name = str(f.relative_to(VAULT))
        if name not in manifest or manifest[name]['hash'] != h:
            chunks = process_file(f)
            for c in chunks:
                out.write(json.dumps(c, ensure_ascii=False)+'\n')
            manifest[name] = {'hash': h}
MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
