# Como Ativar o Modo Foco (Focus Mode)

O snippet `focus-mode.css` depende da classe `.focus-mode` no `<body>` do Obsidian.
Como o Obsidian nativo não expõe essa classe, você precisa de um gatilho.

## Opção 1: Plugin "Toggle Focus Mode" (Recomendado)

1. Abra **Configurações → Plugins da Comunidade**
2. Busque por **"Toggle Focus Mode"** e instale
3. Ative o plugin
4. Vá em **Configurações → Hotkeys**
5. Busque por **"Toggle Focus Mode"**
6. Atribua uma hotkey (ex: `Ctrl+Shift+F` ou `Cmd+Shift+F`)

Este plugin adiciona/remove a classe `.focus-mode` do `<body>` automaticamente.

## Opção 2: Plugin "Focus Mode" (sidharthv)

1. Instale o plugin **"Focus Mode"** pela comunidade
2. Configure a hotkey em **Configurações → Hotkeys → Focus Mode: Toggle**

## Opção 3: Plugin "Commander" + CSS Classes

1. Instale o plugin **Commander**
2. Adicione um botão à toolbar que alterna a classe `.focus-mode` no `<body>`

## Opção 4: JavaScript Manual (via Templater / CustomJS)

Crie um script que faz toggle da classe no body:

```js
// Adicione como um comando no Obsidian via plugin CustomJS ou Script
document.body.classList.toggle('focus-mode');
```

## Dica Extra

Depois de ativar, use `Ctrl+Shift+F` (ou sua hotkey) para alternar entre
modo foco e modo normal instantaneamente.
