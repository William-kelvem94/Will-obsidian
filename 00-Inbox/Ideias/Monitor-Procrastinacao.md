```dataviewjs
// Painel Procrastinação
const p = await dv.io.load('10-Interfaces/dashboards/procrastinacao_report.json','json');
dv.table(["Nota","Data"], p.map(r=>[r.nota, r.data]));
```

**Como usar:**
Visualize rapidamente em um dashboard os tópicos e notas mais adiados.

**Como gerar o painel:**
Rode `.scripts/procrastination-monitor.py`—gera/atualiza `dashboards/procrastinacao_report.json`.
Recomendado rodar ao menos a cada dois dias por automação/manual.

**Dica de integração:**
Painéis produtividade, ação ou autocuidado.

**Problemas comuns:**
- JSON ausente ou vazio = rode o script para registrar novas métricas.
