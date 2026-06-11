# Linear Regression implementation (scratch and scikit-learn)
import numpy as np

# 1. Generate Mock Data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 2. Implementation from scratch using Batch Gradient Descent
class LinearRegressionScratch:
    def __init__(self, lr=0.1, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        m, n = X.shape
        self.weights = np.zeros((n, 1))
        self.bias = 0.0

        for _ in range(self.epochs):
            y_pred = np.dot(X, self.weights) + self.bias
            dw = (1 / m) * np.dot(X.T, (y_pred - y))
            db = (1 / m) * np.sum(y_pred - y)
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias

print("--- Training Linear Regression from Scratch ---")
model_scratch = LinearRegressionScratch(lr=0.1, epochs=1000)
model_scratch.fit(X, y)
y_pred_scratch = model_scratch.predict(X)
print(f"Scratch Coefficients: {model_scratch.weights.ravel()[0]:.4f}, Intercept: {model_scratch.bias:.4f}")

# Calculate metrics from scratch
mse_scratch = np.mean((y - y_pred_scratch) ** 2)
r2_scratch = 1 - (np.sum((y - y_pred_scratch) ** 2) / np.sum((y - np.mean(y)) ** 2))
print(f"Scratch Evaluation: MSE = {mse_scratch:.4f}, R2 = {r2_scratch:.4f}")

try:
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score
    print("\n--- Training Linear Regression using Scikit-Learn ---")
    model_sklearn = LinearRegression()
    model_sklearn.fit(X, y)
    y_pred_sklearn = model_sklearn.predict(X)
    print(f"Sklearn Coefficients: {model_sklearn.coef_[0][0]:.4f}, Intercept: {model_sklearn.intercept_[0]:.4f}")
    mse_sklearn = mean_squared_error(y, y_pred_sklearn)
    r2_sklearn = r2_score(y, y_pred_sklearn)
    print(f"Sklearn Evaluation: MSE = {mse_sklearn:.4f}, R2 = {r2_sklearn:.4f}")
except ImportError:
    pass
