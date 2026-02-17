# Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /build
COPY app/requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
COPY app/ .

# Ensure local bin is on PATH
ENV PATH=/root/.local/bin:$PATH

# Security: Run as non-root user
RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 8080
CMD ["python", "app.py"]