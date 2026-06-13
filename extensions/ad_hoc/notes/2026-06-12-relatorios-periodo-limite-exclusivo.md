# Contrato de relatórios

A API de `GET /api/reports` passou a usar limite superior exclusivo (`lt`) para os períodos, evitando perda de transações no último dia do intervalo. Isso vale para mês e ano e reduz ambiguidade de fronteira.