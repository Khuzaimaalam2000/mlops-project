Milestone 3 - Workflow Automation & Experiment Tracking
=======================================================

This repository contains an automated Machine Learning pipeline managed by Apache Airflow, integrated with MLflow for experiment tracking and GitHub Actions for CI/CD governance.

Setup Instructions
------------------

1.  Bashgit clone https://github.com/Khuzaimaalam2000/ids568-milestone3-khuzaimaalam2000.gitcd ids568-milestone3-khuzaimaalam2000
    
2.  Bashpython3 -m venv project-envsource project-env/bin/activate
    
3.  Bashpip install --upgrade pip "setuptools<70.0.0" wheelpip install -r requirements.txt
    

How to Run the Pipeline
-----------------------

1.  Bashmlflow ui --port 5050 &
    
2.  Bashpython preprocess.pypython train.py 20 5python register.py
    

Architecture Explanation
------------------------

The pipeline uses **Apache Airflow** as the orchestrator. The DAG executes decoupled Python scripts via BashOperator. The tasks flow sequentially: preprocess\_data >> train\_model >> register\_model. This modular architecture ensures that data preparation, model training, and MLflow registry interactions remain independent and safely re-runnable.

DAG Idempotency and Lineage Guarantees
--------------------------------------

*   **Idempotency**: The preprocess.py task overwrites the processed\_data.csv file cleanly on every run. Re-running the DAG multiple times will not create duplicate artifacts or corrupted states.
    
*   **Lineage**: Complete experiment lineage is guaranteed through MLflow. Every model artifact is hashed (SHA256) and logged alongside its hyperparameters (n\_estimators, max\_depth) and training metrics (accuracy).
    

CI-Based Model Governance Approach
----------------------------------

Model governance is enforced via **GitHub Actions** (.github/workflows/train\_and\_validate.yml). Upon every push or pull request, the CI pipeline provisions a fresh environment, runs training, and executes model\_validation.py. This validation script acts as a strict quality gate, failing the build if the model's accuracy drops below the defined acceptable threshold (90%).

Experiment Tracking Methodology
-------------------------------

Experiments are tracked locally using MLflow. We systematically varied hyperparameters across 5 distinct runs to monitor performance impacts. The best-performing model is automatically registered into the MLflow Model Registry and transitioned to the Staging environment for staging validation before manual promotion to Production.

Operational Notes
-----------------

### Retry Strategies and Failure Handling

*   **Retries**: Airflow is configured with retries: 2 and a retry\_delay of 5 minutes in the DAG's default\_args to handle transient failures.
    
*   **Failure Callbacks**: An on\_failure\_callback is implemented to print the exact task\_id that failed, allowing for rapid debugging.
    

### Monitoring and Alerting Recommendations

In a production environment, we recommend monitoring:

1.  **Data Drift**: Shifts in the incoming feature distributions compared to the training baseline.
    
2.  **Inference Latency**: Ensuring the model responds within acceptable SLA timeframes.Alerts should be routed to the MLOps team via PagerDuty if accuracy drops below the 90% threshold.
    

### Rollback Procedures

If a newly deployed model degrades in production:

1.  Open the MLflow Registry UI.
    
2.  Manually transition the failing Production model to the Archived stage.
    
3.  Select the previous stable version and transition it from Archived or Staging back to Production.