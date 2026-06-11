# Decision Trees and SVM comparison on classification task
import numpy as np

# Simple Splitting metric calculations
def calculate_gini(y):
    if len(y) == 0: return 0.0
    p = np.bincount(y) / len(y)
    return 1 - np.sum(p ** 2)

y_mock = np.array([0, 0, 1, 1, 1, 2])
print("--- Theoretical Tree Calculations ---")
print(f"Gini Impurity for {y_mock}: {calculate_gini(y_mock):.4f}")

try:
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.svm import SVC
    
    X, y = make_classification(n_samples=100, n_features=5, n_classes=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    dt_clf = DecisionTreeClassifier(max_depth=3, random_state=42)
    dt_clf.fit(X_train, y_train)
    print(f"Sklearn Decision Tree Accuracy: {dt_clf.score(X_test, y_test):.4f}")
except ImportError:
    pass
