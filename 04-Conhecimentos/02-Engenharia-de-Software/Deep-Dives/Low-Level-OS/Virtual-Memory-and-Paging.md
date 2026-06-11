---
type: deep-dive
category: Low-Level OS
tags: [memory, paging, virtual-memory]
link: "[[02-Engenharia-de-Software/INDEX.md]]"
---

# Virtual Memory and Paging

## Address Translation
Virtual memory decouples the logical address space from physical RAM, allowing processes to use more memory than physically available.

### Page Tables
A data structure used by the Memory Management Unit (MMU) to map virtual addresses to physical frames.
- **Multi-level Paging**: Hierarchical tables (Page Directory $\rightarrow$ Page Table $\rightarrow$ Page) to reduce the memory footprint of the tables themselves.
- **Inverted Page Table**: Maps physical frames to virtual pages, reducing table size for large 64-bit address spaces.

### TLB (Translation Lookaside Buffer)
A high-speed associative cache within the MMU that stores recent virtual-to-physical mappings.
- **TLB Hit**: Immediate translation.
- **TLB Miss**: Requires a "page walk" through the page tables in main memory.

## Memory Management Mechanisms

### Demand Paging
Pages are loaded into RAM only when accessed (on a "page fault").
- **Page Fault**: Occurs when a process accesses a page marked "not present" in the page table. The kernel fetches the page from disk.

### Segmentation
Memory is divided into variable-sized segments based on logical divisions (code, data, stack).
- **Fragmentation**: Susceptible to external fragmentation, often solved by combining segmentation with paging (Paged Segmentation).

### Swapping Algorithms
Moving pages between RAM and secondary storage (disk).
- **Least Recently Used (LRU)**: Replaces the page that hasn't been used for the longest time.
- **Clock Algorithm**: An approximation of LRU using a "use bit" to avoid high overhead.
- **FIFO**: First-In-First-Out; simple but susceptible to Belady's Anomaly.
