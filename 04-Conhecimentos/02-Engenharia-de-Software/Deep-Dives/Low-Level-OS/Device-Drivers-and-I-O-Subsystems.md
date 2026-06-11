---
type: deep-dive
category: Low-Level OS
tags: [drivers, io, hardware]
link: "[[02-Engenharia-de-Software/INDEX.md]]"
---

# Device Drivers and I/O Subsystems

## Communication Patterns

### Polling (Programmed I/O)
The CPU repeatedly checks a status register of the device to see if it is ready.
- **Trade-off**: Zero latency once the device is ready, but wastes CPU cycles (busy-waiting).

### Interrupt-Driven I/O
The device signals the CPU via an interrupt line when data is ready or an operation completes.
- **Trade-off**: Frees the CPU for other tasks, but introduces interrupt handling latency.

## Data Transfer Mechanisms

### DMA (Direct Memory Access)
Allows hardware components to transfer data directly to/from system memory without CPU intervention.
- **Workflow**: CPU initializes the DMA controller with source, destination, and length $\rightarrow$ DMA controller handles the transfer $\rightarrow$ DMA signals CPU via interrupt upon completion.
- **Benefit**: Drastically reduces CPU overhead for bulk data transfers (e.g., disk I/O, NIC).

### MMIO (Memory-Mapped I/O)
Hardware registers are mapped into the CPU's physical address space.
- **Mechanism**: Writing to a specific memory address sends a command to the device; reading from it retrieves device state.
- **Contrast**: Differs from Port-Mapped I/O (PMIO) which uses a separate address space and specialized instructions (e.g., `IN`/`OUT` on x86).

## Driver Architecture
- **Character Devices**: Data accessed as a stream of bytes (e.g., keyboards, serial ports).
- **Block Devices**: Data accessed in fixed-size blocks, supporting random access (e.g., HDDs, SSDs).
- **Network Interfaces**: Do not map to files in `/dev`; they use sockets and packet-based communication.
