---
title: Unsafe Rust and FFI
tags:
  - rust
  - unsafe
  - ffi
  - systems-programming
created: 2026-06-10
updated: 2026-06-10
status: active
---

# Unsafe Rust and FFI

`unsafe` Rust is a superpower that allows the programmer to bypass some of the compiler's safety checks. It does not disable the borrow checker, but it grants five "superpowers".

## The Five Superpowers of Unsafe
1. **Dereference a raw pointer**: `*const T` and `*mut T`.
2. **Call an unsafe function** or an unsafe method.
3. **Access or modify a mutable static variable**.
4. **Implement an unsafe trait**.
5. **Access fields of a `union`**.

## Raw Pointers
Unlike references (`&T`), raw pointers:
- Are not guaranteed to be valid.
- Can be null.
- Do not have lifetimes associated with them.
- Do not perform automatic cleanup.

### Pointer Arithmetic
Unsafe allows performing arithmetic on pointers, which is essential for implementing low-level data structures like `Vec` or `HashMap`.

## Foreign Function Interface (FFI)
FFI is the mechanism used to call functions written in other languages (usually C).

### Interacting with C
To call a C function, you must:
1. Declare the function signature using an `extern` block.
2. Use `#[no_mangle]` in the C side to prevent name mangling.
3. Ensure types are compatible (using `std::os::raw` or `libc`).

```rust
extern "C" {
    fn abs(input: i32) -> i32;
}

fn main() {
    unsafe {
        println!("Absolute value of -42 is {}", abs(-42));
    }
}
```

### Safety Boundaries
The gold standard for `unsafe` is to wrap it in a **Safe Abstraction**. The internal `unsafe` logic should be encapsulated in a safe API that maintains Rust's safety invariants, ensuring that the user of the library cannot cause undefined behavior.

[[02-Engenharia-de-Software]]
