from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import os

# Load model deterministically at startup (outside the request cycle)
# Ensure your model.pkl file is in this same directory
model_path = "model.pkl"
model = joblib.load(model_path)

app = FastAPI()

# Pydantic request model for input validation
class PredictRequest(BaseModel):
    features: list[float]

# Pydantic response model for output schema
class PredictResponse(BaseModel):
    prediction: float

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    # Perform inference using the pre-loaded model
    result = model.predict([request.features])
    return PredictResponse(prediction=float(result[0]))
