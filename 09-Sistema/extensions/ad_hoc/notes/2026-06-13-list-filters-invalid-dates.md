# List filters invalid dates

As rotas `GET /api/transactions` e `GET /api/investments` agora retornam 400 quando `startDate` ou `endDate` chegam inválidas. Isso evita consulta silenciosamente errada e deixa o contrato do filtro explícito.