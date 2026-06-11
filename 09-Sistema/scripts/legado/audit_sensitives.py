"""
Script: scripts/audit_sensitives.py - Segurança
- Percorre todos os .md do vault:
  - Se sensivel: true (frontmatter) fora da allowlist, alerta/bloqueia a ação.
  - Gera report summário de arquivos sensíveis localizados.
- Pode ser plugado como githook pré-push ou executado manual/cron.
"""
import yaml
from pathlib import Path
from datetime import datetime
SENSITIVE_LOG = Path(__file__).resolve().parents[1]/'sensitive_audit_report.txt'
VAULT = Path(__file__).resolve().parents[1]
ALLOW = {'.github','README.md','LICENSE.md'}  # Exemplo
found = []
for f in VAULT.rglob('*.md'):
    if 'node_modules' in str(f):
        continue
    try:
        with f.open(encoding='utf-8') as fp:
            lines = list(fp)
        if lines and lines[0].strip() == '---':
            fm = []
            for l in lines[1:]:
                if l.strip() == '---': break
                fm.append(l)
            meta = yaml.safe_load(''.join(fm)) or {}
            if meta.get('sensivel', False) and f.name not in ALLOW:
                found.append(str(f))
    except Exception: pass
if found:
    with open(SENSITIVE_LOG,'a',encoding='utf-8') as log:
        log.write(f'Run {datetime.now()} - Sensíveis bloqueados\n')
        for path in found:
            log.write(path+'\n')
    print('ATENÇÃO: arquivos sensíveis encontram-se em local não autorizado. Corrija antes do commit!')
    exit(1)
else:
    print('Nenhum arquivo sensível fora da allowlist detectado!')
