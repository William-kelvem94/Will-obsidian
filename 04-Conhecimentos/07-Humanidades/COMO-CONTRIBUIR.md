---
title: "Manual de Curadoria e Normas Exclusivas — Segundo Cérebro (Will-Obsidian)"
description: "Padrões, convenções lógicas de nomenclatura, guias de frontmatter YAML, curadoria de wikilinks e diretrizes de desenvolvimento cooperativo humano-agente para consolidação do cofre."
tags: [governance, onboarding, contributor-guide, rules, conventions, git, folder-structure]
updated: 2026-06-06
date: 2026-06-01
---

# 🧠 Manual de Curadoria, Normas e Contribuição do Cofre

Este repositório consolidado do **Segundo Cérebro (Will-Obsidian)** atua como uma infraestrutura de conhecimento viva, integradora e gamificada. A consistência sintática e a integridade de referências são essenciais para viabilizar as buscas de semântica vetorial (RAG) pelo orquestrador inteligente **JARVIS** e os scripts de geração analítica locais.

Este guia estabelece os **padrões rígidos e regras de boas práticas** que todo colaborador (seja operador humano, micro-rotina ou agente autônomo com capacidades de escrita) deve seguir rigorosamente para modificação ou inserção de arquivos.

---

## 📂 1. Estrutura Física e Árvore de Organização do Vault

O cofre possui uma arquitetura modular desenhada para manter os domínios funcionais isolados dos arquivos operacionais e relatórios temporários. Nunca injete arquivos de forma avulsa na raiz:

| Diretório Pai | Objetivo e Escopo Lógico | Regra de Organização |
|---|---|---|
| `JARVIS/` | Sistema inteligente e canais sistêmicos de controle. | Dividido nos 5 canais canônicos. |
| [Knowledge-Base/](04-Conhecimentos/Knowledge-Base/) | Hubs técnicos condensados (KBs) de mercado. | Cada hub técnico possui sua pasta de recortes, glossários e projetos. |
| [skills/](05-Skills/) | Inventário vivo de competências e trilhas curriculares. | Organizado por prefixado numérico (`01-...`, `02-...`). |
| [Conhecimento-Geral/](04-Conhecimentos/07-Humanidades/) | Ramos transdisciplinares das Humanidades e Ciências. | Dividido em 20 subpastas estanques temáticas. |
| `dashboards/` | Painéis e visualizadores dinâmicos DataviewJS. | Somente consultas estruturadas de metadados do cofre. |
| `.logs/` | Armazenamento privado de patches de tags e auditorias. | Pasta oculta para dados pesados e históricos. |

---

## 📝 2. Diretrizes Estruturais de Nota Markdown

Cada nota injetada ou modificada na base deve obedecer a regras estritas de cabeçalho YAML e encadeamento lógico:

### 2.1 Padrão Mandatório de Frontmatter YAML
A nota deve iniciar obrigatoriamente na linha 1 com delimitadores de três traços `---`. O YAML deve ser saneado, contendo strings protegidas por aspas e formato de listas nativas (`[item_A, item_B]`):

```yaml
---
title: "Título de Alta Densidade Semântica (Usar Aspas)"
description: "Breve síntese explicativa do conteúdo do arquivo em 1 ou 2 sentenças puras."
tags: [conhecimento, subcategoria_especifica, area_tema]
date: 2026-06-06
updated: 2026-06-06
category: base-conhecimento
aliases: ["Título Sinonimizador", "Conceito Alternativo"]
related: ["04-Conhecimentos/07-Humanidades/SubPasta/Nota-Correlata-1", "05-Skills/02-software-engineering/Nota-Correlata-2"]
---
```

### 2.2 Requisitos Mandatórios dos Cabeçalhos Lógicos
1.  **Título Principal Único (`#`)**: Exatamente um único cabeçalho de nível H1 no topo do arquivo Markdown, alinhado com a propriedade `title` de metadados.
2.  **Organização Sequencial de Títulos**: Títulos secundários devem seguir decrescimento semântico estrito. Não utilize cabeçalhos H3 direto abaixo de H1.
3.  **Encadeamento de Links Cruzados (MOCs e Relacionados)**: O encerramento do arquivo deve portar uma seção unificada apontando para as notas lógicas correlatas, garantindo conectividade alta do Grafo de Conexões do Obsidian.

---

## 🔗 3. Convenções de Links e Nomenclatura Estrita

*   **Wikilinks Sem URI Schemes**: Use exclusivamente wikilinks nativos do Obsidian `[[Caminho/Para/Arquivo]]` ou `[[Caminho/Para/Arquivo|Texto Explicativo]]`. Nunca insira prefixos URI locais como `file:///` ou esquemas relativos `./` dentro de links wiki.
*   **Wikilinks com Caminho Completo**: De preferência, especifique o caminho completo a partir da raiz do cofre para evitar erros de desambiguação sintática no Obsidian (ex: `[[04-Conhecimentos/07-Humanidades/Logica/INDEX]]`).
*   **Caixa de Linkage POSIX**: Sempre utilize barras do tipo Unix `/` nos links e caminhos. Nomes de arquivos e pastas criados fisicamente não devem conter caracteres acentuados especiais ou espaços vazios (substitua por hífen `-`).

---

## 🤖 4. Protocolo Exclusivo de Co-Design Humano-Agente

Para viabilizar a edição concorrente por seres humanos no desktop e robôs executores no terminal de desenvolvimento sem perda de dados, o seguinte portão lógico de commits deve ser observado:

```
                  ┌──────────────────────────────────────────────┐
                  │ 1. INSPECT: Agente puxa alterações do Git    │
                  └──────────────────────┬───────────────────────┘
                                         ▼
                  ┌──────────────────────────────────────────────┐
                  │ 2. BUILD: Edição cirúrgica sob Sandbox local  │
                  └──────────────────────┬───────────────────────┘
                                         ▼
                  ┌──────────────────────────────────────────────┐
                  │ 3. VERIFY: Executar scripts de higienização  │
                  └──────────────────────┬───────────────────────┘
                                         ▼
                  ┌──────────────────────────────────────────────┐
                  │ 4. EMIT: Commit assinado por Agente no Git   │
                  └──────────────────────────────────────────────┘
```

1.  **Executar o Validador de Metadados**: Apos criar ou alterar qualquer arquivo Markdown de nota de conhecimento geral ou técnico, execute a rotina de saneamento para atualizar o ranking gamificado de XP do Segundo Cérebro:
    ```powershell
    python .scripts/vault_cleanup.py
    ```
2.  **Alimentação do Baralho Anki**: Garanta que as novas definições criadas contenham clareza de frases para evitar quebras de delimitadores no exportador:
    ```powershell
    python scripts/generate_flashcards.py
    ```
3.  **Auditar Saúde física de Projetos**: Varra as referências lógicas contra quebras funcionais no mapa de dependências através do comando:
    ```powershell
    python .scripts/project_health_checker.py
    ```
4.  **Assinatura de commits Git**: Os commits de git gerados automaticamente por rotinas de agentes inteligentes devem portar descrições claras constando o escopo analisado e as tags correspondentes.

