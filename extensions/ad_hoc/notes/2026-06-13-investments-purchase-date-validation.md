# Investments purchase date validation

As rotas `POST /api/investments` e `PUT /api/investments/[id]` agora validam `purchaseDate` na entrada com schema explícito. Payloads com data inválida deixam de passar para a camada de persistência.