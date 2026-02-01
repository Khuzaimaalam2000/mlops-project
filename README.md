# MLOps Milestone 1: FastAPI Deployment to Google Cloud Run

This repository contains a complete MLOps pipeline for deploying a Machine Learning model using two distinct cloud architectures: **Containerized Microservices (Google Cloud Run)** and **Serverless Functions (Google Cloud Functions)**. 

The goal of this project is to demonstrate the transition of a machine learning model from a static artifact to a scalable, production-ready API. It emphasizes reproducibility, version control, and the trade-offs between different cloud deployment strategies.

---

## Project Structure
* **train.py**: The "Source of Truth" for the model. This script contains the logic to train the regression model and serialize it into a binary artifact (model.pkl).
* **model.pkl**: The trained model artifact. This binary file is the bridge between the Data Science phase and the Operations phase.
* **main.py**: The FastAPI application entry point. It defines the API routes, loads the model, and handles input validation using Pydantic.
* **Dockerfile**: The blueprint for the containerized environment, ensuring the application runs identically on a local machine and in the cloud.
* **cloud_function/**: A dedicated directory for the serverless implementation, containing its own main.py and dependencies tailored for the Google Cloud Functions runtime.
* **requirements.txt**: Pinpoints exact library versions to ensure deterministic behavior and prevent "dependency drift."

---

## Model-API Interaction
The interaction between the web server and the machine learning model is designed for high performance and low latency.

* **Initialization (The "Cold Start"):** When the container or function starts, the model.pkl file is loaded into memory using joblib. This happens **globally**, outside the request loop. This is a critical optimization: loading the model once at startup prevents the latency penalty of reloading the model file for every single incoming user request.
    
* **Request Validation:**
    Before the model ever sees data, the API validates the input using **Pydantic schemas**.
    * If a user sends text instead of numbers, or a list of the wrong length, the API intercepts the request and returns a 422 Validation Error.
    * This protects the model from crashing due to malformed input.

* **Inference:**
    Valid data is passed to the loaded model object's .predict() method. The result is formatted into a JSON response and returned to the client.

---

## Setup & Installation (Local)
To reproduce this project locally, follow these steps:

**1. Clone the Repository**
```bash
git clone [https://github.com/Khuzaimaalam2000/mlops-project.git](https://github.com/Khuzaimaalam2000/mlops-project.git)
cd mlops-project
```
**Initialize Environment** 
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
**Run the API Locally**
```bash
uvicorn main:app --reload
```
## Live Deployment

* **Service URL**: https://fastapi-service-531088242025.us-central1.run.app
* **Interactive API Docs**: https://fastapi-service-531088242025.us-central1.run.app/docs
* **Region**: us-central1
* **Project ID**: project-53d16477-9422-4f6b-9e6

---

## Tech Stack
* **Python 3.11**: Core application logic.
* **FastAPI**: High-performance web framework for the API.
* **Docker**: Containerization of the application and its dependencies.
* **Google Artifact Registry**: Storage for the container image.
* **Google Cloud Run**: Serverless hosting for the live API.

---

## Testing the API
You can test the live prediction endpoint using `curl` from your terminal:

```bash
curl -X POST [https://fastapi-service-531088242025.us-central1.run.app/predict](https://fastapi-service-531088242025.us-central1.run.app/predict) \
    -H "Content-Type: application/json" \
    -d '{"features": [1000.0]}'
```

---

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
  "prediction": 30000.0,
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