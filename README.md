# MLOps Milestone 1: FastAPI Deployment to Google Cloud Run

This project demonstrates a production-ready MLOps workflow for deploying a Machine Learning model as a containerized FastAPI service. This repository contains a deployed machine learning model exposing a prediction endpoint via **FastAPI on Google Cloud Run** and a **Serverless GCP Cloud Function**.

## Live Deployment
* **Service URL**: https://fastapi-service-531088242025.us-central1.run.app
* **Interactive API Docs**: https://fastapi-service-531088242025.us-central1.run.app/docs
* **Region**: us-central1
* **Project ID**: project-53d16477-9422-4f6b-9e6

## Tech Stack
* **Python 3.11**: Core application logic.
* **FastAPI**: High-performance web framework for the API.
* **Docker**: Containerization of the application and its dependencies.
* **Google Artifact Registry**: Storage for the container image.
* **Google Cloud Run**: Serverless hosting for the live API.

## Project Structure
* `main.py`: FastAPI application script defining `/` and `/predict` endpoints.
* `model.pkl`: The serialized scikit-learn model used for inference.
* `Dockerfile`: Instructions for building the container image.
* `requirements.txt`: List of required Python libraries (FastAPI, scikit-learn, etc.).
* `train.py`: Script used to train and export the model.

## Testing the API
You can test the live prediction endpoint using `curl` from your terminal:

curl -X POST [https://fastapi-service-531088242025.us-central1.run.app/predict](https://fastapi-service-531088242025.us-central1.run.app/predict) \
    -H "Content-Type: application/json" \
    -d '{"features": [1000.0]}'

## Deployment URLs
* **Cloud Run (FastAPI):** `https://fastapi-service-531088242025.us-central1.run.app/predict` 
* **Cloud Function:** `https://us-central1-project-53d16477-9422-4f6b-9e6.cloudfunctions.net/predict` 

---

## API Usage Examples
### Local/Cloud Run Test

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [1.0, 2.0, 3.0]}'
    
```

### Expected Response
```json
{
  "prediction": 1.0,
  "model_version": "1.0.0"
}
``` 
---

## ML Lifecycle Explanation
This project represents the **Model Deployment and Inference** stage of the ML Lifecycle.
* **Input**: The stage consumes a versioned `model.pkl` artifact produced during the Training stage.
* **Process**: It wraps the model in a FastAPI service with Pydantic validation to ensure data quality.
* **Output**: It provides a stable inference endpoint for downstream consumers like web or mobile applications.

---

## Comparative Analysis: Cloud Run vs. Cloud Functions
### Latency and Cold Starts
* **Cloud Run**: Observed cold starts of ~2-4 seconds after idling for 15+ minutes. Warm instances respond in <100ms.
* **Cloud Functions**: Shorter cold start overhead (~1s) compared to containers but less efficient for heavy model processing.

### Statefulness vs. Statelessness
* **FastAPI (Cloud Run)**: Stateful loading allows `model.pkl` to be loaded once at startup, remaining in memory for all subsequent requests.
* **Cloud Functions**: Primarily stateless; while easier to scale, managing large artifacts is less optimized than in a dedicated container.

### Reproducibility
* **Cloud Run**: Highly reproducible via Docker, ensuring the OS and system libraries are identical across environments.
* **Cloud Functions**: Reliant on the cloud provider's pre-configured runtime environment, offering less control over system-level dependencies.

---

## Artifact Management
The model artifact (`model.pkl`) is loaded deterministically at application startup. This ensures that the API does not suffer from the overhead of loading the model on every request, maintaining low latency for warm instances.