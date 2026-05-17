---
title: "Privacidade by Default para Agentes"
area: "Conhecimento-Geral/Etica"
tags: ["ethics","privacy","agents","guardrails"]
created: "2026-05-08"
status: "draft"
---

# Privacidade by Default para Agentes

Privacidade by default significa: quando um agente (ou automacao) precisar escolher entre "coletar mais dados" e "resolver com menos", ele escolhe menos por padrao. So coleta o minimo necessario quando houver justificativa clara, risco avaliado e (quando aplicavel) consentimento.

## Principios praticos

- Minimizar dados na entrada: pedir apenas o necessario para executar a tarefa.
- Minimizar dados na saida: nao registrar ou reexpor dados sensiveis sem motivo.
- Minimizar tempo de retencao: nao manter dados alem do periodo util.
- Minimizar alcance: dados ficam no menor escopo possivel (pasta/projeto/nota), evitando espalhar por multiplos hubs.
- Separacao de dominios: dados pessoais ficam separados de dados tecnicos; dados de terceiros ficam separados de dados do usuario.

## Defaults recomendados (operacionais)

1. Nao persistir conteudo sensivel: se um agente ler algo sensivel para resolver um bug, ele nao deve copiar isso para notas canonicamente buscaveis.
2. Nao indexar por padrao: qualquer camada RAG/indexador deve ter lista de inclusao (allowlist) e exclusao (denylist) clara.
3. Nao criar "memory dumps": evitar dumps de conversas, telas, chaves, tokens, cookies, extratos e documentos.
4. Nao citar dados privados em exemplos: use placeholders consistentes (`<EMAIL>`, `<CPF>`, `<API_KEY>`).

## Gatilhos de confirmacao (antes de prosseguir)

- O agente precisa mover/duplicar dados de `Will-Pessoal/` (ou equivalente) para uma area compartilhada.
- O agente quer salvar logs detalhados com conteudo de requests/responses.
- O agente vai anexar outputs completos de `env`, `config`, `.npmrc`, `.pypirc`, `.gitconfig`, tokens, credenciais.

## Prompts de guardrail (para agente)

- "Posso resolver isso com menos dados? Qual o minimo necessario?"
- "Esse dado precisa ser persistido ou so usado agora?"
- "Isso deve ir para um log ou para uma nota canonicamente indexada?"

## Anti-padroes comuns

- Guardar tudo "para o futuro" sem criterio.
- Copiar colagens de logs com PII.
- Transformar notas eticas em burocracia: guardrails devem ser curtos, acionaveis e auditaveis.

## Relacionado

- [[Minimizacao-de-Dados-para-RAG-e-Agentes]]
- [[Politica-de-Logs-para-Agentes]]
- [[Limites-de-Automacao-e-Consentimento]]

