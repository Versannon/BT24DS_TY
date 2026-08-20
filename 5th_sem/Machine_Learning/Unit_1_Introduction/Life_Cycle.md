# Machine Learning Life Cycle Overview

The Machine Learning (ML) life cycle defines the sequential steps taken to build, deploy, and maintain an ML model.

## 1. Problem Definition
What are we trying to solve?
- Identify the business objective or problem.
- Determine if ML is the right solution.
- Define success metrics (e.g., accuracy, latency).

## 2. Data Collection
Where does the data come from?
- Identify data sources (databases, APIs, web scraping, external datasets).
- Gather raw data necessary to solve the defined problem.

## 3. Data Preparation
Is the data clean and usable?
- **Data Cleaning**: Handle missing values, remove duplicates, and deal with outliers.
- **Data Transformation**: Normalize or standardize data.
- **Feature Engineering**: Create new features from existing data to improve model performance.

## 4. Data Exploration (EDA)
What does the data tell us?
- Perform Exploratory Data Analysis (EDA).
- Visualize distributions and correlations using plots.
- Identify patterns and trends to inform model selection.

## 5. Model Selection
Which ML algorithm should we choose?
- **Classification**
    - Logistic regression
    - Support vector machines
    - Decision trees
    - Random forests
    - Naive Bayes [Preferred]
- **Regression**
    - Linear regression
    - Polynomial regression
    - Ridge regression
    - Lasso regression
    - Elastic net regression
- **Clustering**
    - K-means
    - Hierarchical clustering
    - DBSCAN
- **Dimensionality reduction**
    - Principal component analysis (PCA)
    - Linear discriminant analysis (LDA)
    - t-distributed stochastic neighbor embedding (t-SNE)
- **Reinforcement learning**
    - Q-learning
    - Deep Q-learning
    - Policy gradient
    - Actor-critic

## 6. Model Training
How does the computer learn?
- **Process**: Training dataset -> ML algorithm -> Learns Patterns -> Resulting Model (e.g., Spam Detection Model)
- **Dataset Split**: Divide data into training, validation, and testing sets.

## 7. Model Evaluation and Tuning
How do we know if our model works correctly?
- Validate the model on unseen test data.
- If performance is poor -> Improve the model -> Tune hyperparameters -> Train again
- **Key Metrics**: Accuracy, Precision, Recall, and F1 score.

## 8. Deployment
Where will it be used?
- Integrate the trained model into a production environment.
- Example deployment (e.g., Spam Filter):
    - Gmail
    - Outlook
    - Yahoo mail
    - Company mail servers

## 9. Model Monitoring and Maintenance
Will the model always remain accurate?
- **Challenges**:
    - Data changes over time.
    - Concept drift (the statistical properties of the target variable change over time).
- **Solutions**:
    - Continuous monitoring of model predictions.
    - Model retraining with fresh data.
- **Why it is important**:
    - The real world is dynamic.
    - User behavior changes.
    - New data patterns emerge.