---
title: "Brain Health Dashboard"
description: "Painel de saúde do cérebro do Jarvis: indicadores de contexto, ingestão, relevância e sincronização." 
tags: [workspace-study, brain-health, jarvis, analytics, projetos]
updated: 2026-06-08
date: 2026-04-27
---

# Brain Health Dashboard

## Objetivo
Monitorar a saúde do segundo cérebro do Jarvis e garantir que o contexto, a ingestão e a capacidade de resposta estejam ajustados.

## Métricas de saúde
- **Context Load**: quantos arquivos de KB e perfil foram carregados no início da sessão.
- **Recência**: data da última atualização de `Will-Pessoal/Perfil/Cerebro-Will.md` e `JARVIS/KnowledgeBase/SegundoCerebro.md`.
- **Reindexação**: data da última reindexação de `PROJECT_JARVIS_5.0-KnowledgeBase`.
- **Decisões atualizadas**: número de entradas em `JARVIS/Decisoes/` nas últimas 30 dias.
- **Memória ativa**: número de notas recentes em `JARVIS/Memorias/Diario/` e `JARVIS/Memorias/Episodicas/`.
- **Confiança RAG**: presença de notas confiáveis em `Projectos/EstudosFocados` e `JARVIS/KnowledgeBase`.

## Checklist de saúde
- [ ] `Will-Pessoal/Perfil/Cerebro-Will.md` está atualizado.
- [ ] `JARVIS/KnowledgeBase/SegundoCerebro.md` reflete o pipeline de ingestão atual.
- [ ] `JARVIS/KnowledgeBase/Brain-Integration.md` está sincronizado com a arquitetura do vault.
- [ ] `JARVIS/KnowledgeBase/Integracao.md` contém os caminhos corretos de `JARVIS_KB_PATH` e `JARVIS_PROJECT_ROOT`.
- [ ] Há uma nota de decisão recente em `JARVIS/Decisoes/` sobre mudanças no cérebro.
- [ ] Há pelo menos uma memória episódica ou diário relacionado ao Jarvis nas últimas 2 semanas.

## Indicadores de alerta
- **Falta de reindexação**: mais de 14 dias desde a última atualização do KB.
- **Notas obsoletas**: arquivos em `JARVIS/KnowledgeBase/` com mais de 30 dias sem revisão.
- **Conflitos de contexto**: diferenças entre `Will-Pessoal/Perfil/Cerebro-Will.md` e `JARVIS/KnowledgeBase/SegundoCerebro.md`.
- **Ação não registrada**: mudanças no vault sem decisão registrada em `JARVIS/Decisoes/`.

## Ações de correção
- Atualizar `Will-Pessoal/Perfil/Cerebro-Will.md` quando valores ou prioridades mudarem.
- Reindexar a base de conhecimento se `RULES.md`, `INDEX.md` ou `CONFIG.md` mudarem.
- Registrar decisões em `JARVIS/Decisoes/` sempre que uma mudança de cérebro ocorrer.
- Revisar `JARVIS/Memorias/` e identificar aprendizados que devem virar regras ou KB.

## Links úteis
- [[02-JARVIS/KnowledgeBase/Brain-Integration|Brain Integration]]
- [[02-JARVIS/04-Engineering/Architecture/SegundoCerebro|Segundo Cérebro]]
- [[02-JARVIS/02-Operational/Config/Integracao|Integration]]
- [[06-Will-Pessoal/01-Identidade/Perfil/Cerebro-Will|Cérebro Will]]
- [[03-Projetos/03-Estudos/EstudosFocados/Workspace-Study/Practical-Example-Maximum-Files|Practical Example: Máximo de Arquivos]]
