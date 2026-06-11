---
title: Low-Level Memory Management
tags: [programming, systems, memory, performance]
date: 2026-06-09
---

# Low-Level Memory Management

Deep dive into how software interacts with physical and virtual memory, focusing on the architectural boundary between the application and the OS kernel.

## 1. The Memory Hierarchy and Locality
Understanding performance requires acknowledging the cost of data retrieval:
- **L1/L2/L3 Caches**: SRAM-based, extremely fast, but small.
- **Main Memory (RAM)**: DRAM-based, slower, larger capacity.
- **Virtual Memory (Disk/SSD)**: Swap space, slowest, largest.

### Spatial and Temporal Locality
- **Spatial Locality**: If a memory location is accessed, nearby locations are likely to be accessed soon (exploited by cache lines).
- **Temporal Locality**: If a memory location is accessed, it is likely to be accessed again soon (exploited by cache replacement policies).

## 2. Virtual Memory and Paging
Modern OSs use Virtual Memory to provide isolation and the illusion of a larger address space.

### The Page Table and MMU
The **Memory Management Unit (MMU)** translates virtual addresses to physical addresses using a **Page Table**.
- **Pages and Frames**: Memory is divided into fixed-size blocks (typically 4KB). Virtual memory uses "pages," and physical memory uses "frames."
- **TLB (Translation Lookaside Buffer)**: A high-speed cache that stores recent virtual-to-physical mappings to avoid expensive page table walks.

### Page Faults
When the CPU requests a page not present in RAM, a **Page Fault** occurs, triggering the kernel to load the page from disk.

## 3. Memory Allocation Strategies

### The Heap: Dynamic Allocation
The heap allows for runtime memory allocation, managed via `malloc`/`free` (C) or `new`/`delete` (C++).

#### Fragmentation
- **External Fragmentation**: Available memory is broken into small, non-contiguous blocks, making it impossible to satisfy a large allocation request.
- **Internal Fragmentation**: Allocated blocks are larger than the requested size, wasting memory inside the block.

#### Allocator Algorithms
- **First Fit**: Takes the first hole large enough.
- **Best Fit**: Finds the smallest hole that fits (minimizes internal fragmentation).
- **Slab Allocation**: Pre-allocates chunks of memory for specific object types (common in Linux kernels) to avoid fragmentation.

## 4. Automatic Memory Management (GC) vs Manual

### Manual Management
- **Pros**: Deterministic performance, no "stop-the-world" pauses.
- **Cons**: High risk of **Memory Leaks** (forgetting to free) and **Dangling Pointers** (using memory after freeing).

### Garbage Collection (GC)
- **Tracing GCs**: Start from "roots" and mark all reachable objects. Unmarked objects are swept (Mark-and-Sweep).
- **Reference Counting**: Each object tracks how many pointers point to it. When count reaches 0, it's freed. (Problem: Circular references).
- **Generational GC**: Based on the hypothesis that "most objects die young." It divides memory into Young and Old generations, collecting the young generation more frequently.

## 5. Modern Memory Safety: Rust's Ownership Model
Rust solves the manual vs GC dilemma via a compile-time system:
- **Ownership**: Each value has a single owner. When the owner goes out of scope, the memory is freed.
- **Borrowing**: References can be passed without transferring ownership.
- **Lifetimes**: The compiler ensures references do not outlive the data they point to, eliminating dangling pointers.

## Academic References
- *Operating Systems: Three Easy Pieces* (Remzi Arpaci-Dusseau)
- *The Design and Implementation of the FreeBSD Operating System* (Marshall Kirk
