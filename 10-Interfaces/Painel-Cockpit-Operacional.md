---
title: "Painel Cockpit Operacional"
date: 2026-07-07
updated: 2026-07-07
type: dashboard
status: active
tags: [dashboard, cockpit, projetos, vault-ops, dataview]
summary: "Painel central para acompanhar projetos, saúde do vault, gaps de skills e manutenção operacional."
related:
  - [[03-Projetos/01-Ativos/Plano-de-Acao]]
  - [[02-JARVIS/02-Operational/Project-Health-Report]]
  - [[07-Operacoes-do-Vault/Auditoria-Caminhos-Legados]]
  - [[09-Sistema/schema/Politica-de-Privacidade-e-Indexacao]]
---

# Painel Cockpit Operacional 🕹️

Este painel é a entrada prática para acompanhar o estado vivo do WILL-OBSIDIAN.

Ele não substitui os hubs. Ele funciona como **mesa de controle** para execução, manutenção e expansão.

## Acesso rápido

- [[03-Projetos/README|Projetos]]
- [[03-Projetos/01-Ativos/Plano-de-Acao|Plano de Ação dos Projetos]]
- [[03-Projetos/01-Ativos/Privados/README|Projetos Privados Clonados]]
- [[02-JARVIS/README|JARVIS]]
- [[05-Skills/README|Skills]]
- [[07-Operacoes-do-Vault/README|Operações do Vault]]
- [[09-Sistema/schema/Politica-de-Privacidade-e-Indexacao|Política de Privacidade e Indexação]]
- [[07-Operacoes-do-Vault/Auditoria-Caminhos-Legados|Auditoria de Caminhos Legados]]

---

## 1. Projetos ativos por atualização

```dataview
TABLE
  status as Status,
  language as Linguagem,
  priority as Prioridade,
  updated as Atualizado,
  description as Descrição
FROM "03-Projetos/01-Ativos/Privados"
WHERE file.name != "README" AND file.name != "INDEX"
SORT updated desc, file.mtime desc
```

---

## 2. Projetos sem próxima ação explícita

```dataview
TABLE
  status as Status,
  updated as Atualizado,
  file.folder as Pasta
FROM "03-Projetos/01-Ativos/Privados"
WHERE !contains(file.content, "Próxima ação") AND !contains(file.content, "Proxima acao") AND !contains(file.content, "Próximos passos") AND !contains(file.content, "Proximos passos")
SORT file.mtime desc
```

---

## 3. Projetos sem contrato de execução visível

Use esta seção para achar notas sem comandos de run/dev/test/build.

```dataview
TABLE
  language as Linguagem,
  updated as Atualizado,
  description as Descrição
FROM "03-Projetos/01-Ativos/Privados"
WHERE !contains(lower(file.content), "run")
  AND !contains(lower(file.content), "start")
  AND !contains(lower(file.content), "dev")
  AND !contains(lower(file.content), "test")
  AND !contains(lower(file.content), "build")
SORT updated desc
```

---

## 4. Projetos com sincronização local

```dataview
TABLE
  source as Fonte,
  language as Linguagem,
  updated as Atualizado
FROM "03-Projetos/01-Ativos/Privados"
WHERE contains(file.content, "Sincronização Local de Código") OR contains(file.content, "Sincronizacao Local de Codigo")
SORT updated desc
```

---

## 5. Skills por domínio

```dataview
TABLE length(rows) as Total
FROM "05-Skills"
WHERE file.name != "README" AND file.name != "INDEX"
GROUP BY file.folder
SORT length(rows) desc
```

---

## 6. Notas recentes em conhecimento

```dataview
TABLE file.folder as Pasta, file.mtime as Modificado, tags as Tags
FROM "04-Conhecimentos"
SORT file.mtime desc
LIMIT 25
```

---

## 7. Operações recentes do vault

```dataview
TABLE status as Status, updated as Atualizado, summary as Resumo
FROM "07-Operacoes-do-Vault"
SORT file.mtime desc
LIMIT 20
```

---

## 8. Documentos de governança ativos

```dataview
TABLE type as Tipo, status as Status, updated as Atualizado, summary as Resumo
FROM "09-Sistema"
WHERE contains(tags, "governanca") OR contains(tags, "privacidade") OR contains(tags, "schema")
SORT updated desc
```

---

## 9. Alertas manuais

- [ ] Rodar `.scripts/project_health_checker.py` localmente após mudanças grandes.
- [ ] Rodar `.scripts/study_recommender.py` após atualizar skills ou projetos.
- [ ] Revisar notas em `06-Will-Pessoal/` antes de qualquer indexação.
- [ ] Revisar dashboards antigos em `01-Hubs/dashboards/`.
- [ ] Atualizar `07-Operacoes-do-Vault/Status-da-Migracao-Fisica.md` após validação no Obsidian.

---

## 10. Rotina recomendada

### Semanal

1. Abrir este painel.
2. Ver projetos sem próxima ação.
3. Ver projetos sem contrato de execução.
4. Rodar health checker.
5. Atualizar plano de ação.

### Mensal

1. Revisar política de indexação.
2. Revisar caminhos legados.
3. Arquivar notas sem uso.
4. Promover aprendizados de projetos para `04-Conhecimentos/` e `05-Skills/`.

---

## Observação

Este cockpit usa caminhos numerados. Se alguma consulta ficar vazia, verificar se o conteúdo ainda está em pasta legada ou se o plugin Dataview precisa ser atualizado/recarregado no Obsidian.
