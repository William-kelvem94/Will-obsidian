# Utils sanity restore

O arquivo `src/utils/utils.ts` estava truncado no worktree e impedia a validação do backend. Foram restaurados `getInitials`, `calculatePercentage` e `truncate` para manter o projeto compilando e liberar a checagem dos contratos financeiros.