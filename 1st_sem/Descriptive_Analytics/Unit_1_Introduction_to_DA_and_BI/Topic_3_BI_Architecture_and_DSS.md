# Topic 3: BI Architecture and Decision Support Systems (DSS)

## Components of BI Architecture
- **Data Warehouse (DWH)**: Centralized repository optimized for analytical querying.
- **Data Mart**: A department-focused DWH subset.
- **Data Lake**: Store for raw, unstructured, and structured data.
- **Dimensional Modeling**:
  - *Star Schema*: Fact table (measures) surrounded by dimension tables.
  - *Snowflake Schema*: Normalized dimension tables (reduces redundancy, adds joins).
- **OLAP (Online Analytical Processing)**:
  - *Operations*: Slice, Dice, Drill Down/Up, Roll Up.
  - *MOLAP, ROLAP, HOLAP*.
- **DSS**: Includes DBMS, Model-based systems, and user interfaces to support decisions via What-If and Sensitivity analysis.
