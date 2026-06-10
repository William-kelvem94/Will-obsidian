---
tags: [compiler-design, llvm, software-engineering, low-level]
status: complete
created: 2026-06-10
---

# Compiler Design and LLVM

## 1. Lexical Analysis (Lexing)
Lexing is the process of converting a raw stream of characters into a sequence of **tokens**.

### Finite Automata and Regular Expressions
- **Regular Expressions (RE):** Define the patterns for tokens (keywords, identifiers, literals).
- **Deterministic Finite Automata (DFA):** The engine used to recognize these patterns. A lexer typically implements a DFA that transitions between states based on the input character.
- **Tokenization Process:**
    - **Scanning:** Reading characters.
    - **Buffering:** Using a dual-buffer system to minimize I/O.
    - **Tokenization:** Grouping characters into tokens (e.g., `int` $\rightarrow$ `TOKEN_KEYWORD_INT`).

## 2. Syntax Analysis (Parsing)
Parsing transforms the token stream into a structured representation, typically an **Abstract Syntax Tree (AST)**.

### Grammar and Formalisms
- **Context-Free Grammars (CFG):** Defined using Backus-Naur Form (BNF).
- **Parsing Strategies:**
    - **Top-Down (LL):** Starts from the root and works down. Predicts the next production.
    - **Bottom-Up (LR/LALR):** Starts from the leaves and "reduces" them to higher-level constructs. More powerful than LL.
- **Recursive Descent:** A common top-down parsing technique where each non-terminal in the grammar is implemented as a function.

### The Abstract Syntax Tree (AST)
- The AST strips away syntactic sugar and purely structural markers (like parentheses) to focus on the hierarchical logic of the program.

## 3. Semantic Analysis
Ensures the AST is logically consistent and adheres to the language's rules.

- **Symbol Table Management:** A data structure mapping identifiers to their properties (type, scope, memory location).
- **Type Checking:** Verifying that operations are performed on compatible types (e.g., preventing adding a string to an integer).
- **Control Flow Analysis:** Ensuring all paths return a value or that break/continue statements are within loops.

## 4. Intermediate Representation (IR)
Compilers use an IR to decouple the frontend (source language) from the backend (target architecture).

### LLVM IR (The Three-Address Code)
LLVM uses a static single assignment (SSA) based IR.
- **SSA Form:** Every variable is assigned exactly once. If a variable is modified, a new version (e.g., `%x.1`, `%x.2`) is created.
- **Instruction Set:** A RISC-like set of instructions (e.g., `alloca`, `load`, `store`, `add`).
- **Typed IR:** LLVM IR is strongly typed, facilitating optimization.

## 5. Optimization Passes
Optimizations are applied to the IR in a pipeline.

### Local and Global Optimizations
- **Constant Folding:** Evaluating expressions at compile time (e.g., `3 + 4` $\rightarrow$ `7`).
- **Dead Code Elimination (DCE):** Removing instructions that do not affect the program output.
- **Inlining:** Replacing a function call with the actual body of the function to reduce overhead.
- **Loop Unrolling:** Expanding loops to reduce branch overhead and increase instruction-level parallelism.
- **Common Subexpression Elimination (CSE):** Identifying and reusing the result of a repeated computation.

## 6. LLVM Backend Architecture
The backend maps the optimized IR to machine-specific code.

### Target Machine Description
- **Instruction Selection:** Mapping IR instructions to specific target ISA instructions.
- **Register Allocation:** Mapping an infinite number of virtual registers (from SSA) to a finite number of physical hardware registers (using graph coloring algorithms).
- **Instruction Scheduling:** Ordering instructions to minimize pipeline stalls and maximize throughput.
- **Code Emission:** Generating the final binary object files (ELF, Mach-O, PE).

---
**Related Notes:**
- [[Memory-Management-Low-Level]]
- [[Type-Theory-and-Category-Theory]]
