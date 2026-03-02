import pandas as pd
from sklearn.datasets import load_iris
import os

def run_preprocessing():
    os.makedirs('data', exist_ok=True)
    data = load_iris(as_frame=True)
    df = data.frame
    df.to_csv('data/processed_data.csv', index=False)
    print("Preprocessing complete.")

if __name__ == "__main__":
    run_preprocessing()