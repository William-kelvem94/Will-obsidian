---
title: "PROJECT_JARVIS_5.0 Knowledge Base"
description: "Pasta de base de conhecimento do Jarvis para armazenar tudo que o assistente precisa saber." 
tags:
  - jarvis
  - knowledge
  - base
  - assistant
---

# PROJECT_JARVIS_5.0 Knowledge Base

Esta pasta é a base de conhecimento dedicada do Jarvis. Ela contém cópias dos principais documentos e da estratégia que o assistente precisa ter como sua "consciência".

## Objetivo
- Manter um conjunto separado de notas que representam o conhecimento e a persona do Jarvis.
- Permitir que a inteligência acesse uma versão consolidada do que já foi definido sobre o projeto.
- Preservar a organização original de projetos em `Projetos/Privados/PROJECT_JARVIS_5.0.md` e `Projetos/EstudosFocados/PROJECT_JARVIS_5.0.md`.

## Arquivos desta pasta
- `PROJECT_JARVIS_5.0.md` — visão geral e execução do projeto.
- `PROJECT_JARVIS_5.0-Knowledge.md` — base de conhecimento completa.
- `PROJECT_JARVIS_5.0-Personality.md` — persona, tom e estilo do Jarvis.
- `PROJECT_JARVIS_5.0-Architecture.md` — arquitetura proposta do assistente.
- `PROJECT_JARVIS_5.0-Strategy.md` — estratégia duplicada do Estudo Focados para a consciência.

## Como usar
- Considere esta pasta como a "mente" do Jarvis.
- Use os arquivos daqui para alimentar modelos, fazer RAG ou montar o contexto do assistente.
- Mantenha a pasta sincronizada com as versões originais se algo mudar.

## Caminhos e configuração
- Base de conhecimento do Jarvis:
  `D:\OBSIDIAN\Will\Projetos\Privados\PROJECT_JARVIS_5.0-KnowledgeBase`
- Vault raiz de organização:
  `D:\OBSIDIAN\Will`

### Instruções de configuração
Se o Jarvis suportar variáveis de ambiente ou `.env`, configure:
```powershell
$env:JARVIS_KB_PATH = 'D:\OBSIDIAN\Will\Projetos\Privados\PROJECT_JARVIS_5.0-KnowledgeBase'
$env:JARVIS_VAULT_ROOT = 'D:\OBSIDIAN\Will'
```

### Comando sugerido para Jarvis
- variável: `JARVIS_KB_PATH`
- valor: `D:\OBSIDIAN\Will\Projetos\Privados\PROJECT_JARVIS_5.0-KnowledgeBase`

### Estrutura interna
Esta pasta deve conter:
- `PROJECT_JARVIS_5.0.md`
- `PROJECT_JARVIS_5.0-Knowledge.md`
- `PROJECT_JARVIS_5.0-Personality.md`
- `PROJECT_JARVIS_5.0-Architecture.md`
- `PROJECT_JARVIS_5.0-Strategy.md`
- `CONFIG.md`

## Expansão contínua
- Sempre que Jarvis aprender algo novo, crie uma nova nota aqui.
- Use nomes consistentes: `PROJECT_JARVIS_5.0-<Tema>.md`.
- Esta pasta é a consciência dele. O código fica em `Projetos/Privados/PROJECT_JARVIS_5.0.md`.
