---
title: Ownership and Borrowing Deep Dive
tags:
  - rust
  - memory-management
  - systems-programming
created: 2026-06-10
updated: 2026-06-10
status: active
---

# Ownership and Borrowing Deep Dive

## Ownership Model
Rust's memory management is based on three core rules:
1. Each value in Rust has a variable that's called its owner.
2. There can only be one owner at a time.
3. When the owner goes out of scope, the value is dropped.

### Move Semantics
When a variable is assigned to another or passed to a function, ownership is transferred (moved) by default for types that do not implement the `Copy` trait. This prevents double-free errors.

```rust
let s1 = String::from("hello");
let s2 = s1; // s1 is moved to s2. s1 is now invalid.
```

## Borrowing and the Borrow Checker
Borrowing allows access to data without taking ownership, utilizing references (`&T` for shared and `&mut T` for exclusive).

### The Borrowing Rules
The borrow checker enforces these invariants at compile time:
1. Either one mutable reference OR any number of immutable references.
2. References must always be valid.

### Aliasing and Mutation
The "aliasing + mutation = danger" principle is the core of Rust's safety. By ensuring that a mutable reference is unique, Rust eliminates data races at compile time.

## Lifetimes (`'a`)
Lifetimes are a static analysis tool used by the compiler to ensure that no reference outlives the data it points to.

### Lifetime Elision
The compiler applies default rules to omit lifetime annotations in common patterns:
- Each input parameter gets its own lifetime.
- If there is exactly one input lifetime, that lifetime is assigned to all output lifetimes.
- If there are multiple input lifetimes, but one is `&self` or `&mut self`, the lifetime of `self` is assigned to all output lifetimes.

### Variance
Variance describes how sub-types (in Rust, this primarily applies to lifetimes) relate to each other.
- **Covariance**: If `'a: 'b` (a outlives b), then `T<'a>` can be used where `T<'b>` is expected. `&'a T` is covariant over `'a`.
- **Contravariance**: The opposite of covariance. Function arguments are contravariant.
- **Invariance**: Neither covariant nor contravariant. `&mut T` is invariant over `T` to prevent replacing a longer-lived reference with a shorter-lived one.

[[02-Engenharia-de-Software]]
