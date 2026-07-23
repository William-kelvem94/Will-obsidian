# Contrato de dívidas

A rota `GET/PUT /api/debts/[id]` passou a montar o payload uma única vez via `toDebtView`, evitando conversão duplicada e mantendo a serialização consistente entre leitura e atualização.