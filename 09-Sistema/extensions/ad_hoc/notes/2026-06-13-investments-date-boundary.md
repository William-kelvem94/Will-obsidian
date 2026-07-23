# Investments date boundary

A rota `GET /api/investments` agora usa `lt` no fim do intervalo de `purchaseDate`, alinhando com reports e dashboards para evitar duplicidade de registros na borda do período.