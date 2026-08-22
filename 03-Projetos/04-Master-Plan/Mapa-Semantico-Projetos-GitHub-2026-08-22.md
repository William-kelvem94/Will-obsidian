---
title: Mapa semântico dos projetos estratégicos do GitHub
type: mapa-projetos-github
status: atual
updated: 2026-08-22
classe_privacidade: operacional
indexavel: true
uso_ia: permitido
fonte_canonica: https://github.com/William-kelvem94
---

# Mapa semântico dos projetos estratégicos

Este mapa separa evidência documental de interpretação. A evidência vem dos READMEs coletados; a relação com o segundo cérebro é uma classificação operacional para navegação e não substitui auditoria do código.

## 1. [[DEEP-LEARNING]]

- **Repositório:** [DEEP-LEARNING](https://github.com/William-kelvem94/DEEP-LEARNING)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** projeto técnico relacionado
- **Evidências de estrutura/objetivo no README:**
  - # Deep Learning Project - Sumário
  - ## Projeto
  - ## Funcionalidades Principais
  - ## Requisitos
  - ## Instalação
  - # Criar ambiente virtual
  - # Instalar dependências
  - # Configurar variáveis de ambiente
  - # Preencher .env com as credenciais necessárias
  - # Executar o projeto
  - ## Dependências
  - ## Exemplos de Uso
  - # Exemplo de treinamento de modelo
  - # Exemplo de predição
  - ## Contribuindo
  - ## Licença
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 2. [[DeepSeek-V3---C-PIA]]

- **Repositório:** [DeepSeek-V3---C-PIA](https://github.com/William-kelvem94/DeepSeek-V3---C-PIA)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** linha de IA, agentes, modelos ou ferramentas
- **Evidências de estrutura/objetivo no README:**
  - ## Table of Contents
  - ## 1. Introduction
  - ## 2. Model Summary
  - **Architecture: Innovative Load Balancing Strategy and Training Objective**
  - - On top of the efficient architecture of DeepSeek-V2, we pioneer an auxiliary-loss-free strategy for load balancing, which minimizes the performance degradation that arises from encouraging load balancing.
  - -  We investigate a Multi-Token Prediction (MTP) objective and prove it beneficial to model performance. 
  - **Pre-Training: Towards Ultimate Training Efficiency**
  - - We design an FP8 mixed precision training framework and, for the first time, validate the feasibility and effectiveness of FP8 training on an extremely large-scale model.  
  - - Through co-design of algorithms, frameworks, and hardware, we overcome the communication bottleneck in cross-node MoE training, nearly achieving full computation-communication overlap.  
  - - At an economical cost of only 2.664M H800 GPU hours, we complete the pre-training of DeepSeek-V3 on 14.8T tokens, producing the currently strongest open-source base model. The subsequent training stages after pre-training require only 0.1M GPU hours.
  - **Post-Training: Knowledge Distillation from DeepSeek-R1**
  - -   We introduce an innovative methodology to distill reasoning capabilities from the long-Chain-of-Thought (CoT) model, specifically from one of the DeepSeek R1 series models, into standard LLMs, particularly DeepSeek-V3. Our pipeline elegantly incorporates the verification and reflection patterns of R1 into DeepSeek-V3 and notably improves its reasoning performance. Meanwhile, we also maintain a control over the output style and length of DeepSeek-V3.
  - ## 3. Model Downloads
  - ## 4. Evaluation Results
  - ### Base Model
  - ### Chat Model
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 3. [[Domni]]

- **Repositório:** [Domni](https://github.com/William-kelvem94/Domni)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** linha de produtos e sistemas de gestão
- **Evidências de estrutura/objetivo no README:**
  - # Domni
  - ## Visao Geral
  - - isolamento multi-tenant por `saasTenantId`
  - - autenticao baseada em NextAuth
  - - regras de negocio desacopladas em `src/lib/services`
  - - portal publico do inquilino em `/portal`
  - - suporte a IA, OCR, notificacoes e integracoes externas
  - - deploy web em Vercel e banco em Supabase/PostgreSQL
  - ## Status Do Projeto
  - ## O Que O Sistema Entrega
  - ### Operacao imobiliaria
  - - cadastro e gestao de imoveis
  - - cadastro e fluxo de inquilinos
  - - contratos com editor colaborativo e historico
  - - pagamentos e historico financeiro
  - - manutencao com anexos, comentarios e status
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 4. [[Empresa-de-Agentes]]

- **Repositório:** [Empresa-de-Agentes](https://github.com/William-kelvem94/Empresa-de-Agentes)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** linha de IA, agentes, modelos ou ferramentas
- **Evidências de estrutura/objetivo no README:**
  - # Empresa Local de Agentes
  - ## Navegue pelo Projeto
  - - [Visão Geral do Projeto](./visao_geral.md) — descrição, conceitos, ideias e planos completos.
  - - [Cultura Organizacional](./cultura.md) — valores, práticas, inclusão, feedback e inovação.
  - - [Estrutura Organizacional](./estrutura.md) — áreas, funções e composição da empresa.
  - - [Agentes (pessoas/cargos)](./agentes/) — documentação de cada papel, responsabilidades e interfaces.
  - - [Fluxos e Processos](./fluxos/) — passo a passo e detalhamento operacional.
  - - [Templates](./templates/) — modelos para criação de novos agentes, projetos e processos.
  - ## Exemplo Resumido do Novo Padrão de Agente
  - # Nome do Papel
  - ## Objetivo do Cargo
  - ## Atribuições Principais
  - - Item 1
  - - Item 2
  - ## Requisitos Desejáveis
  - - Técnico: ex: Python, Excel, etc.
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 5. [[Gerenciador_Financeiro-7.0]]

- **Repositório:** [Gerenciador_Financeiro-7.0](https://github.com/William-kelvem94/Gerenciador_Financeiro-7.0)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** linha de IA, agentes, modelos ou ferramentas
- **Evidências de estrutura/objetivo no README:**
  - # Numni
  - **Numni** é uma plataforma de gestão financeira multiworkspace para uso pessoal e em equipe. O projeto reúne contas, transações, categorias, orçamentos, metas, investimentos, dívidas, documentos, relatórios, calendário, notificações, equipe, backups e um assistente financeiro com IA.
  - ## Visão rápida
  - - isolamento por workspace (`saasTenantId`) e papéis de equipe;
  - - contas, cofrinhos, transações, categorias, orçamentos, metas, investimentos e dívidas;
  - - dashboard, relatórios, calendário, pesquisa e exportações;
  - - documentos privados com Supabase Storage;
  - - PWA responsiva, estados offline honestos e sistema visual compartilhado;
  - - autenticação NextAuth, primeiro acesso obrigatório quando necessário e revogação de sessões;
  - - assistente financeiro com Gemini, confirmação antes de mutações financeiras e análise de até 30 anexos;
  - - parsers locais para formatos financeiros estruturados, PDF text-first, cache de análises e retrieval lexical para reduzir consumo de IA;
  - - proteção global da cota de IA com no máximo duas chamadas reais simultâneas ao provedor e cooldown compartilhado;
  - - backup lógico criptografado no Supabase Storage com cópia preventiva antes de restaurações;
  - - observabilidade opcional compatível com Sentry/GlitchTip, logging estruturado e health checks.
  - ## Stack principal
  - - Next.js 16 + React 19 + TypeScript
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 6. [[IA_LOCAL_S_ULTRA]]

- **Repositório:** [IA_LOCAL_S_ULTRA](https://github.com/William-kelvem94/IA_LOCAL_S_ULTRA)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** linha de IA, agentes, modelos ou ferramentas
- **Evidências de estrutura/objetivo no README:**
  - # IA LOCAL S ULTRA — JARVIS Mobile
  - ## Estado atual — 0.3.0
  - ### Cérebro local
  - - `Qwen3 4B Q4_K_M` em GGUF, aproximadamente 2,5 GB;
  - - `llama.cpp` Android embarcado e fixado em commit conhecido;
  - - inferência local em `arm64-v8a`;
  - - streaming token a token;
  - - modelo baixado apenas quando ainda não existe uma cópia privada validada;
  - - download retomável por HTTP Range após interrupções;
  - - SHA-256 obrigatório antes de o GGUF ser aceito pelo motor;
  - - arquivo parcial mantido para retomada e removido quando a integridade falha;
  - - sem API de LLM em nuvem.
  - ### Agent Core
  - ### Memória, tarefas e presença
  - - histórico de conversa em SQLite;
  - - banco operacional separado `jarvis_mobile.db` com WAL;
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 7. [[IA-LOCAL]]

- **Repositório:** [IA-LOCAL](https://github.com/William-kelvem94/IA-LOCAL)
- **Estado documental:** README não acessível neste lote
- **Papel no segundo cérebro:** linha de IA, agentes, modelos ou ferramentas
- **Evidências de estrutura/objetivo no README:**
  - Nenhuma seção estruturada recuperada.
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 8. [[openclaude-wk]]

- **Repositório:** [openclaude-wk](https://github.com/William-kelvem94/openclaude-wk)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** linha de IA, agentes, modelos ou ferramentas
- **Evidências de estrutura/objetivo no README:**
  - # OpenClaude
  - ## Sponsors
  - ## Star History
  - ## Why OpenClaude
  - - Use one CLI across cloud APIs and local model backends
  - - Save provider profiles inside the app with `/provider`
  - - Run with OpenAI-compatible services, Gemini, GitHub Models, Codex OAuth, Codex, Ollama, Atomic Chat, and other supported providers
  - - Keep coding-agent workflows in one place: bash, file tools, grep, glob, agents, tasks, MCP, and web tools
  - - Use the bundled VS Code extension for launch integration and theme support
  - ## Quick Start
  - ### Install
  - **Verify / troubleshoot installed version:**
  - ### Start
  - - run `/provider` for guided provider setup and saved profiles
  - - run `/onboard-github` for GitHub Models onboarding
  - ### Resume or fork a conversation
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 9. [[Openclaw_Docker_Will]]

- **Repositório:** [Openclaw_Docker_Will](https://github.com/William-kelvem94/Openclaw_Docker_Will)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** projeto técnico relacionado
- **Evidências de estrutura/objetivo no README:**
  - # OpenClaw
  - ## Render (Docker)
  - ## Local (WSL + Ollama + GPU)
  - ## Scripts
  - - `scripts/install_openclaw.sh` — fallback manual
  - - `scripts/setup_wsl.sh` — setup completo WSL + Ollama + OpenClaw
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 10. [[pixel-agents]]

- **Repositório:** [pixel-agents](https://github.com/William-kelvem94/pixel-agents)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** linha de IA, agentes, modelos ou ferramentas
- **Evidências de estrutura/objetivo no README:**
  - ## Features
  - - **One agent, one character** — every Claude Code terminal gets its own animated character
  - - **Live activity tracking** — characters animate based on what the agent is actually doing (writing, reading, running commands)
  - - **Office layout editor** — design your office with floors, walls, and furniture using a built-in editor
  - - **Speech bubbles** — visual indicators when an agent is waiting for input or needs permission
  - - **Sound notifications** — optional chime when an agent finishes its turn
  - - **Sub-agent visualization** — Task tool sub-agents spawn as separate characters linked to their parent
  - - **Persistent layouts** — your office design is saved and shared across VS Code windows
  - - **External asset directories** — load custom or third-party furniture packs from any folder on your machine
  - - **Diverse characters** — 6 diverse characters. These are based on the amazing work of [JIK-A-4, Metro City](https://jik-a-4.itch.io/metrocity-free-topdown-character-pack).
  - ## Requirements
  - - VS Code 1.105.0 or later
  - - [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) installed and configured
  - - **Platform**: Windows, Linux, and macOS are supported
  - ## Getting Started
  - ### Install from source
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 11. [[PROJECT_JARVIS]]

- **Repositório:** [PROJECT_JARVIS](https://github.com/William-kelvem94/PROJECT_JARVIS)
- **Estado documental:** README não acessível neste lote
- **Papel no segundo cérebro:** linha de IA, agentes, modelos ou ferramentas
- **Evidências de estrutura/objetivo no README:**
  - Nenhuma seção estruturada recuperada.
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 12. [[PROJECT_JARVIS_5.0]]

- **Repositório:** [PROJECT_JARVIS_5.0](https://github.com/William-kelvem94/PROJECT_JARVIS_5.0)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** linha de IA, agentes, modelos ou ferramentas
- **Evidências de estrutura/objetivo no README:**
  - # JARVIS 5.0 — consciência operacional local
  - ## O que existe agora
  - - Serviço de presença independente do microfone, com ícone opcional na bandeja.
  - - SQLite em modo WAL como fonte de eventos, sessões, memórias, tarefas, feedback, decisões e auditoria de ferramentas.
  - - Recuperação de sessões interrompidas e trava contra duas instâncias da presença.
  - - Aplicativo em primeiro plano, tempo ocioso, RAM, CPU e disco; títulos e pastas ficam desligados por padrão.
  - - Modo privado, pausa, lista de aplicativos privados, retenção e horário silencioso.
  - - Memória de trabalho, episódica, semântica, procedural e prospectiva, com FTS5, deduplicação, fonte, confiança, correção e exclusão.
  - - Modelo do mundo com atividade, projeto, objetivo, pendências, agenda, e-mails de ação e recursos do computador.
  - - Iniciativas explicáveis para compromisso próximo, lembrete com prazo, recurso crítico, retorno ao computador, foco longo, fechamento do dia e rotinas confirmadas por pelo menos quatro semanas equivalentes.
  - - Planner imediato de até cinco ações e fila Operator de até 100 etapas configuráveis, com checkpoint, retomada, risco, confirmação e verificação do resultado.
  - - Pesquisa HTTPS pública com fontes, cache e bloqueio de redes locais/SSRF; conteúdo externo nunca autoriza ferramentas.
  - - Catálogo padrão mais allowlist editável de qualquer `.exe` local; Microsoft UI Automation usa seletor exato e clique, alternância ou preenchimento não sensível exigem confirmação e verificação do Windows.
  - - Escuta persistente opcional por wake word, captura única de tela e câmera sob permissão; áudio bruto e imagens não são persistidos.
  - - TTS interrompível, personalidade estável e adaptação apenas por correções explícitas.
  - - Central de três agendas, Gmail, notícias, clima e Morning Digest integrada à GUI e à presença.
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 13. [[search_works]]

- **Repositório:** [search_works](https://github.com/William-kelvem94/search_works)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** linha de pesquisa e recuperação
- **Evidências de estrutura/objetivo no README:**
  - # JobSeeker Bot & Dashboard
  - ## 🚀 Funcionalidades Core
  - ## 📁 Estrutura do Workspace
  - ## 🔧 Configuração e Variáveis de Ambiente (`.env`)
  - * **`AI_PROVIDER`:** Escolha entre `local` (LM Studio/Ollama), `gemini` (Google Cloud) ou `openai`.
  - * **`AI_API_URL`:** URL do endpoint da IA (Ex: `http://localhost:1234/v1` para LM Studio).
  - * **`AI_API_KEY`:** Chave de API se usar Gemini ou OpenAI.
  - * **`AI_MODEL`:** Nome do modelo de IA (Ex: `meta-llama-3-8b-instruct`).
  - * **`SEARCH_KEYWORDS`:** Palavras-chave separadas por vírgula (Ex: *Engenheiro de Computação, Analista de Sistemas*).
  - * **`DAILY_AUTO_APPLY_LIMIT`:** Quantidade máxima de inscrições automáticas diárias (Ex: *5*).
  - * **`PDF_RESUME_PATH`:** Caminho absoluto do seu currículo em PDF.
  - ## 💻 Como Rodar o Projeto
  - ### Abordagem 1: Execução Local (Recomendada para primeira execução/login)
  - ### Abordagem 2: Execução via Docker (Excelente para rodar em segundo plano)
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 14. [[STUDY_LLMS]]

- **Repositório:** [STUDY_LLMS](https://github.com/William-kelvem94/STUDY_LLMS)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** linha de IA, agentes, modelos ou ferramentas
- **Evidências de estrutura/objetivo no README:**
  - # 🧠 STUDY_LLMS (Projeto WILL-JARVIS)
  - ## 🎯 Objetivo
  - ## 📂 Arquitetura do Laboratório
  - *   **`01_Datasets/`**: Recebe os arquivos `.jsonl` com centenas de amostras criadas (Knowledge Distillation) que ensinam a IA a responder profissionalmente e estruturar raciocínios Chain-of-Thought (CoT).
  - *   **`02_Training/`**: O reator do projeto. Contém as instruções de engenharia restritas, injetando o otimizador *Paged_AdamW_8Bit* para acoplar treinamentos complexos fisicamente dentro de placas de vídeo limitadas (VRAM WDDM Bypass).
  - ## 🗃️ Arquivos de Documentação
  - ## ⚙️ Uso
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 15. [[Will-obsidian]]

- **Repositório:** [Will-obsidian](https://github.com/William-kelvem94/Will-obsidian)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** fonte canônica de governança e conhecimento do vault
- **Evidências de estrutura/objetivo no README:**
  - # Will Vault - Obsidian Neural Hub
  - - [[Bem-vindo|Neural Hub]]
  - - [[INDEX|INDEX global]]
  - - [[01-Hubs/README|Hubs Centrais do Vault]]
  - - [[10-Interfaces/Painel-Cockpit-Operacional|Painel Cockpit Operacional]]
  - - [[07-Operacoes-do-Vault/README|Operacoes do Vault]]
  - - [[03-Projetos/04-Master-Plan/Mapa-Cognitivo-Completo-dos-Repositorios|Mapa Cognitivo Completo dos Repositórios]]
  - ## Estrutura fisica canonica
  - ## Papel de cada area
  - ## Sistema tecnico
  - - `11-Dados-Brutos/` para evidencia e fontes;
  - - `04-Conhecimentos/` para sintese e conhecimento curado;
  - - `09-Sistema/schema/` para regras, contratos e governanca;
  - - `09-Sistema/agents/` para instrucoes operacionais de modelos e agentes;
  - - `09-Sistema/scripts/` e `.scripts/` para automacoes e suporte tecnico.
  - ## Governanca e migracao
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## 16. [[Will.Nexus]]

- **Repositório:** [Will.Nexus](https://github.com/William-kelvem94/Will.Nexus)
- **Estado documental:** README acessível e usado como evidência
- **Papel no segundo cérebro:** linha de produtos e sistemas de gestão
- **Evidências de estrutura/objetivo no README:**
  - # WillNexus
  - **Software Portfolio Intelligence para mapear, entender e evoluir todo o ecossistema de projetos Kelvem.**
  - ## v0.3 — Command Center
  - - visão geral do portfólio;
  - - inventário de repositórios;
  - - saúde/maturidade dos projetos;
  - - Capability Graph;
  - - ranking de capacidades;
  - - sobreposições e reutilização;
  - - oportunidades iniciais;
  - - histórico de censos;
  - - central de ações;
  - - execução em Windows, WSL2, Docker e Vercel;
  - - Supabase como memória persistente;
  - - GitHub estritamente read-only nesta fase.
  - ## Arquitetura
- **Próxima análise recomendada:** árvore completa, manifestos, arquitetura, riscos, estado de execução, dependências e vínculo com outros repositórios.

## Relações estratégicas iniciais

- **Will-obsidian** documenta, organiza e governa os demais projetos.
- **PROJECT_JARVIS_5.0**, **IA_LOCAL_S_ULTRA**, **Empresa-de-Agentes**, **openclaude-wk**, **Openclaw_Docker_Will**, **STUDY_LLMS** e **DeepSeek-V3---C-PIA** formam o eixo de IA/agentes/modelos.
- **Domni**, **Gerenciador_Financeiro-7.0** e **Will.Nexus** formam o eixo de aplicações e gestão.
- **search_works** representa pesquisa/recuperação e pode alimentar o eixo de conhecimento.
- As relações acima são organizacionais; dependências reais entre repositórios ainda precisam ser confirmadas por manifestos e imports.
