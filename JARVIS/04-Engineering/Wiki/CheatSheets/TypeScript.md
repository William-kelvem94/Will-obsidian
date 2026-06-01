---
title: "TypeScript — Cheat Sheet"
description: "Guia de referência rápida para TypeScript — tipos, configuração, ferramentas e padrões"
tags: [cheatsheet, typescript, javascript, linguagem, jarvis-engenharia]
updated: 2026-06-01
date: 2026-05-16
---

# TypeScript — Cheat Sheet

Referência completa do sistema de tipos do TypeScript, configuração de projetos e padrões usados no ecossistema.

---

## 📋 Sumário

- [⚙️ Setup e Configuração](#-setup-e-configuração)
- [📝 Tipos Básicos](#-tipos-básicos)
- [🧩 Interfaces vs Types](#-interfaces-vs-types)
- [🔀 Unions e Literals](#-unions-e-literals)
- [🧬 Generics](#-generics)
- [🌀 Tipos Avançados](#-tipos-avançados)
- [🔍 Type Inference e Narrowing](#-type-inference-e-narrowing)
- [🧪 Utility Types](#-utility-types)
- [🛠️ tsconfig.json Essencial](#-tsconfigjson-essencial)
- [🔧 Ferramentas](#-ferramentas)
- [⚛️ React com TypeScript](#-react-com-typescript)
- [🌐 Node.js com TypeScript](#-nodejs-com-typescript)
- [🎯 Padrões Comuns](#-padrões-comuns)
- [🔄 Migração de JavaScript](#-migração-de-javascript)
- [🐛 Troubleshooting](#-troubleshooting)
- [🔗 Relacionados](#-relacionados)

---

## ⚙️ Setup e Configuração

```bash
# Instalar
npm install -g typescript
npm install -D typescript @types/node

# Inicializar (cria tsconfig.json)
npx tsc --init

# Compilar
npx tsc                         # Compila tudo
npx tsc --watch                 # Modo watch
npx tsc --noEmit                # Só checa tipos
npx tsc --project tsconfig.json

# Executar sem compilar (tsx)
npm install -D tsx
npx tsx src/index.ts
npx tsx watch src/index.ts      # Watch + execução

# ts-node (alternativa)
npm install -D ts-node
npx ts-node src/index.ts
```

---

## 📝 Tipos Básicos

```typescript
// Primitivos
let nome: string = "Alice";
let idade: number = 30;
let ativo: boolean = true;
let nulo: null = null;
let indefinido: undefined = undefined;
let qualquer: any = "pode ser qualquer coisa";
let desconhecido: unknown = "precisa de type guard";

// Arrays
let nums: number[] = [1, 2, 3];
let strs: Array<string> = ["a", "b"];
let readonly: readonly number[] = [1, 2];
let tuple: [string, number] = ["Alice", 30];
let namedTuple: [nome: string, idade: number] = ["Bob", 25];

// Objetos
let pessoa: { nome: string; idade: number } = { nome: "Alice", idade: 30 };

// Funções
function soma(a: number, b: number): number {
    return a + b;
}

const multiplica = (a: number, b: number): number => a * b;

// Callback
function executa(fn: (x: number) => void): void {
    fn(42);
}

// Overloads de função
function processar(x: number): number;
function processar(x: string): string;
function processar(x: number | string): number | string {
    if (typeof x === "number") return x * 2;
    return x.toUpperCase();
}
```

---

## 🧩 Interfaces vs Types

```typescript
// Interface (recomendada para objetos/classes)
interface Usuario {
    id: number;
    nome: string;
    email?: string;           // Opcional
    readonly criadoEm: Date;  // Read-only
}

// Type (recomendado para unions, tuples, primitivos)
type Status = "ativo" | "inativo" | "pendente";
type ID = string | number;
type Callback<T> = (data: T) => void;

// Diferenças principais:

// 1. Declaration merging (só interface)
interface Pessoa {
    nome: string;
}
interface Pessoa {
    idade: number;
}
// Resultado: Pessoa tem nome + idade

// 2. Extends vs Intersection
interface Admin extends Usuario {
    role: "admin";
}

type SuperUser = Usuario & { role: "superadmin" };

// 3. Mapped types (só type)
type Readonly<T> = { readonly [K in keyof T]: T[K] };
```

---

## 🔀 Unions e Literals

```typescript
// Union types
type Resultado = string | null;
type ID = number | string;

// Discriminated unions
type EstadoRequisicao =
    | { status: "idle" }
    | { status: "loading" }
    | { status: "success"; data: unknown }
    | { status: "error"; error: Error };

function tratarEstado(estado: EstadoRequisicao) {
    switch (estado.status) {
        case "idle":
            break;
        case "loading":
            console.log("carregando");
            break;
        case "success":
            console.log(estado.data);  // TS sabe que data existe
            break;
        case "error":
            console.error(estado.error);
            break;
    }
}

// Template literal types
type EventName = `on${Capitalize<string>}`;
type Color = "red" | "green" | "blue";
type Brightness = "light" | "dark";
type ThemeColor = `${Brightness}-${Color}`;  // "light-red" | "light-green" | ...

// Literal types
type Tamanho = "pequeno" | "médio" | "grande";
const tamanho: Tamanho = "médio";
```

---

## 🧬 Generics

```typescript
// Função genérica
function primeiro<T>(arr: T[]): T | undefined {
    return arr[0];
}

const num = primeiro([1, 2, 3]);     // number
const str = primeiro(["a", "b"]);    // string

// Múltiplos parâmetros
function par<A, B>(a: A, b: B): [A, B] {
    return [a, b];
}

// Constraints
function getProp<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}

// Inferência de tipo em callback
function mapTo<A, B>(arr: A[], fn: (item: A) => B): B[] {
    return arr.map(fn);
}

// Classe genérica
class Container<T> {
    private value: T;

    constructor(value: T) {
        this.value = value;
    }

    get(): T {
        return this.value;
    }

    set(value: T): void {
        this.value = value;
    }
}

// Factory function genérica
function createPair<T>(a: T, b: T): [T, T] {
    return [a, b];
}

// Inferência em higher-order functions
function curried<T, U>(fn: (a: T, b: U) => unknown) {
    return (a: T) => (b: U) => fn(a, b);
}
```

---

## 🌀 Tipos Avançados

### Conditional Types

```typescript
type IsString<T> = T extends string ? "yes" : "no";

type A = IsString<string>;   // "yes"
type B = IsString<number>;   // "no"

// Distributive conditional types
type ToArray<T> = T extends unknown ? T[] : never;
type Result = ToArray<string | number>;  // string[] | number[]

// Infer (extrair tipos)
type ReturnType<T> = T extends (...args: unknown[]) => infer R ? R : never;
type PromiseValue<T> = T extends Promise<infer U> ? U : T;

type Fn = () => string;
type R = ReturnType<Fn>;           // string
type PV = PromiseValue<Promise<number>>;  // number
```

### Mapped Types

```typescript
type Readonly<T> = {
    readonly [K in keyof T]: T[K];
};

type Optional<T> = {
    [K in keyof T]?: T[K];
};

type Nullable<T> = {
    [K in keyof T]: T[K] | null;
};

// Com remoção de modificadores
type Mutable<T> = {
    -readonly [K in keyof T]: T[K];
};

type Required<T> = {
    [K in keyof T]-?: T[K];
};

// Filtrar chaves
type StringKeys<T> = {
    [K in keyof T as T[K] extends string ? K : never]: T[K];
};

// Template literal com mapped
type Getters<T> = {
    [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
```

### Brand Types (tipos nominais)

```typescript
// TypeScript tem tipagem estrutural, mas podemos criar tipos nominais
type Brand<K, T> = K & { __brand: T };

type UserId = Brand<string, "UserId">;
type OrderId = Brand<string, "OrderId">;

function getUser(id: UserId) { /* ... */ }
function getOrder(id: OrderId) { /* ... */ }

const uid = "abc" as UserId;
const oid = "xyz" as OrderId;

getUser(uid);  // OK
getUser(oid);  // Erro de tipo!

// Factory segura
function createUserId(raw: string): UserId {
    if (!raw.match(/^usr_/)) throw new Error("ID inválido");
    return raw as UserId;
}
```

### Assertion Functions

```typescript
function assert(condition: unknown, msg?: string): asserts condition {
    if (!condition) throw new Error(msg ?? "Assertion failed");
}

function assertString(val: unknown): asserts val is string {
    if (typeof val !== "string") throw new Error("not a string");
}

function shout(val: unknown): string {
    assertString(val);
    return val.toUpperCase();  // TS sabe que é string
}

// Type predicate
function isString(val: unknown): val is string {
    return typeof val === "string";
}

function process(val: string | number) {
    if (isString(val)) {
        console.log(val.length);  // TS sabe que é string
    }
}
```

---

## 🔍 Type Inference e Narrowing

```typescript
// Type narrowing com typeof
function process(val: string | number) {
    if (typeof val === "string") {
        console.log(val.toUpperCase());
    } else {
        console.log(val.toFixed(2));
    }
}

// Narrowing com instanceof
class APIError extends Error {
    constructor(public statusCode: number) {
        super("API error");
    }
}

function handleError(err: Error) {
    if (err instanceof APIError) {
        console.log(err.statusCode);
    }
}

// Narrowing com in
interface Bird { fly(): void; }
interface Fish { swim(): void; }

function move(animal: Bird | Fish) {
    if ("fly" in animal) {
        animal.fly();
    } else {
        animal.swim();
    }
}

// Discriminated union narrowing
type Shape =
    | { kind: "circle"; radius: number }
    | { kind: "square"; side: number }
    | { kind: "triangle"; base: number; height: number };

function area(shape: Shape): number {
    switch (shape.kind) {
        case "circle":
            return Math.PI * shape.radius ** 2;
        case "square":
            return shape.side ** 2;
        case "triangle":
            return (shape.base * shape.height) / 2;
        default:
            const _exhaustive: never = shape;
            return _exhaustive;
    }
}

// satisfies operator (TS 4.9+)
type Colors = "red" | "green" | "blue";
type Config = Record<string, Colors>;

const config = {
    primary: "red",
    secondary: "blue",
} satisfies Config;  // Verifica sem ampliar o tipo
// config.primary é literal "red", não string
```

---

## 🧪 Utility Types

```typescript
interface Usuario {
    id: number;
    nome: string;
    email: string;
    senha: string;
    criadoEm: Date;
}

// Partial<T> — todos opcionais
type PartialUser = Partial<Usuario>;

// Required<T> — todos obrigatórios
type RequiredUser = Required<PartialUser>;

// Readonly<T> — todos readonly
type ReadonlyUser = Readonly<Usuario>;

// Pick<T, K> — seleciona chaves
type PublicInfo = Pick<Usuario, "id" | "nome" | "email">;

// Omit<T, K> — remove chaves
type CreateUser = Omit<Usuario, "id" | "criadoEm">;

// Record<K, T> — dicionário tipado
type UserMap = Record<string, Usuario>;

// Exclude<T, U> — remove tipos de uma union
type Status = "ativo" | "inativo" | "pendente";
type Active = Exclude<Status, "inativo" | "pendente">;  // "ativo"

// Extract<T, U> — extrai tipos de uma union
type OnlyStrings = Extract<string | number | boolean, string>;  // string

// NonNullable<T> — remove null e undefined
type NonNull = NonNullable<string | null | undefined>;  // string

// Parameters<T> — parâmetros de função
type FnParams = Parameters<(a: string, b: number) => void>;  // [string, number]

// ReturnType<T> — retorno de função
type FnReturn = ReturnType<() => Promise<string>>;  // Promise<string>

// Awaited<T> — desembrulha Promise (TS 4.5+)
type Resolved = Awaited<Promise<Promise<string>>>;  // string

// InstanceType<T> — tipo da instância
class Foo {}
type FooInstance = InstanceType<typeof Foo>;

// ThisParameterType<T>
// OmitThisParameter<T>

// Capitalize / Uncapitalize / Uppercase / Lowercase
type Upper = Uppercase<"hello">;  // "HELLO"
type Capital = Capitalize<"hello">;  // "Hello"
```

---

## 🛠️ tsconfig.json Essencial

```json
{
    "compilerOptions": {
        // Target
        "target": "ES2022",
        "module": "ESNext",
        "moduleResolution": "bundler",
        "lib": ["ES2022", "DOM", "DOM.Iterable"],

        // Output
        "outDir": "./dist",
        "rootDir": "./src",
        "declaration": true,
        "declarationMap": true,
        "sourceMap": true,

        // Strict
        "strict": true,
        "noUncheckedIndexedAccess": true,
        "noImplicitOverride": true,
        "noPropertyAccessFromIndexSignature": true,

        // Module resolution
        "baseUrl": ".",
        "paths": {
            "@/*": ["./src/*"]
        },
        "resolveJsonModule": true,
        "allowImportingTsExtensions": true,
        "noEmit": true,

        // Interop
        "esModuleInterop": true,
        "forceConsistentCasingInFileNames": true,
        "isolatedModules": true,
        "verbatimModuleSyntax": true,

        // Extra
        "skipLibCheck": true,
        "erasableSyntaxOnly": true
    },
    "include": ["src"],
    "exclude": ["node_modules", "dist", "**/*.spec.ts"]
}
```

### Configurações por cenário

```jsonc
// Para bibliotecas
{
    "compilerOptions": {
        "declaration": true,
        "declarationMap": true,
        "sourceMap": true
    }
}

// Para apps Node.js
{
    "compilerOptions": {
        "types": ["node"],
        "module": "commonjs" // ou "Node16" com package.json "type": "module"
    }
}

// Para React (Vite)
{
    "compilerOptions": {
        "jsx": "react-jsx",
        "jsxImportSource": "react"
    }
}
```

---

## 🔧 Ferramentas

```bash
# tsc: compilador oficial
npx tsc --noEmit --watch

# tsx: executar TS diretamente (mais rápido que ts-node)
npx tsx src/server.ts
npx tsx watch src/server.ts

# ts-node: alternativa madura
npx ts-node --esm src/index.ts

# tsc-alias: resolve path aliases
npm install -D tsc-alias
# package.json: "build": "tsc && tsc-alias"

# typecheck: lint + types
npm install -D @arethetypeswrong/cli
npx attw --pack .

# ts-blank-space: remove tipos sem reescrever
npm install -D ts-blank-space
npx ts-blank-space src/ dist/

# tsup: bundle rápido (esbuild)
npm install -D tsup
npx tsup src/index.ts --dts

# unbuild: outro bundle (Rollup + mkdist)
npm install -D unbuild
```

### Linter + Formatter

```bash
npm install -D @typescript-eslint/parser @typescript-eslint/eslint-plugin eslint prettier eslint-config-prettier
```

```jsonc
// .eslintrc.json
{
    "parser": "@typescript-eslint/parser",
    "plugins": ["@typescript-eslint"],
    "extends": [
        "eslint:recommended",
        "plugin:@typescript-eslint/recommended",
        "prettier"
    ],
    "rules": {
        "@typescript-eslint/no-explicit-any": "warn",
        "@typescript-eslint/no-unused-vars": ["error", { "argsIgnorePattern": "^_" }],
        "@typescript-eslint/explicit-function-return-type": "warn"
    }
}
```

```bash
npx eslint src/
npx prettier --check src/
npx prettier --write src/
```

---

## ⚛️ React com TypeScript

```typescript
// Componente funcional
interface ButtonProps {
    label: string;
    variant?: "primary" | "secondary";
    disabled?: boolean;
    onClick: () => void;
}

export function Button({ label, variant = "primary", disabled, onClick }: ButtonProps) {
    return (
        <button
            className={`btn btn-${variant}`}
            disabled={disabled}
            onClick={onClick}
        >
            {label}
        </button>
    );
}

// Componente com children
interface CardProps {
    title: string;
    children: React.ReactNode;
}

export function Card({ title, children }: CardProps) {
    return (
        <div className="card">
            <h2>{title}</h2>
            {children}
        </div>
    );
}

// Event handlers
export function Input() {
    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        console.log(e.target.value);
    };

    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" onChange={handleChange} />
        </form>
    );
}

// Hooks tipados
function useLocalStorage<T>(key: string, initial: T) {
    const [value, setValue] = useState<T>(() => {
        const stored = localStorage.getItem(key);
        return stored ? (JSON.parse(stored) as T) : initial;
    });

    useEffect(() => {
        localStorage.setItem(key, JSON.stringify(value));
    }, [key, value]);

    return [value, setValue] as const;
}

// useReducer
interface State {
    count: number;
    step: number;
}

type Action =
    | { type: "increment" }
    | { type: "decrement" }
    | { type: "setStep"; payload: number };

function reducer(state: State, action: Action): State {
    switch (action.type) {
        case "increment":
            return { ...state, count: state.count + state.step };
        case "decrement":
            return { ...state, count: state.count - state.step };
        case "setStep":
            return { ...state, step: action.payload };
    }
}

// Context tipado
interface AuthContextType {
    user: Usuario | null;
    login: (email: string, senha: string) => Promise<void>;
    logout: () => void;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function useAuth(): AuthContextType {
    const ctx = useContext(AuthContext);
    if (!ctx) throw new Error("useAuth must be used within AuthProvider");
    return ctx;
}

// forwardRef com genéricos
const FancyInput = forwardRef<HTMLInputElement, { label: string }>(
    ({ label }, ref) => (
        <div>
            <label>{label}</label>
            <input ref={ref} />
        </div>
    )
);

// Generic component props
interface ListProps<T> {
    items: T[];
    renderItem: (item: T) => React.ReactNode;
}

function List<T>({ items, renderItem }: ListProps<T>) {
    return <ul>{items.map(renderItem)}</ul>;
}

// Uso: <List items={users} renderItem={(u) => <li>{u.name}</li>} />
```

---

## 🌐 Node.js com TypeScript

```typescript
import { createServer, IncomingMessage, ServerResponse } from "node:http";
import { readFile } from "node:fs/promises";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

// __dirname em ESM
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Express com tipos
import express, { Request, Response, NextFunction, RequestHandler } from "express";

const app = express();

// Tipar req.params, req.query, req.body
interface UserParams {
    id: string;
}

interface CreateUserBody {
    nome: string;
    email: string;
}

// Tipagem explícita
app.get("/users/:id", (req: Request<UserParams>, res: Response) => {
    const { id } = req.params;
    res.json({ id });
});

app.post("/users", (req: Request<{}, {}, CreateUserBody>, res: Response) => {
    const { nome, email } = req.body;
    res.status(201).json({ nome, email });
});

// Middleware tipado
function authMiddleware(req: Request, res: Response, next: NextFunction): void {
    const token = req.headers.authorization;
    if (!token) {
        res.status(401).json({ error: "Unauthorized" });
        return;
    }
    (req as any).user = { id: 1 };  // ou estender Request
    next();
}

// Estender Request
declare global {
    namespace Express {
        interface Request {
            user?: { id: number; name: string };
        }
    }
}

// Com async
function asyncHandler(fn: RequestHandler): RequestHandler {
    return (req, res, next) => {
        Promise.resolve(fn(req, res, next)).catch(next);
    };
}

app.get(
    "/data",
    asyncHandler(async (req: Request, res: Response) => {
        const data = await readFile("data.json", "utf-8");
        res.json(JSON.parse(data));
    })
);

// ENV tipado com Zod
import { z } from "zod";

const EnvSchema = z.object({
    PORT: z.coerce.number().default(3000),
    DATABASE_URL: z.string().url(),
    NODE_ENV: z.enum(["development", "production", "test"]),
});

const env = EnvSchema.parse(process.env);
export default env;
```

---

## 🎯 Padrões Comuns

### Discriminated Unions (Exaustivo)

```typescript
type Result<T, E = Error> =
    | { success: true; data: T }
    | { success: false; error: E };

async function tryCatch<T>(fn: () => Promise<T>): Promise<Result<T>> {
    try {
        const data = await fn();
        return { success: true, data };
    } catch (error) {
        return { success: false, error: error as Error };
    }
}

function handleResult<T>(result: Result<T>) {
    if (result.success) {
        console.log(result.data);
    } else {
        console.error(result.error);
    }
}
```

### Builder Pattern

```typescript
class QueryBuilder<T> {
    private conditions: string[] = [];
    private limit?: number;

    where<K extends keyof T>(field: K, value: T[K]): this {
        this.conditions.push(`${String(field)} = ${value}`);
        return this;
    }

    take(n: number): this {
        this.limit = n;
        return this;
    }

    build(): string {
        let sql = `SELECT * FROM table`;
        if (this.conditions.length > 0) {
            sql += ` WHERE ${this.conditions.join(" AND ")}`;
        }
        if (this.limit !== undefined) {
            sql += ` LIMIT ${this.limit}`;
        }
        return sql;
    }
}
```

### Singleton com Genéricos

```typescript
class Singleton<T> {
    private static instances = new Map<string, unknown>();

    static getInstance<T>(key: string, factory: () => T): T {
        if (!this.instances.has(key)) {
            this.instances.set(key, factory());
        }
        return this.instances.get(key) as T;
    }
}

const db = Singleton.getInstance("db", () => new Database());
```

### Type-Safe Event Emitter

```typescript
type EventMap = {
    userLogin: { userId: string; timestamp: Date };
    error: { message: string; code: number };
    dataLoaded: unknown[];
};

class TypedEmitter {
    private listeners = new Map<keyof EventMap, Set<Function>>();

    on<K extends keyof EventMap>(event: K, listener: (data: EventMap[K]) => void): void {
        if (!this.listeners.has(event)) this.listeners.set(event, new Set());
        this.listeners.get(event)!.add(listener);
    }

    emit<K extends keyof EventMap>(event: K, data: EventMap[K]): void {
        const listeners = this.listeners.get(event);
        if (listeners) {
            listeners.forEach((fn) => fn(data));
        }
    }

    off<K extends keyof EventMap>(event: K, listener: (data: EventMap[K]) => void): void {
        this.listeners.get(event)?.delete(listener);
    }
}
```

---

## 🔄 Migração de JavaScript

### Estratégia gradual

```bash
# 1. Adicionar TypeScript ao projeto
npm install -D typescript @types/node
npx tsc --init

# 2. tsconfig.js tolerante
```

```json
{
    "compilerOptions": {
        "allowJs": true,          // Permite arquivos .js
        "checkJs": false,         // Não checa .js (começar assim)
        "noEmit": true,
        "strict": false,          // Começar sem strict
        "skipLibCheck": true
    },
    "include": ["src"]
}
```

```typescript
// 3. Renomear .js para .ts gradualmente
// src/utils.js → src/utils.ts

// 4. Usar @ts-check em arquivos .js
// @ts-check

// 5. Declare modules para libs sem tipos
// src/types.d.ts
declare module "lib-sem-tipos" {
    export function fazAlgo(x: number): string;
    export const versao: string;
}

// 6. Ativar strict gradualmente
// strict: false → strictNullChecks: true → strict: true

// 7. any explícito para código não migrado
let dados: any = getUnsafe();
// Refatorar depois: unknown + type guard
```

---

## 🐛 Troubleshooting

### Issue: "Cannot find module" ou path alias não funciona

```bash
# tsconfig.json tem paths, mas tsc não resolve em runtime
# Solução: tsc-alias ou tsconfig-paths
```

```bash
npm install -D tsc-alias tsconfig-paths
# package.json: "build": "tsc && tsc-alias"
# runtime: node -r tsconfig-paths/register dist/index.js
```

### Issue: "This expression is not callable" com union

```typescript
// Causa: TypeScript não sabe qual tipo da union está sendo chamado
type Fn = ((x: number) => void) | ((x: string) => void);

// Solução: type guard
function callFn(fn: Fn, arg: number | string) {
    if (typeof arg === "number") {
        (fn as (x: number) => void)(arg);
    }
}

// Ou usar overloads
function callFn(fn: (x: number) => void, arg: number): void;
function callFn(fn: (x: string) => void, arg: string): void;
function callFn(fn: any, arg: any): void {
    fn(arg);
}
```

### Issue: "TS2742 — The inferred type of X cannot be named"

```bash
# Causa: tipo inferido usa tipo não exportado
# Solução: exportar explicitamente ou usar explicit type annotation

export function createUser() {
    return { id: 1, name: "Alice" as const };
}
// Erro: tipo inferido { id: number; name: "Alice" } não pode ser nomeado

// Solução:
export type User = { id: number; name: "Alice" };
export function createUser(): User {
    return { id: 1, name: "Alice" };
}
```

### Issue: Erro com "cannot be used as a JSX component"

```typescript
// Causa: retorno do componente não é compatível
// Solução: usar React.FC ou tipar retorno como JSX.Element

const Button: React.FC<{ label: string }> = ({ label }) => {
    return <button>{label}</button>;
};

// Ou
function Button({ label }: { label: string }): JSX.Element {
    return <button>{label}</button>;
}
```

### Issue: "Type instantiation is excessively deep"

```bash
# Causa: tipo recursivo muito profundo
# Solução: simplificar, usar interface ao invés de type, limitar recursão

# Exemplo problemático:
type DeepReadonly<T> = {
    readonly [K in keyof T]: DeepReadonly<T[K]>;
};

# Solução: limitar profundidade
type DeepReadonly<T, Depth extends number = 5> = Depth extends 0
    ? T
    : { readonly [K in keyof T]: DeepReadonly<T[K], Prev[Depth]> };
```

---

## 🔗 Relacionados

- [TypeScript Docs](https://www.typescriptlang.org/docs/)
- [TypeScript Playground](https://www.typescriptlang.org/play/)
- [[skills/02-software-engineering/frontend|Frontend Skills]]
- [[JARVIS/04-Engineering/Wiki/CheatSheets/Next.js|Next.js Cheat Sheet]]
- [[JARVIS/04-Engineering/Wiki/CheatSheets/Prisma|Prisma Cheat Sheet]]

[[JARVIS/README|← Voltar ao Command Center]]
