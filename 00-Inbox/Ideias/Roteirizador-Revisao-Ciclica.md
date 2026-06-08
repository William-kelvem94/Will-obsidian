```dataviewjs
// Painel: Revisão Cíclica
const agenda = await dv.io.load('10-Interfaces/dashboards/agenda_revisao.json','json');
dv.table(["Nota a Revisar", "Último Acesso"], agenda.map(r=>[r.nota, r.ultimo_acesso]));
```

**Como usar:**
Inclua este bloco no dashboard de revisão para listar automaticamente as notas mais esquecidas e promover o ciclo de revisão.

**Como gerar o painel:**
Execute `.scripts/cyclic-review.py` para criar/update `dashboards/agenda_revisao.json`. Recomenda-se agendar semanalmente para melhor disciplina.

**Dica de integração:**
Ideal em dashboards de estudo/projetos ou painel pessoal de evolução.

**Problemas comuns:**
- Veja se o JSON está presente na pasta `dashboards/` e o path correto no snippet.
