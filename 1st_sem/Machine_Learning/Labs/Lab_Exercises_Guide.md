# Machine Learning Lab Exercises Guide (BTDS-301-L)

This document provides a guide to the laboratory exercises required for the Machine Learning course. The code files for key concepts can be found in the adjacent `code_examples/` directories.

## Exercise Index

### Exercise 1: Introduction to Scikit-learn for Supervised Learning
- **Objective**: Load datasets, split into train/test sets, fit basic models, and print performance.
- **Python libraries**: `sklearn.model_selection.train_test_split`, `sklearn.preprocessing`.

### Exercise 2: Exploring Unsupervised Learning with K-Means Clustering
- **Objective**: Implement clustering on mock data, use the elbow method to select clusters, and evaluate using silhouette scores.
- **See Implementation**: [kmeans_and_dbscan.py](../Unit_3_Unsupervised_Learning/code_examples/kmeans_and_dbscan.py)

### Exercise 3: Implementing Linear Regression from Scratch
- **Objective**: Implement analytical (Normal Equation) and iterative (Gradient Descent) linear regression from scratch using NumPy.
- **See Implementation**: [linear_regression.py](../Unit_2_Supervised_Learning/code_examples/linear_regression.py)

### Exercise 4: Binary Classification with Logistic Regression
- **Objective**: Build binary classification pipeline using Logistic Regression, outputting classification report and confusion matrix.
- **See Implementation**: [logistic_regression.py](../Unit_2_Supervised_Learning/code_examples/logistic_regression.py)

### Exercise 5: Decision Tree Classifier for Multiclass Classification
- **Objective**: Build and visualize decision trees on multiclass data (e.g., Iris dataset).
- **See Implementation**: [decision_trees_and_svm.py](../Unit_2_Supervised_Learning/code_examples/decision_trees_and_svm.py)

### Exercise 6: Support Vector Machine (SVM) for Classification
- **Objective**: Classify data using SVM with different kernels (Linear, Poly, RBF) and analyze margin behavior.
- **See Implementation**: [decision_trees_and_svm.py](../Unit_2_Supervised_Learning/code_examples/decision_trees_and_svm.py)

### Exercise 7: Ensemble Learning with Random Forests
- **Objective**: Train Random Forest, examine feature importances, and compare performance against single decision trees.
- **See Implementation**: [ensemble_methods.py](../Unit_4_Advanced_Topics/code_examples/ensemble_methods.py)

### Exercise 8: Hierarchical Clustering
- **Objective**: Apply Agglomerative Clustering and plot dendrogram.
- **Python tools**: `scipy.cluster.hierarchy.dendrogram`, `sklearn.cluster.AgglomerativeClustering`.

### Exercise 9: Density-Based Clustering (DBSCAN)
- **Objective**: Apply DBSCAN clustering to concentric circles dataset and compare with K-means.
- **See Implementation**: [kmeans_and_dbscan.py](../Unit_3_Unsupervised_Learning/code_examples/kmeans_and_dbscan.py)

### Exercise 10: Principal Component Analysis (PCA)
- **Objective**: Run PCA for dimensionality reduction, plot variance ratio, and visualize data in 2D.
- **See Implementation**: [pca_dimensionality_reduction.py](../Unit_3_Unsupervised_Learning/code_examples/pca_dimensionality_reduction.py)

### Exercise 11: Convolutional Neural Network (CNN) for Image Classification
- **Objective**: Build a simple CNN for image classification using Keras/PyTorch.
- **See Implementation**: [simple_neural_network.py](../Unit_4_Advanced_Topics/code_examples/simple_neural_network.py)

### Exercise 12: Recurrent Neural Network (RNN) for Text Generation
- **Objective**: Train simple character/word LSTM/RNN model for sequence completion.
- **See Implementation**: [simple_neural_network.py](../Unit_4_Advanced_Topics/code_examples/simple_neural_network.py)

### Exercise 13: Reinforcement Learning with OpenAI Gym
- **Objective**: Setup gym environment (e.g., CartPole or FrozenLake) and train a basic agent.
- **Code template**: Refer to reinforcement learning sections in Unit 4.

### Exercise 14: Evaluation Metrics for Classification Models
- **Objective**: Compute Accuracy, Precision, Recall, F1, ROC-AUC, and plot Confusion Matrix.
- **See Implementation**: [logistic_regression.py](../Unit_2_Supervised_Learning/code_examples/logistic_regression.py)

### Exercise 15: Regression Model Evaluation Techniques
- **Objective**: Assess regression using MSE, MAE, R², and residual plots.
- **See Implementation**: [linear_regression.py](../Unit_2_Supervised_Learning/code_examples/linear_regression.py)

### Exercise 16: Cluster Validation Measures
- **Objective**: Evaluate clusters using Silhouette Score and Davies-Bouldin index.
- **See Implementation**: [kmeans_and_dbscan.py](../Unit_3_Unsupervised_Learning/code_examples/kmeans_and_dbscan.py)

### Exercise 17: Model Selection Techniques
- **Objective**: Use cross-validation to select between SVM, Random Forest, and Logistic Regression.
- **See Implementation**: [model_evaluation_and_tuning.py](../Unit_5_Evaluation_and_Selection/code_examples/model_evaluation_and_tuning.py)

### Exercise 18: Hyperparameter Tuning and Optimization
- **Objective**: Tune parameters using GridSearchCV and RandomizedSearchCV.
- **See Implementation**: [model_evaluation_and_tuning.py](../Unit_5_Evaluation_and_Selection/code_examples/model_evaluation_and_tuning.py)

### Exercise 19: Transfer Learning in Image Classification
- **Objective**: Load pre-trained MobileNet/VGG16 model, freeze layers, add dense head, and train.
- **Code concept**: Refer to Transfer Learning in Unit 6 notes.

### Exercise 20: Meta-Learning for Few-Shot Learning
- **Objective**: Understand basic few-shot matching or prototypical network training concepts.

### Exercise 21: Adversarial Attacks and Defenses
- **Objective**: Implement FGSM perturbation on a trained neural network and check degradation in classification accuracy.
