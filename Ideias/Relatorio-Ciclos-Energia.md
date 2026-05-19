```dataviewjs
// Painel Ciclos de Energia
const h = await dv.io.load('dashboards/energia_pico_report.json','json');
dv.table(["Horário", "Ocorrências"], h.map(([h,o])=>[h,o]));
```

**Como usar:**
Plugue no dashboard para visualizar seus horários de maior produtividade.

**Como gerar o painel:**
Rode `.scripts/energy-cycle-report.py`—salva `dashboards/energia_pico_report.json` pronto pro painel. Automatize diariamente.

**Dica de integração:**
Vida, produtividade ou painel pessoal semanal.

**Problemas comuns:**
- JSON não existente ou antigo: rode script, ajuste timezone.
