```dataviewjs
// Painel Networking (Follow-up)
const arr = await dv.io.load('10-Interfaces/dashboards/network_report.json','json');
dv.table(["Pessoa","Dias sem contato","Último contato"], arr.map(r=>[r.pessoa, r.dias_desde_ultimo_contato, r.ultimo_contato]));
```

**Como usar:**
Cole este painel em um dashboard para acompanhamento de relações/pessoas.

**Como gerar o painel:**
Rodar `.scripts/networking.py`—gera/atualiza `dashboards/network_report.json` automaticamente. Recomenda-se rodar/automatizar semanalmente.

**Dica de integração:**
Crie um painel dedicado de Networking ou integre à dashboard de produtividade.

**Problemas comuns:**
- Se não carregar, revise path do JSON no snippet e permissões da pasta dashboards/.
