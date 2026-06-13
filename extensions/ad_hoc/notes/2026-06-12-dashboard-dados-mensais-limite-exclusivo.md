# Contrato de dashboard

O endpoint de dados mensais do dashboard passou a usar limite superior exclusivo (`lt`) no mês seguinte. Isso evita perdas em registros com milissegundos no fim do mês e alinha a leitura com o contrato de período fechado.