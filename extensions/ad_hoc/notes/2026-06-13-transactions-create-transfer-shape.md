# Transactions create transfer shape

A criação de transações agora serializa transferências com payload explícito, preservando `transaction` e `destinationTransaction` sem expor o retorno cru do serviço.