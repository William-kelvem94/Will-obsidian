import json
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def pick_canonical(paths):
    # prefer paths not under .agents or .continue; prefer skills/ then Conhecimento-Geral/ then JARVIS/
    priority = ['skills' , 'Conhecimento-Geral', 'JARVIS']
    cleaned = [p for p in paths if '.agents' not in p and '.continue' not in p]
    if not cleaned:
        # fallback: return first
        return paths[0]
    for pref in priority:
        for p in cleaned:
            if f'/{pref}/' in p.replace('\\','/') or f'\\{pref}\\' in p:
                return p
    # otherwise pick shortest path (likely top-level)
    return sorted(cleaned, key=lambda s: len(s))[0]

def main():
    report = ROOT / 'dedupe_report.json'
    data = json.loads(report.read_text(encoding='utf-8'))
    duplicates = data.get('duplicates', {})
    outcsv = ROOT / 'dedupe_report.csv'
    with outcsv.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['hash', 'canonical_path', 'duplicate_paths'])
        for h, paths in duplicates.items():
            canonical = pick_canonical(paths)
            w.writerow([h, canonical, ';'.join(paths)])
    print(f'Wrote CSV to {outcsv}')

if __name__ == '__main__':
    main()
