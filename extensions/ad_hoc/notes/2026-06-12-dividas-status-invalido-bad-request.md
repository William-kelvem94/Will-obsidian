# Contrato de dívidas

A API de listagem de dívidas passou a rejeitar `status` inválido com `400 Bad Request`. Isso evita que o cliente acredite ter filtrado corretamente quando, na verdade, o valor era fora do contrato.