# Multi-layer Perceptron forward pass from scratch
import numpy as np

def relu(z):
    return np.maximum(0, z)

X_mock = np.array([[0.5, -0.2, 0.1]])
np.random.seed(42)
W1 = np.random.randn(3, 4)
b1 = np.zeros((1, 4))

Z1 = np.dot(X_mock, W1) + b1
A1 = relu(Z1)
print("--- MLP Hidden Layer Output (Scratch) ---")
print(A1)
