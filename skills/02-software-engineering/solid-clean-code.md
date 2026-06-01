---
tags: [solid, clean-code, refactoring, code-review, software-engineering, best-practices, skills-eng]
updated: 2026-06-01
title: "SOLID Principles and Clean Code"
date: 2026-06-01
---

# Principios SOLID e Clean Code

Guia completo dos principios SOLID, praticas de codigo limpo e tecnicas de refatoracao com exemplos em Python e TypeScript.

## Sumario

- [[#Principios SOLID]]
- [[#Clean Code]]
- [[#Code Smells]]
- [[#Tecnicas de Refatoracao]]
- [[#Checklist de Code Review]]

---

## Principios SOLID

### S -- Single Responsibility Principle (SRP)

**Definicao:** Uma classe deve ter um, e apenas um, motivo para mudar. Cada modulo/classe deve ser responsavel por uma unica parte da funcionalidade.

**Problema que resolve:** Classes que fazem demais sao dificeis de entender, testar e manter. Mudancas em uma responsabilidade podem quebrar outras.

#### Python -- Violacao e Correcao

```python
# === VIOLACAO DO SRP ===
class Pedido:
    def __init__(self, itens: list[dict]) -> None:
        self.itens = itens

    def total(self) -> float:
        return sum(i["preco"] * i["quantidade"] for i in self.itens)

    def salvar_no_banco(self) -> None:
        # Logica de banco de dados
        pass

    def gerar_pdf(self) -> bytes:
        # Logica de geracao de PDF
        return b""

    def enviar_email(self) -> None:
        # Logica de envio de email
        pass

# === CORRECAO DO SRP ===
class Pedido:
    """Responsabilidade: modelo de dominio do pedido"""
    def __init__(self, itens: list[dict]) -> None:
        self.itens = itens

    def total(self) -> float:
        return sum(i["preco"] * i["quantidade"] for i in self.itens)

class PedidoRepositorio:
    """Responsabilidade: persistencia"""
    def salvar(self, pedido: Pedido) -> None:
        pass

class GeradorPDF:
    """Responsabilidade: geracao de documentos"""
    def gerar(self, pedido: Pedido) -> bytes:
        return b""

class Notificador:
    """Responsabilidade: comunicacao"""
    def enviar_email(self, pedido: Pedido) -> None:
        pass
```

#### TypeScript -- Violacao e Correcao

```typescript
// === VIOLACAO DO SRP ===
class Usuario {
  nome: string;
  email: string;

  salvar(): void { /* DB logic */ }
  gerarRelatorio(): string { /* Report logic */ }
  validar(): boolean { /* Validation logic */ }
}

// === CORRECAO DO SRP ===
class Usuario {
  constructor(
    public nome: string,
    public email: string
  ) {}
}

class UsuarioRepositorio {
  salvar(usuario: Usuario): void { /* DB logic */ }
}

class UsuarioValidador {
  validar(usuario: Usuario): boolean {
    return usuario.email.includes("@");
  }
}

class RelatorioUsuario {
  gerar(usuario: Usuario): string {
    return `Relatorio de ${usuario.nome}`;
  }
}
```

**Equivoque comum:** SRP nao significa "uma classe com um metodo". Significa "uma classe com uma razao para mudar". Uma classe pode ter varios metodos desde que todos sirvam a mesma responsabilidade.

---

### O -- Open/Closed Principle (OCP)

**Definicao:** Entidades de software devem estar abertas para extensao, mas fechadas para modificacao. Novos comportamentos sao adicionados via extensao, nao alterando codigo existente.

**Problema que resolve:** Modificar codigo testado e arriscado. OCP permite adicionar funcionalidades sem tocar no codigo existente.

#### Python -- Violacao e Correcao

```python
# === VIOLACAO DO OCP ===
class CalculadoraDesconto:
    def calcular(self, tipo: str, valor: float) -> float:
        if tipo == "vip":
            return valor * 0.9
        elif tipo == "premium":
            return valor * 0.85
        elif tipo == "normal":
            return valor * 0.95
        # Toda vez que adicionar um tipo, precisa MODIFICAR esta classe

# === CORRECAO DO OCP (Strategy) ===
from abc import ABC, abstractmethod

class EstrategiaDesconto(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float: ...

class DescontoVIP(EstrategiaDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.9

class DescontoPremium(EstrategiaDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.85

class DescontoNormal(EstrategiaDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.95

class CalculadoraDesconto:
    def calcular(self, estrategia: EstrategiaDesconto, valor: float) -> float:
        return estrategia.calcular(valor)

# Novo desconto sem modificar nada existente
class DescontoBlackFriday(EstrategiaDesconto):
    def calcular(self, valor: float) -> float:
        return valor * 0.7
```

#### TypeScript -- Violacao e Correcao

```typescript
// === VIOLACAO DO OCP ===
class FormatadorOutput {
  formatar(dados: any, tipo: string): string {
    if (tipo === "json") return JSON.stringify(dados);
    if (tipo === "csv") return Object.entries(dados).map(([k, v]) => `${k},${v}`).join("\n");
    if (tipo === "xml") return `<root>${Object.entries(dados).map(([k, v]) => `<${k}>${v}</${k}>`).join("")}</root>`;
    throw new Error("Tipo desconhecido");
  }
}

// === CORRECAO DO OCP ===
interface Formatador {
  formatar(dados: Record<string, any>): string;
}

class FormatadorJSON implements Formatador {
  formatar(dados: Record<string, any>): string {
    return JSON.stringify(dados);
  }
}

class FormatadorCSV implements Formatador {
  formatar(dados: Record<string, any>): string {
    return Object.entries(dados).map(([k, v]) => `${k},${v}`).join("\n");
  }
}

class FormatadorXML implements Formatador {
  formatar(dados: Record<string, any>): string {
    const entries = Object.entries(dados)
      .map(([k, v]) => `<${k}>${v}</${k}>`)
      .join("");
    return `<root>${entries}</root>`;
  }
}

// Novo formatador sem modificar os existentes
class FormatadorYAML implements Formatador {
  formatar(dados: Record<string, any>): string {
    return Object.entries(dados).map(([k, v]) => `${k}: ${v}`).join("\n");
  }
}
```

**Equivoque comum:** OCP nao significa "nunca modificar codigo". Significa "projetar de forma que extensoes comuns nao requeiram modificacao". Codigo que muda frequentemente deve ser projetado com OCP em mente.

---

### L -- Liskov Substitution Principle (LSP)

**Definicao:** Objetos de uma classe derivada devem poder substituir objetos da classe base sem alterar a correcao do programa. Subtipos devem ser substitutiveis por seus tipos base.

**Problema que resolve:** Heranca que viola expectativas do codigo cliente causa bugs sutis e comportamento inesperado.

#### Python -- Violacao e Correcao

```python
# === VIOLACAO DO LSP ===
class Passaro:
    def voar(self) -> str:
        return "Voando..."

class Pato(Passaro):
    def voar(self) -> str:
        return "Pato voando..."

class Pinguim(Passaro):
    def voar(self) -> str:
        raise NotImplementedError("Pinguim nao voa!")  # VIOLACAO!

def fazer_voar(passaro: Passaro) -> str:
    return passaro.voar()  # Quebra com Pinguim!

# === CORRECAO DO LSP ===
from abc import ABC, abstractmethod

class Passaro(ABC):
    @abstractmethod
    def mover(self) -> str: ...

class PassaroVoador(Passaro):
    def mover(self) -> str:
        return "Voando..."

class PassaroNadador(Passaro):
    def mover(self) -> str:
        return "Nadando..."

class Pato(PassaroVoador, PassaroNadador):
    def mover(self) -> str:
        return "Pato voando e nadando"

class Pinguim(PassaroNadador):
    def mover(self) -> str:
        return "Pinguim nadando"

def fazer_mover(passaro: Passaro) -> str:
    return passaro.mover()  # Funciona para todos!
```

#### TypeScript -- Violacao e Correcao

```typescript
// === VIOLACAO DO LSP ===
class Retangulo {
  constructor(
    protected _largura: number,
    protected _altura: number
  ) {}

  get largura(): number { return this._largura; }
  set largura(v: number) { this._largura = v; }
  get altura(): number { return this._altura; }
  set altura(v: number) { this._altura = v; }

  area(): number { return this._largura * this._altura; }
}

class Quadrado extends Retangulo {
  constructor(lado: number) {
    super(lado, lado);
  }

  override set largura(v: number) {
    this._largura = v;
    this._altura = v;  // VIOLACAO: comportamento inesperado!
  }

  override set altura(v: number) {
    this._altura = v;
    this._largura = v;
  }
}

function testar(r: Retangulo): void {
  r.largura = 5;
  r.altura = 10;
  console.log(r.area()); // Esperado: 50, Quadrado retorna: 100!
}

// === CORRECAO DO LSP ===
interface Forma {
  area(): number;
}

class Retangulo implements Forma {
  constructor(private largura: number, private altura: number) {}
  area(): number { return this.largura * this.altura; }
}

class Quadrado implements Forma {
  constructor(private lado: number) {}
  area(): number { return this.lado * this.lado; }
}
```

**Equivoque comum:** LSP nao e apenas sobre heranca tecnica -- e sobre contratos comportamentais. Mesmo com duck typing (Python) ou interfaces (TS), o comportamento deve ser consistente.

---

### I -- Interface Segregation Principle (ISP)

**Definicao:** Nenhuma classe deve ser forcada a depender de metodos que nao usa. Interfaces grandes devem ser divididas em interfaces menores e mais especificas.

**Problema que resolve:** Classes sao forcadas a implementar metodos que nao precisam, gerando codigo morto ou excecoes.

#### Python -- Violacao e Correcao

```python
# === VIOLACAO DO ISP ===
from abc import ABC, abstractmethod

class TrabalhadorCompleto(ABC):
    @abstractmethod
    def trabalhar(self) -> None: ...
    @abstractmethod
    def comer(self) -> None: ...
    @abstractmethod
    def dormir(self) -> None: ...

class Robo(TrabalhadorCompleto):
    def trabalhar(self) -> None:
        print("Robo trabalhando")

    def comer(self) -> None:
        raise NotImplementedError("Robo nao come!")  # VIOLACAO

    def dormir(self) -> None:
        raise NotImplementedError("Robo nao dorme!")  # VIOLACAO

# === CORRECAO DO ISP ===
class Trabalhador(ABC):
    @abstractmethod
    def trabalhar(self) -> None: ...

class Comensal(ABC):
    @abstractmethod
    def comer(self) -> None: ...

class Dorminhoco(ABC):
    @abstractmethod
    def dormir(self) -> None: ...

class Humano(Trabalhador, Comensal, Dorminhoco):
    def trabalhar(self) -> None: print("Humano trabalhando")
    def comer(self) -> None: print("Humano comendo")
    def dormir(self) -> None: print("Humano dormindo")

class Robo(Trabalhador):
    def trabalhar(self) -> None: print("Robo trabalhando")
    # Nao precisa implementar comer() ou dormir()
```

#### TypeScript -- Violacao e Correcao

```typescript
// === VIOLACAO DO ISP ===
interface MaquinaCompleta {
  imprimir(): void;
  digitalizar(): void;
  faxar(): void;
}

class ImpressoraSimples implements MaquinaCompleta {
  imprimir(): void { console.log("Imprimindo"); }
  digitalizar(): void { throw new Error("Nao digitaliza"); }  // VIOLACAO
  faxar(): void { throw new Error("Nao faxa"); }              // VIOLACAO
}

// === CORRECAO DO ISP ===
interface Impressora {
  imprimir(): void;
}

interface Digitalizadora {
  digitalizar(): void;
}

interface FaxMachine {
  faxar(): void;
}

class ImpressoraSimples implements Impressora {
  imprimir(): void { console.log("Imprimindo"); }
}

class Multifuncional implements Impressora, Digitalizadora, FaxMachine {
  imprimir(): void { console.log("Imprimindo"); }
  digitalizar(): void { console.log("Digitalizando"); }
  faxar(): void { console.log("Faxando"); }
}
```

**Equivoque comum:** ISP nao significa "interfaces com um unico metodo". Significa "interfaces coesas que fazem sentido para quem as implementa".

---

### D -- Dependency Inversion Principle (DIP)

**Definicao:** Modulos de alto nivel nao devem depender de modulos de baixo nivel. Ambos devem depender de abstracoes. Abstracoes nao devem depender de detalhes; detalhes devem depender de abstracoes.

**Problema que resolve:** Acoplamento direto entre modulos torna o sistema rigido e dificil de testar.

#### Python -- Violacao e Correcao

```python
# === VIOLACAO DO DIP ===
class MySQLDatabase:
    def conectar(self) -> None:
        print("Conectando ao MySQL")

    def executar(self, query: str) -> list:
        return [{"id": 1}]

class ServicoUsuario:
    def __init__(self) -> None:
        self._db = MySQLDatabase()  # Dependencia concreta!

    def buscar_usuario(self, id: int) -> dict:
        self._db.conectar()
        return self._db.executar(f"SELECT * FROM usuarios WHERE id={id}")[0]

# === CORRECAO DO DIP ===
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def conectar(self) -> None: ...
    @abstractmethod
    def executar(self, query: str) -> list: ...

class MySQLDatabase(Database):
    def conectar(self) -> None: print("Conectando ao MySQL")
    def executar(self, query: str) -> list: return [{"id": 1}]

class PostgresDatabase(Database):
    def conectar(self) -> None: print("Conectando ao Postgres")
    def executar(self, query: str) -> list: return [{"id": 1}]

class ServicoUsuario:
    def __init__(self, db: Database) -> None:  # Injecao de dependencia
        self._db = db

    def buscar_usuario(self, id: int) -> dict:
        self._db.conectar()
        return self._db.executar(f"SELECT * FROM usuarios WHERE id={id}")[0]

# Uso com injecao
servico = ServicoUsuario(MySQLDatabase())  # Ou PostgresDatabase()

# DI Container simples
class Container:
    def __init__(self) -> None:
        self._servicos: dict = {}

    def registrar(self, interface, implementacao) -> None:
        self._servicos[interface] = implementacao

    def resolver(self, interface):
        return self._servicos[interface]()

container = Container()
container.register(Database, MySQLDatabase)
db = container.resolve(Database)
servico = ServicoUsuario(db)
```

#### TypeScript -- Violacao e Correcao

```typescript
// === VIOLACAO DO DIP ===
class StripeGateway {
  cobrar(valor: number): Promise<string> {
    return Promise.resolve("tx_stripe_123");
  }
}

class CheckoutService {
  private gateway = new StripeGateway();  // Dependencia concreta!

  async finalizar(valor: number): Promise<string> {
    return this.gateway.cobrar(valor);
  }
}

// === CORRECAO DO DIP ===
interface PagamentoGateway {
  cobrar(valor: number): Promise<string>;
}

class StripeGateway implements PagamentoGateway {
  cobrar(valor: number): Promise<string> {
    return Promise.resolve("tx_stripe_123");
  }
}

class PayPalGateway implements PagamentoGateway {
  cobrar(valor: number): Promise<string> {
    return Promise.resolve("tx_paypal_456");
  }
}

class CheckoutService {
  constructor(private gateway: PagamentoGateway) {}  // Injecao

  async finalizar(valor: number): Promise<string> {
    return this.gateway.cobrar(valor);
  }
}

// DI com Inversao de Controle
const checkout = new CheckoutService(new StripeGateway());
// Ou: new CheckoutService(new PayPalGateway());
```

**Equivoque comum:** DIP nao e o mesmo que DI (Dependency Injection). DI e uma tecnica para implementar DIP. DIP e o principio; DI e o mecanismo.

---

## Clean Code

### Convencoes de Nomenclatura

| Elemento | Python | TypeScript | Exemplo |
|----------|--------|------------|---------|
| Variaveis | snake_case | camelCase | `nome_usuario`, `nomeUsuario` |
| Funcoes | snake_case | camelCase | `calcular_total()`, `calcularTotal()` |
| Classes | PascalCase | PascalCase | `PedidoServico`, `PedidoServico` |
| Constantes | UPPER_SNAKE | UPPER_SNAKE | `MAX_TENTATIVAS`, `MAX_TENTATIVAS` |
| Privado | `_prefixo` | `#prefixo` | `_cache`, `#cache` |
| Modulos | snake_case | kebab-case | `meu_modulo.py`, `meu-modulo.ts` |

**Regras gerais:**
- Nomes devem revelar intencao, nao tipo
- Evitar abreviacoes obscuras (`calc` vs `calcular`)
- Booleanos com prefixo afirmativo (`esta_ativo`, `isActive`)
- Funcoes que retornam booleano com prefixo de pergunta (`pode_cancelar`, `canCancel`)

```python
# Ruim
d = datetime.now()
x = calcular(a, b)
flag = True

# Bom
data_criacao = datetime.now()
total_pedido = calcular_total(itens)
pedido_esta_ativo = True
```

```typescript
// Ruim
const d = new Date();
const x = calc(a, b);
const flag = true;

// Bom
const dataCriacao = new Date();
const totalPedido = calcularTotal(itens);
const pedidoEstaAtivo = true;
```

### Design de Funcoes

**Regras:**
- Uma funcao deve fazer UMA coisa e fazer bem
- Idealmente menos de 20 linhas
- Sem efeitos colaterais inesperados
- Maximo 3 parametros (agrupar em objeto/classe se necessario)

```python
# Ruim -- faz demais, muitos parametros
def processar_pedido(
    nome: str, email: str, endereco: str, cidade: str,
    estado: str, cep: str, itens: list, desconto: float,
    frete: float, imposto: float
) -> dict:
    # 100 linhas de codigo misturando validacao, calculo, persistencia
    pass

# Bom -- funcoes pequenas e focadas
def calcular_total(itens: list[dict], desconto: float) -> float:
    subtotal = sum(i["preco"] * i["quantidade"] for i in itens)
    return subtotal * (1 - desconto)

def validar_endereco(endereco: dict) -> bool:
    return all(k in endereco for k in ["rua", "cidade", "estado", "cep"])

def processar_pedido(pedido: dict) -> dict:
    validar_dados(pedido)
    total = calcular_total(pedido["itens"], pedido["desconto"])
    return salvar_pedido({**pedido, "total": total})
```

### Filosofia de Comentarios

**Principio:** Codigo deve ser autoexplicativo. Comentarios devem explicar o PORQUE, nao o QUE.

```python
# Ruim -- repete o codigo
i = i + 1  # Incrementa i em 1

# Bom -- explica o por que
# Compensacao de fuso horario: o servidor UTC precisa ajustar
# para o horario de Brasilia (UTC-3)
offset_horario = -3
```

```typescript
// Ruim
// Retorna o total
function getTotal(items: any[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}

// Bom -- explica regra de negocio
// Desconto progressivo: acima de 10 itens, 5% de desconto
// para incentivar compras em volume
function aplicarDescontoVolume(total: number, quantidade: number): number {
  return quantidade >= 10 ? total * 0.95 : total;
}
```

### Tratamento de Erros

```python
# Python -- Excecoes customizadas
class ErroDominio(Exception):
    """Classe base para erros de dominio"""
    pass

class EstoqueInsuficienteError(ErroDominio):
    def __init__(self, sku: str, disponivel: int, solicitado: int) -> None:
        self.sku = sku
        self.disponivel = disponivel
        self.solicitado = solicitado
        super().__init__(
            f"SKU {sku}: disponivel={disponivel}, solicitado={solicitado}"
        )

class PagamentoRecusadoError(ErroDominio):
    def __init__(self, motivo: str) -> None:
        self.motivo = motivo
        super().__init__(f"Pagamento recusado: {motivo}")

# Uso
def reservar_estoque(sku: str, quantidade: int) -> None:
    disponivel = buscar_estoque(sku)
    if disponivel < quantidade:
        raise EstoqueInsuficienteError(sku, disponivel, quantidade)
    atualizar_estoque(sku, disponivel - quantidade)
```

```typescript
// TypeScript -- Erros customizados
class ErroDominio extends Error {
  constructor(message: string) {
    super(message);
    this.name = "ErroDominio";
  }
}

class EstoqueInsuficienteError extends ErroDominio {
  constructor(
    public sku: string,
    public disponivel: number,
    public solicitado: number
  ) {
    super(`SKU ${sku}: disponivel=${disponivel}, solicitado=${solicitado}`);
    this.name = "EstoqueInsuficienteError";
  }
}

class PagamentoRecusadoError extends ErroDominio {
  constructor(public motivo: string) {
    super(`Pagamento recusado: ${motivo}`);
    this.name = "PagamentoRecusadoError";
  }
}

// Uso
function reservarEstoque(sku: string, quantidade: number): void {
  const disponivel = buscarEstoque(sku);
  if (disponivel < quantidade) {
    throw new EstoqueInsuficienteError(sku, disponivel, quantidade);
  }
  atualizarEstoque(sku, disponivel - quantidade);
}
```

### Principios DRY, KISS, YAGNI

| Principio | Significado | Exemplo |
|-----------|-------------|---------|
| **DRY** | Don't Repeat Yourself | Extrair logica duplicada em funcao compartilhada |
| **KISS** | Keep It Simple, Stupid | Preferir solucao simples a solucao "inteligente" |
| **YAGNI** | You Ain't Gonna Need It | Nao implementar funcionalidade "para o futuro" |

```python
# DRY -- antes (duplicacao)
def calcular_imposto_sp(valor: float) -> float:
    return valor * 0.18

def calcular_imposto_rj(valor: float) -> float:
    return valor * 0.20

# DRY -- depois
TABELA_ICMS = {"SP": 0.18, "RJ": 0.20, "MG": 0.17}

def calcular_imposto(estado: str, valor: float) -> float:
    aliquota = TABELA_ICMS.get(estado, 0.18)
    return valor * aliquota

# KISS -- antes (complexo demais)
def get_user(u: dict) -> str | None:
    return u.get("n") if u and isinstance(u, dict) and "n" in u else None

# KISS -- depois (simples)
def obter_nome_usuario(usuario: dict) -> str | None:
    return usuario.get("nome")

# YAGNI -- NAO faca isso
class Usuario:
    # Nao adicione campos "para o futuro"
    # nome_futuro: str  # "Vamos precisar depois"
    # plano_premium: bool  # "Quando lancarmos o premium"
    pass
```

---

## Code Smells

| Code Smell | Sintoma | Solucao |
|-----------|---------|---------|
| **Long Method** | Funcao com 50+ linhas | [[#Extract Method]] |
| **Large Class** | Classe com 10+ responsabilidades | [[#Extract Class]] |
| **Feature Envy** | Metodo usa mais dados de outra classe | Mover metodo para a classe certa |
| **Data Clumps** | Grupos de dados que sempre aparecem juntos | [[#Introduce Parameter Object]] |
| **Shotgun Surgery** | Uma mudanca exige edicoes em muitas classes | Consolidar responsabilidades |
| **Long Parameter List** | Funcao com 5+ parametros | [[#Introduce Parameter Object]] |
| **Switch Statements** | Condicionais baseadas em tipo | [[#Replace Conditional with Polymorphism]] |
| **Primitive Obsession** | Usar primitivos onde objetos fariam sentido | Criar Value Objects |
| **Dead Code** | Codigo nao utilizado | Remover |
| **Comments** | Comentarios explicando codigo confuso | Refatorar para ser autoexplicativo |

---

## Tecnicas de Refatoracao

### Extract Method

Transformar um trecho de codigo em uma funcao com nome descritivo.

```python
# Antes
def processar_pedido(pedido: dict) -> dict:
    # ... 50 linhas ...
    subtotal = sum(i["preco"] * i["quantidade"] for i in pedido["itens"])
    desconto = subtotal * 0.1 if subtotal > 1000 else 0
    frete = 15.0 if subtotal < 100 else 0
    total = subtotal - desconto + frete
    # ... mais 50 linhas ...

# Depois
def calcular_total_pedido(itens: list[dict]) -> float:
    subtotal = sum(i["preco"] * i["quantidade"] for i in itens)
    desconto = subtotal * 0.1 if subtotal > 1000 else 0
    frete = 15.0 if subtotal < 100 else 0
    return subtotal - desconto + frete

def processar_pedido(pedido: dict) -> dict:
    total = calcular_total_pedido(pedido["itens"])
    # ... resto do metodo ...
```

### Extract Class

Dividir uma classe que faz demais em classes separadas.

```typescript
// Antes
class Usuario {
  nome: string;
  email: string;
  rua: string;
  cidade: string;
  estado: string;
  cep: string;
  // Metodos de usuario E de endereco misturados
}

// Depois
class Usuario {
  constructor(
    public nome: string,
    public email: string,
    public endereco: Endereco
  ) {}
}

class Endereco {
  constructor(
    public rua: string,
    public cidade: string,
    public estado: string,
    public cep: string
  ) {}
}
```

### Replace Conditional with Polymorphism

Substituir condicionais baseadas em tipo por polimorfismo.

```python
# Antes
def calcular_area(forma: dict) -> float:
    if forma["tipo"] == "circulo":
        return 3.14159 * forma["raio"] ** 2
    elif forma["tipo"] == "retangulo":
        return forma["largura"] * forma["altura"]
    elif forma["tipo"] == "triangulo":
        return (forma["base"] * forma["altura"]) / 2

# Depois
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Circulo(Forma):
    def __init__(self, raio: float) -> None:
        self.raio = raio
    def area(self) -> float:
        return 3.14159 * self.raio ** 2

class Retangulo(Forma):
    def __init__(self, largura: float, altura: float) -> None:
        self.largura = largura
        self.altura = altura
    def area(self) -> float:
        return self.largura * self.altura
```

### Introduce Parameter Object

Agrupar parametros relacionados em um objeto.

```python
# Antes
def criar_conta(
    nome: str, cpf: str, email: str,
    rua: str, numero: str, cidade: str, estado: str
) -> dict: ...

# Depois
class Endereco:
    def __init__(self, rua: str, numero: str, cidade: str, estado: str) -> None:
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

class DadosPessoais:
    def __init__(self, nome: str, cpf: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.endereco = endereco

def criar_conta(dados: DadosPessoais) -> dict: ...
```

---

## Checklist de Code Review

### Checklist de 20 Pontos para PR

| # | Categoria | Item |
|---|-----------|------|
| 1 | Funcionalidade | O codigo faz o que se propoe a fazer? |
| 2 | SOLID | Os principios SOLID foram respeitados? |
| 3 | Nomenclatura | Nomes sao claros e revelam intencao? |
| 4 | Tamanho | Funcoes e classes tem tamanho adequado? |
| 5 | DRY | Ha duplicacao de codigo? |
| 6 | Tratamento de erros | Erros sao tratados de forma apropriada? |
| 7 | Seguranca | Ha vulnerabilidades (SQL injection, XSS, etc)? |
| 8 | Performance | Ha operacoes desnecessarias ou ineficientes? |
| 9 | Testes | Ha testes para a nova funcionalidade? |
| 10 | Testes | Os testes cobrem casos de borda? |
| 11 | Logging | Logs sao informativos e nao expoem dados sensiveis? |
| 12 | Documentacao | API e funcoes publicas estao documentadas? |
| 13 | Comentarios | Comentarios explicam o PORQUE, nao o QUE? |
| 14 | Consistencia | Segue o padrao do projeto existente? |
| 15 | Acoplamento | Ha dependencias desnecessarias entre modulos? |
| 16 | Coesao | Cada modulo tem responsabilidade clara? |
| 17 | Configuracao | Valores magicos foram extraidos para constantes/config? |
| 18 | Compatibilidade | Ha breaking changes? Sao intencionais? |
| 19 | Clean Code | Codigo e legivel e autoexplicativo? |
| 20 | Git | Commits sao atomicos e com mensagens claras? |

### Verificacoes Automatizadas

```yaml
# Pipeline de qualidade de codigo
linters:
  python:
    - ruff          # Linter rapido
    - black         # Formatacao
    - mypy          # Type checking
    - bandit        # Seguranca
  typescript:
    - eslint        # Linter
    - prettier      # Formatacao
    - tsc --noEmit  # Type checking
    - sonarqube     # Analise estatica

metricas:
  cobertura_minima: 80%
  complexidade_cicomatica_max: 10
  tamanho_max_funcao: 30 linhas
  duplicacao_maxima: 3%
```

### Areas de Foco Manual

1. **Logica de negocio** -- Regras estao corretas e completas?
2. **Design de API** -- Endpoints sao RESTful e consistentes?
3. **Modelo de dados** -- Schema e normalizado e eficiente?
4. **Seguranca** -- Autenticacao, autorizacao, sanitizacao?
5. **Experiencia do desenvolvedor** -- Codigo e facil de entender e modificar?

---

## Referencias Cruzadas

- Ver [[design-patterns]] para padroes de projeto GoF
- Ver [[testing/SKILL]] para estrategias de teste
- Ver [[backend]] para implementacoes de servicos
- Ver [[frontend]] para aplicacoes no lado do cliente