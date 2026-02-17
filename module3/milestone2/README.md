# ML Service - Milestone 2

[![CI/CD Pipeline](https://github.com/Khuzaimaalam2000/mlops-project/actions/workflows/build.yml/badge.svg)](https://github.com/Khuzaimaalam2000/mlops-project/actions/workflows/build.yml)

This repository contains the deliverables for Module 3, Milestone 2 of the MLOps course. It includes a multi-stage Dockerized Flask API for machine learning inference and an automated CI/CD pipeline using GitHub Actions.

## Pulling and Running the Image (Cloud)
To download and run the latest successfully built image from the GitHub Container Registry:

```bash
# Pull the image
docker pull ghcr.io/khuzaimaalam2000/mlops-project/ml-service:v1.0.2

# Run the container
docker run -p 8080:8080 ghcr.io/khuzaimaalam2000/mlops-project/ml-service:v1.0.2