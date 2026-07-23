# Contrato de transações

A API de listagem de transações passou a exigir `limit` e `offset` positivos, usando defaults seguros quando o cliente envia valores negativos, zero ou inválidos.