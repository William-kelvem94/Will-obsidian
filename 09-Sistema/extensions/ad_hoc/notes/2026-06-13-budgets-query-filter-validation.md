# Budgets query filter validation

A listagem de orçamentos agora valida `status` e `period` antes da consulta. Filtros inválidos retornam 400 e não viram query silenciosamente inconsistente.