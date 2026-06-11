# Ensemble methods
import numpy as np

try:
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
    
    X, y = make_classification(n_samples=100, n_features=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    rf = RandomForestClassifier(n_estimators=10, random_state=42)
    rf.fit(X_train, y_train)
    print(f"Random Forest Accuracy: {rf.score(X_test, y_test):.4f}")
except ImportError:
    print("scikit-learn not installed. Skipping ensemble code.")
