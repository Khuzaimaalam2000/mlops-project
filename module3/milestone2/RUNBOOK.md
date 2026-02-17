# Operations Runbook

This runbook documents the operational procedures, architecture decisions, and troubleshooting steps for the ML Service containerization and CI/CD pipeline.

### 1. Dependency Pinning Strategy
All dependencies are strictly pinned in `app/requirements.txt` using exact versions (e.g., `Flask==3.0.0`, `pytest==7.4.3`). This guarantees deterministic builds across all environments and prevents pipeline failures or security vulnerabilities caused by unexpected upstream package updates.

### 2. Image Optimization
We utilize a **multi-stage Docker build** to minimize the final image footprint:
* **Before Optimization**: A standard `python:3.11` base image installs unnecessary build tools (like gcc) and caches, resulting in an image size of over 1GB.
* **After Optimization**: By using `python:3.11-slim` as a builder to compile a virtual environment (`/opt/venv`), and copying *only* that compiled environment to a fresh runtime stage, we eliminate build tools from the final image. Size is drastically reduced to `<150MB`. We also utilize a `.dockerignore` file to prevent copying `__pycache__` and Git histories.

### 3. Security Considerations
* **Non-root Execution**: The Dockerfile explicitly creates a specific user (`appuser`), transfers ownership of the application files to them using `--chown=appuser:appuser`, and switches to that user before execution. This ensures the container does not run as root.
* **Minimal Attack Surface**: Using the Debian-slim base image removes unnecessary OS packages that could harbor vulnerabilities.

### 4. CI/CD Workflow
1. **Trigger**: Code pushed to `main` triggers the `test` job. Pushing a tag (e.g., `v1.0.2`) triggers both the `test` and `build-and-push` jobs.
2. **Test Job**: GitHub Actions checks out the code, sets up Python 3.11, installs the pinned requirements, and runs unit tests via `pytest`.
3. **Build/Push Job**: Dependent on the `test` job passing. It authenticates to the GitHub Container Registry (GHCR) using a securely stored Personal Access Token (`REGISTRY_TOKEN`), builds the image using the multi-stage Dockerfile, and pushes it with the provided semantic version tag.

### 5. Versioning Strategy
We use strict **Semantic Versioning (SemVer)** formatted as `vMAJOR.MINOR.PATCH` (e.g., `v1.0.0`, `v1.0.2`). 
* The CI pipeline is configured to parse this Git tag and automatically apply it to the pushed Docker image. 
* This ensures that every container image in the registry maps exactly to a specific, immutable point in the Git history.

### 6. Troubleshooting Guide
* **Issue: `ModuleNotFoundError` when running the container locally.**
  * *Solution*: This usually means a dependency was added to `app.py` but not pinned in `requirements.txt`. Add the package to `requirements.txt`, rebuild the image (`docker compose build`), and run again.
* **Issue: Tests fail in CI but pass locally.**
  * *Solution*: Ensure your local development environment perfectly matches `app/requirements.txt`. Clear your local cache (`pip cache purge`) and rebuild the environment.
* **Issue: Docker push authentication fails (`denied`).**
  * *Solution*: Verify that the `REGISTRY_TOKEN` in GitHub Repository Secrets has not expired and has `read:packages` and `write:packages` permissions.
* **Issue: Port 8080 is already in use.**
  * *Solution*: Stop any currently running containers using `docker ps` and `docker stop <container_id>`, or change the port mapping in your run command to `8081:8080`.