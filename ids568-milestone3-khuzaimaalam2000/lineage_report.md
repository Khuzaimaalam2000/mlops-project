# Model Lineage & Hyperparameter Comparison

The following runs were conducted to optimize the RandomForestClassifier:

| Run ID | n_estimators | max_depth | Accuracy |
|--------|--------------|-----------|----------|
| Run 1  | 10           | 3         | 1.0      |
| Run 2  | 20           | 5         | 1.0      |
| Run 3  | 50           | 10        | 1.0      |
| Run 4  | 100          | 15        | 1.0      |
| Run 5  | 200          | 20        | 1.0      |

**Justification:** Since all configurations achieved 100% accuracy on the Iris/Synthetic dataset, the model with `n_estimators=50` and `max_depth=10` was selected for Production to balance model complexity and performance.