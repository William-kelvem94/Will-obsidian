```dataviewjs
// Painel: Health Mental & Humor
const fs = dv.io.load('01-Hubs/dashboards/health_mental_report.json','json');
dv.table(["Data", "Humor", "Arquivo"], fs.map(r=>[r.data, r.humor, r.arquivo]));
```

**Como usar:**
Cole este bloco em um dashboard Obsidian, ajuste o path do JSON conforme sua estrutura. O output será uma tabela "Data | Humor | Arquivo" das análises mais recentes.

**Como gerar o painel:**
Rode o script `.scripts/extract-mood.py` para atualizar `dashboards/health_mental_report.json`. Recomenda-se agendar este script para rodar 1x ao dia usando Task Scheduler (Windows) ou plugin Obsidian runner.

**Dica de integração:**
Ideal para painel pessoal de saúde, autocuidado ou Diário.

**Problemas comuns:**
- Se não aparecer nada, confira se o arquivo JSON existe e o caminho está correto.
