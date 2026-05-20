---
title: "Minimizacao de Dados para RAG e Agentes"
area: "Conhecimento-Geral/Etica"
tags: ["ethics","privacy","rag","agents","data-minimization"]
created: "2026-05-08"
status: "draft"
---

# Minimizacao de Dados para RAG e Agentes

Minimizacao de dados e a pratica de reduzir (1) o que entra, (2) o que fica armazenado, (3) o que e indexado e (4) o que e compartilhado entre agentes.

## Onde o risco cresce (pontos de vazamento)

- Coleta: prompts pedindo contexto demais.
- Persistencia: salvar "artefatos" completos (logs, dumps, screenshots, transcricoes).
- Indexacao: embedar e tornar recuperavel conteudo que deveria ser efemero.
- Distribuicao: multiplos agentes lendo a mesma base sem necessidade.

## Regras simples (boa padronizacao)

1. Use allowlist de pastas para indexacao.
2. Separe "memoria episodica" (efemera) de "memoria semantica" (canonica).
3. Redija PII antes de persistir.
4. Registre apenas agregados quando possivel (contagens, erros, hashes, ids internos).
5. Prefira referencias: em vez de copiar conteudo, aponte para o local original.

## Nivel de detalhe (escolha conscientemente)

Pergunta: "O que eu preciso recuperar depois para agir com seguranca?"

- Para debug: padrao e guardar sinais (mensagem, stack, versoes, passos), nao dumps completos.
- Para operacao: padrao e guardar indicadores (SLO, taxa de erro), nao payloads integrais.
- Para aprendizado: padrao e guardar o "porque" e o "como reproduzir", nao o conteudo do usuario.

## Checklist (antes de indexar uma pasta)

- Ha dados pessoais, de clientes ou terceiros?
- Ha segredos (tokens, chaves, cookies, credenciais)?
- Existe justificativa para recuperacao futura?
- Consigo indexar um resumo seguro em vez do material bruto?
- Quem (quais agentes) tera acesso a esse indice?

## Relacionado

- [[Privacidade-by-Default-para-Agentes]]
- [[Auditoria-de-Agentes-e-Evidencias]]
- [[Politica-de-Logs-para-Agentes]]


[[Conhecimento-Geral/Etica/INDEX|← Voltar ao índice de Ética]]
