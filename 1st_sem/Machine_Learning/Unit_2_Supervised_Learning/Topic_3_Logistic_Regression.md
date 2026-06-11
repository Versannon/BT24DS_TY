# Topic 3: Logistic Regression

## Mathematical Formulation
Used for binary classification. Output is model probability:
$$P(Y=1|X) = \sigma(w^T X + b)$$
where $\sigma$ is the Sigmoid activation function:
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

## Loss Function
Minimizes **Binary Cross-Entropy (Log Loss)**:
$$\mathcal{L} = -\frac{1}{m} \sum_{i=1}^{m} \left[ y_i \log(\hat{y}_i) + (1-y_i) \log(1-\hat{y}_i) \right]$$
