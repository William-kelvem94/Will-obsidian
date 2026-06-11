---
type: deep-dive
category: Low-Level OS
tags: [filesystem, storage, vfs]
link: "[[02-Engenharia-de-Software/INDEX.md]]"
---

# File System Internals

## Data Structures

### Inodes (Index Nodes)
A data structure that describes a file system object (file, directory).
- **Contents**: File size, permissions, timestamps, and pointers to data blocks on disk.
- **Crucial Detail**: The inode does *not* store the filename; filenames are stored in directory entries (dentries) mapping a name to an inode number.

### VFS (Virtual File System)
An abstraction layer that provides a common interface for different underlying file systems (e.g., Ext4, NTFS, NFS).
- **Function**: Translates generic calls like `open()` or `read()` into file-system-specific operations.

## Reliability and Performance

### Journaling (Ext4, XFS)
A technique to prevent corruption after a crash by logging changes before applying them to the main file system.
- **Write-Ahead Logging (WAL)**: Changes are written to a journal. On recovery, the kernel replays the journal to ensure consistency.

### Copy-on-Write (CoW) - ZFS, Btrfs
Instead of overwriting data in place, the system writes modified data to a new block.
- **Advantages**: Atomic updates, instantaneous snapshots, and reduced data fragmentation.
- **Tree structure**: Updates a leaf node, which triggers a recursive update of parent pointers up to the root.

## Storage Layering
- **Block Layer**: Manages I/O requests using request queues and I/O schedulers (e.g., Deadline, BFQ) to optimize disk head movement or SSD wear.
