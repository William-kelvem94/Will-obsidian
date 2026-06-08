---
aplicacao: Will-obsidian
criacao: 2026-05-19
---

# Registro de Evolução de Ideias Inéditas

> Este arquivo mantém o histórico, a data e comentários de progresso para cada ideia nova que expanda as capacidades do vault. Use para priorização, acompanhamento, reviews e futuras integrações.

## 2026-05-19 — Primeira Onda de Expansão

### 1. Painel de Health Mental & Humor via Diário
- **Status:** 🟡 Em teste
- **Resumo:** Painel de análise de humor/sentimentos extraídos do diário via NLP.
- **Valor:** Métricas de saúde mental no tempo, alerta precoce, mindfulness.
- **Como Implementar:** Script NLP nas notas do diário + dashboard gráfico já desenvolvido: veja .scripts/extract-mood.py e dashboards/health-humor.json. Painel DataviewJS e instruções em Ideias/Painel-Health-Mental-Humor.md.
- **Comentário/Integração:** Pronto para integração aos dashboards pessoais; plug-and-play via DataviewJS.
### 2. Roteirizador de Revisão Cíclica de Conhecimento
- **Status:** 🟡 Em teste
- **Resumo:** Script para gerar agenda de revisão rotativa de notas/projetos antigos.
- **Valor:** Retenção e atualização do conhecimento.
- **Como Implementar:** Dataview/script identifica e notifica docs esquecidos. Script funcional: .scripts/cyclic-review.py; painel e instrução Ideias/Roteirizador-Revisao-Ciclica.md.
- **Comentário/Integração:** Testes concluídos; painel recomenda-se adicionar a dashboard de estudos/ação.
### 3. Módulo “Inspirações Aleatórias”
- **Status:** ✅ Finalizado
- **Resumo:** Widget sugere nota esquecida/reflexão/insight a cada login.
- **Valor:** Estimular criatividade, revisitar pensamentos.
- **Como Implementar:** Script frontend + integração com dashboard. Script funcional: .scripts/random-inspiration.py; painel DataviewJS pronto em Ideias/Inspiracoes-Aleatorias.md.
- **Comentário/Integração:** Código pronto; plugar painel em Home ou dashboard diária.
### 4. Monitor de Networking (Pessoas & Colaborações)
- **Status:** 🟡 Em teste
- **Resumo:** Dashboard de rastreamento de pessoas, follow-ups, relações.
- **Valor:** Aumenta capital social, networking vivo.
- **Como Implementar:** Parse de @menções, painéis integram datas de contato. Script em .scripts/networking.py; painel pronto para uso em Ideias/Monitor-Networking.md.
- **Comentário/Integração:** Integra facilmente em dashboards de produtividade ou networking.
### 5. Analista de Tópicos Emergentes
- **Status:** 🟡 Em teste
- **Resumo:** Script sinaliza temas/tags em crescimento mês a mês no vault.
- **Valor:** Detectar tendências espontâneas/nichos novos.
- **Como Implementar:** Script analisa frequência de tags e notas. Script: .scripts/topic-trends.py; painel Ideias/Topicos-Emergentes.md.
- **Comentário/Integração:** Recomendado plugar em dashboard de estratégias/insights.
### 6. Orquestrador de Rituais & Micro-rotinas Automáticos
- **Status:** 🟡 Em teste
- **Resumo:** Automatiza lembrete e tracking de micro-hábitos diários/semanais.
- **Valor:** Melhora autocuidado e constância de hábitos.
- **Como Implementar:** Script de automação/notificações agendadas. Ver .scripts/rituals-orchestrator.py, painel em Ideias/Orquestrador-Rituais.md.
- **Comentário/Integração:** Pode ser agendado e integrado ao painel de vida/hábitos.
### 7. Monitor de Procrastinação
- **Status:** 🟡 Em teste
- **Resumo:** Detecta via padrões/tags tarefas cronicamente adiadas, sugere plano de ação.
- **Valor:** Ajuda a combater procrastinação recorrente.
- **Como Implementar:** NLP processa entradas de diário e tarefas adiadas. Script .scripts/procrastination-monitor.py, painel Ideias/Monitor-Procrastinacao.md.
- **Comentário/Integração:** Plugar ao painel de produtividade ou dashboard de hábitos.
### 8. Mapeador Visual de Conexões Não Explícitas
- **Status:** 🟡 Em teste
- **Resumo:** Visualização/graph de links temáticos ocultos entre notas.
- **Valor:** Revela sinergias/pesquisas interdisciplinares.
- **Como Implementar:** Script/processador distância semântica + renderer de grafo. Script: .scripts/semantic-graph.py; painel Ideias/Mapeador-Conexoes-Impensas.md.
- **Comentário/Integração:** Ideal para painel visual central ou pesquisa avançada.
### 9. Relatório de Ciclos de Energia/Pico Produtivo
- **Status:** ✅ Finalizado
- **Resumo:** Análise de hábitos/checkins para visualizar horários de pico de rendimento.
- **Valor:** Otimiza programação de tarefas e self-care.
- **Como Implementar:** Dashboard DATAmining hábitos x logs x produtividade. Script funcional: .scripts/energy-cycle-report.py; painel pronto em Ideias/Relatorio-Ciclos-Energia.md.
- **Comentário/Integração:** Integrado ao dashboard Vida/Produtividade por padrão.
### 10. Motor de Consultas “What If?” multi-nota/projeto
- **Status:** 🔄 Em desenvolvimento
- **Resumo:** Simulação visual e lógica de impactos ao alterar foco/prioridade de projetos.
- **Valor:** Decisão estratégica e planejamento robusto.
- **Como Implementar:** Script/processador de dependências + UI/consultas. Script base e painel experimental em Ideias/Motor-What-If.md.
- **Comentário/Integração:** Em prototypagem; integração futura com painel de planejamento.
---

> Sempre registre neste arquivo a cada nova ideia, progresso ou conclusão. Status: ✅ feito, 🔄 em progresso, ❌ não iniciado.
