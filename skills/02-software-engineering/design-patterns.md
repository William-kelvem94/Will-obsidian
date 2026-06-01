---
tags: [design-patterns, software-engineering, GoF, architecture, coding-agent, skills-eng]
updated: 2026-06-01
title: "Design Patterns - GoF Catalog"
date: 2026-06-01
---

# Design Patterns - Catalogo GoF

Catalogo completo dos 23 padroes de projeto GoF (Gang of Four) com implementacoes em Python e TypeScript.

## Sumario

- [[#Padroes Criacionais]]
- [[#Padroes Estruturais]]
- [[#Padroes Comportamentais]]

---

## Padroes Criacionais

Padroes criacionais abstraem o processo de instanciacao de objetos, tornando um sistema independente de como seus objetos sao criados, compostos e representados.

### Singleton

**Intento:** Garantir que uma classe tenha apenas uma instancia e fornecer um ponto de acesso global a ela.

**Problema que resolve:** Quando exatamente uma instancia e necessaria para coordenar acoes em todo o sistema (ex: conexao com banco de dados, logger, cache).

**Analogia:** Um unico gerente de banco que atende todos os clientes -- nao faz sentido ter dois gerentes com chaves diferentes do cofre.

```ascii
+------------------+
|    Singleton     |
+------------------+
| - instance       |
+------------------+
| + getInstance()  |
| - Singleton()    |
+------------------+
         |
         v
   [Unica Instancia]
```

**Python -- Thread-safe:**

```python
import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'connected'):
            self.connected = True
            print("Conectado ao banco de dados")

    def query(self, sql: str) -> list:
        return [{"result": f"Executando: {sql}"}]

# Uso
db1 = DatabaseConnection()
db2 = DatabaseConnection()
assert db1 is db2  # Mesma instancia
```

**TypeScript -- Thread-safe (single-threaded guarantee):**

```typescript
class DatabaseConnection {
  private static instance: DatabaseConnection | null = null;
  private connected: boolean = false;

  private constructor() {
    this.connected = true;
    console.log("Conectado ao banco de dados");
  }

  static getInstance(): DatabaseConnection {
    if (!DatabaseConnection.instance) {
      DatabaseConnection.instance = new DatabaseConnection();
    }
    return DatabaseConnection.instance;
  }

  query(sql: string): Array<{ result: string }> {
    return [{ result: `Executando: ${sql}` }];
  }
}

// Uso
const db1 = DatabaseConnection.getInstance();
const db2 = DatabaseConnection.getInstance();
console.assert(db1 === db2); // Mesma instancia
```

**Quando usar:** Logging, cache, pool de conexoes, configuracao global.
**Quando NAO usar:** Quando a instancia pode variar por contexto (use Factory), ou em testes onde isolamento e necessario.
**Padroes relacionados:** [[#Factory Method]], [[#Facade]]

---

### Factory Method

**Intento:** Definir uma interface para criar um objeto, mas deixar que as subclasses decidam qual classe instanciar.

**Problema que resolve:** Desacopla a criacao de objetos do codigo cliente, permitindo extensao sem modificacao (OCP).

**Analogia:** Uma franquia de restaurantes -- cada filial cria seu cardapio local seguindo o mesmo processo padrao.

```ascii
+----------------+       +------------------+
|   Creator      |       | ConcreteCreator  |
+----------------+       +------------------+
| + factoryMethod|       | + factoryMethod()|
| + operation()  |       +------------------+
+----------------+                 |
        |                          v
        |               +----------------------+
        |               | ConcreteProduct      |
        +-------------->+----------------------+
                        | + operation()        |
                        +----------------------+
```

**Python:**

```python
from abc import ABC, abstractmethod

class Notificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem: str) -> None:
        pass

class EmailNotificacao(Notificacao):
    def enviar(self, mensagem: str) -> None:
        print(f"Email: {mensagem}")

class SMSNotificacao(Notificacao):
    def enviar(self, mensagem: str) -> None:
        print(f"SMS: {mensagem}")

class PushNotificacao(Notificacao):
    def enviar(self, mensagem: str) -> None:
        print(f"Push: {mensagem}")

class NotificadorFactory(ABC):
    @abstractmethod
    def criar_notificacao(self) -> Notificacao:
        pass

    def notificar(self, mensagem: str) -> None:
        notificacao = self.criar_notificacao()
        notificacao.enviar(mensagem)

class EmailFactory(NotificadorFactory):
    def criar_notificacao(self) -> Notificacao:
        return EmailNotificacao()

class SMSFactory(NotificadorFactory):
    def criar_notificacao(self) -> Notificacao:
        return SMSNotificacao()

# Uso
factory: NotificadorFactory = EmailFactory()
factory.notificar("Pedido confirmado!")  # Email: Pedido confirmado!
```

**TypeScript:**

```typescript
interface Notificacao {
  enviar(mensagem: string): void;
}

class EmailNotificacao implements Notificacao {
  enviar(mensagem: string): void {
    console.log(`Email: ${mensagem}`);
  }
}

class SMSNotificacao implements Notificacao {
  enviar(mensagem: string): void {
    console.log(`SMS: ${mensagem}`);
  }
}

abstract class NotificadorFactory {
  abstract criarNotificacao(): Notificacao;

  notificar(mensagem: string): void {
    const notificacao = this.criarNotificacao();
    notificacao.enviar(mensagem);
  }
}

class EmailFactory extends NotificadorFactory {
  criarNotificacao(): Notificacao {
    return new EmailNotificacao();
  }
}

// Uso
const factory: NotificadorFactory = new EmailFactory();
factory.notificar("Pedido confirmado!");
```

**Quando usar:** Quando nao se sabe antecipadamente os tipos exatos de objetos, ou quando se quer permitir extensao.
**Quando NAO usar:** Quando ha poucos tipos e eles nao mudam -- criacao direta e mais simples.
**Padroes relacionados:** [[#Abstract Factory]], [[#Prototype]], [[#Template Method]]

---

### Abstract Factory

**Intento:** Fornecer uma interface para criar familias de objetos relacionados sem especificar suas classes concretas.

**Problema que resolve:** Garante compatibilidade entre produtos de uma mesma familia (ex: widgets de UI para plataformas diferentes).

**Analogia:** Uma fabrica de moveis que produz cozinhas completas -- todos os itens combinam entre si (moderno, classico, rustico).

```ascii
+-------------------------+
|    AbstractFactory      |
+-------------------------+
| + criarBotao(): Botao   |
| + criarMenu(): Menu     |
+-------------------------+
      |           |
      v           v
+-----------+ +-----------+
| WinFactory| | MacFactory|
+-----------+ +-----------+
```

**Python:**

```python
from abc import ABC, abstractmethod

class Botao(ABC):
    @abstractmethod
    def renderizar(self) -> str: ...

class Menu(ABC):
    @abstractmethod
    def renderizar(self) -> str: ...

class WinBotao(Botao):
    def renderizar(self) -> str: return "[Botao Windows]"

class MacBotao(Botao):
    def renderizar(self) -> str: return "[Botao macOS]"

class WinMenu(Menu):
    def renderizar(self) -> str: return "[Menu Windows]"

class MacMenu(Menu):
    def renderizar(self) -> str: return "[Menu macOS]"

class UIFactory(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao: ...
    @abstractmethod
    def criar_menu(self) -> Menu: ...

class WinFactory(UIFactory):
    def criar_botao(self) -> Botao: return WinBotao()
    def criar_menu(self) -> Menu: return WinMenu()

class MacFactory(UIFactory):
    def criar_botao(self) -> Botao: return MacBotao()
    def criar_menu(self) -> Menu: return MacMenu()

def app(factory: UIFactory) -> None:
    print(factory.criar_botao().renderizar())
    print(factory.criar_menu().renderizar())

app(MacFactory())  # [Botao macOS] [Menu macOS]
```

**TypeScript:**

```typescript
interface Botao { renderizar(): string; }
interface Menu { renderizar(): string; }

class WinBotao implements Botao {
  renderizar(): string { return "[Botao Windows]"; }
}
class MacBotao implements Botao {
  renderizar(): string { return "[Botao macOS]"; }
}

interface UIFactory {
  criarBotao(): Botao;
  criarMenu(): Menu;
}

class WinFactory implements UIFactory {
  criarBotao(): Botao { return new WinBotao(); }
  criarMenu(): Menu { return new WinMenu(); }
}
class WinMenu implements Menu {
  renderizar(): string { return "[Menu Windows]"; }
}

function app(factory: UIFactory): void {
  console.log(factory.criarBotao().renderizar());
  console.log(factory.criarMenu().renderizar());
}
```

**Quando usar:** Sistemas cross-platform, familias de produtos relacionados, quando se quer garantir compatibilidade.
**Quando NAO usar:** Quando se precisa de apenas um tipo de produto (use Factory Method).
**Padroes relacionados:** [[#Factory Method]], [[#Builder]]

---

### Builder

**Intento:** Separar a construcao de um objeto complexo da sua representacao, permitindo o mesmo processo criar diferentes representacoes.

**Problema que resolve:** Evita construtores telescoping com muitos parametros opcionais.

**Analogia:** Montar um computador -- o processo e o mesmo, mas as pecas variam (gamer, escritorio, servidor).

**Python:**

```python
class Computador:
    def __init__(self) -> None:
        self.cpu: str = ""
        self.ram: str = ""
        self.storage: str = ""
        self.gpu: str = ""

    def __str__(self) -> str:
        return f"CPU={self.cpu}, RAM={self.ram}, Storage={self.storage}, GPU={self.gpu}"

class ComputadorBuilder:
    def __init__(self) -> None:
        self._computador = Computador()

    def com_cpu(self, cpu: str) -> "ComputadorBuilder":
        self._computador.cpu = cpu
        return self

    def com_ram(self, ram: str) -> "ComputadorBuilder":
        self._computador.ram = ram
        return self

    def com_storage(self, storage: str) -> "ComputadorBuilder":
        self._computador.storage = storage
        return self

    def com_gpu(self, gpu: str) -> "ComputadorBuilder":
        self._computador.gpu = gpu
        return self

    def construir(self) -> Computador:
        return self._computador

# Uso
gamer = (ComputadorBuilder()
    .com_cpu("i9-13900K")
    .com_ram("64GB DDR5")
    .com_storage("2TB NVMe")
    .com_gpu("RTX 4090")
    .construir())
```

**TypeScript:**

```typescript
class Computador {
  constructor(
    public cpu: string = "",
    public ram: string = "",
    public storage: string = "",
    public gpu: string = ""
  ) {}
}

class ComputadorBuilder {
  private computador = new Computador();

  comCpu(cpu: string): this { this.computador.cpu = cpu; return this; }
  comRam(ram: string): this { this.computador.ram = ram; return this; }
  comStorage(storage: string): this { this.computador.storage = storage; return this; }
  comGpu(gpu: string): this { this.computador.gpu = gpu; return this; }

  construir(): Computador { return this.computador; }
}

const gamer = new ComputadorBuilder()
  .comCpu("i9-13900K")
  .comRam("64GB DDR5")
  .comStorage("2TB NVMe")
  .comGpu("RTX 4090")
  .construir();
```

**Quando usar:** Objetos com muitos parametros opcionais, construcao passo-a-passo, diferentes representacoes.
**Quando NAO usar:** Objetos simples com poucos atributos obrigatorios.
**Padroes relacionados:** [[#Factory Method]], [[#Abstract Factory]], [[#Composite]]

---

### Prototype

**Intento:** Criar novos objetos copiando uma instancia existente (clone), em vez de criar do zero.

**Problema que resolve:** Quando a criacao direta e custosa ou complexa, e mais eficiente copiar um objeto ja configurado.

**Analogia:** Clonacao de uma celula -- a copia e geneticamente identica mas independente.

```ascii
+------------------+       clone()      +------------------+
|    Prototype     | -----------------> |     Clone        |
+------------------+                    +------------------+
| - estado: dict   |                    | - estado: dict   |
| + clone()        |                    | + clone()        |
+------------------+                    +------------------+
```

**Python -- Deep vs Shallow Clone:**

```python
import copy
from abc import ABC, abstractmethod

class Documento(ABC):
    def __init__(self, titulo: str, conteudo: list[str]) -> None:
        self.titulo = titulo
        self.conteudo = conteudo

    @abstractmethod
    def clone(self) -> "Documento": ...

class Relatorio(Documento):
    def __init__(self, titulo: str, conteudo: list[str], dados: dict) -> None:
        super().__init__(titulo, conteudo)
        self.dados = dados

    def clone(self) -> "Relatorio":
        # Deep clone -- copia tudo recursivamente
        return Relatorio(
            titulo=self.titulo,
            conteudo=copy.deepcopy(self.conteudo),
            dados=copy.deepcopy(self.dados)
        )

    def shallow_clone(self) -> "Relatorio":
        # Shallow clone -- copia apenas referencias
        return Relatorio(
            titulo=self.titulo,
            conteudo=self.conteudo,
            dados=self.dados
        )

# Uso
original = Relatorio("Vendas", ["Jan", "Fev"], {"total": 1000})
copia = original.clone()
copia.dados["total"] = 2000
print(original.dados["total"])  # 1000 -- nao foi afetado
```

**TypeScript:**

```typescript
interface Prototype {
  clone(): Prototype;
}

class Relatorio implements Prototype {
  constructor(
    public titulo: string,
    public conteudo: string[],
    public dados: Record<string, number>
  ) {}

  clone(): Relatorio {
    return new Relatorio(
      this.titulo,
      [...this.conteudo],
      { ...this.dados }
    );
  }
}

const original = new Relatorio("Vendas", ["Jan", "Fev"], { total: 1000 });
const copia = original.clone();
copia.dados.total = 2000;
console.log(original.dados.total); // 1000
```

**Quando usar:** Objetos caros de criar, quando se precisa de snapshots, sistemas com muitas variacoes similares.
**Quando NAO usar:** Objetos simples, quando cada instancia precisa de configuracao unica desde o inicio.
**Padroes relacionados:** [[#Factory Method]], [[#Memento]] (nao GoF)

---

## Padroes Estruturais

Padroes estruturais tratam da composicao de classes e objetos para formar estruturas maiores e mais flexiveis.

### Adapter

**Intento:** Converter a interface de uma classe em outra interface esperada pelo cliente. Permite que classes com interfaces incompativeis trabalhem juntas.

**Problema que resolve:** Integracao com sistemas legados ou bibliotecas de terceiros sem modificar seu codigo.

**Analogia:** Adaptador de tomada -- permite que um plugue americano funcione em uma tomada brasileira.

```ascii
+----------+         +-----------------+         +-----------+
|  Target  | <------ |    Adapter      | ------> |  Adaptee  |
+----------+         +-----------------+         +-----------+
| request()|         | request()       |         | specific()|
+----------+         | - adaptee       |         +-----------+
                     +-----------------+
```

**Python:**

```python
from abc import ABC, abstractmethod

class PagamentoModerno(ABC):
    @abstractmethod
    def pagar(self, valor: float) -> bool: ...

class GatewayLegado:
    def processar_pagamento(self, amount: int, currency: str) -> dict:
        return {"status": "ok", "valor": amount, "moeda": currency}

class PagamentoAdapter(PagamentoModerno):
    def __init__(self, gateway: GatewayLegado) -> None:
        self._gateway = gateway

    def pagar(self, valor: float) -> bool:
        resultado = self._gateway.processar_pagamento(
            int(valor * 100), "BRL"
        )
        return resultado["status"] == "ok"

# Uso
gateway = GatewayLegado()
adaptador = PagamentoAdapter(gateway)
adaptador.pagar(99.90)  # True
```

**TypeScript:**

```typescript
interface PagamentoModerno {
  pagar(valor: number): boolean;
}

class GatewayLegado {
  processarPagamento(amount: number, currency: string): { status: string } {
    return { status: "ok" };
  }
}

class PagamentoAdapter implements PagamentoModerno {
  constructor(private gateway: GatewayLegado) {}

  pagar(valor: number): boolean {
    const resultado = this.gateway.processarPagamento(
      Math.round(valor * 100), "BRL"
    );
    return resultado.status === "ok";
  }
}

const gateway = new GatewayLegado();
const adaptador = new PagamentoAdapter(gateway);
adaptador.pagar(99.90);
```

**Quando usar:** Integracao com APIs de terceiros, sistemas legados, bibliotecas incompativeis.
**Quando NAO usar:** Quando se pode modificar o codigo original -- refatorar e melhor que adaptar.
**Padroes relacionados:** [[#Facade]], [[#Decorator]], [[#Proxy]]

---

### Decorator

**Intento:** Adicionar responsabilidades a um objeto dinamicamente, fornecendo uma alternativa flexivel a heranca.

**Problema que resolve:** Estender funcionalidades sem criar uma explosao de subclasses para cada combinacao.

**Analogia:** Roupa de inverno -- voce pode adicionar camadas (casaco, cachecol, luvas) conforme necessario.

```ascii
+----------------+
|   Component    |
+----------------+
| + operation()  |
+----------------+
       ^
       |
+------------------+        +------------------+
| ConcreteComponent|        |    Decorator     |
+------------------+        +------------------+
| + operation()    |        | - component      |
+------------------+        | + operation()    |
                            +------------------+
                                   ^
                                   |
                     +---------------------------+
                     | ConcreteDecoratorA/B      |
                     +---------------------------+
```

**Python:**

```python
from abc import ABC, abstractmethod
from functools import wraps

# Decorator pattern com classes
class Notificacao(ABC):
    @abstractmethod
    def enviar(self, mensagem: str) -> str: ...

class NotificacaoEmail(Notificacao):
    def enviar(self, mensagem: str) -> str:
        return f"Email: {mensagem}"

class NotificacaoDecorator(Notificacao):
    def __init__(self, notificacao: Notificacao) -> None:
        self._notificacao = notificacao

class NotificacaoSMS(NotificacaoDecorator):
    def enviar(self, mensagem: str) -> str:
        base = self._notificacao.enviar(mensagem)
        return f"{base} + SMS: {mensagem}"

class NotificacaoPush(NotificacaoDecorator):
    def enviar(self, mensagem: str) -> str:
        base = self._notificacao.enviar(mensagem)
        return f"{base} + Push: {mensagem}"

# Uso
n = NotificacaoPush(NotificacaoSMS(NotificacaoEmail()))
print(n.enviar("Alerta!"))
# Email: Alerta! + SMS: Alerta! + Push: Alerta!

# Decorator como funcao (Python nativo)
def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executando {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_execution
def processar_pedido(id: int) -> str:
    return f"Pedido {id} processado"
```

**TypeScript:**

```typescript
interface Notificacao {
  enviar(mensagem: string): string;
}

class NotificacaoEmail implements Notificacao {
  enviar(mensagem: string): string {
    return `Email: ${mensagem}`;
  }
}

abstract class NotificacaoDecorator implements Notificacao {
  constructor(protected notificacao: Notificacao) {}
  abstract enviar(mensagem: string): string;
}

class NotificacaoSMS extends NotificacaoDecorator {
  enviar(mensagem: string): string {
    const base = this.notificacao.enviar(mensagem);
    return `${base} + SMS: ${mensagem}`;
  }
}

class NotificacaoPush extends NotificacaoDecorator {
  enviar(mensagem: string): string {
    const base = this.notificacao.enviar(mensagem);
    return `${base} + Push: ${mensagem}`;
  }
}

// Uso
const n: Notificacao = new NotificacaoPush(
  new NotificacaoSMS(new NotificacaoEmail())
);
console.log(n.enviar("Alerta!"));

// Decorator como decorator de classe (TypeScript)
function LogExecution(target: any, key: string, descriptor: PropertyDescriptor) {
  const original = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`[LOG] Executando ${key}`);
    return original.apply(this, args);
  };
}

class ServicoPedido {
  @LogExecution
  processar(id: number): string {
    return `Pedido ${id} processado`;
  }
}
```

**Quando usar:** Middleware, logging, caching, validacao, compressao, criptografia.
**Quando NAO usar:** Quando a funcionalidade e fixa e nao precisa ser combinada -- heranca simples basta.
**Padroes relacionados:** [[#Adapter]], [[#Proxy]], [[#Composite]], [[#Strategy]]

---

### Facade

**Intento:** Fornecer uma interface unificada e simplificada para um conjunto de interfaces em um subsistema.

**Problema que resolve:** Reduz a complexidade de interagir com sistemas complexos, fornecendo uma API de alto nivel.

**Analogia:** O painel de um carro -- voce usa volante, pedais e alavanca, sem precisar entender motor, transmissao e freios.

```ascii
Cliente --> [ Facade ] --> Subsystem A
                          --> Subsystem B
                          --> Subsystem C
```

**Python:**

```python
class Motor:
    def ligar(self) -> str: return "Motor ligado"
    def desligar(self) -> str: return "Motor desligado"

class Transmissao:
    def engatar_marcha(self, marcha: int) -> str: return f"Marcha {marcha}"

class Freios:
    def aplicar(self, intensidade: float) -> str: return f"Freio {intensidade}%"

class CarroFacade:
    def __init__(self) -> None:
        self._motor = Motor()
        self._transmissao = Transmissao()
        self._freios = Freios()

    def dirigir(self) -> list[str]:
        return [
            self._motor.ligar(),
            self._transmissao.engatar_marcha(1),
            self._freios.aplicar(0.0),
        ]

    def estacionar(self) -> list[str]:
        return [
            self._freios.aplicar(1.0),
            self._transmissao.engatar_marcha(0),
            self._motor.desligar(),
        ]

# Uso
carro = CarroFacade()
print(carro.dirigir())
```

**TypeScript:**

```typescript
class Motor {
  ligar(): string { return "Motor ligado"; }
  desligar(): string { return "Motor desligado"; }
}

class Transmissao {
  engatarMarcha(marcha: number): string { return `Marcha ${marcha}`; }
}

class Freios {
  aplicar(intensidade: number): string { return `Freio ${intensidade}%`; }
}

class CarroFacade {
  private motor = new Motor();
  private transmissao = new Transmissao();
  private freios = new Freios();

  dirigir(): string[] {
    return [
      this.motor.ligar(),
      this.transmissao.engatarMarcha(1),
      this.freios.aplicar(0),
    ];
  }

  estacionar(): string[] {
    return [
      this.freios.aplicar(1),
      this.transmissao.engatarMarcha(0),
      this.motor.desligar(),
    ];
  }
}

const carro = new CarroFacade();
console.log(carro.dirigir());
```

**Quando usar:** Simplificar APIs complexas, camadas de abstracao, bibliotecas com muitas dependencias.
**Quando NAO usar:** Quando o cliente precisa de controle fino sobre o subsistema.
**Padroes relacionados:** [[#Singleton]], [[#Adapter]], [[#Mediator]] (nao GoF)

---

### Composite

**Intento:** Compor objetos em estruturas de arvore para representar hierarquias parte-todo. Permite tratar objetos individuais e composicoes de forma uniforme.

**Problema que resolve:** Trabalhar com estruturas hierarquicas (arvores) de forma polimorfica.

**Analogia:** Sistema de arquivos -- pastas e arquivos sao tratados de forma similar (listar, deletar, mover).

```ascii
+------------------+
|    Component     |
+------------------+
| + operacao()     |
| + adicionar()    |
| + remover()      |
+------------------+
      /       \
     v         v
+--------+ +----------+
| Leaf   | | Composite|
+--------+ +----------+
|op()    | |op()      |
+--------+ |add()/rem()|
           +----------+
                |
                v
         [Componentes filhos]
```

**Python:**

```python
from abc import ABC, abstractmethod

class FileSystem(ABC):
    def __init__(self, nome: str) -> None:
        self.nome = nome

    @abstractmethod
    def listar(self, indent: int = 0) -> str: ...

class Arquivo(FileSystem):
    def __init__(self, nome: str, tamanho: int) -> None:
        super().__init__(nome)
        self.tamanho = tamanho

    def listar(self, indent: int = 0) -> str:
        return f"{'  ' * indent}- {self.nome} ({self.tamanho} bytes)"

class Pasta(FileSystem):
    def __init__(self, nome: str) -> None:
        super().__init__(nome)
        self._filhos: list[FileSystem] = []

    def adicionar(self, item: FileSystem) -> None:
        self._filhos.append(item)

    def remover(self, item: FileSystem) -> None:
        self._filhos.remove(item)

    def listar(self, indent: int = 0) -> str:
        linhas = [f"{'  ' * indent}+ {self.nome}/"]
        for filho in self._filhos:
            linhas.append(filho.listar(indent + 1))
        return "\n".join(linhas)

# Uso
raiz = Pasta("projeto")
raiz.adicionar(Arquivo("main.py", 1024))
src = Pasta("src")
src.adicionar(Arquivo("app.py", 2048))
raiz.adicionar(src)
print(raiz.listar())
```

**TypeScript:**

```typescript
abstract class FileSystem {
  constructor(protected nome: string) {}
  abstract listar(indent?: number): string;
}

class Arquivo extends FileSystem {
  constructor(nome: string, private tamanho: number) {
    super(nome);
  }
  listar(indent = 0): string {
    return `${"  ".repeat(indent)}- ${this.nome} (${this.tamanho} bytes)`;
  }
}

class Pasta extends FileSystem {
  private filhos: FileSystem[] = [];

  adicionar(item: FileSystem): void { this.filhos.push(item); }
  remover(item: FileSystem): void {
    this.filhos = this.filhos.filter(f => f !== item);
  }

  listar(indent = 0): string {
    const linhas = [`${"  ".repeat(indent)}+ ${this.nome}/`];
    for (const filho of this.filhos) {
      linhas.push(filho.listar(indent + 1));
    }
    return linhas.join("\n");
  }
}

const raiz = new Pasta("projeto");
raiz.adicionar(new Arquivo("main.py", 1024));
const src = new Pasta("src");
src.adicionar(new Arquivo("app.py", 2048));
raiz.adicionar(src);
console.log(raiz.listar());
```

**Quando usar:** Sistemas de arquivos, menus hierarquicos, organizacoes, expressoes matematicas.
**Quando NAO usar:** Quando nao ha hierarquia parte-todo, ou quando folhas e compostos tem comportamentos muito diferentes.
**Padroes relacionados:** [[#Decorator]], [[#Iterator]], [[#Visitor]] (nao GoF)

---

### Proxy

**Intento:** Fornecer um substituto ou placeholder para outro objeto, controlando o acesso a ele.

**Problema que resolve:** Adicionar controle de acesso, lazy loading, caching ou logging sem modificar o objeto real.

**Analogia:** Um seguranca de balada -- ele decide quem pode entrar, sem alterar o funcionamento da balada.

```ascii
+----------------+         +----------------+         +----------------+
|    Subject     | <------ |     Proxy      | ------> |  RealSubject   |
+----------------+         +----------------+         +----------------+
| + request()    |         | - realSubject  |         | + request()    |
+----------------+         | + request()    |         +----------------+
                           | - checkAccess()|
                           | - logAccess()  |
                           +----------------+
```

**Python:**

```python
from abc import ABC, abstractmethod
import time

class Documento(ABC):
    @abstractmethod
    def carregar(self) -> str: ...
    @abstractmethod
    def exibir(self) -> str: ...

class DocumentoReal(Documento):
    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._carregar()

    def _carregar(self) -> None:
        print(f"Carregando {self._nome}...")
        time.sleep(1)  # Simula operacao custosa
        self._conteudo = f"Conteudo de {self._nome}"

    def carregar(self) -> str:
        return self._conteudo

    def exibir(self) -> str:
        return self._conteudo

class DocumentoProxy(Documento):
    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._real: DocumentoReal | None = None

    def carregar(self) -> str:
        if self._real is None:
            self._real = DocumentoReal(self._nome)
        return self._real.carregar()

    def exibir(self) -> str:
        return self.carregar()

# Uso -- Lazy Loading
proxy = DocumentoProxy("relatorio.pdf")
print("Proxy criado, documento ainda nao carregado")
print(proxy.exibir())  # So agora carrega
```

**TypeScript:**

```typescript
interface Documento {
  carregar(): string;
  exibir(): string;
}

class DocumentoReal implements Documento {
  private conteudo: string = "";

  constructor(private nome: string) {
    this.carregar();
  }

  carregar(): string {
    console.log(`Carregando ${this.nome}...`);
    this.conteudo = `Conteudo de ${this.nome}`;
    return this.conteudo;
  }

  exibir(): string {
    return this.carregar();
  }
}

class DocumentoProxy implements Documento {
  private real: DocumentoReal | null = null;

  constructor(private nome: string) {}

  carregar(): string {
    if (!this.real) {
      this.real = new DocumentoReal(this.nome);
    }
    return this.real.carregar();
  }

  exibir(): string {
    return this.carregar();
  }
}

// Proxy de acesso (controle)
class DocumentoProtegido implements Documento {
  constructor(
    private real: Documento,
    private usuario: string
  ) {}

  carregar(): string {
    if (this.usuario === "admin") return this.real.carregar();
    throw new Error("Acesso negado");
  }

  exibir(): string {
    return this.carregar();
  }
}

// Proxy de cache
class DocumentoCache implements Documento {
  private cache: string | null = null;

  constructor(private real: Documento) {}

  carregar(): string {
    if (!this.cache) {
      this.cache = this.real.carregar();
    }
    return this.cache;
  }

  exibir(): string {
    return this.carregar();
  }
}
```

**Quando usar:** Lazy loading, controle de acesso, caching, logging remoto, virtualizacao.
**Quando NAO usar:** Quando o objeto real e leve e nao precisa de controle adicional.
**Padroes relacionados:** [[#Adapter]], [[#Decorator]], [[#Facade]]

---

## Padroes Comportamentais

Padroes comportamentais tratam da comunicacao entre objetos e da distribuicao de responsabilidades.

### Observer

**Intento:** Definir uma dependencia um-para-muitos entre objetos, de forma que quando um objeto muda de estado, todos os seus dependentes sao notificados.

**Problema que resolve:** Desacoplar o sujeito dos observadores, permitindo notificacao automatica de eventos.

**Analogia:** Assinatura de revista -- quando uma nova edicao e publicada, todos os assinantes recebem automaticamente.

```ascii
+----------------+     1      +----------------+
|    Subject     |---------->|   Observer     |
+----------------+            +----------------+
| + attach()     |            | + update()     |
| + detach()     |            +----------------+
| + notify()     |                    ^
+----------------+                    |
        |                      +------------------+
        |                      | ConcreteObserver |
        v                      +------------------+
+------------------+
| ConcreteSubject  |
+------------------+
| - state          |
+------------------+
```

**Python:**

```python
from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def atualizar(self, evento: str, dados: dict) -> None: ...

class Sujeto:
    def __init__(self) -> None:
        self._observadores: list[Observador] = []

    def adicionar(self, obs: Observador) -> None:
        self._observadores.append(obs)

    def remover(self, obs: Observador) -> None:
        self._observadores.remove(obs)

    def notificar(self, evento: str, dados: dict) -> None:
        for obs in self._observadores:
            obs.atualizar(evento, dados)

class Pedido(Sujeto):
    def __init__(self, id: int) -> None:
        super().__init__()
        self.id = id
        self.status = "criado"

    def mudar_status(self, novo_status: str) -> None:
        self.status = novo_status
        self.notificar("status_mudou", {"id": self.id, "status": self.status})

class NotificadorEmail(Observador):
    def atualizar(self, evento: str, dados: dict) -> None:
        if evento == "status_mudou":
            print(f"Email: Pedido {dados['id']} -> {dados['status']}")

class NotificadorSMS(Observador):
    def atualizar(self, evento: str, dados: dict) -> None:
        if evento == "status_mudou":
            print(f"SMS: Pedido {dados['id']} -> {dados['status']}")

# Uso
pedido = Pedido(123)
pedido.adicionar(NotificadorEmail())
pedido.adicionar(NotificadorSMS())
pedido.mudar_status("pago")
pedido.mudar_status("enviado")
```

**TypeScript:**

```typescript
interface Observador {
  atualizar(evento: string, dados: Record<string, any>): void;
}

class Sujeto {
  private observadores: Observador[] = [];

  adicionar(obs: Observador): void { this.observadores.push(obs); }
  remover(obs: Observador): void {
    this.observadores = this.observadores.filter(o => o !== obs);
  }
  notificar(evento: string, dados: Record<string, any>): void {
    for (const obs of this.observadores) {
      obs.atualizar(evento, dados);
    }
  }
}

class Pedido extends Sujeto {
  status: string = "criado";

  constructor(public id: number) { super(); }

  mudarStatus(novoStatus: string): void {
    this.status = novoStatus;
    this.notificar("status_mudou", { id: this.id, status: this.status });
  }
}

class NotificadorEmail implements Observador {
  atualizar(evento: string, dados: Record<string, any>): void {
    if (evento === "status_mudou") {
      console.log(`Email: Pedido ${dados.id} -> ${dados.status}`);
    }
  }
}

// Uso
const pedido = new Pedido(123);
pedido.adicionar(new NotificadorEmail());
pedido.mudarStatus("pago");
```

**Quando usar:** Sistemas de eventos, pub/sub, reatividade, MVC, atualizacao de UI.
**Quando NAO usar:** Quando a ordem de notificacao importa, ou quando ha poucos observadores fixos.
**Padroes relacionados:** [[#Mediator]] (nao GoF), [[#Strategy]], [[#Command]]

---

### Strategy

**Intento:** Definir uma familia de algoritmos, encapsular cada um e torna-los intercambiaveis. Permite variar o algoritmo independentemente dos clientes que o utilizam.

**Problema que resolve:** Eliminar condicionais complexos (if/else, switch) trocando algoritmos em tempo de execucao.

**Analogia:** Rotas de viagem -- voce pode ir de carro, onibus ou aviao. O destino e o mesmo, a estrategia muda.

```ascii
+----------------+        +------------------+
|   Context      |------->|    Strategy      |
+----------------+        +------------------+
| - strategy     |        | + executar()     |
| + executar()   |        +------------------+
+----------------+                ^
                    +-------------+-------------+
                    |             |             |
              +-----------+ +-----------+ +-----------+
              | StrategyA | | StrategyB | | StrategyC |
              +-----------+ +-----------+ +-----------+
```

**Python:**

```python
from abc import ABC, abstractmethod

class EstrategiaPagamento(ABC):
    @abstractmethod
    def processar(self, valor: float) -> str: ...

class PagamentoCartao(EstrategiaPagamento):
    def __init__(self, numero: str, cvv: str) -> None:
        self.numero = numero
        self.cvv = cvv

    def processar(self, valor: float) -> str:
        return f"Cartao {self.numero[-4:]}: R$ {valor:.2f}"

class PagamentoPix(EstrategiaPagamento):
    def __init__(self, chave: str) -> None:
        self.chave = chave

    def processar(self, valor: float) -> str:
        return f"Pix ({self.chave}): R$ {valor:.2f}"

class PagamentoBoleto(EstrategiaPagamento):
    def processar(self, valor: float) -> str:
        return f"Boleto: R$ {valor:.2f} (3 dias para compensar)"

class Checkout:
    def __init__(self, estrategia: EstrategiaPagamento) -> None:
        self._estrategia = estrategia

    def definir_estrategia(self, estrategia: EstrategiaPagamento) -> None:
        self._estrategia = estrategia

    def finalizar(self, valor: float) -> str:
        return self._estrategia.processar(valor)

# Uso
checkout = Checkout(PagamentoPix("email@teste.com"))
print(checkout.finalizar(99.90))
checkout.definir_estrategia(PagamentoCartao("1234567812345678", "123"))
print(checkout.finalizar(149.90))
```

**TypeScript:**

```typescript
interface EstrategiaPagamento {
  processar(valor: number): string;
}

class PagamentoCartao implements EstrategiaPagamento {
  constructor(private numero: string, private cvv: string) {}
  processar(valor: number): string {
    return `Cartao ${this.numero.slice(-4)}: R$ ${valor.toFixed(2)}`;
  }
}

class PagamentoPix implements EstrategiaPagamento {
  constructor(private chave: string) {}
  processar(valor: number): string {
    return `Pix (${this.chave}): R$ ${valor.toFixed(2)}`;
  }
}

class PagamentoBoleto implements EstrategiaPagamento {
  processar(valor: number): string {
    return `Boleto: R$ ${valor.toFixed(2)}`;
  }
}

class Checkout {
  constructor(private estrategia: EstrategiaPagamento) {}

  definirEstrategia(estrategia: EstrategiaPagamento): void {
    this.estrategia = estrategia;
  }

  finalizar(valor: number): string {
    return this.estrategia.processar(valor);
  }
}

const checkout = new Checkout(new PagamentoPix("email@teste.com"));
console.log(checkout.finalizar(99.90));
checkout.definirEstrategia(new PagamentoCartao("1234567812345678", "123"));
console.log(checkout.finalizar(149.90));
```

**Quando usar:** Algoritmos intercambiaveis, evitar condicionais complexas, variacoes em tempo de execucao.
**Quando NAO usar:** Quando o algoritmo nunca muda -- uma implementacao direta basta.
**Padroes relacionados:** [[#State]], [[#Command]], [[#Decorator]]

---

### Command

**Intento:** Encapsular uma solicitacao como um objeto, permitindo parametrizar clientes com diferentes solicitacoes, enfileirar ou registrar solicitacoes e suportar operacoes desfazer/refazer.

**Problema que resolve:** Desacoplar o objeto que invoca a operacao do objeto que sabe executa-la.

**Analogia:** Pedido em restaurante -- o garcom (invoker) leva o pedido (command) ao chef (receiver), sem saber cozinhar.

```ascii
+----------+     execute()    +----------+     acao()    +----------+
| Invoker  | ---------------> | Command  | ------------> | Receiver |
+----------+                  +----------+                 +----------+
| + queue()  |                  | + execute()  |            | + acao()  |
| + undo()   |                  | + undo()     |            +----------+
+----------+                  +----------+
                                   ^
                                   |
                          +-----------------+
                          | ConcreteCommand |
                          +-----------------+
```

**Python:**

```python
from abc import ABC, abstractmethod

class Comando(ABC):
    @abstractmethod
    def executar(self) -> str: ...
    @abstractmethod
    def desfazer(self) -> str: ...

class Luz:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.ligada = False

    def ligar(self) -> str:
        self.ligada = True
        return f"{self.nome} ligada"

    def desligar(self) -> str:
        self.ligada = False
        return f"{self.nome} desligada"

class LigarLuz(Comando):
    def __init__(self, luz: Luz) -> None:
        self._luz = luz

    def executar(self) -> str:
        return self._luz.ligar()

    def desfazer(self) -> str:
        return self._luz.desligar()

class ControleRemoto:
    def __init__(self) -> None:
        self._historico: list[Comando] = []

    def executar(self, comando: Comando) -> str:
        resultado = comando.executar()
        self._historico.append(comando)
        return resultado

    def desfazer(self) -> str:
        if self._historico:
            return self._historico.pop().desfazer()
        return "Nada para desfazer"

# Uso
luz_sala = Luz("Sala")
controle = ControleRemoto()
print(controle.executar(LigarLuz(luz_sala)))  # Sala ligada
print(controle.desfazer())                     # Sala desligada
```

**TypeScript:**

```typescript
interface Comando {
  executar(): string;
  desfazer(): string;
}

class Luz {
  ligada = false;
  constructor(public nome: string) {}
  ligar(): string { this.ligada = true; return `${this.nome} ligada`; }
  desligar(): string { this.ligada = false; return `${this.nome} desligada`; }
}

class LigarLuz implements Comando {
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
    if (this.historico.length === 0) return "Nada para desfazer";
    return this.historico.pop()!.desfazer();
  }
}

const luzSala = new Luz("Sala");
const controle = new ControleRemoto();
console.log(controle.executar(new LigarLuz(luzSala)));
console.log(controle.desfazer());
```

**Quando usar:** Undo/redo, filas de tarefas, macros, logging de operacoes, transacoes.
**Quando NAO usar:** Quando nao ha necessidade de desfazer ou enfileirar operacoes.
**Padroes relacionados:** [[#Memento]] (nao GoF), [[#Observer]], [[#Strategy]]

---

### Template Method

**Intento:** Definir o esqueleto de um algoritmo em uma operacao, adiando alguns passos para subclasses. Permite que subclasses redefinam certos passos sem mudar a estrutura do algoritmo.

**Problema que resolve:** Eliminar duplicacao de codigo quando algoritmos similares compartilham estrutura.

**Analogia:** Receita de bolo -- a estrutura e fixa (misturar, assar, decorar), mas os ingredientes variam.

```ascii
+------------------------+
|    AbstractClass       |
+------------------------+
| + templateMethod()     |
|   - passo1()           |
|   - passo2()           |
|   - passo3() [abstract]|
|   - gancho() [virtual] |
+------------------------+
          ^
          |
    +------------------+
    |  ConcreteClass   |
    +------------------+
    | + passo3()       |
    | + gancho()       |
    +------------------+
```

**Python:**

```python
from abc import ABC, abstractmethod

class ProcessadorDados(ABC):
    def processar(self, caminho: str) -> None:
        """Template Method -- estrutura fixa"""
        dados = self._ler(caminho)
        dados = self._transformar(dados)
        self._salvar(dados)
        if self._deve_logar():
            self._log("Processamento concluido")

    def _ler(self, caminho: str) -> list[dict]:
        print(f"Lendo {caminho}")
        return [{"id": 1, "valor": 100}]

    @abstractmethod
    def _transformar(self, dados: list[dict]) -> list[dict]: ...

    def _salvar(self, dados: list[dict]) -> None:
        print(f"Salvando {len(dados)} registros")

    def _deve_logar(self) -> bool:
        return True  # Gancho padrao

    def _log(self, msg: str) -> None:
        print(f"[LOG] {msg}")

class ProcessadorCSV(ProcessadorDados):
    def _transformar(self, dados: list[dict]) -> list[dict]:
        print("Transformando CSV...")
        return [{**d, "formato": "csv"} for d in dados]

class ProcessadorJSON(ProcessadorDados):
    def _transformar(self, dados: list[dict]) -> list[dict]:
        print("Transformando JSON...")
        return [{**d, "formato": "json"} for d in dados]

    def _deve_logar(self) -> bool:
        return False  # Sobrescreve gancho

# Uso
ProcessadorCSV().processar("dados.csv")
ProcessadorJSON().processar("dados.json")
```

**TypeScript:**

```typescript
abstract class ProcessadorDados {
  processar(caminho: string): void {
    const dados = this.ler(caminho);
    const transformados = this.transformar(dados);
    this.salvar(transformados);
    if (this.deveLogar()) {
      this.log("Processamento concluido");
    }
  }

  protected ler(caminho: string): Record<string, any>[] {
    console.log(`Lendo ${caminho}`);
    return [{ id: 1, valor: 100 }];
  }

  protected abstract transformar(dados: Record<string, any>[]): Record<string, any>[];

  protected salvar(dados: Record<string, any>[]): void {
    console.log(`Salvando ${dados.length} registros`);
  }

  protected deveLogar(): boolean { return true; }

  protected log(msg: string): void {
    console.log(`[LOG] ${msg}`);
  }
}

class ProcessadorCSV extends ProcessadorDados {
  protected transformar(dados: Record<string, any>[]): Record<string, any>[] {
    console.log("Transformando CSV...");
    return dados.map(d => ({ ...d, formato: "csv" }));
  }
}

class ProcessadorJSON extends ProcessadorDados {
  protected transformar(dados: Record<string, any>[]): Record<string, any>[] {
    console.log("Transformando JSON...");
    return dados.map(d => ({ ...d, formato: "json" }));
  }

  protected deveLogar(): boolean { return false; }
}

new ProcessadorCSV().processar("dados.csv");
new ProcessadorJSON().processar("dados.json");
```

**Quando usar:** Frameworks, algoritmos com etapas fixas mas variacoes nos detalhes, evitar duplicacao.
**Quando NAO usar:** Quando as subclasses precisam de controle total sobre o fluxo.
**Padroes relacionados:** [[#Factory Method]], [[#Strategy]], [[#Command]]

---

### Iterator

**Intento:** Fornecer uma maneira de acessar sequencialmente os elementos de um objeto agregado sem expor sua representacao subjacente.

**Problema que resolve:** Unificar a traversao de diferentes estruturas de dados com uma interface comum.

**Analogia:** Controle remoto de TV -- voce passa pelos canais sem saber como a TV os armazena internamente.

```ascii
+----------------+         +------------------+
|    Aggregate   |         |    Iterator      |
+----------------+         +------------------+
| + createIter() | ------> | + hasNext()      |
+----------------+         | + next()         |
                           +------------------+
          ^                        ^
          |                        |
    +-----------+          +------------------+
    |Collection |          | ConcreteIterator |
    +-----------+          +------------------+
```

**Python:**

```python
from collections.abc import Iterator, Iterable

class ColecaoInversa(Iterable):
    def __init__(self, dados: list) -> None:
        self._dados = dados

    def __iter__(self) -> Iterator:
        return IteradorInverso(self._dados)

class IteradorInverso(Iterator):
    def __init__(self, dados: list) -> None:
        self._dados = dados
        self._indice = len(dados) - 1

    def __next__(self):
        if self._indice < 0:
            raise StopIteration
        valor = self._dados[self._indice]
        self._indice -= 1
        return valor

# Uso
colecao = ColecaoInversa([1, 2, 3, 4, 5])
for item in colecao:
    print(item)  # 5, 4, 3, 2, 1
```

**TypeScript:**

```typescript
interface Iterador<T> {
  hasNext(): boolean;
  next(): T;
}

class IteradorInverso<T> implements Iterador<T> {
  private indice: number;

  constructor(private dados: T[]) {
    this.indice = dados.length - 1;
  }

  hasNext(): boolean { return this.indice >= 0; }

  next(): T {
    if (!this.hasNext()) throw new Error("Sem mais elementos");
    return this.dados[this.indice--];
  }
}

class ColecaoInversa<T> implements Iterable<T> {
  constructor(private dados: T[]) {}

  [Symbol.iterator](): Iterator<T> {
    let i = this.dados.length - 1;
    return {
      next: () => {
        if (i < 0) return { done: true, value: undefined as any };
        return { done: false, value: this.dados[i--] };
      }
    };
  }
}

// Uso
const colecao = new ColecaoInversa([1, 2, 3, 4, 5]);
for (const item of colecao) {
  console.log(item); // 5, 4, 3, 2, 1
}
```

**Quando usar:** Traversao customizada, esconder estrutura interna, multiplas traversoes simultaneas.
**Quando NAO usar:** Quando a estrutura nativa ja fornece iteracao adequada (listas, arrays).
**Padroes relacionados:** [[#Composite]], [[#Visitor]] (nao GoF), [[#Memento]] (nao GoF)

---

### State

**Intento:** Permitir que um objeto altere seu comportamento quando seu estado interno muda. O objeto parece mudar de classe.

**Problema que resolve:** Eliminar condicionais complexas baseadas em estado, distribuindo comportamento entre classes de estado.

**Analogia:** Semafaro -- o comportamento (pare, atencao, siga) depende inteiramente da cor atual.

```ascii
+----------------+         +------------------+
|    Context     |         |     State        |
+----------------+         +------------------+
| - state        | ------> | + handle()       |
| + request()    |         +------------------+
+----------------+                ^
                    +-------------+-------------+
                    |             |             |
              +-----------+ +-----------+ +-----------+
              | EstadoA   | | EstadoB   | | EstadoC   |
              +-----------+ +-----------+ +-----------+
```

**Python:**

```python
from abc import ABC, abstractmethod

class Estado(ABC):
    @abstractmethod
    def proximo(self, contexto: "Semafaro") -> None: ...
    @abstractmethod
    def acao(self) -> str: ...

class Verde(Estado):
    def proximo(self, contexto: "Semafaro") -> None:
        contexto.estado = Amarelo()
    def acao(self) -> str: return "SIGA"

class Amarelo(Estado):
    def proximo(self, contexto: "Semafaro") -> None:
        contexto.estado = Vermelho()
    def acao(self) -> str: return "ATENCAO"

class Vermelho(Estado):
    def proximo(self, contexto: "Semafaro") -> None:
        contexto.estado = Verde()
    def acao(self) -> str: return "PARE"

class Semafaro:
    def __init__(self) -> None:
        self.estado: Estado = Verde()

    def avancar(self) -> None:
        self.estado.proximo(self)

    def exibir(self) -> str:
        return self.estado.acao()

# Uso
semaforo = Semafaro()
print(semaforo.exibir())  # SIGA
semaforo.avancar()
print(semaforo.exibir())  # ATENCAO
semaforo.avancar()
print(semaforo.exibir())  # PARE
semaforo.avancar()
print(semaforo.exibir())  # SIGA (ciclo)
```

**TypeScript:**

```typescript
interface Estado {
  proximo(contexto: Semafaro): void;
  acao(): string;
}

class Verde implements Estado {
  proximo(contexto: Semafaro): void { contexto.estado = new Amarelo(); }
  acao(): string { return "SIGA"; }
}

class Amarelo implements Estado {
  proximo(contexto: Semafaro): void { contexto.estado = new Vermelho(); }
  acao(): string { return "ATENCAO"; }
}

class Vermelho implements Estado {
  proximo(contexto: Semafaro): void { contexto.estado = new Verde(); }
  acao(): string { return "PARE"; }
}

class Semafaro {
  estado: Estado = new Verde();

  avancar(): void { this.estado.proximo(this); }
  exibir(): string { return this.estado.acao(); }
}

const semaforo = new Semafaro();
console.log(semaforo.exibir()); // SIGA
semaforo.avancar();
console.log(semaforo.exibir()); // ATENCAO
```

**Quando usar:** Maquinas de estado, workflows, parsers, jogos, protocolos de rede.
**Quando NAO usar:** Quando ha poucos estados e eles nao mudam frequentemente -- um enum basta.
**Padroes relacionados:** [[#Strategy]], [[#State Machine]] (nao GoF), [[#Observer]]

---

## Tabela Comparativa de Padroes

| Categoria | Padrao | Complexidade | Frequencia de Uso |
|-----------|--------|-------------|-------------------|
| Criacional | Singleton | Baixa | Muito Alta |
| Criacional | Factory Method | Media | Muito Alta |
| Criacional | Abstract Factory | Media | Alta |
| Criacional | Builder | Media | Alta |
| Criacional | Prototype | Baixa | Media |
| Estrutural | Adapter | Baixa | Muito Alta |
| Estrutural | Decorator | Media | Alta |
| Estrutural | Facade | Baixa | Muito Alta |
| Estrutural | Composite | Media | Media |
| Estrutural | Proxy | Media | Alta |
| Comportamental | Observer | Media | Muito Alta |
| Comportamental | Strategy | Baixa | Muito Alta |
| Comportamental | Command | Media | Alta |
| Comportamental | Template Method | Baixa | Alta |
| Comportamental | Iterator | Baixa | Alta |
| Comportamental | State | Media | Media |

## Referencias Cruzadas

- Ver [[advanced-backend-architecture]] para padroes de arquitetura de sistemas
- Ver [[backend]] para implementacoes praticas em servicos
- Ver [[api-design]] para padroes aplicados a design de APIs