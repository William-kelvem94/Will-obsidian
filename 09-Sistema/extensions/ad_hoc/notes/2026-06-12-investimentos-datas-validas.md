# Contrato de investimentos

A API de listagem de investimentos passou a validar `startDate` e `endDate` antes de aplicar o filtro. Datas inválidas agora viram `null`, evitando `Invalid Date` no Prisma.