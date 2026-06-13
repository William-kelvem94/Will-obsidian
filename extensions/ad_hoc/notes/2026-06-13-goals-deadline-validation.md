# Goals deadline validation

As rotas `POST /api/goals` e `PUT /api/goals/[id]` agora validam `deadline` na entrada antes de montar o `Date`. Isso evita que payloads ruins dependam da conversão tardia e fortalece o contrato da meta.