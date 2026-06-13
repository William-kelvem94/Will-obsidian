# Contrato de dívidas

A rota `POST /api/debts` passou a montar o payload uma única vez via helper comum, evitando duplicação de `toDebtView` e deixando o contrato de criação alinhado ao GET/PUT.