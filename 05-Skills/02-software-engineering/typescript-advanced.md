---
tags: [skills, skills-eng, typescript, type-system, generics, utility-types]
updated: 2026-06-08
title: "TypeScript Avancado - Sistema de Tipos, Genericos e Programacao em Nivel de Tipo"
date: 2026-05-16
---

# TypeScript Avancado

Referencia completa sobre o sistema de tipos do TypeScript, genericos, tipos condicionais, tipos mapeados, programacao em nivel de tipo, configuracao do compilador e estrategias de teste de tipos. Guia pratico para treinamento do agente JARVIS.

## Sistema de Tipos

### Tipagem Estrutural vs Nominal

TypeScript usa tipagem estrutural (duck typing): se a forma corresponde, o tipo e compativel.

```typescript
// Tipagem estrutural - forma importa, nao o nome
interface Pessoa {
  nome: string;
  idade: number;
}

interface Cliente {
  nome: string;
  idade: number;
}

function saudar(p: Pessoa): string {
  return `Ola, ${p.nome}`;
}

const cliente: Cliente = { nome: "Ana", idade: 30 };
saudar(cliente); // OK - forma compativel (tipagem estrutural)
```

```python
# Python usa duck typing nativamente (similar a tipagem estrutural)
from typing import Protocol

class PessoaProtocol(Protocol):
    nome: str
    idade: int

def saudar(p: PessoaProtocol) -> str:
    return f"Ola, {p.nome}"

class Cliente:
    def __init__(self):
        self.nome = "Ana"
        self.idade = 30

saudar(Cliente())  # OK - duck typing
```

### Type Narrowing e Guards

```typescript
// Type guards com typeof
function processar(valor: string | number): string {
  if (typeof valor === "string") {
    return valor.toUpperCase(); // TypeScript sabe que e string aqui
  }
  return valor.toFixed(2); // TypeScript sabe que e number aqui
}

// Type guards com instanceof
class Cachorro { late(): string { return "Au!"; } }
class Gato { mia(): string { return "Miau!"; } }

function som(animal: Cachorro | Gato): string {
  if (animal instanceof Cachorro) {
    return animal.late();
  }
  return animal.mia();
}

// Type predicates (predicados de tipo)
interface Veiculo { tipo: string; }
interface Carro extends Veiculo { portas: number; }
interface Moto extends Veiculo { cilindradas: number; }

function isCarro(v: Veiculo): v is Carro {
  return (v as Carro).portas !== undefined;
}

function detalhes(v: Veiculo): string {
  if (isCarro(v)) {
    return `Carro com ${v.portas} portas`; // v e Carro aqui
  }
  return `Moto com ${(v as Moto).cilindradas}cc`;
}

// Assertion functions
function assertIsString(val: unknown): asserts val is string {
  if (typeof val !== "string") {
    throw new Error("Nao e uma string");
  }
}

function processarString(val: unknown): void {
  assertIsString(val);
  console.log(val.toUpperCase()); // val e string aqui
}

// Narrowing com discriminant union
interface Sucesso { tipo: "sucesso"; dados: string; }
interface Erro { tipo: "erro"; mensagem: string; }
type Resultado = Sucesso | Erro;

function handler(res: Resultado): string {
  switch (res.tipo) {
    case "sucesso": return res.dados; // Sucesso
    case "erro": return res.mensagem; // Erro
  }
}
```

```python
# Type narrowing em Python com isinstance e TypeGuard
from typing import Union, TypeGuard

class Cachorro:
    def late(self) -> str: return "Au!"

class Gato:
    def mia(self) -> str: return "Miau!"

def som(animal: Union[Cachorro, Gato]) -> str:
    if isinstance(animal, Cachorro):
        return animal.late()
    return animal.mia()

# Python 3.10+ com TypeGuard
from typing_extensions import TypeGuard

def is_cachorro(animal: object) -> TypeGuard[Cachorro]:
    return isinstance(animal, Cachorro)
```

## Genericos

### Funcoes, Classes e Interfaces Genericas

```typescript
// Funcao generica
function primeiro<T>(arr: T[]): T | undefined {
  return arr[0];
}

const n = primeiro([1, 2, 3]); // number
const s = primeiro(["a", "b"]); // string

// Multiplos parametros genericos
function merge<T, U>(obj1: T, obj2: U): T & U {
  return { ...obj1, ...obj2 };
}

const resultado = merge({ nome: "Ana" }, { idade: 30 });
// { nome: string } & { idade: number }

// Interface generica
interface Repositorio<T> {
  buscar(id: string): T | undefined;
  salvar(item: T): void;
  listar(): T[];
  remover(id: string): boolean;
}

// Classe generica
class RepositorioEmMemoria<T extends { id: string }> implements Repositorio<T> {
  private itens: Map<string, T> = new Map();

  buscar(id: string): T | undefined {
    return this.itens.get(id);
  }

  salvar(item: T): void {
    this.itens.set(item.id, item);
  }

  listar(): T[] {
    return Array.from(this.itens.values());
  }

  remover(id: string): boolean {
    return this.itens.delete(id);
  }
}

// Uso
interface Usuario { id: string; nome: string; email: string; }
const repo = new RepositorioEmMemoria<Usuario>();
repo.salvar({ id: "1", nome: "Ana", email: "ana@email.com" });
```

```python
# Genericos em Python com TypeVar
from typing import TypeVar, Generic, Protocol

T = TypeVar('T')

class Repositorio(Generic[T]):
    def buscar(self, id: str) -> T | None:
        raise NotImplementedError

    def salvar(self, item: T) -> None:
        raise NotImplementedError

class RepositorioMemoria(Repositorio[T]):
    def __init__(self):
        self._itens: dict[str, T] = {}

    def buscar(self, id: str) -> T | None:
        return self._itens.get(id)

    def salvar(self, item: T) -> None:
        self._itens[id(item)] = item
```

### Restricoes Genericas

```typescript
// Restricao com extends
interface TemId { id: string; }

function buscarPorId<T extends TemId>(itens: T[], id: string): T | undefined {
  return itens.find(item => item.id === id);
}

// Restricao com keyof
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const usuario = { nome: "Ana", idade: 30, email: "ana@email.com" };
getProperty(usuario, "nome"); // OK - string
getProperty(usuario, "endereco"); // Erro: "endereco" nao existe em typeof usuario

// Restricao com new
function criarInstancia<T>(ctor: new () => T): T {
  return new ctor();
}

class Servico {
  executar(): string { return "Executando..."; }
}

const servico = criarInstancia(Servico);
servico.executar(); // OK
```

### Parametros de Tipo Padrao

```typescript
interface Resposta<TDados = unknown, TErro = string> {
  dados?: TDados;
  erro?: TErro;
  sucesso: boolean;
}

const resp1: Resposta = { sucesso: true }; // TDados=unknown, TErro=string
const resp2: Resposta<Usuario> = { sucesso: true, dados: usuario };
const resp3: Resposta<Usuario, Error> = { sucesso: false, erro: new Error("Falha") };
```

### Variancia

```typescript
// Covariancia: subtipo preserva direcao
interface Animal { nome: string; }
interface Cachorro extends Animal { raca: string; }

type Getter<T> = () => T;
let getAnimal: Getter<Animal> = () => ({ nome: "Rex" });
let getDog: Getter<Cachorro> = () => ({ nome: "Rex", raca: "Labrador" });

getAnimal = getDog; // OK - Getter e covariante (Cachorro extends Animal => Getter<Cachorro> extends Getter<Animal>)

// Contravariancia: subtipo inverte direcao
type Setter<T> = (value: T) => void;
let setAnimal: Setter<Animal> = (a: Animal) => console.log(a.nome);
let setDog: Setter<Cachorro> = (d: Cachorro) => console.log(d.raca);

setDog = setAnimal; // OK - Setter e contravariante
// (precisa aceitar Animal, que e supertipo de Cachorro)

// Bivariancia: ambas direcoes (comportamento padrao do TS para metodos)
class Comparador<T> {
  comparar(a: T, b: T): number {
    return 0;
  }
}
```

## Tipos Condicionais

### extends e infer

```typescript
// Tipo condicional basico
type EhString<T> = T extends string ? "sim" : "nao";

type A = EhString<string>; // "sim"
type B = EhString<number>; // "nao"

// infer - extrair tipos
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;

function soma(a: number, b: number): number { return a + b; }
type ResultadoSoma = ReturnType<typeof soma>; // number

// Extrair tipo de Promise
type UnwrapPromise<T> = T extends Promise<infer U> ? U : T;

type A = UnwrapPromise<Promise<string>>; // string
type B = UnwrapPromise<number>; // number

// Extrair parametro de funcao
type FirstParam<T> = T extends (arg: infer P, ...rest: any[]) => any ? P : never;

function greet(name: string, age: number): void {}
type NomeParam = FirstParam<typeof greet>; // string

// Extrair tipo de array
type ArrayElement<T> = T extends (infer U)[] ? U : never;

type Elemento = ArrayElement<string[]>; // string
```

### Tipos Condicionais Distributivos

```typescript
// Tipos condicionais distribuem sobre unions automaticamente
type ToArray<T> = T extends any ? T[] : never;

type StringsOrNumbers = ToArray<string | number>;
// = ToArray<string> | ToArray<number>
// = string[] | number[]

// Para evitar distribuicao, usar [T]
type ToArrayNonDist<T> = [T] extends [any] ? T[] : never;

type Resultado = ToArrayNonDist<string | number>;
// = (string | number)[]
```

### Template Literal Types

```typescript
// Template literal types
type Evento = "click" | "hover" | "scroll";
type HandlerName = `on${Capitalize<Evento>}`;
// = "onClick" | "onHover" | "onScroll"

// Extrair partes de string
type Rota = `/api/${string}`;
const rota1: Rota = "/api/users"; // OK
const rota2: Rota = "/users"; // Erro

// Parsing de template literal com infer
type ParseEventName<T extends string> = T extends `on${infer E}` ? Lowercase<E> : never;

type EventoParseado = ParseEventName<"onClick">; // "click"

// Uppercase/Lowercase/Capitalize/Uncapitalize
type Upper = Uppercase<"hello">; // "HELLO"
type Lower = Lowercase<"HELLO">; // "hello"
type Cap = Capitalize<"hello">; // "Hello"
type Uncap = Uncapitalize<"Hello">; // "hello"
```

## Tipos Mapeados

### keyof, typeof e in

```typescript
interface Usuario {
  nome: string;
  idade: number;
  email: string;
}

// keyof - extrai chaves como union de string literals
type ChavesUsuario = keyof Usuario; // "nome" | "idade" | "email"

// typeof - extrai tipo de valor
const config = { url: "http://api.com", timeout: 5000 };
type ConfigType = typeof config; // { url: string; timeout: number }

// in - iterar sobre chaves em tipo mapeado
type Readonly<T> = {
  readonly [P in keyof T]: T[P];
};

type UsuarioReadonly = Readonly<Usuario>;
// { readonly nome: string; readonly idade: number; readonly email: string; }
```

### Utility Types Built-in

```typescript
interface Produto {
  id: number;
  nome: string;
  preco: number;
  descricao: string;
  criadoEm: Date;
}

// Partial<T> - todas propriedades opcionais
type ProdutoParcial = Partial<Produto>;
// { id?: number; nome?: string; preco?: number; descricao?: string; criadoEm?: Date }

// Required<T> - todas propriedades obrigatorias
type ProdutoObrigatorio = Required<ProdutoParcial>;

// Readonly<T> - todas propriedades readonly
type ProdutoSomenteLeitura = Readonly<Produto>;

// Pick<T, K> - selecionar propriedades
type ProdutoResumo = Pick<Produto, "id" | "nome">;
// { id: number; nome: string }

// Omit<T, K> - excluir propriedades
type ProdutoSemData = Omit<Produto, "criadoEm">;
// { id: number; nome: string; preco: number; descricao: string }

// Record<K, T> - objeto com chaves K e valores T
type ConfigMap = Record<string, number>;
// { [key: string]: number }

// Exclude<T, U> - remover U de T
type SemNumero = Exclude<string | number | boolean, number>;
// string | boolean

// Extract<T, U> - manter apenas U em T
type ApenasString = Extract<string | number | boolean, string>;
// string

// NonNullable<T> - remover null e undefined
type NaoNulo = NonNullable<string | null | undefined>;
// string

// Parameters<T> - extrair parametros de funcao
type Params = Parameters<(a: string, b: number) => void>;
// [string, number]

// ConstructorParameters<T> - extrair parametros de construtor
type ConstrutorParams = ConstructorParameters<typeof Date>;
// [string?] | []

// InstanceType<T> - extrair tipo de instancia
type DataInstance = InstanceType<typeof Date>;
// Date

// ThisParameterType<T> / OmitThisParameter<T>
function comThis(this: { nome: string }): void {}
type ThisType = ThisParameterType<typeof comThis>; // { nome: string }
```

### Tipos Mapeados Customizados

```typescript
// Tornar todas as propriedades async
type Asyncify<T> = {
  [P in keyof T]: T[P] extends (...args: infer A) => infer R
    ? (...args: A) => Promise<R>
    : T[P];
};

interface SyncAPI {
  buscar(id: string): Usuario;
  listar(): Usuario[];
}

type AsyncAPI = Asyncify<SyncAPI>;
// { buscar(id: string): Promise<Usuario>; listar(): Promise<Usuario[]> }

// Deep Partial (recursivo)
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object ? DeepPartial<T[P]> : T[P];
};

interface Endereco { rua: string; numero: number; }
interface PessoaCompleta { nome: string; endereco: Endereco; }

type PessoaParcial = DeepPartial<PessoaCompleta>;
// { nome?: string; endereco?: { rua?: string; numero?: number } }

// Remapeamento de chaves com 'as'
type Getters<T> = {
  [P in keyof T as `get${Capitalize<string & P>}`]: () => T[P];
};

type UsuarioGetters = Getters<{ nome: string; idade: number }>;
// { getNome(): string; getIdade(): number }

// Excluir chaves por tipo
type StringKeysOnly<T> = {
  [P in keyof T as T[P] extends string ? P : never]: T[P];
};

type SomenteStrings = StringKeysOnly<{ nome: string; idade: number; email: string }>;
// { nome: string; email: string }
```

## Padroes Avancados

### Builder Pattern com Type Safety

```typescript
class QueryBuilder<TEntidade> {
  private tabela: string;
  private condicoes: string[] = [];
  private camposSelecionados: string[] = ["*"];
  private limite?: number;

  constructor(tabela: string) {
    this.tabela = tabela;
  }

  select<K extends keyof TEntidade>(...campos: K[]): this {
    this.camposSelecionados = campos as string[];
    return this;
  }

  where(campo: keyof TEntidade, valor: TEntidade[keyof TEntidade]): this {
    this.condicoes.push(`${String(campo)} = '${valor}'`);
    return this;
  }

  limit(n: number): this {
    this.limite = n;
    return this;
  }

  build(): string {
    let sql = `SELECT ${this.camposSelecionados.join(", ")} FROM ${this.tabela}`;
    if (this.condicoes.length > 0) {
      sql += ` WHERE ${this.condicoes.join(" AND ")}`;
    }
    if (this.limite) sql += ` LIMIT ${this.limite}`;
    return sql;
  }
}

// Uso com type safety
interface Produto { id: number; nome: string; preco: number; }

const query = new QueryBuilder<Produto>("produtos")
  .select("nome", "preco")
  .where("preco", 100)
  .limit(10)
  .build();
// SELECT nome, preco FROM produtos WHERE preco = '100' LIMIT 10
```

### Branded Types (Tipos Nominais)

```typescript
// Branded type para simular tipagem nominal
type Branded<T, B> = T & { __brand: B };

type UserId = Branded<string, "UserId">;
type OrderId = Branded<string, "OrderId">;

function criarUserId(id: string): UserId {
  return id as UserId;
}

function buscarUsuario(id: UserId): void {
  console.log(`Buscando usuario: ${id}`);
}

const uid = criarUserId("user-123");
buscarUsuario(uid); // OK

const oid = "order-456" as OrderId;
// buscarUsuario(oid); // Erro: OrderId nao e atribuivel a UserId

// Validacao em runtime
function validarUserId(id: string): UserId | null {
  if (id.startsWith("user-")) return id as UserId;
  return null;
}
```

```python
# Branded types em Python com NewType
from typing import NewType

UserId = NewType('UserId', str)
OrderId = NewType('OrderId', str)

def buscar_usuario(id: UserId) -> None:
    print(f"Buscando usuario: {id}")

uid = UserId("user-123")
buscar_usuario(uid)  # OK

# oid = OrderId("order-456")
# buscar_usuario(oid)  # mypy error: Argument 1 has incompatible type "OrderId"
```

### Decorator Types e Metadata

```typescript
// Decorator com metadata
function LogExecucao(
  target: any,
  propertyKey: string,
  descriptor: PropertyDescriptor
): PropertyDescriptor {
  const original = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`[${propertyKey}] chamado com:`, args);
    const resultado = original.apply(this, args);
    console.log(`[${propertyKey}] retornou:`, resultado);
    return resultado;
  };
  return descriptor;
}

class ServicoUsuario {
  @LogExecucao
  buscar(id: string): string {
    return `Usuario ${id}`;
  }
}
```

### Augmentacao de Modulos

```typescript
// Augmentar modulo Express
declare module "express" {
  interface Request {
    usuario?: { id: string; nome: string; role: string };
  }
}

// Uso
app.get("/perfil", (req, res) => {
  const usuario = req.usuario; // TypeScript reconhece
  res.json(usuario);
});

// Declaration merging com interfaces
interface Config {
  apiUrl: string;
}

interface Config {
  timeout: number;
}

// Resultado: { apiUrl: string; timeout: number }
```

## Programacao em Nivel de Tipo

### Aritmetica em Nivel de Tipo

```typescript
// Numeros em nivel de tipo (usando tuplas)
type Nat = [] | [any, ...any[]];

type Length<T extends any[]> = T["length"];

type Add<A extends any[], B extends any[]> = [...A, ...B]["length"];

type Tres = Length<[any, any, any]>; // 3
type Cinco = Add<[any, any], [any, any, any]>; // 5

// Booleanos em nivel de tipo
type Bool = true | false;
type Not<B extends Bool> = B extends true ? false : true;
type And<A extends Bool, B extends Bool> = A extends true ? B : false;
type Or<A extends Bool, B extends Bool> = A extends true ? true : B;

type A = Not<true>; // false
type B = And<true, false>; // false
type C = Or<true, false>; // true
```

### Tipos Condicionais Recursivos

```typescript
// Flatten recursivo
type Flatten<T> = T extends (infer U)[]
  ? U extends any[]
    ? Flatten<U>
    : U
  : T;

type DeepArray = number[][][];
type Flat = Flatten<DeepArray>; // number

// Deep Readonly recursivo
type DeepReadonly<T> = T extends object
  ? { readonly [P in keyof T]: DeepReadonly<T[P]> }
  : T;

interface Config {
  database: { host: string; port: number };
  cache: { enabled: boolean; ttl: number };
}

type ConfigReadonly = DeepReadonly<Config>;
// { readonly database: { readonly host: string; readonly port: number }; ... }

// Deep Pick recursivo
type DeepPick<T, K extends string> = T extends object
  ? {
      [P in keyof T as P extends K ? P : never]: T[P];
    } & {
      [P in keyof T as P extends string
        ? DeepPick<T[P], K> extends never ? never : P
        : never]: DeepPick<Extract<T[P], object>, K>;
    } extends infer O
    ? { [P in keyof O]: O[P] }
    : never;
```

### Manipulacao de Tuplas em Nivel de Tipo

```typescript
// Primeiro elemento
type First<T extends any[]> = T extends [infer F, ...any[]] ? F : never;

// Ultimo elemento
type Last<T extends any[]> = T extends [...any[], infer L] ? L : never;

// Cauda (todos exceto primeiro)
type Tail<T extends any[]> = T extends [any, ...infer Rest] ? Rest : [];

// Inverter tupla
type Reverse<T extends any[]> = T extends [infer F, ...infer Rest]
  ? [...Reverse<Rest>, F]
  : [];

type A = First<[string, number, boolean]>; // string
type B = Last<[string, number, boolean]>; // boolean
type C = Tail<[string, number, boolean]>; // [number, boolean]
type D = Reverse<[1, 2, 3]>; // [3, 2, 1]

// Filter em tupla
type Filter<T extends any[], U> = T extends [infer F, ...infer Rest]
  ? F extends U
    ? [F, ...Filter<Rest, U>]
    : Filter<Rest, U>
  : [];

type StringsOnly = Filter<[string, number, string, boolean], string>;
// [string, string]
```

### Inferencia de Tipo JSON

```typescript
type JsonValue = string | number | boolean | null | JsonObject | JsonArray;
interface JsonObject { [key: string]: JsonValue; }
interface JsonArray extends Array<JsonValue> {}

// Extrair todas as chaves de um tipo JSON
type JsonKeys<T, Prefix extends string = ""> = T extends object
  ? {
      [K in keyof T]: K extends string
        ? T[K] extends object
          ? JsonKeys<T[K], `${Prefix}${K}.`>
          : `${Prefix}${K}`
        : never;
    }[keyof T]
  : never;

interface Config {
  database: { host: string; port: number };
  debug: boolean;
}

type Chaves = JsonKeys<Config>;
// "database.host" | "database.port" | "debug"
```

## Configuracao do Compilador

### tsconfig.json Essencial

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "useUnknownInCatchVariables": true,
    "alwaysStrict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "incremental": true,
    "composite": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@utils/*": ["src/utils/*"],
      "@types/*": ["src/types/*"]
    }
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "**/*.test.ts"]
}
```

### Flags Strict Mode

| Flag | O que faz | Impacto |
|------|-----------|---------|
| `strict` | Ativa todas as flags strict | Recomendado sempre |
| `noImplicitAny` | Erro quando tipo e implicitamente `any` | Forca tipagem explicita |
| `strictNullChecks` | `null` e `undefined` sao tipos distintos | Previne erros de null reference |
| `strictFunctionTypes` | Verificacao contravariante de parametros | Mais seguranca em funcoes |
| `strictBindCallApply` | Tipos corretos para bind/call/apply | Previne erros em metodos |
| `strictPropertyInitialization` | Propriedades devem ser inicializadas | Previne undefined em classes |
| `noImplicitThis` | Erro quando `this` e implicitamente `any` | Seguranca em callbacks |
| `useUnknownInCatchVariables` | `catch` variables sao `unknown` | Forca type narrowing |

### Resolucao de Modulos

```
node (legacy):     node_modules + package.json "main"
node16/node18:     ESM/CJS baseado em "type" do package.json
bundler:           Otimizado para bundlers (Vite, esbuild, webpack)

Exemplo com paths:
import { helper } from "@/utils/helper";
// Resolvido para: src/utils/helper.ts
```

### Compilacao Incremental e Project References

```json
// tsconfig.base.json
{
  "compilerOptions": {
    "composite": true,
    "incremental": true,
    "tsBuildInfoFile": "./.tsbuildinfo"
  }
}

// packages/core/tsconfig.json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": { "outDir": "./dist" },
  "include": ["src"]
}

// packages/api/tsconfig.json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": { "outDir": "./dist" },
  "include": ["src"],
  "references": [{ "path": "../core" }]
}

// Compilar com referencias
// npx tsc --build packages/api
```

## Teste de Tipos

### tsd - Teste de Tipos

```typescript
// types.test.ts
import { expectType, expectError, expectAssignable } from "tsd";
import { primeiro, merge } from "./utils";

// Testar retorno de funcao generica
expectType<number | undefined>(primeiro([1, 2, 3]));
expectType<string | undefined>(primeiro(["a", "b"]));

// Testar merge
expectType<{ nome: string; idade: number }>(
  merge({ nome: "Ana" }, { idade: 30 })
);

// Testar que erro e lancado
expectError(primeiro(42)); // Argumento nao e array

// Testar assignability
expectAssignable<{ nome: string }>({ nome: "Ana", idade: 30 });
```

### expect-type

```typescript
import { expectTypeOf } from "expect-type";

expectTypeOf(primeiro([1, 2, 3])).toEqualTypeOf<number | undefined>();
expectTypeOf(primeiro(["a"])).toEqualTypeOf<string | undefined>();

// Testar que tipos NAO sao iguais
expectTypeOf<number>().not.toEqualTypeOf<string>();

// Testar propriedades
expectTypeOf<{ nome: string; idade: number }>().toHaveProperty("nome");
expectTypeOf<{ nome: string }>().not.toHaveProperty("email");

// Testar com branded types
expectTypeOf<UserId>().toMatchTypeOf<string>();
expectTypeOf<UserId>().not.toEqualTypeOf<string>();
```

### Runtime vs Compile-time

```typescript
// Compile-time check (type system)
function processarArray<T extends readonly unknown[]>(arr: T): T["length"] {
  return arr.length;
}

// Runtime check (validacao)
function validarUsuario(dados: unknown): dados is Usuario {
  return (
    typeof dados === "object" &&
    dados !== null &&
    "nome" in dados &&
    typeof (dados as any).nome === "string" &&
    "idade" in dados &&
    typeof (dados as any).idade === "number"
  );
}

// Combinar ambos: zod para runtime + TypeScript para compile-time
import { z } from "zod";

const UsuarioSchema = z.object({
  nome: z.string().min(2),
  idade: z.number().int().positive(),
  email: z.string().email(),
});

type Usuario = z.infer<typeof UsuarioSchema>;
// { nome: string; idade: number; email: string }

function criarUsuario(dados: unknown): Usuario {
  return UsuarioSchema.parse(dados); // Runtime validation + type inference
}
```

## Migracao de JavaScript para TypeScript

### Estrategia Passo a Passo

```
Fase 1: Setup Basico
├── Renomear .js para .ts (ou .tsx para React)
├── Adicionar tsconfig.json com strict: false
├── Corrigir erros de compilacao basicos
└── Adicionar allowJs: true para coexistencia

Fase 2: Tipagem Progressiva
├── Adicionar tipos em funcoes publicas (APIs)
├── Usar JSDoc para tipagem sem renomear arquivos
├── Ativar noImplicitAny gradualmente
└── Adicionar tipos em interfaces externas

Fase 3: Strict Mode
├── Ativar strictNullChecks
├── Corrigir null/undefined errors
├── Ativar strict: true
└── Refatorar codigo para ser type-safe

Fase 4: Otimizacao
├── Adicionar tipos genericos onde necessario
├── Criar tipos compartilhados em @types/
├── Configurar paths e aliases
└── Adicionar testes de tipo com tsd
```

### JSDoc como Ponte

```javascript
// JSDoc type annotations em arquivos .js

/**
 * @typedef {Object} Usuario
 * @property {string} nome
 * @property {number} idade
 * @property {string} email
 */

/**
 * Busca usuario por ID
 * @param {string} id - ID do usuario
 * @returns {Promise<Usuario|undefined>}
 */
async function buscarUsuario(id) {
  const res = await fetch(`/api/users/${id}`);
  return res.json();
}

/**
 * @template T
 * @param {T[]} arr
 * @returns {T|undefined}
 */
function primeiro(arr) {
  return arr[0];
}

/**
 * @param {import('express').Request} req
 * @param {import('express').Response} res
 */
function handler(req, res) {
  res.json({ status: "ok" });
}
```

### Armadilhas Comuns

| Problema | Causa | Solucao |
|----------|-------|---------|
| `any` implicito | `noImplicitAny` desativado | Ativar flag, adicionar tipos |
| `null` reference | `strictNullChecks` desativado | Ativar flag, usar optional chaining |
| `this` incorreto | Callbacks sem bind | Usar arrow functions ou bind |
| Importacao errada | `esModuleInterop` desativado | Ativar flag, usar import padrao |
| Tipos nao encontrados | Sem @types/pacote | Instalar `@types/nome-pacote` |
| JSX sem tipo | Extensao .js com JSX | Renomear para .tsx |
| Module resolution | Config incorreta | Usar `moduleResolution: "bundler"` |

## Referencias Cruzadas

- [[frontend]] - TypeScript no desenvolvimento frontend com React/Vue
- [[backend]] - TypeScript no backend com Express/NestJS
- [[testing-advanced]] - Testes de tipos e testes unitarios avancados
- [[design-patterns]] - Padroes de projeto com type safety
- [[api-design]] - Design de APIs com tipos seguros
