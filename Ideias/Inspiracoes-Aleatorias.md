```dataviewjs
// Painel Inspiração Aleatória
const sug = await dv.io.load('dashboards/inspiracao_diaria.json', 'json');
dv.paragraph(`Sugestão do dia: [[${sug.nota}]]`);
```

**Como usar:**
Bloco para inserir em seu painel Home/entrada diária, mostrando sugestão automática para reflexão.

**Como gerar o painel:**
Execute `.scripts/random-inspiration.py` para gerar o JSON `dashboards/inspiracao_diaria.json`.
Pode automatizar via Task Scheduler (manhã cedo, por exemplo).

**Dica de integração:**
Painel recomendado para Home, Diário, página de insights.

**Problemas comuns:**
- JSON ausente ou corrompido impede exibição. Refaça execução do script.
