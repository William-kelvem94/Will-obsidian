---
tags: [skills, skills-eng, frontend, react, vue]
updated: 2026-05-16
title: "Frontend Skills - React, Vue, Gerenciamento de Estado"
date: 2026-04-27
---

# Frontend Skills — React, Vue e Padroes de Interface

Referencia pratica para construcao de interfaces modulares com React e Vue, incluindo gerenciamento de estado, hooks/composables, testes e acessibilidade.

## React — Padroes de Componentes

### Componente com Custom Hook

```tsx
function useUser(id: string) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`/api/users/${id}`)
      .then(res => res.json())
      .then(setUser)
      .finally(() => setLoading(false));
  }, [id]);

  return { user, loading };
}

function UserProfile({ userId }: { userId: string }) {
  const { user, loading } = useUser(userId);
  if (loading) return <Skeleton />;
  return <div>{user?.nome}</div>;
}
```

### Gerenciamento de Estado com Zustand

```typescript
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface AuthState {
  token: string | null;
  user: User | null;
  login: (credentials: Credentials) => Promise<void>;
  logout: () => void;
}

const useAuthStore = create<AuthState>()(
  persist(
    (set) => ({
      token: null,
      user: null,
      login: async (credentials) => {
        const res = await api.post('/auth/login', credentials);
        set({ token: res.token, user: res.user });
      },
      logout: () => set({ token: null, user: null }),
    }),
    { name: 'auth-storage' }
  )
);
```

### Estrategias de Renderizacao

```tsx
// React Query para cache e fetching
function UserList() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['users'],
    queryFn: () => fetch('/api/users').then(r => r.json()),
    staleTime: 5 * 60 * 1000, // 5 min cache
  });

  if (isLoading) return <Spinner />;
  if (error) return <ErrorBoundary error={error} />;
  return data.map(user => <UserCard key={user.id} user={user} />);
}
```

## Vue — Padroes de Componentes

### Composables (equivalente a hooks)

```typescript
// composables/useAuth.ts
export function useAuth() {
  const user = ref<User | null>(null);
  const loading = ref(false);

  async function login(email: string, senha: string) {
    loading.value = true;
    try {
      const res = await api.post('/auth/login', { email, senha });
      user.value = res.user;
      navigateTo('/dashboard');
    } finally {
      loading.value = false;
    }
  }

  return { user, loading, login };
}
```

### Gerenciamento de Estado com Pinia

```typescript
// stores/counter.ts
export const useCounterStore = defineStore('counter', () => {
  const count = ref(0);
  const double = computed(() => count.value * 2);

  function increment() { count.value++; }
  function reset() { count.value = 0; }

  return { count, double, increment, reset };
});
```

## Estrategias de Teste

### Testes Unitarios (Vitest)

```typescript
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { LoginForm } from './LoginForm';

describe('LoginForm', () => {
  it('deve validar email invalido', async () => {
    render(<LoginForm />);
    await userEvent.type(screen.getByLabelText('Email'), 'invalido');
    await userEvent.click(screen.getByRole('button'));
    expect(screen.getByText('Email invalido')).toBeInTheDocument();
  });
});
```

### Testes de Integracao (Playwright)

```typescript
test('fluxo de login completo', async ({ page }) => {
  await page.goto('/login');
  await page.fill('[data-testid="email"]', 'user@email.com');
  await page.fill('[data-testid="senha"]', 'minha-senha');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL('/dashboard');
  await expect(page.locator('text= Bem-vindo')).toBeVisible();
});
```

## Acessibilidade

- Use roles e aria-* corretamente em componentes customizados
- Garanta navegacao por teclado (tabindex, focus management)
- Contraste de cores conforme WCAG 2.1 AA
- Labels semanticas para formularios
- Mensagens de erro claras e programaticamente associadas

## Padroes de Performance

- Lazy loading de componentes com `React.lazy` ou `defineAsyncComponent`
- Virtualizacao de listas longas (react-window, vue-virtual-scroller)
- Debounce em campos de busca e filtros
- Memoizacao com `useMemo`, `useCallback` ou `computed`

## Referencias

- [[backend|Backend]] — APIs que consomem estes componentes
- [[Web-Components|Web Components]] — Alternativa agnostica a frameworks
- [[skills/ai/Engenharia-de-Prompts|Engenharia de Prompts]] — Prompts para geracao de componentes
- [[skills/devops/Observabilidade|Observabilidade]] — RUM e monitoramento de frontend
