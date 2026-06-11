# Topic 2: Data Cleaning and Preparation

## Missing Data Mechanisms
- **MCAR**: Missing Completely at Random.
- **MAR**: Missing at Random (depends on observed features).
- **MNAR**: Missing Not at Random (depends on the missing value itself).
- *Imputation*: Mean, Median, Mode, Regression, KNN.

## Outlier Detection
- **Z-Score**: $|Z| > 3$.
- **IQR (Interquartile Range)**: Values outside $[Q_1 - 1.5 \times IQR, Q_3 + 1.5 \times IQR]$.
