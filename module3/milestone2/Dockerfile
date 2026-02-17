# Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /build

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
WORKDIR /app

# 1. Create the secure non-root user FIRST
RUN useradd -m appuser

# 2. Copy the venv and GIVE OWNERSHIP to appuser
COPY --from=builder --chown=appuser:appuser /opt/venv /opt/venv

# 3. Copy your app code and GIVE OWNERSHIP to appuser
COPY --chown=appuser:appuser app/ .

# 4. Activate the virtual environment
ENV PATH="/opt/venv/bin:$PATH"

# 5. Switch to the secure user
USER appuser

EXPOSE 8080
CMD ["python", "app.py"]