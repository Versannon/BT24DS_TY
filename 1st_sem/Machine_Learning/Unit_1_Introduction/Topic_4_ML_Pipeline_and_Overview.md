# Topic 4: ML Pipeline and Overview of Paradigms

## The General Machine Learning Pipeline
1. **Data Collection & Aggregation**: Gathering data from various sources (databases, APIs, scraping) and combining it into a unified dataset.
2. **Data Preprocessing & Cleaning**: Handling missing values, removing outliers, normalizing or standardizing ranges, and encoding categorical variables.
3. **Feature Engineering & Extraction**: Deriving new, meaningful features from raw data to improve model performance. This may include dimensionality reduction techniques (e.g., PCA) or domain-specific transformations.
4. **Model Selection**: Choosing the appropriate algorithm(s) based on the problem type (classification, regression, etc.), data size, interpretability requirements, and computational resources.
5. **Model Training & Hyperparameter Tuning**: Feeding data to the selected model to learn underlying patterns, and optimizing hyperparameters using techniques like Grid Search or Random Search.
6. **Model Evaluation & Validation**: Assessing model performance using a separate validation/test set and appropriate metrics (e.g., accuracy, F1-score, RMSE) to ensure it generalizes well to unseen data.
7. **Deployment & Monitoring**: Serving the model in a production environment (via APIs or embedded systems) and continuously tracking its performance to detect and address data drift or model degradation over time.

## Machine Learning Paradigms
- **Supervised Learning**: Model is trained on labeled pairs $(X, y)$.
- **Unsupervised Learning**: Model extracts structure from unlabeled data $X$ (e.g. clustering, dimensionality reduction).
- **Reinforcement Learning**: Agent learns to act in an environment to maximize cumulative reward.
