"""
Script: scripts/gen_skill.py
Gera automaticamente nota de skill a partir de nome e área.
Uso: python scripts/gen_skill.py "Nome da Skill" "Área/Tema"
Cria arquivo com frontmatter e template mínimo em skills/Nome-da-Skill.md
"""
import sys
from pathlib import Path
import yaml
from datetime import date
if len(sys.argv)<3:
    print('Uso: python scripts/gen_skill.py "Nome da Skill" "Área"')
    sys.exit(1)
SKILL = sys.argv[1]
AREA = sys.argv[2]
FILE = Path(__file__).resolve().parents[1]/'skills'/f'{SKILL.replace(" ","-")}.md'
front = {
  'title': SKILL,
  'tags': [AREA],
  'nivel': 'intermediário',
  'fonte': '',
  'updated': str(date.today()),
  'backlinks': [],
  'assets': [],
  'referencias': [],
  'sensivel': False
}
with open(FILE,'w',encoding='utf-8') as f:
    f.write('---\n')
    f.write(yaml.dump(front, allow_unicode=True))
    f.write('---\n\n')
    f.write(f'# {SKILL}\n\nPreencha descrição, aplicações e exemplos para a skill {SKILL}.\n')
