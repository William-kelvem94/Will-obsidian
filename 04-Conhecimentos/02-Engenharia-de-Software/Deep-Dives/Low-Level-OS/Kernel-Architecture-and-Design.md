---
type: deep-dive
category: Low-Level OS
tags: [kernel, architecture, design]
link: "[[02-Engenharia-de-Software/INDEX.md]]"
---

# Kernel Architecture and Design

## Kernel Paradigms

### Monolithic Kernels
The entire operating system runs in kernel space. All OS services (file system, drivers, networking) share the same address space.
- **Advantages**: High performance due to minimal context switching and direct function calls between components.
- **Disadvantages**: Poor fault isolation; a crash in a driver can bring down the entire system.
- **Examples**: Linux, BSD.

### Microkernels
The kernel provides only the absolute minimum functionality: low-level memory management, thread scheduling, and Inter-Process Communication (IPC). All other services run in user space as "servers."
- **Advantages**: High robustness, modularity, and security. Servers can be restarted independently.
- **Disadvantages**: Performance overhead due to frequent context switching and IPC messaging.
- **Examples**: L4, QNX, Minix.

### Hybrid Kernels
A compromise that keeps the microkernel structure but runs some critical services in kernel space to reduce performance penalties.
- **Examples**: Windows NT, XNU (macOS).

## Interrupt Handling
Interrupts allow hardware to signal the CPU for immediate attention.
- **Hardware Interrupts**: Triggered by peripherals (e.g., keyboard, NIC).
- **Software Interrupts (Traps)**: Triggered by instructions (e.g., `int 0x80` in x86).
- **Interrupt Service Routine (ISR)**: The handler executed when an interrupt occurs.
- **Top Half vs. Bottom Half**:
    - **Top Half**: Critical, time-sensitive code that clears the interrupt.
    - **Bottom Half (Deferred Procedure Calls/Tasklets)**: Non-critical processing performed later to avoid blocking the system.

## System Call Interface (SCI)
The API between user-space applications and the kernel.
- **Mechanism**: User-space calls a library function (e.g., `glibc` for `read()`), which executes a specific CPU instruction (e.g., `SYSCALL` or `SVC`) to transition from User Mode (Ring 3) to Kernel Mode (Ring 0).
- **System Call Table**: An array of function pointers indexed by the system call number, used by the kernel to dispatch the request to the correct handler.
