---
title: Concurrency in Rust
tags:
  - rust
  - concurrency
  - multithreading
created: 2026-06-10
updated: 2026-06-10
status: active
---

# Concurrency in Rust

Rust's approach to concurrency is centered on "Fearless Concurrency," leveraging the ownership system to prevent data races.

## Shared State and Synchronization

### Arc (Atomic Reference Counted)
`Arc<T>` provides shared ownership of a value of type `T`. It is a thread-safe version of `Rc<T>`, using atomic operations for reference counting. It allows multiple threads to hold a reference to the same data.

### Mutex and RwLock
Since `Arc` only provides immutable access, interior mutability is required for modification:
- **Mutex<T>** (Mutual Exclusion): Ensures only one thread can access the data at a time.
- **RwLock<T>** (Read-Write Lock): Allows multiple readers OR one writer.

Typical pattern: `Arc<Mutex<T>>`.

## Marker Traits: Send and Sync
These traits are the foundation of Rust's concurrency safety and are automatically implemented by the compiler.

### Send
A type is `Send` if ownership of the value can be transferred between threads. Most types are `Send`, but `Rc<T>` is not because its reference count is not atomic.

### Sync
A type is `Sync` if it is safe for the type to be referenced by multiple threads simultaneously. `T` is `Sync` if and only if `&T` is `Send`.

## Rust vs Go: Concurrency Models
| Feature | Rust | Go |
| :--- | :--- | :--- |
| **Core Primitive** | Threads / Async Tasks | Goroutines |
| **Communication** | Channels (`std::sync::mpsc`) | Channels (Native) |
| **Memory Safety** | Compile-time (Borrow Checker) | Runtime (Garbage Collector) |
| **State Sharing** | `Arc<Mutex<T>>` | Shared memory (requires manual mutex/channels) |
| **Overhead** | Low (Zero-cost) | Low (Green threads/stack management) |

Rust prioritizes the elimination of data races at compile time, whereas Go provides high-level primitives to manage concurrency but allows race conditions at runtime.

[[02-Engenharia-de-Software]]
