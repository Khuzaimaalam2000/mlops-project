# MLOps Milestone 1: FastAPI Deployment to Google Cloud Run

This project demonstrates a production-ready MLOps workflow for deploying a Machine Learning model as a containerized FastAPI service.

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

## Project Overview
[cite_start]This repository contains a deployed machine learning model exposing a prediction endpoint via **FastAPI on Google Cloud Run** and a **Serverless GCP Cloud Function**[cite: 1, 6, 21].

---

## 1. Deployment URLs
* [cite_start]**Cloud Run (FastAPI):** `https://fastapi-service-531088242025.us-central1.run.app/predict` [cite: 117, 193]
* [cite_start]**Cloud Function:** `https://us-central1-project-53d16477-9422-4f6b-9e6.cloudfunctions.net/predict` [cite: 127, 193]

---

## 2. API Usage Examples
### Local/Cloud Run Test

```bash
curl -X POST "http://localhost:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"features": [1.0, 2.0, 3.0]}'
[cite_start]``` [cite: 103, 104]
```

### Expected Response
```json
{
  "prediction": 1.0,
  "model_version": "1.0.0"
}
[cite_start]``` [cite: 78, 79, 171]

---

## 3. ML Lifecycle Explanation
This project represents the **Model Deployment and Inference** stage of the ML Lifecycle[cite: 13, 172].
* **Input**: The stage consumes a versioned `model.pkl` artifact produced during the Training stage[cite: 12, 176].
* **Process**: It wraps the model in a FastAPI service with Pydantic validation to ensure data quality[cite: 8, 9, 168].
* **Output**: It provides a stable inference endpoint for downstream consumers like web or mobile applications[cite: 16, 176].

---

## 4. Comparative Analysis: Cloud Run vs. Cloud Functions
### Latency and Cold Starts
* **Cloud Run**: Observed cold starts of ~2-4 seconds after idling for 15+ minutes. Warm instances respond in <100ms[cite: 30, 137, 142].
* **Cloud Functions**: Shorter cold start overhead (~1s) compared to containers but less efficient for heavy model processing[cite: 183].

### Statefulness vs. Statelessness
* **FastAPI (Cloud Run)**: Stateful loading allows `model.pkl` to be loaded once at startup, remaining in memory for all subsequent requests[cite: 28, 58, 64].
* **Cloud Functions**: Primarily stateless; while easier to scale, managing large artifacts is less optimized than in a dedicated container[cite: 28, 184].

### Reproducibility
* **Cloud Run**: Highly reproducible via Docker, ensuring the OS and system libraries are identical across environments[cite: 31, 186].
* **Cloud Functions**: Reliant on the cloud provider's pre-configured runtime environment, offering less control over system-level dependencies[cite: 186].

---

## 5. Artifact Management
The model artifact (`model.pkl`) is loaded deterministically at application startup[cite: 12, 50, 64]. This ensures that the API does not suffer from the overhead of loading the model on every request, maintaining low latency for warm instances[cite: 58, 62].