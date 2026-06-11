---
title: Async Rust and Tokio
tags:
  - rust
  - async
  - tokio
  - event-loop
created: 2026-06-10
updated: 2026-06-10
status: active
---

# Async Rust and Tokio

Async Rust allows for non-blocking concurrency by pausing execution of a function and yielding control back to the runtime.

## The Future Trait
At the core of async Rust is the `Future` trait.
```rust
pub trait Future {
    type Output;
    fn poll(self: Pin<&mut Self>, cx: &mut Context<'_>) -> Poll<Self::Output>;
}
```
A `Future` is a state machine that represents a value that will be available in the future. Unlike Promises in JS, Rust futures are **lazy**: they do nothing until they are polled.

### Polling and Wakers
- **Poll**: The runtime calls `poll()` to see if the future has completed.
- **Waker**: When a future is blocked (e.g., waiting for I/O), it registers a `Waker`. When the I/O is ready, the `Waker` notifies the executor to poll the future again.
- **Pinning**: `Pin` ensures that a future cannot be moved in memory once it has been polled, which is critical for futures containing self-referential pointers.

## The Tokio Runtime Architecture
Tokio is the most popular async runtime for Rust. It provides the executor, the I/O driver, and the timer.

### Multi-threaded Scheduler
Tokio uses a **work-stealing scheduler**. Each processor core has its own local queue of tasks. If one core finishes its tasks, it "steals" tasks from other cores to maximize CPU utilization.

### I/O Driver (Mio)
Tokio leverages `mio` (Metal I/O), which provides a cross-platform abstraction over OS-level event notifications:
- **epoll** (Linux)
- **kqueue** (macOS/BSD)
- **IOCP** (Windows)

### Tasks vs Threads
- **Threads**: OS-level, heavy, stack-allocated.
- **Tasks** (`tokio::spawn`): Green threads, lightweight, managed by the Tokio runtime, multiplexed onto a small number of OS threads.

## Execution Flow
1. `async` block defines a state machine.
2. `.await` pauses execution and returns control to the runtime.
3. Runtime polls futures until completion.
4. Wakers signal the runtime to re-poll.

[[02-Engenharia-de-Software]]
