# Contrato de transações

A API de `GET /api/transactions` passou a reutilizar `result.totals` vindo do serviço, em vez de recalcular totais só com a página atual. Isso evita resumo incorreto quando a listagem é paginada.