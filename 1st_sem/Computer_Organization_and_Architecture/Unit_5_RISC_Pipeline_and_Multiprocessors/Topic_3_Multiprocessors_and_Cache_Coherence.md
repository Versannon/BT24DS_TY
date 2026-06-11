# Topic 3: Multiprocessors and Cache Coherence

- **Cache Coherence**: Ensuring all CPU caches in a shared system contain matching memory values.
- **Protocols**:
  - *Snooping*: Caches watch the shared bus for write operations to invalidate/update.
  - *Directory-based*: Central directory tracks cache copy states.
