# Contrato de metas

A rota `PUT /api/goals/[id]` passou a montar o payload uma única vez via `toGoalView`, alinhando a serialização com o padrão usado em outras rotas centrais.