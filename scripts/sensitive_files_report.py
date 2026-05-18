from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

SENSITIVE_PATTERNS = [
    'Will-Pessoal',
    'JARVIS/Blueprints',
    'JARVIS/Templates',
    'Projetos/Privados',
]

def main():
    matches = []
    for p in ROOT.rglob('*.md'):
        s = str(p)
        for pat in SENSITIVE_PATTERNS:
            if pat in s:
                matches.append(s)
                break
    out = ROOT / 'sensitive_files.txt'
    out.write_text('\n'.join(matches), encoding='utf-8')
    print(f'Wrote {len(matches)} sensitive file paths to {out}')

if __name__ == '__main__':
    main()
