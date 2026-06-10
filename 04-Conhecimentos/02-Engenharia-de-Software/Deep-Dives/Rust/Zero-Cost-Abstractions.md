---
title: Zero-Cost Abstractions
tags:
  - rust
  - compiler-optimization
  - generics
created: 2026-06-10
updated: 2026-06-10
status: active
---

# Zero-Cost Abstractions

The principle of "zero-cost abstractions" in Rust means:
1. What you don't use, you don't pay for.
2. What you do use, you couldn't possibly implement any better by hand.

## Generics and Monomorphization
Rust implements generics through monomorphization. Instead of using type erasure (like Java's `Object`), the compiler generates specialized code for every concrete type used.

### The Process
1. The compiler analyzes the generic function calls.
2. For each unique set of type arguments, it generates a concrete version of the function.
3. The linker removes unused versions.

**Trade-off**: This increases binary size (code bloat) but allows for aggressive inlining and optimization, as the compiler knows the exact size and alignment of the types.

## Trait-Based Polymorphism
Rust provides two ways to handle polymorphism:

### Static Dispatch (Generics)
Using trait bounds, the compiler generates specialized code at compile time.
```rust
fn print_it<T: Display>(value: T) {
    println!("{}", value);
}
```
This is resolved at compile time, allowing for zero overhead.

### Dynamic Dispatch (Trait Objects)
Using `dyn Trait`, Rust uses a vtable (virtual method table) to resolve methods at runtime.
```rust
fn print_it(value: &dyn Display) {
    println!("{}", value);
}
```
This involves a pointer dereference and a lookup in the vtable, introducing a small runtime cost.

## Iterators and Higher-Order Functions
Rust's iterators (e.g., `.map()`, `.filter()`, `.fold()`) are designed to be zero-cost. The compiler typically collapses these chains into tight loops, often performing the same optimizations as a manual `for` loop.

[[02-Engenharia-de-Software]]
