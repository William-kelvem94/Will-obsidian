# Budgets date validation

As rotas `POST /api/budgets` e `PUT /api/budgets/[id]` agora validam `startDate` e `endDate` com schema explícito antes de converter para `Date`. Isso evita orçamentos com período quebrado por payload inválido.