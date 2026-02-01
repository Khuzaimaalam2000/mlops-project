import joblib
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Define sample data (e.g., house sizes vs. prices)
X = np.array([[1000], [1500], [2000], [2500]])
y = np.array([300000, 450000, 600000, 750000])

# 2. Train a simple model
model = LinearRegression()
model.fit(X, y)

# 3. Save the model as a .pkl file
# This 'model.pkl' is the artifact your FastAPI main.py needs
joblib.dump(model, "model.pkl")

print("model.pkl has been successfully created in your directory.")
