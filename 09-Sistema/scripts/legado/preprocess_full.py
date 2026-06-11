import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.preprocess_poc import process_file

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / 'indexer_config.json'

def load_denylist():
    try:
        cfg = json.loads(CONFIG.read_text(encoding='utf-8'))
        return cfg.get('denylist', [])
    except Exception:
        return []

def is_denied(p: Path, denylist):
    s = str(p).replace('\\','/')
    for patt in denylist:
        pp = patt.replace('**', '')
        if pp.startswith('/'):
            if pp in s:
                return True
        if pp.lower() in s.lower():
            return True
    # skip node_modules explicitly
    if 'node_modules' in s:
        return True
    return False

def main():
    denylist = load_denylist()
    md_files = [p for p in ROOT.rglob('*.md') if p.is_file()]
    out = ROOT / 'preprocess_full.jsonl'
    count = 0
    with out.open('w', encoding='utf-8') as f:
        for p in md_files:
            if is_denied(p, denylist):
                continue
            try:
                chunks = process_file(p)
                for c in chunks:
                    f.write(json.dumps(c, ensure_ascii=False) + '\n')
                    count += 1
            except Exception:
                continue
    print(f'Wrote {count} chunks to {out}')

if __name__ == '__main__':
    main()
