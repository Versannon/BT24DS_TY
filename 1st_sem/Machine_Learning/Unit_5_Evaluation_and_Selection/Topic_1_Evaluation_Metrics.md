# Topic 1: Evaluation Metrics

## Classification
- **Accuracy**: $(TP+TN)/(TP+TN+FP+FN)$
- **Precision**: $TP/(TP+FP)$
- **Recall**: $TP/(TP+FN)$
- **F1-Score**: $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$
- **ROC-AUC**: True Positive Rate vs False Positive Rate.

## Regression
- **MSE**: $\frac{1}{n} \sum (y_i - \hat{y}_i)^2$
- **MAE**: $\frac{1}{n} \sum |y_i - \hat{y}_i|$
- **R²**: Proportion of variance explained by features.
