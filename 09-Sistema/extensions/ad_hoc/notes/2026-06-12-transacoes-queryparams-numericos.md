# Contrato de transações

A API de `GET /api/transactions` passou a sanitizar `limit`, `offset`, `minAmount` e `maxAmount`. Valores inválidos não viram `NaN` na consulta; caem em defaults seguros ou `null`.