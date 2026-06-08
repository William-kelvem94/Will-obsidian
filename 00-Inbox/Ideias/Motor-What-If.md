```dataviewjs
// Painel Motor What If
const w = await dv.io.load('01-Hubs/dashboards/simulador_what_if.json','json');
dv.table(["Nota","Depende de"], w.map(e=>[e.nota,e.depende_de]));
```

**Como usar:**
Simule cenários de dependências entre notas/projetos diretamente num painel Obsidian.

**Como gerar o painel:**
Rode `.scripts/what-if-engine.py` para gerar `dashboards/simulador_what_if.json` e visualizar relações hipotéticas de dependências.

**Dica de integração:**
Painel master de estratégia/planejamento avançado ou projetos.

**Problemas comuns:**
- JSON desatualizado gera análise imprecisa; rode script sempre a cada mudança relevante em projetos.
