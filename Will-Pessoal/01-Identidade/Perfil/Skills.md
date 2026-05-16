---
title: "Skills — William Pereira"
description: "Mapeamento completo de habilidades técnicas, soft skills, áreas de domínio, projetos comprobatórios e roteiro de aprendizado."
tags:
  - skills
  - perfil-identidade
  - perfil
  - talento
updated: 2026-05-16
date: 2026-04-27
---

# Skills

## Mapa de proficiência técnica

| Skill | Nível (1-5) | Último uso | Projetos associados |
|-------|:-----------:|-----------|---------------------|
| **Python** | 5 | Diário | IA-LOCAL, Jarvis, Auto-boletos, scripts |
| **FastAPI** | 4 | Semanal | APIs de todos os projetos SaaS |
| **SQLAlchemy** | 4 | Semanal | Modelagem de dados, migrations |
| **TypeScript** | 4 | Semanal | Front-end dos projetos (React/Next) |
| **React / Next.js** | 3 | Mensal | Interfaces web do Gestor Aluguel |
| **Node.js** | 4 | Semanal | Scripts, APIs auxiliares |
| **PHP** | 3 | Mensal | Manutenção de projetos legados |
| **Docker / Compose** | 4 | Semanal | Infra de todos os projetos ativos |
| **Traefik / Nginx** | 3 | Mensal | Roteamento, SSL, proxy reverso |
| **Ollama / LLM local** | 4 | Diário | Jarvis, experimentos RAG, testes |
| **FAISS / Embeddings** | 3 | Semanal | Memória vetorial, busca semântica |
| **LangChain / LlamaIndex** | 3 | Semanal | Orquestração de agentes, chains |
| **PostgreSQL / MySQL** | 4 | Semanal | Armazenamento principal |
| **Redis** | 3 | Mensal | Cache, sessões, filas |
| **Git / GitHub** | 4 | Diário | Versionamento, CI básico |
| **Linux (servidor)** | 4 | Diário | VPS, homelab, scripts shell |
| **Playwright / Puppeteer** | 3 | Mensal | Automação de navegador |
| **Scrapy / BeautifulSoup** | 4 | Mensal | Web scraping, crawlers |
| **Vite / shadcn** | 3 | Mensal | Setup e estilização de front-end |
| **Celery / Redis Queue** | 2 | Mensal | Filas de tarefas assíncronas |
| **Whisper (ASR)** | 3 | Semanal | Transcrição de áudio para o Jarvis |
| **C# / Java** | 2 | Raro | Fundamentos OOP, manutenção |
| **Shell Script** | 3 | Semanal | Automação de servidor, cron jobs |
| **Pandas / OpenPyXL** | 3 | Mensal | Processamento de dados, relatórios |

### Legenda de níveis
1. **Fundamentos** — Conhece conceitos, faz exemplos simples, precisa de documentação.
2. **Básico** — Usa com ajuda de documentação, resolve problemas comuns com eficiência.
3. **Intermediário** — Uso regular em projetos reais, boas práticas, debug independente.
4. **Avançado** — Domínio sólido, arquitetura, otimização, capaz de ensinar outros.
5. **Expert** — Referência na área, contribui para ferramentas, inova e publica.

## Projetos que comprovam cada skill

| Skill | Projeto comprovatório |
|-------|----------------------|
| Python, FastAPI, PostgreSQL | Auto-boletos — API REST com autenticação, filas, integração bancária |
| React, TypeScript, Vite | Gestor Aluguel — SPA com multi-tenancy, formulários complexos |
| Docker, Traefik, Linux | Infraestrutura completa — 3 VPS com proxy reverso, SSL, monitoramento |
| Ollama, FAISS, RAG | IA-LOCAL + Jarvis — Retrieval aumentado com documentos pessoais |
| Whisper, agentes | PROJECT_JARVIS_5.0 — Assistente com voz, memória e execução de tarefas |
| Scrapy, Playwright | Pipelines de coleta de dados — scraping estruturado com rotação de IP |
| Pandas, OpenPyXL | Relatórios financeiros dos produtos SaaS |

## Soft skills — aprofundamento

| Habilidade | Descrição | Como aplico no dia a dia | Exemplo concreto |
|------------|-----------|--------------------------|------------------|
| **Pensamento sistêmico** | Enxergar o todo antes das partes | Arquitetura de projetos e ecossistema pessoal | Decidir que um novo feature precisa de refatoração na base de dados antes |
| **Comunicação técnica** | Explicar conceitos complexos de forma simples | Documentação técnica, [[Will-Pessoal/04-Social/Rede/Pessoas|network]] | Explicar RAG para um amigo não-técnico |
| **Autogestão** | Priorizar e executar sem supervisão | Rotina de projetos pessoais e freelance | Manter 3 projetos ativos com entregas semanais |
| **Resolução de problemas** | Debugging lógico e criativo | Dia a dia como desenvolvedor solo | Encontrar gargalo de performance em query N+1 |
| **Aprendizado autodidata** | Absorver novas tecnologias rapidamente | Transição de PHP para IA local em menos de 1 ano | Aprender LangChain em 2 semanas lendo docs e exemplos |
| **Resiliência** | Continuar quando algo não funciona | Longa jornada de projetos que não deram certo | Projeto X que ficou 6 meses sem tração até pivotar |
| **Foco em entrega** | MVP funcional > perfeição teórica | Todos os produtos lançados | Lançar Gestor Aluguel com 60% das features planejadas |
| **Tomada de decisão** | Decidir com informação incompleta | Roadmap de produtos solo | Escolher entre feature A e B baseado em feedback de 3 usuários |

## Roteiro de aprendizado — 2026

### Trimestre 1 (Jan-Mar) — Concluído ✅
- [x] Aprofundar RAG com fontes múltiplas (PDF, áudio, web).
- [x] Refatorar pipeline de memória do Jarvis para usar FAISS + SQLite.
- [x] Estudar estratégias de chunking semântico e recuperação hierárquica.
- [x] Workshops internos: documentar lições de cada experimento.

### Trimestre 2 (Abr-Jun) — Em andamento 🔄
- [ ] Fine-tuning de modelos pequenos (Phi-3, Llama-3.2, Qwen 2.5) com LoRA.
- [ ] Implementar voz como entrada no Jarvis (Whisper local + wake word).
- [ ] Estudar arquitetura de agentes multi-etapa com reflexão.
- [ ] Curso/leitura: sistemas distribuídos e mensageria (RabbitMQ/Kafka conceitos).
- [ ] Melhorar cobertura de testes no Auto-boletos (meta: 60%+).

### Trimestre 3 (Jul-Set) — Planejado 📅
- [ ] Visão computacional básica — processamento de imagens com modelos locais (YOLO, Florence-2).
- [ ] Otimização de performance para inferência em CPU (quantização, ONNX).
- [ ] Produto SaaS: melhorias de UX e onboarding baseado em feedback.
- [ ] Leitura: "Designing Data-Intensive Applications" (finalizar).
- [ ] Configurar monitoramento com Prometheus + Grafana nos servidores.

### Trimestre 4 (Out-Dez) — Alvo 🎯
- [ ] Framework de agente pessoal reutilizável — documentado e publicável.
- [ ] Publicação de artigo técnico sobre IA local em português.
- [ ] Contribuição para projeto open source relacionado (LangChain, Ollama-py).
- [ ] Avaliação geral do ano: o que aprendi, onde ainda sou fraco, plano 2027.

## Skills a desenvolver prioritariamente

### Alta prioridade (impacto direto nos projetos atuais)
1. **Fine-tuning de LLMs** — Customizar modelos para tarefas específicas (classificação, extração).
2. **Sistemas de voz (ASR/TTS)** — Whisper, Coqui, voz como interface nativa do Jarvis.
3. **Arquitetura de agentes** — Planejamento, chain-of-thought, ferramentas, memória de longo prazo.

### Média prioridade (fortalecer a base)
4. **Mensageria e eventos** — RabbitMQ, Redis Streams, event sourcing.
5. **Testes automatizados** — Cobertura decente (60%+) nos projetos principais.
6. **Monitoramento e observabilidade** — Prometheus, Grafana, logging estruturado.

### Baixa prioridade (interesse futuro)
7. **Rust** — Performance crítica, ferramentas de sistema, WebAssembly.
8. **Elixir / Phoenix** — Concorrência e aplicações em tempo real, salas, notificações.
9. **Blender / 3D** — Criativo, hobby, modelagem para visualização de dados.

## Matriz de competências — visão geral

```
Python      ████████████████░░░░  80%
TypeScript  ████████████░░░░░░░░  60%
DevOps      ██████████░░░░░░░░░░  50%
IA local    ████████████░░░░░░░░  60%
BD          ██████████████░░░░░░  70%
Automação   ████████████████░░░░  80%
Front-end   ████████░░░░░░░░░░░░  40%
Arquitetura ██████████████░░░░░░  70%
Produto     ██████████░░░░░░░░░░  50%
```

## Como mantenho e atualizo esta nota

- **Revisão mensal**: Ajustar níveis de proficiência e aprendizados.
- **Cada novo projeto**: Adiciona skills à lista com nível inicial.
- [[Will-Pessoal/03-Vida-Estilo/Conhecimento/Leituras|Leituras]] são refletidas aqui quando relevantes para o roadmap.
- **Skills abaixo de nível 3**: Entram como alvo de estudo ativo no próximo trimestre.
- **O [[Cerebro-Will|Cérebro Will]]** integra essas skills com os projetos ativos e decisões de arquitetura.
