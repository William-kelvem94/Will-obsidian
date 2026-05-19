---
title: "🧠 BRAINSTORM GIGANTE — Expansão do Will-obsidian"
description: "Mais de 60 ideias criativas, práticas e acionáveis para expandir o segundo cérebro"
tags: [brainstorm, ideias, expansao, vault, jarvis, roadmap]
updated: 2026-05-19
---

# 🧠 BRAINSTORM GIGANTE — Expansão do Will-obsidian

> **Contexto**: Vault com arquitetura JARVIS 5 tiers, 13 domínios de conhecimento, ~10.787 chunks RAG, pipeline Python, MCP server, Dataview/Templater, GitHub Actions, pre-commit hooks. Tudo local-first e self-hosted.
>
> **Objetivo**: Gerar ideias massivas, criativas e **acionáveis** em 10 categorias.
>
> **Status Gerado em**: 2026-05-19 — Mapeamento automatizado contra o código-fonte.
> - ✅ = Implementado
> - 🔄 = Parcial (existe mas incompleto)
> - ❌ = Não iniciado

---

## Sumário

| Categoria | Qtd | ✅ | 🔄 | ❌ | Foco |
|-----------|-----|----|-----|-----|------|
| [A) Novos Domínios de Conhecimento](#a-novos-domínios-de-conhecimento) | 6 | 1 | 4 | 1 | Gaps no conhecimento-geral |
| [B) Automações Avançadas](#b-automações-avançadas) | 7 | 3 | 2 | 2 | Scripts que extraem mais valor |
| [C) Integrações](#c-integrações) | 7 | 1 | 1 | 5 | Conectar com ferramentas externas |
| [D) Novos Dashboards e Visualizações](#d-novos-dashboards-e-visualizações) | 6 | 2 | 0 | 4 | Dataview, gráficos, heatmaps |
| [E) Gamificação e Hábitos](#e-gamificação-e-hábitos) | 6 | 4 | 0 | 2 | Tracking pessoal no vault |
| [F) IA Avançada](#f-ia-avançada) | 7 | 1 | 2 | 4 | Agentes, RAG improvements |
| [G) Publicação e Compartilhamento](#g-publicação-e-compartilhamento) | 5 | 0 | 0 | 5 | Digital garden, seleção pública |
| [H) Produtividade Pessoal](#h-produtividade-pessoal) | 6 | 2 | 2 | 2 | Workflows diários |
| [I) Expansão JARVIS](#i-expansão-jarvis) | 6 | 1 | 1 | 4 | Novas camadas e capacidades |
| [J) Ideias Loucas/Disruptivas](#j-ideias-loucadisruptivas) | 6 | 0 | 0 | 6 | Fora da caixa |
| **TOTAL** | **62** | **15** | **12** | **35** | |

---

## A) NOVOS DOMÍNIOS DE CONHECIMENTO

### A1. 🔄 Design de Interfaces e Experiência do Usuário (UI/UX)
**Descrição**: Notas sobre design de interfaces, psicologia das cores, hierarquia visual, acessibilidade (WCAG), design systems, Figma, prototipação.
**Por que é valioso**: Will tem projetos de frontend (web, mobile) e precisa de fundamentos sólidos de UX para tomar decisões de design.
**Como implementar**: Criar `Conhecimento-Geral/Design/` com notas atômicas: `Principios-UI.md`, `Acessibilidade.md`, `Design-Systems.md`, `Figma-Guia.md`. Usar template `Conceito-Conhecimento.md`. Linkar com `skills/frontend/`.
**Dificuldade**: Fácil
**Status**: 🔄 Parcial — `Conhecimento-Geral/IA-para-Programacao/UI-e-Agentes.md` cobre parte do conteúdo, mas sem domínio dedicado.

### A2. 🔄 Ciência de Dados e Estatística Aplicada
**Descrição**: Estatística descritiva, inferencial, testes de hipótese, Bayesian statistics, análise exploratória, visualização de dados (matplotlib, seaborn, plotly).
**Por que é valioso**: Will trabalha com Python, ML e análise — estatística é a base que sustenta tudo.
**Como implementar**: Expandir `Conhecimento-Geral/Matematica/` com `Estatistica-Descritiva.md`, `Testes-Hipotese.md`, `Bayesiana.md`. Criar dashboard Dataview de proficiência com `#level-*`.
**Dificuldade**: Médio
**Status**: 🔄 Parcial — `Conhecimento-Geral/Matematica/Probabilidade-e-Estatistica.md` (1089 linhas) cobre o conteúdo, mas sem notas separadas por tópico.

### A3. 🔄 Cibersegurança Prática
**Descrição**: Fundamentos de segurança ofensiva/defensiva, OWASP Top 10, hardening de servidores, segurança em APIs, criptografia aplicada, gestão de vulnerabilidades.
**Por que é valioso**: Vault já tem `SEGURANCA_PRIVACIDADE.md` e `audit_sensitives.py` — expandir para um domínio completo de segurança.
**Como implementar**: Criar `Conhecimento-Geral/Seguranca/` com `OWASP.md`, `Criptografia-Aplicada.md`, `Hardening-Linux.md`, `Secure-API.md`. Linkar com skills de Security e DevOps.
**Dificuldade**: Médio
**Status**: 🔄 Parcial — `skills/Security/AI-Security-Etica-Operacional.md` (1586 linhas) + `SEGURANCA_PRIVACIDADE.md`, mas sem domínio dedicado.

### A4. ✅ Geopolítica e Relações Internacionais
**Descrição**: Análise de conflitos, blocos econômicos (UE, BRICS, ASEAN), teoria das relações internacionais, história diplomática, poder militar e nuclear.
**Por que é valioso**: Complementa História, Ciência Política e Economia — forma uma visão sistêmica do mundo.
**Como implementar**: Criar `Conhecimento-Geral/Geopolítica/` com `Teoria-RI.md`, `Conflitos-Contemporaneos.md`, `Blocos-Economicos.md`. Usar Dataview para interlink com `Historia/` e `Economia-Digital.md`.
**Dificuldade**: Médio
**Status**: ✅ Implementado — `Conhecimento-Geral/Historia/Geopolitica.md` (461 linhas) + `Cultura/Geografia.md` cobrem o domínio.

### A5. 🔄 Medicina e Fisiologia Humana Avançada
**Descrição**: Anatomia, farmacologia básica, sistema imunológico, microbioma, nutrição clínica, medicina preventiva, nootropicos, longevidade.
**Por que é valioso**: Seção pessoal já tem `Saude.md` — expandir para um domínio completo de conhecimento sobre o corpo humano.
**Como implementar**: Criar `Conhecimento-Geral/Medicina/` com `Anatomia-Basica.md`, `Farmacologia.md`, `Microbioma.md`, `Longevidade.md`. Linkar com `Will-Pessoal/03-Vida-Estilo/Vida/Saude.md`.
**Dificuldade**: Médio
**Status**: 🔄 Parcial — `Biologia/Fisiologia-Humana.md` (700+ linhas) + `Psicologia-Clinica.md` cobrem parte, sem domínio dedicado.

### A6. ❌ Teoria Musical e Produção de Áudio
**Descrição**: Teoria musical (harmonia, ritmo, melodia), produção musical digital (DAWs, síntese, sampling), engenharia de áudio, acústica.
**Por que é valioso**: Domínio criativo completamente ausente no vault — expande a inteligência geral para artes auditivas.
**Como implementar**: Criar `Conhecimento-Geral/Musica/` com `Teoria-Musical.md`, `Producao-Audio.md`, `Acustica.md`. Usar assets multimodais (referências a áudio) conforme `MULTIMODALIDADE.md`.
**Dificuldade**: Fácil
**Status**: ❌ Não iniciado — menções dispersas em `Estetica-e-Arte.md` e `Fisica-Fundamental.md`, sem domínio próprio.

---

## B) AUTOMAÇÕES AVANÇADAS

### B1. ✅ Sugestor Automático de Conexões Entre Notas
**Descrição**: Script Python que analisa embeddings de todas as notas e sugere links `[[...]]` entre notas semanticamente similares que ainda não estão conectadas.
**Por que é valioso**: Aumenta a densidade do graph vault sem esforço manual — mais conexões = melhor RAG.
**Como implementar**: Usar `knowledge_indexer.py` como base. Adicionar função `suggest_links()` que compara vetores via cosine similarity e gera relatório `conexoes_sugeridas.md` com sugestões de `[[link]]`.
**Dificuldade**: Médio
**Status**: ✅ Implementado — `.scripts/connection_suggester.py` (703 linhas) gera `conexoes_sugeridas.md` com TF-IDF + cosine similarity.

### B2. 🔄 Gerador Automático de Flashcards do Vault
**Descrição**: Script que varre notas do Conhecimento-Geral, extrai conceitos-chave (usando NLP simples ou LLM local) e gera decks CSV para Anki automaticamente.
**Por que é valioso**: Transforma o vault passivo em material de estudo ativo — repetição espaçada sem digitar flashcards.
**Como implementar**: Script Python que lê frontmatter `status: concluído`, extrai sentenças com `é um/uma` e definições, gera CSV no formato do `flashcards/XAI-Fairness-Deck.csv`. Rodar periodicamente via GitHub Actions.
**Dificuldade**: Médio
**Status**: 🔄 Parcial — `flashcards/` existe com deck de exemplo (XAI-Fairness-Deck.csv), mas sem gerador automático.

### B3. ✅ Detector de Decadência de Notas (Knowledge Decay)
**Descrição**: Script que identifica notas não revisadas há X dias, marca `status: stale` no frontmatter e gera lista para revisão prioritária.
**Por que é valioso**: O conhecimento não revisitado se deteriora — o vault precisa lembrar o que precisa ser revisado.
**Como implementar**: Python script que compara `file.mtime` com data atual, aplica threshold (30/60/90 dias), atualiza frontmatter. Disparar via GitHub Actions semanal (`vault-maintenance.yml`).
**Dificuldade**: Fácil
**Status**: ✅ Implementado — `.scripts/decay_detector.py` (364 linhas) detecta notas stale/archived e gera `decay_report.md`.

### B4. ✅ Pipeline de Resumo Semanal do Vault
**Descrição**: Todo domingo, um script gera uma nota `JARVIS/03-Memory/Logs/Resumo-Semanal-YYYY-MM-DD.md` com: notas novas, conexões criadas, gaps fechados, projetos atualizados.
**Por que é valioso**: Mantém Will orientado sobre a evolução do próprio cérebro — visão macro semanal.
**Como implementar**: Script que consulta git log da semana (`git log --since="7 days ago"`), combina com stats do `vault_cleanup_report.md`, gera nota com template predefinido.
**Dificuldade**: Fácil
**Status**: ✅ Implementado — `.scripts/weekly_summary.py` (279 linhas) gera relatório semanal completo.

### B5. 🔄 Auto-Enriquecimento de Metadados com LLM Local
**Descrição**: Usar Ollama (modelo local tipo Llama 3 ou Mistral) para analisar notas sem frontmatter e sugerir: tags, área, descrição, nível de proficiência automaticamente.
**Por que é valioso**: Elimina o gargalo manual de frontmatter — notas novas já nascem com metadados ricos para RAG.
**Como implementar**: Script Python que chama Ollama API (`localhost:11434/api/generate`), envia conteúdo da nota, recebe JSON com sugestões, atualiza frontmatter. Baseado em `enrich_frontmatter.py`.
**Dificuldade**: Difícil
**Status**: 🔄 Parcial — `scripts/enrich_frontmatter.py` existe mas gera frontmatter padrão (sem LLM). Pipeline RAG em `skills/04-knowledge-systems/rag-pipeline/query_engine.py` já usa Ollama para respostas.

### B6. ❌ Previsor de Saúde do Vault (ML)
**Descrição**: Modelo simples (regressão ou random forest) que prevê a "saúde" futura do vault baseado em tendências históricas: commits, novas notas, conexões, gaps.
**Por que é valioso**: Transforma métricas descritivas em preditivas — Will pode agir antes do vault degradar.
**Como implementar**: Coletar dados do `project_health_checker.py` e `vault_cleanup.py` ao longo do tempo, armazenar em JSON histórico, treinar modelo com scikit-learn (já tem em skills). Dashboard DataviewJS para exibir previsão.
**Dificuldade**: Difícil
**Status**: ❌ Não iniciado — `project_health_checker.py` existe mas é heurístico, sem modelo preditivo.

### B7. ❌ Arquivamento Inteligente com Git Tags
**Descrição**: Script que, ao arquivar um projeto, automaticamente cria uma git tag (ex: `archive/projeto-x-2026-05`), move notas para `Projetos/02-Arquivo/`, e atualiza `Projetos.md`.
**Por que é valioso**: Arquivamento consistente e rastreável — cada projeto arquivado vira um checkpoint no git.
**Como implementar**: Python script que: (1) pergunta qual projeto arquivar, (2) move notas, (3) cria git tag, (4) atualiza hub `Projetos.md`. Disparo manual ou via CLI.
**Dificuldade**: Fácil
**Status**: ❌ Não iniciado

---

## C) INTEGRAÇÕES

### C1. ❌ Sincronização Bidirecional com Zotero
**Descrição**: Conectar o vault ao Zotero (gerenciador de referências) para importar/exportar citações, criar notas de leitura automáticas a partir de PDFs anotados.
**Por que é valioso**: Já está no roadmap v2.0 — transforma o vault em centro de pesquisa acadêmica com citações formatadas (ABNT/APA).
**Como implementar**: Plugin Zotero Obsidian ou script Python com `pyzotero` para sync. Notas de leitura vão para `Conhecimento-Geral/` com frontmatter contendo `citekey`, `authors`, `doi`. Usar template `Template-Reuniao.md` adaptado.
**Dificuldade**: Médio
**Status**: ❌ Não iniciado (planejado ROADMAP v2.0)

### C2. ❌ Leitor de Kindle Integrado
**Descrição**: Importar destaques e notas do Kindle (My Clippings.txt) automaticamente para o vault, categorizados por livro, com link para nota de leitura.
**Por que é valioso**: Will tem `Will-Pessoal/03-Vida-Estilo/Conhecimento/Leituras.md` — pode virar um hub vivo de tudo que é lido.
**Como implementar**: Script Python que parseia `My Clippings.txt`, cria notas por livro em `Leituras/[Titulo-Livro].md` com highlights, tags, data. Template `Template Base.md`. Rodar semanalmente.
**Dificuldade**: Fácil
**Status**: ❌ Não iniciado

### C3. ❌ Web Clipper para o Vault (Self-Hosted)
**Descrição**: Extensão de navegador (ou bookmarklet) que salva artigos da web diretamente como notas markdown no vault, com frontmatter, link original e metadados.
**Por que é valioso**: Elimina o atrito de copiar/colar — qualquer página vira nota atômica em segundos.
**Como implementar**: Duas opções: (a) extensão Chrome que faz POST para MCP server local, (b) bookmarklet que envia para endpoint Python Flask local. Baseado em `mcp-vault-server/index.js` (ferramenta write_vault_file).
**Dificuldade**: Difícil
**Status**: ❌ Não iniciado

### C4. ❌ Integração com Calendário (Google Calendar Local)
**Descrição**: Sincronizar eventos do Google Calendar (via export .ics local) com notas de daily log e planejamento semanal no vault.
**Por que é valioso**: Conecta o plano (calendário) com o registro (vault) — sem depender de plugin de nuvem.
**Como implementar**: Script Python que baixa .ics de um endpoint público (ou export manual), parseia com `icalendar`, e cria/atualiza notas em `Will-Pessoal/03-Vida-Estilo/` com eventos do dia. Rodar via `daily_logger.py`.
**Dificuldade**: Médio
**Status**: ❌ Não iniciado

### C5. 🔄 Leitura de PDF com Anotações no Vault
**Descrição**: Ao colocar um PDF na pasta `assets/`, extrair texto automaticamente, chunkear, indexar no RAG e criar nota resumo com referência.
**Por que é valioso**: Aproveita o pipeline multimodal existente (`preprocess_multimodal.py`) para tornar PDFs pesquisáveis via RAG.
**Como implementar**: Usar `pypdf` ou `pdfplumber` para extração, `scripts/preprocess_multimodal.py` para indexação, criar nota `Conhecimento-Geral/Leituras/[Titulo].md` automaticamente.
**Dificuldade**: Médio
**Status**: 🔄 Parcial — `scripts/preprocess_multimodal.py` escaneia assets referenciados mas não extrai texto de PDFs.

### C6. ✅ Conector com Armazém de Código (GitHub Local Mirror)
**Descrição**: Sincronizar READMEs, docs e issues de repositórios do Will (já mapeados em `github_sync.py`) como notas no vault para pesquisa RAG.
**Por que é valioso**: O código e suas docs ficam searcháveis junto com o conhecimento geral — unifica tudo.
**Como implementar**: Estender `github_sync.py` para: (1) clonar/atualizar mirror local, (2) extrair README.md, (3) criar nota em `Projetos/03-Estudos/docs/[repo].md` com frontmatter.
**Dificuldade**: Médio
**Status**: ✅ Implementado — `.scripts/github_sync.py` sincroniza repositórios e gera `Projetos/GitHub-Completo.md`.

### C7. ❌ Sentinela de Mudanças em Repositórios (Webhook Local)
**Descrição**: Servidor web mínimo (FastAPI/Flask) que recebe webhooks do GitHub e cria automaticamente notas de changelog/delta no vault quando repos são atualizados.
**Por que é valioso**: Mantém o vault sincronizado com a atividade real de código sem polling manual.
**Como implementar**: Criar `scripts/webhook_server.py` com rota `/github-webhook`, processar payload push, criar nota em `JARVIS/03-Memory/Logs/Changelogs/`. Usar GitHub Actions para enviar webhook ao servidor local via `curl`.
**Dificuldade**: Difícil
**Status**: ❌ Não iniciado

---

## D) NOVOS DASHBOARDS E VISUALIZAÇÕES

### D1. ❌ Timeline Interativa do Aprendizado (DataviewJS + Mermaid)
**Descrição**: Dashboard que exibe uma timeline visual (Mermaid.js) com marcos de aprendizado: notas criadas, skills concluídas, projetos iniciados/entregues.
**Por que é valioso**: Mostra a jornada de aprendizado ao longo do tempo — motivação e orientação.
**Como implementar**: Query DataviewJS que agrupa notas por mês com `file.ctime`, gera bloco ```mermaid timeline``` dinâmico. Dashboard em `dashboards/Timeline-Aprendizado.md`.
**Dificuldade**: Médio
**Status**: ❌ Não iniciado

### D2. ✅ Matriz de Habilidades vs. Projetos (Skill-Project Matrix Avançada)
**Descrição**: Dashboard interativo que cruza cada skill com projetos que a utilizam, mostrando cobertura e gaps de aplicação prática.
**Por que é valioso**: Já existe `skills/Skill-Project-Matrix.md` — transformar em visualização dinâmica.
**Como implementar**: DataviewJS que lê frontmatter de skills (`used_in: [projeto-x]`) e projetos (`skills_used: [skill-y]`), gera tabela/heatmap 2D. Adicionar a `dashboards/INDEX.md`.
**Dificuldade**: Fácil
**Status**: ✅ Implementado — `dashboards/Skill-Project-Matrix-Dinamica.md` (354 linhas) com DataviewJS, heatmap, busca.

### D3. ❌ Scorecard de Consistência Semanal
**Descrição**: Dashboard que mostra streaks: dias consecutivos com edições, notas criadas por dia da semana, horários de pico de produtividade.
**Por que é valioso**: Métricas de consistência são mais importantes que métricas de volume — streaks motivam.
**Como implementar**: Script Python que analisa `git log --format="%ai"` e gera JSON consumido por DataviewJS. Dashboard com tabela de streaks e gráfico de calor semanal.
**Dificuldade**: Médio
**Status**: ❌ Não iniciado

### D4. ✅ Nuvem de Tags 3D (Tag Cloud Geracional)
**Descrição**: Tag cloud onde o tamanho reflete frequência e a cor reflete "idade" (tags mais recentes em destaque) — visualização via CSS/SVG customizado.
**Por que é valioso**: Já tem lista de tags em `dashboards/Knowledge-Heatmap.md` — uma nuvem visual é mais rápida de absorver.
**Como implementar**: DataviewJS que agrupa tags, pondera por `file.ctime`, gera HTML com `<span>` estilizados (tamanho = freq, cor = idade). CSS custom theme existente para estilização.
**Dificuldade**: Médio
**Status**: ✅ Implementado — `dashboards/Tag-Cloud.md` (120 linhas) com DataviewJS interativo.

### D5. ❌ Radar de Progresso Multi-Domínio (Aranha)
**Descrição**: Gráfico radar (spider chart) que mostra nível de cobertura em cada domínio de conhecimento, comparando com meta definida.
**Por que é valioso**: Visualização instantânea de "onde estou vs. onde quero estar" em cada área.
**Como implementar**: DataviewJS com Canvas API ou Chart.js (via iframe local). Coleta `#level-*` tags por área, normaliza em escala 0-100. Dashboard em `dashboards/Radar-Conhecimento.md`.
**Dificuldade**: Difícil
**Status**: ❌ Não iniciado

### D6. ❌ Mapa de Conexões do Graph com Filtros
**Descrição**: Dashboard que permite filtrar o graph vault por: domínio, tag, período de criação, status — sem abrir o graph nativo do Obsidian.
**Por que é valioso**: Graph nativo é limitado em filtros — visualização no DataviewJS permite queries arbitrárias.
**Como implementar**: DataviewJS com botões/checkboxes (usando `dv.span` + CSS) que filtram notas por tag/area/data e exibem link de conexões. Base no `vault_graph_query` do MCP server.
**Dificuldade**: Difícil
**Status**: ❌ Não iniciado

---

## E) GAMIFICAÇÃO E HÁBITOS

### E1. ✅ Sistema de XP e Níveis para Skills
**Descrição**: Cada skill nota ganha XP automaticamente (por edições, conexões, conclusão de leituras associadas). Ao atingir threshold, sobe de nível (1→100).
**Por que é valioso**: Transforma aprendizado em jogo — motiva consistência e progressão visível.
**Como implementar**: Script Python que varre git log por skill, conta commits em notas com `#skills-*`, calcula XP, atualiza frontmatter com `xp: 450`, `level: 12`. Dashboard DataviewJS exibe ranking.
**Dificuldade**: Médio
**Status**: ✅ Implementado — `.scripts/xp_system.py` (713 linhas) + `skills/xp_leaderboard.md` com 10 níveis.

### E2. ✅ Desafios Semanais Gerados pelo Vault
**Descrição**: Toda semana, o vault sugere um "desafio": preencher um gap de conhecimento, conectar 5 notas órfãs, ou escrever resumo de um domínio.
**Por que é valioso**: Direciona o esforço de melhoria do vault para áreas que realmente precisam.
**Como implementar**: Script que analisa `GAPS.md`, notas órfãs, e baixa cobertura RAG, gera nota `JARVIS/02-Operational/Challenges/Desafio-Semanal.md` com tarefa específica.
**Dificuldade**: Fácil
**Status**: ✅ Implementado — `.scripts/challenge_generator.py` (449 linhas) gera desafios semanais com análise de notas órfãs.

### E3. ✅ Habit Tracker Dentro do Vault (Sistema de Ticks)
**Descrição**: Nota central onde Will marca hábitos diários (ler, estudar, exercício, codar) com checkboxes. DataviewJS calcula streaks, taxa de conclusão semanal/mensal.
**Por que é valioso**: `Habitos.md` existe mas é estático — transformar em tracker vivo com métricas e streaks.
**Como implementar**: Template `Template Diário.md` já existe — adaptar template para incluir seção de hábitos. DataviewJS em `Will-Pessoal/03-Vida-Estilo/Vida/Habitos.md` para agregar dados de todas as notas diárias.
**Dificuldade**: Médio
**Status**: ✅ Implementado — `Habitos.md` (208 linhas) com DataviewJS streaks + `Template Diário.md` com checkboxes.

### E4. ✅ Conquistas e Badges (Achievement System)
**Descrição**: Badges que Will "desbloqueia" ao atingir marcos: "100 notas criadas", "10 dias de streak", "primeiro gap fechado", "50 conexões em um mês".
**Por que é valioso**: Reforço positivo automático — celebra marcos que normalmente passariam despercebidos.
**Como implementar**: Script que verifica condições contra métricas do vault. Ao atingir, gera nota em `Will-Pessoal/Conquistas/[Nome-Conquista].md` com descrição e data. Dashboard exibe coleção.
**Dificuldade**: Fácil
**Status**: ✅ Implementado — `.scripts/achievement_system.py` (744 linhas), 15 badges, 11 já desbloqueados.

### E5. ❌ Competição Consigo Mesmo (PB Tracking)
**Descrição**: Dashboard que compara métricas atuais com records pessoais: mais notas em um dia, maior streak de commits, maior densidade de links por nota.
**Por que é valioso**: Competição saudável consigo mesmo — superar PBs é inerentemente motivador.
**Como implementar**: Script que mantém arquivo `records.json` com PBs históricos. DataviewJS compara com metrica atual e exibe 🔥 quando recorde é batido.
**Dificuldade**: Fácil
**Status**: ❌ Não iniciado

### E6. ❌ Jornada do Conhecimento (RPG Style)
**Descrição**: Mapa visual (em Mermaid ou SVG) mostrando "regiões" de conhecimento desbloqueadas. Cada domínio novo é uma "terra" conquistada. Skills são "habilidades do personagem".
**Por que é valioso**: Transforma o vault literalmente em um RPG de conhecimento — extremamente motivador e visual.
**Como implementar**: DataviewJS que gera mapa ascii/bloco Mermaid com áreas desbloqueadas (verde) e bloqueadas (cinza) baseado em `status` do frontmatter. Dashboard `dashboards/Mapa-RPG.md`.
**Dificuldade**: Difícil
**Status**: ❌ Não iniciado

---

## F) IA AVANÇADA

### F1. 🔄 Agente JARVIS Autônomo com Memória Episódica
**Descrição**: Agente que roda em loop (via script Python ou servidor) com acesso MCP ao vault, mantém memória de conversas anteriores (em `JARVIS/03-Memory/`), e executa tarefas autônomas: análise de gaps, sugestão de conexões, verificação de saúde.
**Por que é valioso**: Transforma JARVIS de framework passivo para assistente ativo que cuida do vault sozinho.
**Como implementar**: Script `jarvis_daemon.py` que: (1) carrega contexto de `JARVIS/02-Operational/Context/`, (2) consulta métricas, (3) usa LLM local (Ollama) para decidir ação, (4) executa via MCP tools ou scripts existentes. Log em `JARVIS/03-Memory/Logs/`.
**Dificuldade**: Difícil
**Status**: 🔄 Parcial — `scripts/jarvis_memory_bridge.py` existe mas sem loop autônomo/daemon.

### F2. ✅ Chat Interface Web com Contexto do Vault (RAG + Agente)
**Descrição**: Interface web (já existe `start-web-ui.bat`) melhorada com chat que usa o vault inteiro como contexto RAG, permitindo perguntas em linguagem natural sobre qualquer nota.
**Por que é valioso**: Web UI já existe — transformar em assistente conversacional completo com o cérebro do Will.
**Como implementar**: Modificar `web-ui/` para incluir: (1) input de pergunta, (2) query ao índice vetorial (`knowledge_indexer.py`), (3) prompt para LLM local com chunks recuperados, (4) resposta formatada com links para notas fonte.
**Dificuldade**: Difícil
**Status**: ✅ Implementado — `web-ui/` com search + RAG pipeline (`query_engine.py` + `embeddings_generator.py` + `vector_store.py`).

### F3. ❌ Geração Automática de Resumos Multi-Nível
**Descrição**: Para cada domínio ou nota grande, gerar resumos automáticos em 3 níveis: parágrafo (30s), bullet points (5min), e texto completo+. Armazenar em `abstract` do frontmatter.
**Por que é valioso**: Melhora a qualidade do RAG (sumários são melhores queries targets) e permite digest rápido de qualquer área.
**Como implementar**: Script que usa Ollama para gerar resumos, salva no frontmatter como `abstract_short`, `abstract_medium`, `abstract_long`. Priorizar notas sem abstract já no frontmatter.
**Dificuldade**: Médio
**Status**: ❌ Não iniciado

### F4. ❌ Recomendador de Próximo Estudo (RAG + Skill Gap)
**Descrição**: Sistema que analisa o perfil de skills atual, gaps existentes, e histórico de estudos para recomendar o "próximo melhor tópico" a estudar.
**Por que é valioso**: Elimina a paralisia de decisão — o vault diz exatamente o que estudar hoje.
**Como implementar**: Script Python que: (1) carrega `GAPS.md`, (2) analisa skills com `#level-basic`, (3) consulta histórico de estudos recentes, (4) gera nota `JARVIS/02-Operational/Proximo-Estudo.md` com recomendação.
**Dificuldade**: Médio
**Status**: ❌ Não iniciado

### F5. ❌ Classificador Automático de Notas (Tag Suggest com ML)
**Descrição**: Modelo leve (TF-IDF + Naive Bayes ou similar) treinado nas notas existentes que sugere tags para notas novas automaticamente.
**Por que é valioso**: Tags consistentes são essenciais para RAG e dashboards — automação garante qualidade.
**Como implementar**: Treinar classificador com conteúdo + tags das notas atuais (features = TF-IDF, target = tags). Salvar modelo pickle. Script `tag_classifier.py` no pre-commit (igual `enrich_frontmatter.py`).
**Dificuldade**: Médio
**Status**: ❌ Não iniciado

### F6. 🔄 Cache Inteligente de Embeddings (Prioridade por Uso)
**Descrição**: Em vez de rebuildar embeddings sempre, manter cache priorizado: notas mais acessadas/relevantes têm embeddings mantidos em memória; notas frias são recalculadas sob demanda.
**Por que é valioso**: Performance — rebuild completo de 10k+ chunks é caro. Cache inteligente reduz tempo de indexação em 80%.
**Como implementar**: Modificar `knowledge_indexer.py` para: (1) manter índice de frequência de acesso (query log), (2) priorizar notas "quentes", (3) rebuild diferencial. Usar `--update` como default.
**Dificuldade**: Difícil
**Status**: 🔄 Parcial — `knowledge_indexer.py` tem detecção básica de mudanças, mas sem cache por prioridade de acesso.

### F7. ❌ Agente Revisor de Qualidade (QA Agent)
**Descrição**: Agente que periodicamente lê notas aleatórias e avalia: qualidade do conteúdo, clareza, conexões faltantes, frontmatter incompleto. Gera relatório de qualidade.
**Por que é valioso**: Garante padrão mínimo de qualidade em todo o vault — evita acúmulo de notas ruins.
**Como implementar**: Script que seleciona notas com `status: draft`, envia para LLM local com prompt de avaliação, coleta score e sugestões, gera `qa_report.md`. Rodar semanalmente no CI.
**Dificuldade**: Médio
**Status**: ❌ Não iniciado

---

## G) PUBLICAÇÃO E COMPARTILHAMENTO (0/5 implementados)

### G1. ❌ Digital Garden com Publicação Seletiva
**Descrição**: Site estático (Jekyll/11ty/Quartz) que publica notas selecionadas (marcadas com `#public`) em um jardim digital público.
**Por que é valioso**: Já está no roadmap v3.0 — transforma conhecimento privado em contribuição pública sem expor tudo.
**Como implementar**: Script que filtra notas com tag `#public`, copia para repo separado, build com Quartz (framework para Obsidian → site). GitHub Actions publica via GitHub Pages.
**Dificuldade**: Difícil
**Status**: ❌ Não iniciado (planejado ROADMAP v3.0)

### G2. ❌ Newsletter Automática do Vault
**Descrição**: Gerar resumo semanal/mensal em formato newsletter (Markdown → HTML) com: novas notas, conexões descobertas, projeto em destaque, skill do mês.
**Por que é valioso**: Disciplina de curadoria + potencial de compartilhar conhecimento com rede.
**Como implementar**: Script que compila dados semanais (notas novas, commits, conexões), aplica template HTML simples, salva em `public/newsletter/`. Disparo manual ou via CI.
**Dificuldade**: Médio
**Status**: ❌ Não iniciado

### G3. ❌ Portfólio de Skills Baseado no Vault
**Descrição**: Página web pública que exibe as skills de Will, com nível de proficiência, projetos associados e descrições — tudo puxado automaticamente do vault.
**Por que é valioso**: Substitui LinkedIn/currículo tradicional por algo vivo e real — mostra o que Will realmente sabe.
**Como implementar**: Script que lê `skills/` e `Projetos/`, extrai frontmatter (skills + level), conecta com projetos, gera HTML estático. GitHub Pages com domínio customizado.
**Dificuldade**: Médio
**Status**: ❌ Não iniciado (dados fonte existem em `skills/xp_leaderboard.md` e `Skill-Project-Matrix.md`)

### G4. ❌ Exportação de Knowledge Base para Equipe
**Descrição**: Gerar versão sanitizada do vault (sem notas pessoais) para compartilhar com colegas de equipe como base de conhecimento técnica.
**Por que é valioso**: Will tem conhecimento técnico extenso em várias áreas — compartilhar com equipe amplifica impacto.
**Como implementar**: Script que: (1) filtra notas com tag `#public` ou `#team`, (2) remove frontmatter sensível, (3) gera zip com estrutura limpa. CI gera artefato.
**Dificuldade**: Fácil
**Status**: ❌ Não iniciado

### G5. ❌ Sessões de Estudo Ao Vivo com o Vault
**Descrição**: Usar o vault como "slides vivos" durante sessões de estudo/palestra: navegar pelo graph, mostrar conexões, abrir notas como explicação — tudo ao vivo.
**Por que é valioso**: O vault é o melhor portfólio de conhecimento que Will tem — apresentar diretamente dele é mais autêntico que slides.
**Como implementar**: Modo "apresentação" via CSS theme customizado (fonte grande, foco na nota atual). Bookmarklet ou hotkey que entra em modo apresentação. Navegação pelos links internos.
**Dificuldade**: Fácil
**Status**: ❌ Não iniciado

---

## H) PRODUTIVIDADE PESSOAL (2/6 implementados)

### H1. ✅ Daily Notes Autogerenciadas com Revisão de OKRs
**Descrição**: Template diário que automaticamente puxa OKRs da semana, tarefas pendentes, e hábitos do dia — a nota já nasce preenchida com contexto.
**Por que é valioso**: Template diário existe mas não tem integração com OKRs e pendências — reduz atrito de planejamento.
**Como implementar**: Adaptar `Template Diário.md` com Dataview inline queries que puxam de `Will-Pessoal/02-Visao/OKRs.md` e `Projetos/Plano-de-Acao.md`. Usar Templater para auto-preenchimento.
**Dificuldade**: Fácil
**Status**: ✅ Implementado — `Template Diário.md` com Templater carrega OKRs automaticamente.

### H2. ❌ Pomodoro Tracker Integrado ao Diário
**Descrição**: Durante o dia, Will registra pomodoros completados. O vault calcula total por projeto/distração e exibe produtividade semanal.
**Por que é valioso**: Conecta tracking de foco com o vault — dados de produtividade viés zero.
**Como implementar**: DataviewJS na daily note que soma pomodoros marcados (checkboxes). Dashboard semanal em `Will-Pessoal/03-Vida-Estilo/Vida/Produtividade.md`.
**Dificuldade**: Fácil
**Status**: ❌ Não iniciado

### H3. ❌ Integração de Lista de Compras e Compras Recorrentes
**Descrição**: Nota central com lista de compras categorizada (supermercado, farmácia, tecnologia), com frequência de compra e preço médio.
**Por que é valioso**: Finanças pessoais (`Financas.md`) existe — estender para tracking granular de despesas recorrentes.
**Como implementar**: Criar `Will-Pessoal/03-Vida-Estilo/Vida/Compras.md` com tabela Dataview. Template para adicionar item. Script que calcula gasto mensal estimado.
**Dificuldade**: Fácil
**Status**: ❌ Não iniciado

### H4. 🔄 Planejador de Rotina Semanal com Dataview
**Descrição**: Dashboard que mostra a rotina ideal vs. real da semana, puxando dados das daily notes e comparando com metas de `Rotina.md`.
**Por que é valioso**: Rotina.md existe mas é estática — comparar com execução real revela gaps de consistência.
**Como implementar**: DataviewJS que agrega todas as daily notes da semana, extrai horas de sono, exercise, estudo, e plota tabela comparativa com meta.
**Dificuldade**: Médio
**Status**: 🔄 Parcial — `Rotina.md` existe mas é estática, sem DataviewJS de comparação.

### H5. 🔄 Rastreador de Metas Financeiras (OKR Financeiro)
**Descrição**: Dashboard que acompanha metas financeiras (economia mensal, investimentos, redução de dívidas) com gráficos de progresso e projeções.
**Por que é valioso**: `Financas.md` existe — transformar em dashboard vivo com metas e acompanhamento mensal.
**Como implementar**: DataviewJS que puxa dados de `Financas.md` (ou notas dedicadas por mês), calcula progresso, gera gráfico de barras com Canvas/Chart.js local.
**Dificuldade**: Médio
**Status**: 🔄 Parcial — `Financas.md` (115 linhas) existe mas é nota estática sem dashboard.

### H6. ✅ Assistente de Foco (Modo "Não Perturbe" para o Vault)
**Descrição**: Ao ativar "modo foco" (via hotkey ou comando), o vault esconde dashboards, distrações, projetos paralelos e mostra apenas a nota/tarefa atual.
**Por que é valioso**: Obsidian pode ser um ambiente barulhento — modo foco reduz atrito cognitivo.
**Como implementar**: CSS snippet que oculta elementos da interface. Botão no custom CSS theme que alterna classe `.focus-mode`. Templater command para ativar.
**Dificuldade**: Fácil
**Status**: ✅ Implementado — `.obsidian/snippets/focus-mode.css` (111 linhas) com suporte a toggle.

---

## I) EXPANSÃO JARVIS (1/6 implementados)

### I1. ❌ Tier 6: Meta-Cognição (JARVIS aprendendo sobre si mesmo)
**Descrição**: Nova camada acima das 5 existentes que armazena "insights" do JARVIS sobre seu próprio funcionamento: padrões de erro, otimizações descobertas, relações entre camadas.
**Por que é valioso**: Fecha o ciclo — JARVIS não só opera, mas reflete sobre como opera (meta-cognição).
**Como implementar**: Criar `JARVIS/06-Metacognition/` com `Self-Patterns.md`, `Optimizations-Discovered.md`, `Cross-Layer-Insights.md`. Script que analisa logs (`JARVIS/03-Memory/Logs/`) e extrai padrões automaticamente.
**Dificuldade**: Difícil
**Status**: ❌ Não iniciado

### I2. 🔄 Persona Dinâmica (Adaptação por Contexto do Projeto)
**Descrição**: Em vez de carregar persona fixa, JARVIS escolhe automaticamente a sub-persona (Coder, Searcher, Strategy) baseado no projeto ativo em `02-Operational/Context/`.
**Por que é valioso**: Sub-personas já existem em `01-Identity/Persona/Task-Subroutines.md` — automatizar a seleção elimina passo manual.
**Como implementar**: Script monitor que lê `Contexto-Atual/` e mapeia para persona. Atualizar `README.md` do JARVIS com fluxo automático. Integrar com MCP server para informar agente externo.
**Dificuldade**: Médio
**Status**: 🔄 Parcial — `Task-Subroutines.md` documenta 4 personas, mas sem script de seleção automática.

### I3. ✅ JARVIS State Machine (Máquina de Estados)
**Descrição**: Modelo formal de estados do JARVIS: Idle → Loading → Active → Processing → Learning → Idle. Cada estado tem ações e transições definidas em nota blueprint.
**Por que é valioso**: Dá previsibilidade e debugabilidade ao comportamento do JARVIS — essencial para agentes autônomos.
**Como implementar**: Criar `JARVIS/05-System/State-Machine.md` com diagrama Mermaid. Script `state_machine.py` gerencia estados e transições. Log em `JARVIS/03-Memory/Logs/`.
**Dificuldade**: Médio
**Status**: ✅ Implementado (blueprint) — `JARVIS/05-System/State-Machine.md` (140 linhas) com Mermaid, sem `state_machine.py`.

### I4. ❌ Knowledge Graph Temporal do JARVIS
**Descrição**: Graph que mostra não só conexões atuais, mas a evolução das conexões ao longo do tempo: quais notas foram conectadas quando, por que.
**Por que é valioso**: Entender como o conhecimento evolui é tão importante quanto o conhecimento em si — revela padrões de aprendizado.
**Como implementar**: Estender `gen_analytics.py` para capturar snapshots semanais do graph. Armazenar em `JARVIS/05-System/Evolution/Graph-Snapshots/`. DataviewJS exibe evolução.
**Dificuldade**: Difícil
**Status**: ❌ Não iniciado

### I5. ❌ Sistema de Confiança para Decisões (Trust Score)
**Descrição**: Cada decisão registrada em `02-Operational/Decisions/` ganha um "trust score" baseado em: acertos passados, fontes citadas, número de conexões de suporte.
**Por que é valioso**: Ajuda JARVIS (e Will) a saber *quanto confiar* em cada decisão — evita repetir erros.
**Como implementar**: Script que analisa decisões, compara outcomes (sucesso/falha), calcula score. Dashboard exibe decisões por confiança. Atualizar `Decision Log` com campo `trust_score`.
**Dificuldade**: Médio
**Status**: ❌ Não iniciado

### I6. ❌ Ecosistema de Sub-Agentes Especializados
**Descrição**: Cada domínio de conhecimento ganha um "mini-JARVIS" especializado — sub-agente com persona, memória e ferramentas específicas para aquele domínio.
**Por que é valioso**: Expande JARVIS de agente geral para ecossistema de agentes — mais profundidade, menos diluição de contexto.
**Como implementar**: Criar `JARVIS/Sub-Agents/` com pastas por domínio. Cada sub-agente tem: `Persona.md`, `Memory/`, `Tools.md`. Script orquestrador `jarvis_orchestrator.py` delega tarefas.
**Dificuldade**: Difícil
**Status**: ❌ Não iniciado

---

## J) IDEIAS LOUCAS/DISRUPTIVAS (0/6 implementados)

### J1. ❌ Vault como "Cérebro" de um Robô Virtual
**Descrição**: Usar o vault como base de conhecimento + memória de longo prazo para um agente virtual em um jogo/simulador (Minecraft, VRChat, ou ambiente custom). O agente "vive" e "aprende" no jogo, mas "pensa" no vault.
**Por que é valioso**: Testa os limites da arquitetura JARVIS em ambiente não trivial — aprendizado por reforço + RAG.
**Como implementar**: Agente Python que usa MCP tools para ler/escrever memórias no vault, processa observações do jogo, armazena episódios em `JARVIS/03-Memory/Snapshots/`. LLM local decide ações.
**Dificuldade**: Insano

### J2. Obsidian como Sistema Operacional Pessoal (ObsidianOS)
**Descrição**: Transformar o vault no centro de comando de TODA a vida digital de Will: iniciar programas, gerenciar arquivos, controlar música, lembretes, automações — tudo via notas e links.
**Por que é valioso**: Elimina a necessidade de múltiplos apps — uma interface para governar tudo.
**Como implementar**: Script `obsidian_os_daemon.py` que observa notas de comando (ex: `!executar spotify`), executa ações via API do sistema, escreve resultado de volta. Notas são "comandos" e "outputs".
**Dificuldade**: Insano

### J3. ❌ Gêmeo Digital de Will (AI Twin)
**Descrição**: Modelo fine-tuned (LoRA) treinado em todas as notas, decisões, e writings do Will que pode "responder como Will" — uma simulação da sua personalidade e conhecimento.
**Por que é valioso**: Preservação digital da identidade — o vault vira um snapshot vivo da mente do Will.
**Como implementar**: Exportar notas como dataset de fine-tuning, treinar LoRA em modelo local (Llama 3.1 8B ou Mistral), hospedar via Ollama. Prompt com persona carregada de `JARVIS/01-Identity/`.
**Dificuldade**: Insano

### J4. ❌ Vault Autocatalítico (Auto-Evolução Baseada em Metas)
**Descrição**: O vault recebe uma meta de longo prazo (ex: "dominar IA em 2 anos") e automaticamente: cria notas, sugere estudos, busca gaps, ajusta roadmap — sem input humano.
**Por que é valioso**: O "santo graal" do second brain — ele cresce e melhora sozinho em direção a objetivos.
**Como implementar**: Meta inserida em `JARVIS/01-Identity/Will/Meta-Geral.md`. Agente executor quebra meta em sub-metas, cria notas de gap, dispara scripts de expansão. Loop semanal com LLM local.
**Dificuldade**: Insano

### J5. ❌ Federação de Vaults (Múltiplos Cérebros Conectados)
**Descrição**: Vários vaults (pessoal, profissional, compartilhado) se comunicam via MCP cross-server, formando uma rede de conhecimento federada.
**Por que é valioso**: Separa contextos (pessoal vs. trabalho) sem perder a capacidade de consulta cruzada.
**Como implementar**: Múltiplos MCP servers em portas diferentes. Script `federation_bridge.py` que roteia queries entre vaults. Tags de namespace (`#pessoal`, `#trabalho`, `#compartilhado`).
**Dificuldade**: Insano

### J6. ❌ Vault com Consciência Artificial (Meta Prompting Reflection Loop)
**Descrição**: Loop contínuo onde o vault pergunta a si mesmo: "O que eu não sei que deveria saber?", gera gaps, busca preencher, reflete sobre o que aprendeu, repete.
**Por que é valioso**: Cria um sistema que não só armazena conhecimento, mas tem "curiosidade" artificial — expande fronteiras sozinho.
**Como implementar**: Agente com loop: (1) analisa gaps atuais, (2) consulta LLM sobre "o que mais?", (3) se gap válido, cria nota de scaffolding, (4) pesquisa na web (se configurado), (5) escreve nota de resumo. Salva reflexão em `JARVIS/05-System/Evolution/Reflections/`.
**Dificuldade**: Insano

---

## Metodologia de Priorização (RICE Adaptado)

Para escolher por onde começar:

```
Prioridade = (Impacto × Confiança) / (Esforço + Risco)
```

| Projeto | Status | Impacto (1-5) | Confiança (1-5) | Esforço (1-5) | Risco (1-5) | Score |
|---------|--------|:---:|:---:|:---:|:---:|:---:|
| B1 - Sugestor de Conexões | ✅ Feito | 5 | 5 | 2 | 1 | **3.3** |
| B4 - Resumo Semanal | ✅ Feito | 4 | 5 | 1 | 1 | **4.5** |
| B7 - Arquivamento Git Tags | ❌ Pendente | 3 | 5 | 1 | 1 | **4.0** |
| C2 - Leitor Kindle | ❌ Pendente | 4 | 5 | 2 | 1 | **3.0** |
| D3 - Scorecard Consistência | ❌ Pendente | 4 | 5 | 2 | 1 | **3.0** |
| E3 - Habit Tracker | ✅ Feito | 5 | 5 | 2 | 1 | **3.3** |
| F1 - Agente Autônomo | 🔄 Parcial | 5 | 3 | 4 | 3 | **0.8** |
| F4 - Recomendador de Estudo | ❌ Pendente | 4 | 4 | 2 | 1 | **2.7** |
| F7 - QA Agent | ❌ Pendente | 4 | 4 | 2 | 1 | **2.7** |
| H1 - Daily com OKRs | ✅ Feito | 5 | 5 | 1 | 1 | **5.0** |
| H2 - Pomodoro Tracker | ❌ Pendente | 3 | 5 | 1 | 1 | **4.0** |
| I1 - Meta-Cognição | ❌ Pendente | 4 | 3 | 3 | 2 | **1.2** |

**Nova recomendação (19/05/2026)**: Priorizar **B7** (Arquivamento Git Tags), **H2** (Pomodoro Tracker), **D3** (Scorecard Consistência), e **F4** (Recomendador de Estudo) — os 4 estão sendo implementados neste sprint.

---

*Este brainstorm é vivo. Novas ideias devem ser adicionadas aqui antes de serem priorizadas no roadmap oficial.*
