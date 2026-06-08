---
title: "Web Components"
category: "Frontend"
level: 3
description: "Padroes para construir componentes web modulares com Custom Elements, Shadow DOM, templates e eventos customizados."
projects:
  - "Gestor Aluguel"
related_skills:
  - "Observabilidade"
  - "Kubernetes"
resources:
  - "Web Components MDN documentation"
  - "Lit library documentation"
  - "Web Components best practices articles"
date: 2026-04-29
tags: [skills, frontend, web-components]
updated: 2026-06-08
---

# Web Components

Web Components permitem criar elementos reutilizaveis, encapsulados e agnosticos a framework, baseados em Custom Elements, Shadow DOM, HTML Templates e Custom Events.

## Custom Elements — Ciclo de Vida

```javascript
class JarvisCard extends HTMLElement {
  static get observedAttributes() {
    return ['title', 'status', 'loading'];
  }

  constructor() {
    super();
    this._title = '';
    this._status = 'idle';
    this._loading = false;
    this.attachShadow({ mode: 'open' });
  }

  connectedCallback() {
    this.render();
    this.addEventListener('click', this._handleClick);
  }

  disconnectedCallback() {
    this.removeEventListener('click', this._handleClick);
  }

  attributeChangedCallback(name, oldValue, newValue) {
    if (oldValue === newValue) return;
    this[`_${name}`] = newValue;
    this.render();
  }

  _handleClick = (e) => {
    this.dispatchEvent(new CustomEvent('card-selected', {
      bubbles: true,
      composed: true,
      detail: { title: this._title, status: this._status }
    }));
  }

  render() {
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: block;
          border: 1px solid var(--card-border, #e0e0e0);
          border-radius: 8px;
          padding: 16px;
          cursor: pointer;
          transition: box-shadow 0.2s;
        }
        :host(:hover) {
          box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        :host([loading]) {
          opacity: 0.6;
          pointer-events: none;
        }
        .title { font-weight: 600; margin-bottom: 8px; }
        .status {
          display: inline-block;
          padding: 2px 8px;
          border-radius: 12px;
          font-size: 0.75em;
        }
        .status[value="active"] { background: #e8f5e9; color: #2e7d32; }
        .status[value="inactive"] { background: #fbe9e7; color: #c62828; }
      </style>
      <div class="title">${this._title}</div>
      <div class="status" value="${this._status}">${this._status}</div>
    `;
  }
}

customElements.define('jarvis-card', JarvisCard);
```

## Shadow DOM — Encapsulamento

### Modos de Encapsulamento

```javascript
// Modo 'open' — acessivel via element.shadowRoot
const shadow = element.attachShadow({ mode: 'open' });
console.log(element.shadowRoot); // retorna o Shadow DOM

// Modo 'closed' — inacessivel externamente
const shadow = element.attachShadow({ mode: 'closed' });
console.log(element.shadowRoot); // null
```

### Slots para Composicao

```javascript
class JarvisLayout extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: 'open' });
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: grid;
          grid-template-areas:
            "header header"
            "sidebar content"
            "footer footer";
          grid-template-columns: 250px 1fr;
          gap: 16px;
          min-height: 100vh;
        }
        header { grid-area: header; }
        aside { grid-area: sidebar; }
        main { grid-area: content; }
        footer { grid-area: footer; }
        ::slotted(*) { box-sizing: border-box; }
      </style>
      <header><slot name="header"></slot></header>
      <aside><slot name="sidebar"></slot></aside>
      <main><slot name="content"></slot></main>
      <footer><slot name="footer"></slot></footer>
    `;
  }
}
customElements.define('jarvis-layout', JarvisLayout);
```

## Custom Events

```javascript
class JarvisAutocomplete extends HTMLElement {
  constructor() {
    super();
    this._items = [];
    this.attachShadow({ mode: 'open' });
  }

  connectedCallback() {
    this.render();
    this.shadowRoot.querySelector('input')
      .addEventListener('input', this._onInput);
    this.shadowRoot.querySelector('.dropdown')
      .addEventListener('click', this._onSelect);
  }

  _onInput = (e) => {
    const query = e.target.value;
    this.dispatchEvent(new CustomEvent('search', {
      bubbles: true,
      composed: true,
      detail: { query }
    }));
  }

  _onSelect = (e) => {
    const item = e.target.closest('[data-value]');
    if (!item) return;
    this.dispatchEvent(new CustomEvent('selected', {
      bubbles: true,
      composed: true,
      detail: { value: item.dataset.value, label: item.textContent }
    }));
  }

  set items(items) {
    this._items = items;
    this._renderDropdown();
  }

  render() {
    this.shadowRoot.innerHTML = `
      <div class="autocomplete">
        <input type="text" part="input" placeholder="Pesquisar...">
        <div class="dropdown" part="dropdown"></div>
      </div>
    `;
  }
}
```

## Usando com Lit (Biblioteca Recomendada)

```javascript
import { LitElement, html, css } from 'lit';

class JarvisButton extends LitElement {
  static properties = {
    variant: { type: String },
    disabled: { type: Boolean }
  };

  static styles = css`
    :host { display: inline-block; }
    button {
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-family: inherit;
    }
    button[disabled] { opacity: 0.5; cursor: not-allowed; }
    .primary { background: #1976d2; color: white; }
    .secondary { background: #e0e0e0; color: #333; }
  `;

  render() {
    return html`
      <button
        class="${this.variant || 'primary'}"
        ?disabled="${this.disabled}"
        @click="${this._handleClick}"
      >
        <slot></slot>
      </button>
    `;
  }

  _handleClick(e) {
    this.dispatchEvent(new CustomEvent('jarvis-click', {
      bubbles: true, composed: true
    }));
  }
}
customElements.define('jarvis-button', JarvisButton);
```

## Testando Web Components

```javascript
import { fixture, assert } from '@open-wc/testing';

describe('JarvisCard', () => {
  it('deve renderizar titulo e status', async () => {
    const el = await fixture(
      '<jarvis-card title="Teste" status="active"></jarvis-card>'
    );
    assert.include(el.shadowRoot.textContent, 'Teste');
    assert.include(el.shadowRoot.textContent, 'active');
  });

  it('deve emitir evento card-selected ao clicar', async () => {
    const el = await fixture('<jarvis-card title="Teste"></jarvis-card>');
    const handler = sinon.spy();
    el.addEventListener('card-selected', handler);
    el.click();
    assert(handler.calledOnce);
  });
});
```

## Boas Praticas

- Sempre use `attachShadow({ mode: 'open' })` para facilitar testes e debug
- Use `observedAttributes` para sincronizar propriedades com atributos
- Evite dependencias externas no Shadow DOM — encapsule estilos
- Use CSS custom properties (`var(--...)`) para theming externo
- Nomeie componentes com prefixo para evitar conflitos (`jarvis-*`)
- Prefira Lit para projetos complexos (reatividade, templates eficientes)

## Referencias

- [[05-Skills/02-software-engineering/frontend|Frontend Skills]] — Integracao com React/Vue
- [[05-Skills/02-software-engineering/backend|Backend]] — APIs que alimentam os componentes
- [[05-Skills/devops/Observabilidade|Observabilidade]] — RUM e monitoramento de componentes
