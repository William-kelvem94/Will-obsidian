# Contrato de transações

A rota `GET/PUT /api/transactions/[id]` passou a devolver `{ data, transaction }` e a responder `404` de forma explícita quando a transação não existe, mantendo o contrato de saída alinhado ao restante do backend.