import mlflow
from mlflow.tracking import MlflowClient

def register_latest_model():
    mlflow.set_tracking_uri("http://localhost:5000")
    client = MlflowClient()
    experiment = client.get_experiment_by_name("milestone3_experiment")
    
    runs = client.search_runs(experiment_ids=[experiment.experiment_id], order_by=["metrics.accuracy DESC"], max_results=1)
    best_run = runs[0]
    
    model_uri = f"runs:/{best_run.info.run_id}/model"
    model_details = mlflow.register_model(model_uri=model_uri, name="Milestone3_Prod_Model")
    
    # Transition to Staging
    client.transition_model_version_stage(
        name="Milestone3_Prod_Model",
        version=model_details.version,
        stage="Staging"
    )
    print(f"Registered version {model_details.version} and moved to Staging.")

if __name__ == "__main__":
    register_latest_model()