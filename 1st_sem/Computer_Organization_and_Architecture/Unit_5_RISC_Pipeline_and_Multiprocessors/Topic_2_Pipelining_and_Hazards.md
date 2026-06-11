# Topic 2: Pipelining and Hazards

Pipelining overlaps instruction execution stages.
- **Pipeline Hazards**:
  - *Structural*: Resource conflict (e.g. CPU tries to fetch and load data simultaneously).
  - *Data*: Dependency on uncompleted instruction values.
  - *Control*: Caused by conditional branches before next address is known.
