---
title: "PR Checklist for Frontend Changes (Agents) — Guia de Revisão e Garantia Frontend"
category: "Frontend"
level: 4
description: "Checklist avançado e guia de revisão de código para mudanças em interfaces frontend, cobrando acessibilidade, performance Web Vitals, limites de estado e segurança de hidratação."
tags: [skills, frontend, pr-checklist, web-vitals, accessibility, nextjs, react]
updated: 2026-06-13
date: 2026-06-01
---

# PR Checklist for Frontend Changes & Code Review (Agents & Humans)

Desenvolver e revisar alterações de interface frontend requer um equilíbrio refinado entre estabilidade de código, acessibilidade universal e otimização obsessiva de tempos de renderização (*Core Web Vitals*). Quando agentes de inteligência artificial realizam edições em arquivos TypeScript baseados em frameworks interativos (React, Vue, Web Components ou Next.js), o potencial de introduzir lentidões invisíveis, incompatibilidade de estados de hidratação ou quebras no suporte acessível é de alto risco.

Este guia orienta o rigor e os critérios de validação necessários para aprovação de alterações em camadas de apresentação frontend.

---

## 📐 1. A Fronteira Next.js: Server vs Client Components

Ao editar códigos no ecossistema do React Server Components (RSC), o limite físico entre o processamento estático no servidor e a interatividade no navegador deve ser rigidamente respeitado:

```
                  ┌──────────────────────────────────────────────┐
                  │          NEXT.JS ARCHITECTURAL BOUNDS        │
                  └──────────────────────┬───────────────────────┘
                                         │
        ┌────────────────────────────────┴────────────────────────────────┐
        ▼                                                                 ▼
┌──────────────────────────┐                                      ┌──────────────────────────┐
│   SERVER COMPONENTS      │                                      │   CLIENT COMPONENTS      │
│ • "use server" (Action)  │                                      │ • "use client" (Directive)│
│ • Acesso direto ao DB/API│                                      │ • Interatividade (hooks) │
│ • Segredos de API puros  │                                      │ • Event Listeners        │
│ • CSS estático           │                                      │ • Componentes dependentes│
└──────────────────────────┘                                      └──────────────────────────┘
```

*   **Minimização da Diretiva `"use client"`**: Não insira a diretiva `"use client"` por padrão no topo de todos os novos componentes criados. Preserve o processamento estático e a renderização no lado do servidor (RSC) para o máximo de nodos da árvore DOM possível. Reserve o contexto de cliente apenas para as sub-folhas interativas (formulários, botões de clique com estado, sliders e carrosséis).
*   **Isolamento de Segredos de Servidor**: Certifique-se de que chaves privadas e dependências diretas de banco de dados utilizadas em ações de servidor (`Server Actions`) nunca escapem por engano em componentes baixados pelo navegador sob risco de quebra de OpSec.

---

## ♿ 2. Acessibilidade (A11y) e Compatibilidade Universal

O software deve ser utilizável de forma democrática por todas as pessoas, incluindo aquelas dependentes de leitores de tela ou que utilizam exclusivamente o teclado para navegação:

*   **Estrutura de Cabeçalhos Semânticos**: Garanta o uso sequencial lógico de tags HTML (`<h1>`, `<h2>`, `<h3>`...) sem saltar escalas estruturais por motivos puramente estéticos (ex: usar h4 direto abaixo de h1 apenas pelo tamanho da fonte). Use CSS para formatação visual.
*   **Contraste de Cores**: Respeitar a classificação mínima AA recomendada pelas diretrizes WCAG 2.1 (relação de contraste de cores de no mínimo **$4.5:1$** para texto normal e **$3.0:1$** para texto grande ou botões interativos).
*   **Foco no Teclado e Focus Traps**: 
    1.  Mantenha anéis de foco visualmente transparentes e nítidos (`outline-focus`) para que o usuário saiba precisamente qual link ou botão está focado ao usar a tecla Tab.
    2.  Ao implementar áreas modais suspensas ou menus deslizantes laterais (*Drawers*), institua um **Focus Trap** (conter o foco de navegação Tab dentro do painel modal suspenso enquanto ele permanecer aberto), garantindo o fechamento imediato do modal e o retorno de foco ao elemento chamador quando o usuário pressionar a tecla `Escape`.
*   **Suporte ARIA**: O uso de tags cruas que emulam botões (como elementos `<div>` interativos) exige a entrega de atributos ARIA mínimos para reconhecimento por softwares auxiliares:
    ```html
    <!-- ❌ RUIM: Inacessível a leitores e navegação teclado -->
    <div onclick="submitForm()">Enviar Dados</div>
    
    <!-- ✅ BOM: Completamente acessível e semântico -->
    <button type="button" aria-label="Enviar formulário de clientes" onclick="submitForm()">
      Enviar Dados
    </button>
    ```

---

## ⚡ 3. Otimização de Performance: Core Web Vitals

A interface criada ou alterada pelo agente deve ser validada contra gargalos de velocidade de interação e layout:

### 3.1 Prevenção a Saltos Visuais: CLS (Cumulative Layout Shift)
*   **O Problema**: Imagens ou blocos de propaganda dinâmica sem largura (`width`) e altura (`height`) explicitadas em sua tag fazem com que o navegador mude todo o texto da página de lugar quando o asset finalmente termina de carregar, irritando o usuário.
*   **A Solução**: Sempre determine tamanhos explícitos de carregamento para imagens e blocos dinâmicos (`aspect-ratio` no CSS ou *Skeleton Loaders* com altura estrita parametrizada).

### 3.2 Otimizações de Carregamento de Recursos

| Indicador Web Vital | Descrição | Estratégia de Mitigação |
|---|---|---|
| **LCP (Largest Contentful Paint)** | Tempo de carregamento da imagem ou bloco principal visível. | Utilizar tags modernas de imagem (`next/image`), otimizar dimensões e evitar que imagens de destaque (*above the fold*) sejam carregadas de forma preguiçosa (`lazy`). |
| **FID/INP (Interactive Responsiveness)** | Tempo de resposta do clique do usuário sobre a interface. | Eliminar códigos longos que bloqueiam o loop central e quebrar tarefas Javascript pesadas usando `requestIdleCallback` ou web workers. |
| **Bundle Size Control** | Impacto do tamanho total do JavaScript baixado na execução. | Evitar a importação indiscriminada de pacotes massivos completos como `lodash` ou `three.js` se for utilizar apenas uma função helper curta. Prefira o uso de *Tree-shaking* e carregamentos dinâmicos (`next/dynamic` ou `React.lazy`). |

---

## 🛡️ 4. Segurança de Hidratação (SSR Hydration Safety)

Erros clássicos de desacordo de hidratação (Hydration Mismatch) ocorrem em frameworks baseados em Server-Side Rendering (SSR) quando o DOM inicial renderizado no servidor é estaticamente diferente da árvore construída pelo React no cliente no primeiro renderizador:

*   **O Erro**:
    ```
    Error: Hydration failed because the initial UI does not match what was rendered on the server.
    ```
*   **A Causa**: Uso excessivo de variáveis que mudam dependendo do ambiente da máquina do cliente no nível de renderização inicial (como o uso cru de funções utilitárias baseadas em horários locais `new Date()`, verificações de tela baseadas em `window.innerWidth`, ou dados dinâmicos do LocalStorage sem proteção).
*   **A Solução**: Embrulhe dados variáveis do navegador dentro do hook de gatilho pós-montagem `useEffect()` ou use variáveis de estado que se estabilizam exclusivamente após a montagem do componente cliente:
    ```typescript
    const [mounted, setMounted] = useState(false);
    
    useEffect(() => {
      setMounted(true);
    }, []);
    
    if (!mounted) return <SkeletonLoader />; // Renderizador estático idêntico seguro
    return <InteractiveClientPanel />;
    ```
---

## 📋 5. Manifesto Curto de PR Checklist Frontend (Gatilha de Aprovação)

- [ ] A alteração não introduz erros visuais ou warnings em console na renderização das principais páginas.
- [ ] Os estados de **Carregamento (Loading)**, **Entrada Sem Dados (Empty)** e **Tratamento de Falhas (Error boundary)** de rede foram desenhados na interface.
- [ ] A alteração de estilos CSS ou de Tailwind é responsiva, funcionando perfeitamente em telas móveis (*MobileFirst*) e desktop.
- [ ] Todos os novos componentes interativos possuem testes unitários e de componente correspondentes validados.


