# Contrato de orçamentos

As rotas `POST /api/budgets` e `PUT /api/budgets/[id]` passaram a montar o payload uma única vez via helper comum, alinhando a serialização de orçamento ao padrão das demais rotas centrais.