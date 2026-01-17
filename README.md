# MLOps Project - Milestone 0
![CI](https://github.com/Khuzaimaalam2000/mlops-project/actions/workflows/ci.yml/badge.svg)

A reproducible Python environment for IDS 568, validated with automated CI.

## Prerequisites
- **Operating System:** macOS (Sonoma/Sequoia), Linux, or Windows (WSL2).
- **Python Version:** Python 3.12.4 is required for stability and library compatibility.

## Quick Start (Fresh Clone Setup)
To ensure this project is reproducible, follow these steps to set up the environment from scratch:
1. **Clone the repository**:
   ```bash
   git clone [https://github.com/Khuzaimaalam2000/mlops-project.git](https://github.com/Khuzaimaalam2000/mlops-project.git)
   cd mlops-project 
2. **Create virtual environment**:
    Bash
    python3.12 -m venv venv
    
3. **Activate**:
    Bash
    source venv/bin/activate

4. **Install pinned dependencies**:
    Bash
    pip install -r requirements.txt

5. **Verify installation with smoke tests**:
    Bash
    pytest tests/ -v

**Reproducibility Principles**
This project implements three fundamental software engineering practices to ensure reproducibility and maintainability within the machine learning lifecycle:

Dependency Pinning: By locking every library to an exact version in requirements.txt (e.g., pandas==2.1.4), we eliminate "version drift." This ensures that every developer and automated system uses the exact same code logic, preventing the "works on my machine" syndrome caused by floating dependencies.

Environment Isolation: Using venv ensures that our project dependencies do not conflict with the system Python or other projects. This isolation is critical for ML reliability; a minor update to a system-wide library could otherwise silently change how a model processes data or calculates gradients.

Automated Validation: Our GitHub Actions CI pipeline recreates the environment from scratch on every push. This provides immediate feedback on the health of the system and ensures that the codebase remains deployable and reliable throughout the lifecycle.

In the ML lifecycle, these practices are essential for trust and collaboration. If the training environment cannot be perfectly recreated, the resulting model cannot be trusted in production. By enforcing these standards at the start (Milestone 0), we guarantee that our models are built on a stable, verifiable foundation, which is crucial for identifying technical drift and ensuring long-term project viability.

**Project Structure**
├── .github/workflows/
│   └── ci.yml          # CI pipeline
├── src/                # Source code
│   ├── __init__.py
│   └── model.py        # ML logic (Model definition/training)
├── tests/              # Test suite
│   ├── __init__.py
│   ├── test_smoke.py   # Environment check
│   └── test_model.py   # Logic check for model.py
├── requirements.txt    # Pinned dependencies
└── README.md           # Documentation