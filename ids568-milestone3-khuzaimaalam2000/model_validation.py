import sys
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

MIN_ACCURACY = 0.90

def validate():
    X, y = load_iris(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=10, random_state=42)
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))

    if acc < MIN_ACCURACY:
        print(f"FAILED: Accuracy {acc} below threshold {MIN_ACCURACY}")
        sys.exit(1)
    print(f"PASSED: Accuracy {acc} meets threshold {MIN_ACCURACY}")

if __name__ == "__main__":
    validate()