# Contrato de investimentos

A atualização de investimento passou a ignorar `purchaseDate` inválida em vez de tentar gravar `null`. Isso evita erro de tipo no Prisma e mantém o campo anterior quando o payload vier ruim.