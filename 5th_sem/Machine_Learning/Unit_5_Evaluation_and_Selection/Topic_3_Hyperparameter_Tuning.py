# Hyperparameter Tuning
import numpy as np

try:
    from sklearn.datasets import make_classification
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import GridSearchCV
    
    X, y = make_classification(n_samples=80, n_features=5, random_state=42)
    grid = GridSearchCV(RandomForestClassifier(random_state=42), {'n_estimators': [5, 10]}, cv=2)
    grid.fit(X, y)
    print(f"Best parameters: {grid.best_params_}")
except ImportError:
    print("scikit-learn not installed. Skipping Grid Search code.")
