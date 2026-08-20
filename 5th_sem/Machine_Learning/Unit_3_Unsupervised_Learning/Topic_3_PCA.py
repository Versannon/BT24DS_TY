# PCA from scratch
import numpy as np

np.random.seed(42)
X = np.random.randn(10, 4)

X_centered = X - np.mean(X, axis=0)
cov_matrix = np.cov(X_centered, rowvar=False)
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("--- PCA Eigenvalues (Scratch) ---")
print(np.round(eigenvalues, 4))
