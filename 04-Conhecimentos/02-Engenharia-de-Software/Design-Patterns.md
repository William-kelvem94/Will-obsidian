---
title: "Design Patterns"
date: 2026-05-16
area: "Programação e Engenharia de Software"
tags: [conhecimento, programacao, design-patterns, gof]
related: ["04-Conhecimentos/02-Engenharia-de-Software/Arquitetura-de-Software"]
aliases: ["Design Patterns", "GoF Patterns", "Padrões de Projeto"]
---

# Design Patterns

Design Patterns (Padrões de Projeto) são **soluções reutilizáveis** para problemas recorrentes no desenvolvimento de software. O catálogo seminal da **Gang of Four** (GoF) — Gamma, Helm, Johnson e Vlissides — publicado em 1994, definiu 23 padrões organizados em três categorias.

**Referência:** Gamma, E.; Helm, R.; Johnson, R.; Vlissides, J. *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994.

---

## 1. Padrões Criacionais (Creational)

Padrões que abstraem o processo de **criação de objetos**, tornando o sistema independente de como seus objetos são criados, compostos e representados.

### 1.1 Singleton

Garante que uma classe tenha **apenas uma instância** e fornece um ponto global de acesso a ela.

```python
class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._config = {}
        return cls._instance

    def set(self, chave: str, valor: str) -> None:
        self._config[chave] = valor

    def get(self, chave: str) -> str | None:
        return self._config.get(chave)

# Uso
config1 = ConfigManager()
config2 = ConfigManager()
config1.set("host", "localhost")
print(config2.get("host"))  # localhost
print(config1 is config2)   # True
```

```typescript
class ConfigManager {
  private static instance: ConfigManager;
  private config = new Map<string, string>();

  private constructor() {}

  static getInstance(): ConfigManager {
    if (!ConfigManager.instance) {
      ConfigManager.instance = new ConfigManager();
    }
    return ConfigManager.instance;
  }

  set(key: string, value: string): void {
    this.config.set(key, value);
  }

  get(key: string): string | undefined {
    return this.config.get(key);
  }
}

const config1 = ConfigManager.getInstance();
const config2 = ConfigManager.getInstance();
console.log(config1 === config2); // true
```

**Cuidado:** Singleton é frequentemente considerado **anti-pattern** por criar dependências ocultas e dificultar testes. Considere **Dependency Injection** como alternativa.

### 1.2 Factory Method

Define uma interface para criar um objeto, mas permite que subclasses decidam qual classe instanciar.

```python
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def entregar(self) -> str: ...

class Caminhao(Veiculo):
    def entregar(self) -> str:
        return "Entrega por caminhão"

class Navio(Veiculo):
    def entregar(self) -> str:
        return "Entrega por navio"

class Logistica(ABC):
    @abstractmethod
    def criar_veiculo(self) -> Veiculo: ...

    def planejar_entrega(self) -> str:
        veiculo = self.criar_veiculo()
        return f"Planejando: {veiculo.entregar()}"

class LogisticaTerrestre(Logistica):
    def criar_veiculo(self) -> Veiculo:
        return Caminhao()

class LogisticaMaritima(Logistica):
    def criar_veiculo(self) -> Veiculo:
        return Navio()

# Uso
logistica = LogisticaTerrestre()
print(logistica.planejar_entrega())  # Planejando: Entrega por caminhão
```

```typescript
interface Veiculo {
  entregar(): string;
}

class Caminhao implements Veiculo {
  entregar(): string {
    return "Entrega por caminhão";
  }
}

class Navio implements Veiculo {
  entregar(): string {
    return "Entrega por navio";
  }
}

abstract class Logistica {
  abstract criarVeiculo(): Veiculo;

  planejarEntrega(): string {
    const veiculo = this.criarVeiculo();
    return `Planejando: ${veiculo.entregar()}`;
  }
}

class LogisticaTerrestre extends Logistica {
  criarVeiculo(): Veiculo {
    return new Caminhao();
  }
}
```

### 1.3 Abstract Factory

Fornece uma interface para criar **famílias de objetos** relacionados sem especificar suas classes concretas.

```python
from abc import ABC, abstractmethod

# Produtos abstratos
class Botao(ABC):
    @abstractmethod
    def renderizar(self) -> str: ...

class Checkbox(ABC):
    @abstractmethod
    def renderizar(self) -> str: ...

# Produtos concretos Windows
class BotaoWindows(Botao):
    def renderizar(self) -> str:
        return "Botão estilo Windows"

class CheckboxWindows(Checkbox):
    def renderizar(self) -> str:
        return "Checkbox estilo Windows"

# Produtos concretos Mac
class BotaoMac(Botao):
    def renderizar(self) -> str:
        return "Botão estilo Mac"

class CheckboxMac(Checkbox):
    def renderizar(self) -> str:
        return "Checkbox estilo Mac"

# Abstract Factory
class FabricaGUI(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao: ...

    @abstractmethod
    def criar_checkbox(self) -> Checkbox: ...

class FabricaWindows(FabricaGUI):
    def criar_botao(self) -> Botao:
        return BotaoWindows()
    def criar_checkbox(self) -> Checkbox:
        return CheckboxWindows()

class FabricaMac(FabricaGUI):
    def criar_botao(self) -> Botao:
        return BotaoMac()
    def criar_checkbox(self) -> Checkbox:
        return CheckboxMac()

# Uso
def criar_interface(fabrica: FabricaGUI) -> str:
    botao = fabrica.criar_botao()
    checkbox = fabrica.criar_checkbox()
    return f"{botao.renderizar()} + {checkbox.renderizar()}"

print(criar_interface(FabricaWindows()))  # Botão estilo Windows + Checkbox estilo Windows
```

```typescript
interface Botao {
  renderizar(): string;
}

interface Checkbox {
  renderizar(): string;
}

class BotaoWindows implements Botao {
  renderizar(): string {
    return "Botão estilo Windows";
  }
}

class CheckboxWindows implements Checkbox {
  renderizar(): string {
    return "Checkbox estilo Windows";
  }
}

class BotaoMac implements Botao {
  renderizar(): string {
    return "Botão estilo Mac";
  }
}

class CheckboxMac implements Checkbox {
  renderizar(): string {
    return "Checkbox estilo Mac";
  }
}

interface FabricaGUI {
  criarBotao(): Botao;
  criarCheckbox(): Checkbox;
}

class FabricaWindows implements FabricaGUI {
  criarBotao(): Botao { return new BotaoWindows(); }
  criarCheckbox(): Checkbox { return new CheckboxWindows(); }
}

class FabricaMac implements FabricaGUI {
  criarBotao(): Botao { return new BotaoMac(); }
  criarCheckbox(): Checkbox { return new CheckboxMac(); }
}
```

### 1.4 Builder

Separa a construção de um objeto complexo de sua representação, permitindo o mesmo processo de construção criar diferentes representações.

```python
class Pizza:
    def __init__(self):
        self._massa: str = ""
        self._molho: str = ""
        self._coberturas: list[str] = []

    def __str__(self) -> str:
        return f"Pizza {self._massa}, {self._molho}, coberturas: {', '.join(self._coberturas)}"

class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza()

    def reset(self) -> None:
        self._pizza = Pizza()

    def com_massa(self, tipo: str) -> "PizzaBuilder":
        self._pizza._massa = tipo
        return self

    def com_molho(self, tipo: str) -> "PizzaBuilder":
        self._pizza._molho = tipo
        return self

    def adicionar_cobertura(self, cobertura: str) -> "PizzaBuilder":
        self._pizza._coberturas.append(cobertura)
        return self

    def build(self) -> Pizza:
        pizza = self._pizza
        self.reset()
        return pizza

# Uso (fluent interface)
builder = PizzaBuilder()
pizza = (
    builder
    .com_massa("fina")
    .com_molho("tomate")
    .adicionar_cobertura("queijo")
    .adicionar_cobertura("calabresa")
    .build()
)
print(pizza)  # Pizza fina, tomate, coberturas: queijo, calabresa
```

```typescript
class Pizza {
  massa = "";
  molho = "";
  coberturas: string[] = [];

  toString(): string {
    return `Pizza ${this.massa}, ${this.molho}, coberturas: ${this.coberturas.join(", ")}`;
  }
}

class PizzaBuilder {
  private pizza = new Pizza();

  reset(): void {
    this.pizza = new Pizza();
  }

  comMassa(tipo: string): this {
    this.pizza.massa = tipo;
    return this;
  }

  comMolho(tipo: string): this {
    this.pizza.molho = tipo;
    return this;
  }

  adicionarCobertura(cobertura: string): this {
    this.pizza.coberturas.push(cobertura);
    return this;
  }

  build(): Pizza {
    const pizza = this.pizza;
    this.reset();
    return pizza;
  }
}

const builder = new PizzaBuilder();
const pizza = builder
  .comMassa("fina")
  .comMolho("tomate")
  .adicionarCobertura("queijo")
  .adicionarCobertura("calabresa")
  .build();
```

### 1.5 Prototype

Permite criar novos objetos **copiando** um protótipo existente, em vez de instanciar uma classe.

```python
import copy
from dataclasses import dataclass

@dataclass
class Endereco:
    rua: str
    numero: str

@dataclass
class Documento:
    titulo: str
    conteudo: str
    autor: str
    endereco: Endereco

    def clonar(self) -> "Documento":
        return copy.deepcopy(self)

# Uso
original = Documento("Relatório", "Conteúdo...", "João", Endereco("Rua A", "123"))
copia = original.clonar()
copia.titulo = "Relatório Modificado"
copia.endereco.numero = "456"

print(original.titulo)  # Relatório
print(original.endereco.numero)  # 123 (deep copy garante independência)
```

```typescript
interface Prototype<T> {
  clone(): T;
}

class Endereco {
  constructor(public rua: string, public numero: string) {}
}

class Documento implements Prototype<Documento> {
  constructor(
    public titulo: string,
    public conteudo: string,
    public autor: string,
    public endereco: Endereco,
  ) {}

  clone(): Documento {
    return new Documento(
      this.titulo,
      this.conteudo,
      this.autor,
      new Endereco(this.endereco.rua, this.endereco.numero),
    );
  }
}

const original = new Documento("Relatório", "Conteúdo...", "João", new Endereco("Rua A", "123"));
const copia = original.clone();
copia.titulo = "Relatório Modificado";
```

---

## 2. Padrões Estruturais (Structural)

Padrões que lidam com a **composição de classes e objetos** para formar estruturas maiores.

### 2.1 Adapter

Permite que interfaces incompatíveis trabalhem juntas. Converte a interface de uma classe para outra interface esperada pelo cliente.

```python
# Interface esperada pelo sistema
class TomadaEuropeia:
    def conectar(self, voltagem: int) -> str:
        return f"Conectado em {voltagem}V (europeu)"

# Interface existente (incompatível)
class TomadaAmericana:
    def plugar(self, voltagem: int) -> str:
        return f"Plugado em {voltagem}V (americano)"

# Adapter
class AdaptadorAmericanoParaEuropeu(TomadaEuropeia):
    def __init__(self, tomada_americana: TomadaAmericana):
        self._tomada = tomada_americana

    def conectar(self, voltagem: int) -> str:
        return self._tomada.plugar(voltagem)

# Uso
adaptador = AdaptadorAmericanoParaEuropeu(TomadaAmericana())
print(adaptador.conectar(110))  # Plugado em 110V (americano)
```

```typescript
interface TomadaEuropeia {
  conectar(voltagem: number): string;
}

class TomadaAmericana {
  plugar(voltagem: number): string {
    return `Plugado em ${voltagem}V (americano)`;
  }
}

class AdaptadorAmericanoParaEuropeu implements TomadaEuropeia {
  constructor(private tomada: TomadaAmericana) {}

  conectar(voltagem: number): string {
    return this.tomada.plugar(voltagem);
  }
}
```

### 2.2 Bridge

Separa uma abstração de sua implementação, permitindo que ambas variem independentemente.

```python
from abc import ABC, abstractmethod

# Implementação
class Dispositivo(ABC):
    @abstractmethod
    def ligar(self) -> str: ...
    @abstractmethod
    def desligar(self) -> str: ...

class Televisao(Dispositivo):
    def ligar(self) -> str:
        return "TV ligada"
    def desligar(self) -> str:
        return "TV desligada"

class Radio(Dispositivo):
    def ligar(self) -> str:
        return "Rádio ligado"
    def desligar(self) -> str:
        return "Rádio desligado"

# Abstração
class ControleRemoto:
    def __init__(self, dispositivo: Dispositivo):
        self._dispositivo = dispositivo

    def ligar(self) -> str:
        return self._dispositivo.ligar()

    def desligar(self) -> str:
        return self._dispositivo.desligar()

class ControleRemotoAvancado(ControleRemoto):
    def mute(self) -> str:
        return f"Mute no {self._dispositivo.__class__.__name__}"

# Uso
tv = Televisao()
controle = ControleRemotoAvancado(tv)
print(controle.ligar())   # TV ligada
print(controle.mute())    # Mute na Televisao
```

```typescript
interface Dispositivo {
  ligar(): string;
  desligar(): string;
}

class Televisao implements Dispositivo {
  ligar(): string { return "TV ligada"; }
  desligar(): string { return "TV desligada"; }
}

class Radio implements Dispositivo {
  ligar(): string { return "Rádio ligado"; }
  desligar(): string { return "Rádio desligado"; }
}

class ControleRemoto {
  constructor(protected dispositivo: Dispositivo) {}

  ligar(): string { return this.dispositivo.ligar(); }
  desligar(): string { return this.dispositivo.desligar(); }
}

class ControleRemotoAvancado extends ControleRemoto {
  mute(): string {
    return `Mute no ${this.dispositivo.constructor.name}`;
  }
}
```

### 2.3 Composite

Compõe objetos em estruturas de árvore para representar hierarquias **parte-todo**. Permite tratar objetos individuais e composições de maneira uniforme.

```python
from abc import ABC, abstractmethod

class Componente(ABC):
    @abstractmethod
    def get_preco(self) -> float: ...

class Produto(Componente):
    def __init__(self, nome: str, preco: float):
        self._nome = nome
        self._preco = preco

    def get_preco(self) -> float:
        return self._preco

class Caixa(Componente):
    def __init__(self, nome: str):
        self._nome = nome
        self._itens: list[Componente] = []

    def adicionar(self, item: Componente) -> None:
        self._itens.append(item)

    def remover(self, item: Componente) -> None:
        self._itens.remove(item)

    def get_preco(self) -> float:
        return sum(item.get_preco() for item in self._itens)

# Uso
mouse = Produto("Mouse", 50.0)
teclado = Produto("Teclado", 150.0)
monitor = Produto("Monitor", 800.0)

caixa_perifericos = Caixa("Periféricos")
caixa_perifericos.adicionar(mouse)
caixa_perifericos.adicionar(teclado)

caixa_computador = Caixa("Computador")
caixa_computador.adicionar(monitor)
caixa_computador.adicionar(caixa_perifericos)

print(caixa_computador.get_preco())  # 1000.0
```

```typescript
interface Componente {
  getPreco(): number;
}

class Produto implements Componente {
  constructor(private nome: string, private preco: number) {}

  getPreco(): number {
    return this.preco;
  }
}

class Caixa implements Componente {
  private itens: Componente[] = [];

  constructor(private nome: string) {}

  adicionar(item: Componente): void {
    this.itens.push(item);
  }

  getPreco(): number {
    return this.itens.reduce((acc, item) => acc + item.getPreco(), 0);
  }
}

const mouse = new Produto("Mouse", 50);
const caixa = new Caixa("Kit");
caixa.adicionar(mouse);
console.log(caixa.getPreco()); // 50
```

### 2.4 Decorator

Anexa responsabilidades adicionais a um objeto dinamicamente. Fornece uma alternativa flexível à herança para extensão de funcionalidade.

```python
from abc import ABC, abstractmethod

class Cafe(ABC):
    @abstractmethod
    def custo(self) -> float: ...
    @abstractmethod
    def descricao(self) -> str: ...

class CafeSimples(Cafe):
    def custo(self) -> float:
        return 5.0
    def descricao(self) -> str:
        return "Café simples"

class DecoradorCafe(Cafe):
    def __init__(self, cafe: Cafe):
        self._cafe = cafe

    def custo(self) -> float:
        return self._cafe.custo()

    def descricao(self) -> str:
        return self._cafe.descricao()

class Leite(DecoradorCafe):
    def custo(self) -> float:
        return super().custo() + 2.0
    def descricao(self) -> str:
        return super().descricao() + " + leite"

class Chocolate(DecoradorCafe):
    def custo(self) -> float:
        return super().custo() + 3.0
    def descricao(self) -> str:
        return super().descricao() + " + chocolate"

# Uso
cafe = CafeSimples()
cafe = Leite(cafe)
cafe = Chocolate(cafe)
print(f"{cafe.descricao()}: R${cafe.custo():.2f}")
# Café simples + leite + chocolate: R$10.00
```

```typescript
interface Cafe {
  custo(): number;
  descricao(): string;
}

class CafeSimples implements Cafe {
  custo(): number { return 5; }
  descricao(): string { return "Café simples"; }
}

class Leite implements Cafe {
  constructor(private cafe: Cafe) {}

  custo(): number { return this.cafe.custo() + 2; }
  descricao(): string { return this.cafe.descricao() + " + leite"; }
}

class Chocolate implements Cafe {
  constructor(private cafe: Cafe) {}

  custo(): number { return this.cafe.custo() + 3; }
  descricao(): string { return this.cafe.descricao() + " + chocolate"; }
}

let cafe: Cafe = new CafeSimples();
cafe = new Leite(cafe);
cafe = new Chocolate(cafe);
console.log(`${cafe.descricao()}: R$${cafe.custo()}`);
```

### 2.5 Facade

Fornece uma interface **simplificada** para um subsistema complexo.

```python
class SubsistemaVideo:
    def carregar_arquivo(self, nome: str) -> str:
        return f"Vídeo {nome} carregado"
    def decodificar(self) -> str:
        return "Vídeo decodificado"

class SubsistemaAudio:
    def carregar_audio(self, nome: str) -> str:
        return f"Áudio {nome} carregado"
    def sincronizar(self) -> str:
        return "Áudio sincronizado"

class SubsistemaLegendas:
    def carregar_legendas(self, idioma: str) -> str:
        return f"Legendas em {idioma} carregadas"

class PlayerFacade:
    def __init__(self):
        self._video = SubsistemaVideo()
        self._audio = SubsistemaAudio()
        self._legendas = SubsistemaLegendas()

    def reproduzir(self, arquivo: str, idioma: str = "pt-BR") -> str:
        steps = [
            self._video.carregar_arquivo(arquivo),
            self._audio.carregar_audio(arquivo),
            self._video.decodificar(),
            self._audio.sincronizar(),
            self._legendas.carregar_legendas(idioma),
        ]
        return " | ".join(steps)

player = PlayerFacade()
print(player.reproduzir("filme.mp4"))
```

```typescript
class PlayerFacade {
  private video = new SubsistemaVideo();
  private audio = new SubsistemaAudio();
  private legendas = new SubsistemaLegendas();

  reproduzir(arquivo: string, idioma = "pt-BR"): string {
    return [
      this.video.carregarArquivo(arquivo),
      this.audio.carregarAudio(arquivo),
      this.video.decodificar(),
      this.audio.sincronizar(),
      this.legendas.carregarLegendas(idioma),
    ].join(" | ");
  }
}
```

### 2.6 Proxy

Fornece um **substituto** ou **placeholder** para outro objeto, controlando o acesso a ele.

```python
from abc import ABC, abstractmethod

class Video(ABC):
    @abstractmethod
    def assistir(self) -> str: ...

class VideoReal(Video):
    def __init__(self, url: str):
        self._url = url
        self._carregar()

    def _carregar(self) -> None:
        print(f"Carregando vídeo de {self._url}...")

    def assistir(self) -> str:
        return f"Reproduzindo {self._url}"

class ProxyVideo(Video):
    def __init__(self, url: str):
        self._url = url
        self._video_real: VideoReal | None = None

    def assistir(self) -> str:
        if not self._video_real:
            self._video_real = VideoReal(self._url)
        return self._video_real.assistir()

# Uso: o vídeo só é carregado quando assistido
video = ProxyVideo("https://exemplo.com/video.mp4")
print("Proxy criado, vídeo ainda não carregado")
print(video.assistir())
```

```typescript
interface Video {
  assistir(): string;
}

class VideoReal implements Video {
  constructor(private url: string) {
    this.carregar();
  }

  private carregar(): void {
    console.log(`Carregando vídeo de ${this.url}...`);
  }

  assistir(): string {
    return `Reproduzindo ${this.url}`;
  }
}

class ProxyVideo implements Video {
  private videoReal: VideoReal | null = null;

  constructor(private url: string) {}

  assistir(): string {
    if (!this.videoReal) {
      this.videoReal = new VideoReal(this.url);
    }
    return this.videoReal.assistir();
  }
}
```

---

## 3. Padrões Comportamentais (Behavioral)

Padrões que lidam com **comunicação e responsabilidade** entre objetos.

### 3.1 Strategy

Define uma família de algoritmos, encapsula cada um e os torna intercambiáveis. O algoritmo pode variar independentemente dos clientes que o usam.

```python
from abc import ABC, abstractmethod

class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular(self, peso: float) -> float: ...

class FreteSedex(EstrategiaFrete):
    def calcular(self, peso: float) -> float:
        return peso * 1.5 + 10

class FretePAC(EstrategiaFrete):
    def calcular(self, peso: float) -> float:
        return peso * 1.0 + 5

class FreteInternacional(EstrategiaFrete):
    def calcular(self, peso: float) -> float:
        return peso * 3.0 + 50

class CalculadoraFrete:
    def __init__(self, estrategia: EstrategiaFrete):
        self._estrategia = estrategia

    def definir_estrategia(self, estrategia: EstrategiaFrete) -> None:
        self._estrategia = estrategia

    def calcular(self, peso: float) -> float:
        return self._estrategia.calcular(peso)

# Uso
calc = CalculadoraFrete(FretePAC())
print(calc.calcular(5.0))  # 10.0

calc.definir_estrategia(FreteSedex())
print(calc.calcular(5.0))  # 17.5
```

```typescript
interface EstrategiaFrete {
  calcular(peso: number): number;
}

class FreteSedex implements EstrategiaFrete {
  calcular(peso: number): number {
    return peso * 1.5 + 10;
  }
}

class FretePAC implements EstrategiaFrete {
  calcular(peso: number): number {
    return peso * 1.0 + 5;
  }
}

class CalculadoraFrete {
  constructor(private estrategia: EstrategiaFrete) {}

  definirEstrategia(estrategia: EstrategiaFrete): void {
    this.estrategia = estrategia;
  }

  calcular(peso: number): number {
    return this.estrategia.calcular(peso);
  }
}
```

### 3.2 Observer

Define uma dependência **um-para-muitos** entre objetos, de modo que quando um objeto muda de estado, todos os dependentes são notificados.

```python
from typing import Protocol

class Observador(Protocol):
    def atualizar(self, mensagem: str) -> None: ...

class Publicador:
    def __init__(self):
        self._observadores: list[Observador] = []

    def inscrever(self, observador: Observador) -> None:
        self._observadores.append(observador)

    def desinscrever(self, observador: Observador) -> None:
        self._observadores.remove(observador)

    def notificar(self, mensagem: str) -> None:
        for obs in self._observadores:
            obs.atualizar(mensagem)

class EmailService:
    def atualizar(self, mensagem: str) -> None:
        print(f"[Email] Notificação enviada: {mensagem}")

class LogService:
    def atualizar(self, mensagem: str) -> None:
        print(f"[Log] Evento registrado: {mensagem}")

# Uso
publicador = Publicador()
publicador.inscrever(EmailService())
publicador.inscrever(LogService())
publicador.notificar("Pedido #123 confirmado")
```

```typescript
interface Observador {
  atualizar(mensagem: string): void;
}

class Publicador {
  private observadores: Observador[] = [];

  inscrever(obs: Observador): void {
    this.observadores.push(obs);
  }

  desinscrever(obs: Observador): void {
    this.observadores = this.observadores.filter(o => o !== obs);
  }

  notificar(mensagem: string): void {
    for (const obs of this.observadores) {
      obs.atualizar(mensagem);
    }
  }
}

class EmailService implements Observador {
  atualizar(mensagem: string): void {
    console.log(`[Email] Notificação enviada: ${mensagem}`);
  }
}
```

### 3.3 Command

Encapsula uma solicitação como um **objeto**, permitindo parametrizar clientes com filas, requisições e operações de desfazer.

```python
from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def executar(self) -> str: ...
    @abstractmethod
    def desfazer(self) -> str: ...

class Luz:
    def ligar(self) -> str:
        return "Luz ligada"
    def desligar(self) -> str:
        return "Luz desligada"

class ComandoLigarLuz(Comando):
    def __init__(self, luz: Luz):
        self._luz = luz
    def executar(self) -> str:
        return self._luz.ligar()
    def desfazer(self) -> str:
        return self._luz.desligar()

class ComandoDesligarLuz(Comando):
    def __init__(self, luz: Luz):
        self._luz = luz
    def executar(self) -> str:
        return self._luz.desligar()
    def desfazer(self) -> str:
        return self._luz.ligar()

class ControleRemoto:
    def __init__(self):
        self._historico: list[Comando] = []

    def executar(self, comando: Comando) -> str:
        resultado = comando.executar()
        self._historico.append(comando)
        return resultado

    def desfazer(self) -> str:
        if self._historico:
            comando = self._historico.pop()
            return comando.desfazer()
        return "Nada para desfazer"

luz = Luz()
controle = ControleRemoto()
print(controle.executar(ComandoLigarLuz(luz)))    # Luz ligada
print(controle.desfazer())                         # Luz desligada
```

```typescript
interface Comando {
  executar(): string;
  desfazer(): string;
}

class Luz {
  ligar(): string { return "Luz ligada"; }
  desligar(): string { return "Luz desligada"; }
}

class ComandoLigarLuz implements Comando {
  constructor(private luz: Luz) {}
  executar(): string { return this.luz.ligar(); }
  desfazer(): string { return this.luz.desligar(); }
}

class ControleRemoto {
  private historico: Comando[] = [];

  executar(comando: Comando): string {
    const resultado = comando.executar();
    this.historico.push(comando);
    return resultado;
  }

  desfazer(): string {
    const comando = this.historico.pop();
    return comando ? comando.desfazer() : "Nada para desfazer";
  }
}
```

### 3.4 Template Method

Define o **esqueleto** de um algoritmo em uma operação, transferindo alguns passos para subclasses.

```python
from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def preparar(self) -> list[str]:
        return [
            self.ferver_agua(),
            self.adicionar_ingrediente(),
            self.despejar_no_copo(),
            self.adicionar_complementos(),
        ]

    def ferver_agua(self) -> str:
        return "Água fervida"

    def despejar_no_copo(self) -> str:
        return "Bebida despejada no copo"

    @abstractmethod
    def adicionar_ingrediente(self) -> str: ...

    @abstractmethod
    def adicionar_complementos(self) -> str: ...

class Cafe(BebidaQuente):
    def adicionar_ingrediente(self) -> str:
        return "Café solúvel adicionado"
    def adicionar_complementos(self) -> str:
        return "Açúcar adicionado"

class Cha(BebidaQuente):
    def adicionar_ingrediente(self) -> str:
        return "Saquinho de chá adicionado"
    def adicionar_complementos(self) -> str:
        return "Limão adicionado"

# Uso
cafe = Cafe()
print(cafe.preparar())
# Água fervida, Café solúvel adicionado, Bebida despejada no copo, Açúcar adicionado
```

```typescript
abstract class BebidaQuente {
  preparar(): string[] {
    return [
      this.ferverAgua(),
      this.adicionarIngrediente(),
      this.despejarNoCopo(),
      this.adicionarComplementos(),
    ];
  }

  ferverAgua(): string { return "Água fervida"; }
  despejarNoCopo(): string { return "Bebida despejada no copo"; }

  abstract adicionarIngrediente(): string;
  abstract adicionarComplementos(): string;
}

class Cafe extends BebidaQuente {
  adicionarIngrediente(): string { return "Café solúvel adicionado"; }
  adicionarComplementos(): string { return "Açúcar adicionado"; }
}
```

### 3.5 Iterator

Fornece uma maneira de **acessar sequencialmente** os elementos de um objeto agregado sem expor sua representação subjacente.

```python
class ListaInvertida:
    def __init__(self, itens: list):
        self._itens = itens

    def __iter__(self):
        return _IteradorListaInvertida(self._itens)

class _IteradorListaInvertida:
    def __init__(self, itens: list):
        self._itens = itens
        self._indice = len(itens) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._indice < 0:
            raise StopIteration
        valor = self._itens[self._indice]
        self._indice -= 1
        return valor

lista = ListaInvertida([1, 2, 3, 4])
print(list(item for item in lista))  # [4, 3, 2, 1]
```

```typescript
class ListaInvertida<T> implements Iterable<T> {
  constructor(private itens: T[]) {}

  [Symbol.iterator](): Iterator<T> {
    let indice = this.itens.length - 1;
    return {
      next: (): IteratorResult<T> => {
        if (indice < 0) return { done: true, value: undefined as any };
        return { done: false, value: this.itens[indice--] };
      },
    };
  }
}

const lista = new ListaInvertida([1, 2, 3, 4]);
console.log([...lista]); // [4, 3, 2, 1]
```

### 3.6 State

Permite que um objeto altere seu comportamento quando seu estado interno muda. Parece que o objeto mudou de classe.

```python
from abc import ABC, abstractmethod

class EstadoMaquina(ABC):
    @abstractmethod
    def inserir_moeda(self, maquina: "MaquinaVenda") -> str: ...
    @abstractmethod
    def selecionar_produto(self, maquina: "MaquinaVenda") -> str: ...
    @abstractmethod
    def entregar(self, maquina: "MaquinaVenda") -> str: ...

class EstadoAguardando(EstadoMaquina):
    def inserir_moeda(self, maquina: "MaquinaVenda") -> str:
        maquina.estado = EstadoComMoeda()
        return "Moeda inserida"
    def selecionar_produto(self, maquina: "MaquinaVenda") -> str:
        return "Insira uma moeda primeiro"
    def entregar(self, maquina: "MaquinaVenda") -> str:
        return "Nada para entregar"

class EstadoComMoeda(EstadoMaquina):
    def inserir_moeda(self, maquina: "MaquinaVenda") -> str:
        return "Moeda já inserida"
    def selecionar_produto(self, maquina: "MaquinaVenda") -> str:
        maquina.estado = EstadoEntregando()
        return "Produto selecionado"
    def entregar(self, maquina: "MaquinaVenda") -> str:
        return "Selecione um produto primeiro"

class EstadoEntregando(EstadoMaquina):
    def inserir_moeda(self, maquina: "MaquinaVenda") -> str:
        return "Aguarde, entregando produto"
    def selecionar_produto(self, maquina: "MaquinaVenda") -> str:
        return "Já selecionado, aguarde"
    def entregar(self, maquina: "MaquinaVenda") -> str:
        maquina.estado = EstadoAguardando()
        return "Produto entregue"

class MaquinaVenda:
    def __init__(self):
        self.estado: EstadoMaquina = EstadoAguardando()

    def inserir_moeda(self) -> str:
        return self.estado.inserir_moeda(self)
    def selecionar_produto(self) -> str:
        return self.estado.selecionar_produto(self)
    def entregar(self) -> str:
        return self.estado.entregar(self)

maquina = MaquinaVenda()
print(maquina.selecionar_produto())  # Insira uma moeda primeiro
print(maquina.inserir_moeda())       # Moeda inserida
print(maquina.selecionar_produto())  # Produto selecionado
print(maquina.entregar())            # Produto entregue
```

```typescript
interface EstadoMaquina {
  inserirMoeda(maq: MaquinaVenda): string;
  selecionarProduto(maq: MaquinaVenda): string;
  entregar(maq: MaquinaVenda): string;
}

class EstadoAguardando implements EstadoMaquina {
  inserirMoeda(maq: MaquinaVenda): string {
    maq.estado = new EstadoComMoeda();
    return "Moeda inserida";
  }
  selecionarProduto(_maq: MaquinaVenda): string {
    return "Insira uma moeda primeiro";
  }
  entregar(_maq: MaquinaVenda): string {
    return "Nada para entregar";
  }
}

class EstadoComMoeda implements EstadoMaquina {
  inserirMoeda(_maq: MaquinaVenda): string { return "Moeda já inserida"; }
  selecionarProduto(maq: MaquinaVenda): string {
    maq.estado = new EstadoEntregando();
    return "Produto selecionado";
  }
  entregar(_maq: MaquinaVenda): string { return "Selecione um produto primeiro"; }
}

class EstadoEntregando implements EstadoMaquina {
  inserirMoeda(_maq: MaquinaVenda): string { return "Aguarde, entregando"; }
  selecionarProduto(_maq: MaquinaVenda): string { return "Já selecionado"; }
  entregar(maq: MaquinaVenda): string {
    maq.estado = new EstadoAguardando();
    return "Produto entregue";
  }
}

class MaquinaVenda {
  estado: EstadoMaquina = new EstadoAguardando();

  inserirMoeda(): string { return this.estado.inserirMoeda(this); }
  selecionarProduto(): string { return this.estado.selecionarProduto(this); }
  entregar(): string { return this.estado.entregar(this); }
}
```

### 3.7 Chain of Responsibility

Permite que mais de um objeto trate uma solicitação, encadeando os objetos receptores e passando a solicitação ao longo da cadeia.

```python
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self):
        self._proximo: Handler | None = None

    def definir_proximo(self, handler: "Handler") -> "Handler":
        self._proximo = handler
        return handler

    @abstractmethod
    def tratar(self, requisicao: str) -> str | None: ...

class HandlerAutenticacao(Handler):
    def tratar(self, requisicao: str) -> str | None:
        if requisicao == "autenticado":
            return self._proximo.tratar(requisicao) if self._proximo else None
        return "Falha na autenticação"

class HandlerPermissao(Handler):
    def tratar(self, requisicao: str) -> str | None:
        if requisicao == "admin":
            return self._proximo.tratar(requisicao) if self._proximo else None
        return "Sem permissão"

class HandlerCache(Handler):
    def tratar(self, requisicao: str) -> str | None:
        return f"Dados em cache para {requisicao}"

# Montagem da cadeia
handler = HandlerAutenticacao()
handler.definir_proximo(HandlerPermissao()).definir_proximo(HandlerCache())

print(handler.tratar("autenticado"))  # Dados em cache para autenticado
print(handler.tratar("anonimo"))      # Falha na autenticação
```

```typescript
abstract class Handler {
  protected proximo: Handler | null = null;

  definirProximo(handler: Handler): Handler {
    this.proximo = handler;
    return handler;
  }

  abstract tratar(requisicao: string): string | null;
}

class HandlerAutenticacao extends Handler {
  tratar(requisicao: string): string | null {
    if (requisicao === "autenticado") {
      return this.proximo?.tratar(requisicao) ?? null;
    }
    return "Falha na autenticação";
  }
}

class HandlerPermissao extends Handler {
  tratar(requisicao: string): string | null {
    if (requisicao === "admin") {
      return this.proximo?.tratar(requisicao) ?? null;
    }
    return "Sem permissão";
  }
}

class HandlerCache extends Handler {
  tratar(requisicao: string): string | null {
    return `Dados em cache para ${requisicao}`;
  }
}
```

---

## 4. Padrões de Arquitetura Empresarial (Enterprise Patterns)

**Referência:** Fowler, Martin. *Patterns of Enterprise Application Architecture*. Addison-Wesley, 2002.

### 4.1 Repository

Media entre o domínio e a camada de dados, oferecendo uma interface similar a coleções para acesso a objetos de domínio.

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Usuario:
    id: str
    nome: str
    email: str

class RepositorioUsuarios(ABC):
    @abstractmethod
    def buscar_por_id(self, id: str) -> Usuario | None: ...
    @abstractmethod
    def buscar_todos(self) -> list[Usuario]: ...
    @abstractmethod
    def salvar(self, usuario: Usuario) -> None: ...
    @abstractmethod
    def remover(self, id: str) -> None: ...

class RepositorioUsuariosMemoria(RepositorioUsuarios):
    def __init__(self):
        self._dados: dict[str, Usuario] = {}

    def buscar_por_id(self, id: str) -> Usuario | None:
        return self._dados.get(id)

    def buscar_todos(self) -> list[Usuario]:
        return list(self._dados.values())

    def salvar(self, usuario: Usuario) -> None:
        self._dados[usuario.id] = usuario

    def remover(self, id: str) -> None:
        self._dados.pop(id, None)
```

```typescript
interface Usuario {
  id: string;
  nome: string;
  email: string;
}

interface RepositorioUsuarios {
  buscarPorId(id: string): Promise<Usuario | null>;
  buscarTodos(): Promise<Usuario[]>;
  salvar(usuario: Usuario): Promise<void>;
  remover(id: string): Promise<void>;
}

class RepositorioUsuariosMemoria implements RepositorioUsuarios {
  private dados = new Map<string, Usuario>();

  async buscarPorId(id: string): Promise<Usuario | null> {
    return this.dados.get(id) ?? null;
  }

  async buscarTodos(): Promise<Usuario[]> {
    return Array.from(this.dados.values());
  }

  async salvar(usuario: Usuario): Promise<void> {
    this.dados.set(usuario.id, usuario);
  }

  async remover(id: string): Promise<void> {
    this.dados.delete(id);
  }
}
```

### 4.2 Unit of Work

Mantém uma lista de objetos afetados por uma transação e coordena a escrita das mudanças, resolvendo problemas de concorrência.

```python
from dataclasses import dataclass, field
from enum import Enum

class Estado(Enum):
    NOVO = 1
    MODIFICADO = 2
    REMOVIDO = 3

@dataclass
class Entidade:
    id: str
    dados: dict

class UnitOfWork:
    def __init__(self):
        self._novos: dict[str, Entidade] = {}
        self._modificados: dict[str, Entidade] = {}
        self._removidos: dict[str, Entidade] = {}

    def registrar_novo(self, entidade: Entidade) -> None:
        self._novos[entidade.id] = entidade

    def registrar_modificado(self, entidade: Entidade) -> None:
        self._modificados[entidade.id] = entidade

    def registrar_removido(self, entidade: Entidade) -> None:
        self._removidos[entidade.id] = entidade

    def commit(self) -> None:
        for entidade in self._novos.values():
            print(f"INSERT: {entidade}")
        for entidade in self._modificados.values():
            print(f"UPDATE: {entidade}")
        for entidade in self._removidos.values():
            print(f"DELETE: {entidade}")
        self._limpar()

    def _limpar(self) -> None:
        self._novos.clear()
        self._modificados.clear()
        self._removidos.clear()

uow = UnitOfWork()
uow.registrar_novo(Entidade("1", {"nome": "João"}))
uow.registrar_modificado(Entidade("2", {"nome": "Maria"}))
uow.commit()
```

```typescript
type Estado = "novo" | "modificado" | "removido";

interface Entidade {
  id: string;
  dados: Record<string, unknown>;
}

class UnitOfWork {
  private novos = new Map<string, Entidade>();
  private modificados = new Map<string, Entidade>();
  private removidos = new Map<string, Entidade>();

  registrarNovo(e: Entidade): void { this.novos.set(e.id, e); }
  registrarModificado(e: Entidade): void { this.modificados.set(e.id, e); }
  registrarRemovido(e: Entidade): void { this.removidos.set(e.id, e); }

  commit(): void {
    for (const e of this.novos.values()) console.log(`INSERT: ${JSON.stringify(e)}`);
    for (const e of this.modificados.values()) console.log(`UPDATE: ${JSON.stringify(e)}`);
    for (const e of this.removidos.values()) console.log(`DELETE: ${JSON.stringify(e)}`);
    this.novos.clear();
    this.modificados.clear();
    this.removidos.clear();
  }
}
```

---

## 5. Padrões Modernos

### 5.1 Dependency Injection

Injeção de dependências em vez de criá-las internamente. Fundamental para testabilidade e baixo acoplamento.

```python
from typing import Protocol

class ServicoEmail(Protocol):
    def enviar(self, para: str, mensagem: str) -> None: ...

class ServicoEmailSMTP:
    def enviar(self, para: str, mensagem: str) -> None:
        print(f"Enviando email para {para} via SMTP")

class ServicoEmailMock:
    def enviar(self, para: str, mensagem: str) -> None:
        print(f"[MOCK] Email para {para}: {mensagem}")

class Notificador:
    def __init__(self, email: ServicoEmail):
        self._email = email  # Injetado

    def notificar_usuario(self, usuario_id: str, msg: str) -> None:
        self._email.enviar(f"usuario{usuario_id}@email.com", msg)

# Produção
notificador = Notificador(ServicoEmailSMTP())
# Teste
notificador_teste = Notificador(ServicoEmailMock())
```

```typescript
interface ServicoEmail {
  enviar(para: string, mensagem: string): void;
}

class ServicoEmailSMTP implements ServicoEmail {
  enviar(para: string, mensagem: string): void {
    console.log(`Enviando email para ${para} via SMTP`);
  }
}

class ServicoEmailMock implements ServicoEmail {
  enviar(para: string, mensagem: string): void {
    console.log(`[MOCK] Email para ${para}: ${mensagem}`);
  }
}

class Notificador {
  constructor(private readonly email: ServicoEmail) {}

  notificarUsuario(usuarioId: string, msg: string): void {
    this.email.enviar(`usuario${usuarioId}@email.com`, msg);
  }
}
```

### 5.2 Middleware (Pipeline)

Encadeia funções em um pipeline onde cada função processa a requisição e opcionalmente passa para a próxima.

```python
from typing import Callable

Request = dict
MiddlewareFn = Callable[[Request, Callable], str]

class MiddlewarePipeline:
    def __init__(self):
        self._middlewares: list[MiddlewareFn] = []

    def usar(self, middleware: MiddlewareFn) -> None:
        self._middlewares.append(middleware)

    def executar(self, request: Request) -> str:
        def wrap(idx: int) -> Callable[[], str]:
            def next_middleware() -> str:
                if idx < len(self._middlewares):
                    return self._middlewares[idx](request, wrap(idx + 1))
                return "Fim do pipeline"
            return next_middleware
        return wrap(0)()

pipeline = MiddlewarePipeline()
pipeline.usar(lambda req, next: f"Auth({next()})")
pipeline.usar(lambda req, next: f"Log({next()})")
pipeline.usar(lambda req, next: f"Handler({req.get('path', '/')})")

print(pipeline.executar({"path": "/api/users"}))
# Auth(Log(Handler(/api/users)))
```

```typescript
type Request = Record<string, unknown>;
type MiddlewareFn = (req: Request, next: () => string) => string;

class MiddlewarePipeline {
  private middlewares: MiddlewareFn[] = [];

  usar(middleware: MiddlewareFn): void {
    this.middlewares.push(middleware);
  }

  executar(request: Request): string {
    const wrap = (idx: number): (() => string) => {
      return () => {
        if (idx < this.middlewares.length) {
          return this.middlewares[idx](request, wrap(idx + 1));
        }
        return "Fim do pipeline";
      };
    };
    return wrap(0)();
  }
}

const pipeline = new MiddlewarePipeline();
pipeline.usar((req, next) => `Auth(${next()})`);
pipeline.usar((req, next) => `Log(${next()})`);
pipeline.usar((req, _next) => `Handler(${req.path ?? "/"})`);

console.log(pipeline.executar({ path: "/api/users" }));
```

### 5.3 Circuit Breaker

Previne que um sistema tente repetidamente uma operação que provavelmente vai falhar, permitindo recuperação.

```python
import time
from enum import Enum

class CircuitState(Enum):
    FECHADO = "fechado"
    ABERTO = "aberto"
    SEMI_ABERTO = "semi_aberto"

class CircuitBreaker:
    def __init__(self, threshold: int = 3, timeout: float = 30.0):
        self._state = CircuitState.FECHADO
        self._failure_count = 0
        self._threshold = threshold
        self._timeout = timeout
        self._last_failure_time: float = 0

    def call(self, fn, *args, **kwargs):
        if self._state == CircuitState.ABERTO:
            if time.time() - self._last_failure_time > self._timeout:
                self._state = CircuitState.SEMI_ABERTO
            else:
                raise Exception("Circuit breaker aberto")

        try:
            result = fn(*args, **kwargs)
            if self._state == CircuitState.SEMI_ABERTO:
                self._state = CircuitState.FECHADO
                self._failure_count = 0
            return result
        except Exception as e:
            self._failure_count += 1
            self._last_failure_time = time.time()
            if self._failure_count >= self._threshold:
                self._state = CircuitState.ABERTO
            raise e

def servico_instavel(x: int) -> int:
    if x < 0:
        raise ValueError("Erro simulado")
    return x * 2

cb = CircuitBreaker(threshold=2, timeout=1)
for i in [1, -1, -1, 3]:
    try:
        print(cb.call(servico_instavel, i))
    except Exception as e:
        print(f"Erro: {e}")
```

```typescript
type CircuitState = "fechado" | "aberto" | "semi_aberto";

class CircuitBreaker {
  private state: CircuitState = "fechado";
  private failureCount = 0;
  private lastFailureTime = 0;

  constructor(
    private threshold = 3,
    private timeout = 30000,
  ) {}

  async call<T>(fn: () => Promise<T>): Promise<T> {
    if (this.state === "aberto") {
      if (Date.now() - this.lastFailureTime > this.timeout) {
        this.state = "semi_aberto";
      } else {
        throw new Error("Circuit breaker aberto");
      }
    }

    try {
      const result = await fn();
      if (this.state === "semi_aberto") {
        this.state = "fechado";
        this.failureCount = 0;
      }
      return result;
    } catch (error) {
      this.failureCount++;
      this.lastFailureTime = Date.now();
      if (this.failureCount >= this.threshold) {
        this.state = "aberto";
      }
      throw error;
    }
  }
}
```

---

## 6. Anti-Patterns Comuns

| Anti-Pattern | Descrição | Solução |
|---|---|---|
| **God Class** | Classe que faz tudo | SRP, decomposição |
| **Spaghetti Code** | Código sem estrutura, goto-like | Refatoração, padrões |
| **Golden Hammer** | Usar o mesmo pattern pra tudo | Avaliar contexto |
| **Copy & Paste** | Duplicação de código | Extrair para função |
| **Lava Flow** | Código morto nunca removido | Limpeza periódica |
| **Boat Anchor** | Código/framework não utilizado | Remover |
| **Cargo Cult** | Usar pattern sem entender por que | Estudar trade-offs |
| **Premature Optimization** | Otimizar antes de medir | Medir primeiro |
| **Singleton Overuse** | Abusar de singletons | DI e fábricas |
| **Yo-Yo Problem** | Herança excessiva e profunda | Composição |

---

## 7. Referências Bibliográficas

- Gamma, E.; Helm, R.; Johnson, R.; Vlissides, J. *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley, 1994.
- Fowler, M. *Patterns of Enterprise Application Architecture*. Addison-Wesley, 2002.
- Martin, R. C. *Agile Software Development, Principles, Patterns, and Practices*. Prentice Hall, 2002.
- Freeman, E.; Freeman, E. *Head First Design Patterns*. O'Reilly, 2004.
- Evans, E. *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Addison-Wesley, 2003.
- Nystrom, R. *Game Programming Patterns*. Genever Benning, 2014.
- Shvets, A. *Dive Into Design Patterns*. Refactoring.Guru, 2019.
- Bloch, J. *Effective Java* (3rd ed.). Addison-Wesley, 2018.

## Ver Também

- [[04-Conhecimentos/02-Engenharia-de-Software/Arquitetura-de-Software]]
- [[04-Conhecimentos/02-Engenharia-de-Software/Paradigmas-de-Programacao]]
- [[04-Conhecimentos/02-Engenharia-de-Software/APIs-e-Integracoes]]
