```dataviewjs
// Painel Conexões Não Explícitas
const c = await dv.io.load('dashboards/conexoes_implicitas.json','json');
dv.table(["Origem", "Relacionado", "Palavras em Comum"],
Object.entries(c).flatMap(([origem, lista])=>lista.map(e=>[origem, e.com, e.palavras_comum])));
```

**Como usar:**
Cole o código num dashboard para ver recomendações automáticas de novas conexões de conhecimento.

**Como gerar o painel:**
Rodar `.scripts/semantic-graph.py` para gerar `dashboards/conexoes_implicitas.json`.
Ideal agendamento semanal/manual (brainstorm/discovery).

**Dica de integração:**
Painel visual central, pesquisa avançada ou dashboards de insights/conhecimento profundo.

**Problemas comuns:**
- Se erro, verifique integridade do JSON e se o script rodou com permissão.
