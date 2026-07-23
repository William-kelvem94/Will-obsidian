# Transactions end-date exclusive

O serviço de listagem de transações passou a tratar `endDate` com limite superior exclusivo (`lt`). Isso alinha a listagem com reports e dashboards e evita perder ou duplicar lançamentos na borda do período.