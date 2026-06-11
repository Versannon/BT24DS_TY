# Topic 2: Memory Hierarchy and Cache Mapping

- **Hierarchy**: Registers -> Cache -> Main Memory -> Auxiliary Disk.
- **Cache Mapping**:
  - *Direct*: Block $i$ maps to cache line $i \pmod N$.
  - *Fully Associative*: Block can map to any cache line.
  - *Set-Associative*: Cache split into sets; block maps to set and any line within.
