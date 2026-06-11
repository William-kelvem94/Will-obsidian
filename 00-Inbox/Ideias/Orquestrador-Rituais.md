```dataviewjs
// Painel Micro-hábitos/rituais
const r = await dv.io.load('01-Hubs/dashboards/rituais_microhabitos.json','json');
dv.table(["Hábito","Feito?","Última Execução"], Object.entries(r).map(([h,info])=>[h,info.feito,info.ultima_execucao]));
```

**Como usar:**
Cole em seu dashboard pessoal para controle de micro-rituais e streaks.

**Como gerar o painel:**
Execute `.scripts/rituals-orchestrator.py` para atualizar `dashboards/rituais_microhabitos.json`. Ideal agendamento diário (hora de início do dia).

**Dica de integração:**
Dashboard pessoal, painel de hábitos/vida ou produtividade.

**Problemas comuns:**
- Sem execução do script, painel não será atualizado.
