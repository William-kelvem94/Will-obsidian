---
title: "Segurança e Governança Local-First no Vault"
description: "Práticas para proteger segredos, logs, RAG, agentes e automações mantendo o vault local como fonte de verdade."
tags: [seguranca, governanca, local-first, privacidade, jarvis, vault, jarvis-engenharia]
date: 2026-05-20
updated: 2026-06-08
---

# Segurança e Governança Local-First

Esta nota consolida práticas de proteção para o JARVIS e o vault. Ela complementa [[Segurança, Privacidade & RAG Compliance]], [[Privacidade-by-Default-para-Agentes]] e [[Minimizacao-de-Dados-para-RAG-e-Agentes]].

## Princípios

1. **Local como fonte de verdade:** conhecimento pessoal, logs e dados sensíveis ficam sob controle local.
2. **Menor privilégio:** cada agente ou script acessa apenas o necessário.
3. **Escrita auditável:** alterações relevantes passam por diff, validação e Git.
4. **Sensível por padrão:** se há dúvida, trate como privado.
5. **Backup antes de automação destrutiva:** mover, apagar e sobrescrever exigem cuidado extra.

## Segredos e arquivos sensíveis

Nunca versionar:

- `.env` real;
- tokens de API;
- credenciais;
- chaves privadas;
- dumps com dados pessoais;
- logs contendo prompts privados ou respostas completas sensíveis.

Use como apoio:

- `gitleaks.toml` para detecção;
- `sensitive_files.txt` para inventário;
- `.env.example` para documentar variáveis sem segredo;
- frontmatter `sensivel: true` quando a nota exigir restrição.

## RAG e privacidade

Antes de indexar:

- excluir arquivos sensíveis;
- evitar logs/transcrições brutas;
- manter metadados de origem;
- separar notas privadas de notas públicas;
- registrar qual modelo de embedding e versão foram usados.

RAG não deve ser lixeira semântica. Ele deve indexar conhecimento curado.

## Governança de agentes

Agentes devem operar com contrato claro:

- escopo de leitura;
- escopo de escrita;
- arquivos proibidos;
- necessidade de confirmação;
- critérios de validação;
- responsabilidade por commit.

Para múltiplos agentes, veja [[Arquiteturas-Cooperativas-de-Agentes]].

## Logs

Logs são úteis para auditoria, mas podem vazar contexto.

Boas práticas:

- registrar metadados, não conteúdo sensível integral;
- rotacionar logs grandes;
- não usar logs como notas permanentes;
- revisar logs antes de commit;
- separar logs operacionais de conhecimento consolidado.

## Sincronização local/remoto

Antes de push:

- revisar `git status`;
- evitar `git add .` em vaults grandes;
- commitar por grupos coerentes;
- confirmar que deleções são intencionais;
- preservar conteúdo movido em `LEGACY` quando houver reorganização;
- nunca forçar push sem motivo explícito.

## Checklist rápido

- [ ] Nenhum segredo entrou no commit.
- [ ] Arquivos sensíveis estão marcados ou excluídos do RAG.
- [ ] Deleções foram revisadas.
- [ ] Arquivos movidos preservam conteúdo.
- [ ] Notas novas estão linkadas a notas existentes.
- [ ] O commit tem mensagem clara em PT-BR.

## Links relacionados

- [[Ecossistema-e-Protocolos-MCP]]
- [[RAG-Avancado-Playbook]]
- [[Arquiteturas-Cooperativas-de-Agentes]]
- [[Segredos-e-Dados-Sensiveis]]
- [[Politica-de-Logs-para-Agentes]]
