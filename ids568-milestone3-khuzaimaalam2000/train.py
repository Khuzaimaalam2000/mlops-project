import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import mlflow
import mlflow.sklearn
import hashlib
import sys
import os

def train(n_estimators=10, max_depth=5):
    if not os.path.exists('data/processed_data.csv'):
        print("Data not found. Run preprocess.py first.")
        sys.exit(1)

    df = pd.read_csv('data/processed_data.csv')
    X = df.drop('target', axis=1)
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    mlflow.set_tracking_uri("http://localhost:5000")
    mlflow.set_experiment("milestone3_experiment")

    with mlflow.start_run() as run:
        model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
        model.fit(X_train, y_train)
        acc = accuracy_score(y_test, model.predict(X_test))

        # Log parameters and metrics
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")

        # Generate and log artifact hash
        model_hash = hashlib.sha256(str(model.get_params()).encode('utf-8')).hexdigest()
        mlflow.set_tag("model_hash", model_hash)

        print(f"Run ID: {run.info.run_id} | Accuracy: {acc}")

if __name__ == "__main__":
    n_est = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    depth = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    train(n_est, depth)