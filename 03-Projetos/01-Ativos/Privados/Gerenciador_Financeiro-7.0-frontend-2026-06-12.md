---
title: "Gerenciador Financeiro 7.0 - Frontend 2026-06-12"
date: 2026-06-12
tags:
  - privados
  - frontend
  - financeiro
  - mapeamento
updated: 2026-06-13
---

# Frontend - Estado atual

## O que foi consolidado
- `src/components/layout/Sidebar.tsx`: fechamento do menu mobile ao navegar e remoção de interação solta no botão de ação.
- `src/components/layout/Header.tsx`: busca do header alinhada ao contexto financeiro.
- `src/app/(protected)/transacoes/page.tsx`: remoção do shell externo próprio e unificação com `MainLayout`.
- `src/app/(protected)/contas/page.tsx`: saldo total normalizado com `toMoneyNumber` e remoção de título duplicado no corpo da página.
- `src/app/(protected)/contatos/page.tsx`: inclusão de resumo de lista, empty state mais acionável e melhor leitura dos filtros.
- `src/app/(protected)/dividas/page.tsx`: resumo de dívidas, empty state com ação e leitura mais rápida do saldo em aberto.
- `src/app/(protected)/metas/page.tsx`: resumo de metas ativas/concluídas/total no topo da tela.
- `src/app/(protected)/investimentos/page.tsx`: resumo de investimentos, positivos e resultado líquido no topo.
- `src/app/(protected)/orcamento/page.tsx`: resumo de orçamento, excedidos, gasto total e limite total no topo.

## Decisão de arquitetura
- Frontend deve usar `MainLayout` como padrão das telas protegidas.
- Telas com shell próprio só permanecem se houver justificativa clara de UX.
- A frente de frontend não deve alterar schema ou contratos de banco; quando encontrar desalinhamento estrutural, registrar e passar para a frente de backend.

## Verificação
- `npm.cmd run type-check` passou.
- `npm.cmd run build` passou após limpar `.next`.

## Próxima verificação
- Runtime do servidor está sujeito ao processo que já está ativo na porta 3000; a build verde confirma a integridade do frontend consolidado.

## Observação
- O projeto Domni continua apenas como referência visual e de organização.
- Não copiar regras de aluguel, portal do inquilino ou fluxos imobiliários.
