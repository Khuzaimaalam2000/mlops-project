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

```bash
curl -X POST [https://fastapi-service-531088242025.us-central1.run.app/predict](https://fastapi-service-531088242025.us-central1.run.app/predict) \
    -H "Content-Type: application/json" \
    -d '{"features": [1000.0]}'