```dataviewjs
// Painel tópicos emergentes
const t = await dv.io.load('dashboards/topicos_emergentes.json','json');
dv.table(["Tag","Ocorrências"], t.map(([tag,oc])=>[tag,oc]));
```

**Como usar:**
Para visão rápida dos trends/novidades nas discussões e temas do vault.

**Como gerar o painel:**
Execute `.scripts/topic-trends.py` para atualizar `dashboards/topicos_emergentes.json` manual ou agendado semanal.

**Dica de integração:**
Dashboard de estratégias, insights rápidos, ou painel de ideias/tendências.

**Problemas comuns:**
- Conferir se nomes de tags coincidem entre script e vault.
