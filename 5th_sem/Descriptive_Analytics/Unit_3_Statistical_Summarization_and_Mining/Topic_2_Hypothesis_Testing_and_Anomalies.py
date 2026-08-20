# Hypothesis Testing and Anomaly Detection
import numpy as np

# Two-sample t-test from scratch
np.random.seed(42)
group_A = np.random.normal(loc=50, scale=10, size=30)
group_B = np.random.normal(loc=54, scale=11, size=30)

t_statistic = (np.mean(group_A) - np.mean(group_B)) / np.sqrt(np.var(group_A)/30 + np.var(group_B)/30)
print("--- Two-Sample T-test (Scratch) ---")
print(f"T-statistic: {t_statistic:.4f}")
