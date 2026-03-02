from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

def on_failure_callback(context):
    print(f"Task Failed: {context.get('task_instance').task_id}")

default_args = {
    'owner': 'mlops',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'on_failure_callback': on_failure_callback
}

with DAG(
    'train_pipeline', 
    default_args=default_args, 
    start_date=datetime(2024, 1, 1), 
    schedule_interval=None, 
    catchup=False
) as dag:
    
    # Task 1
    preprocess = BashOperator(
        task_id='preprocess_data',
        bash_command='cd ~/ids568-milestone3-khuzaimaalam2000 && python3 preprocess.py'
    )

    # Task 2
    train = BashOperator(
        task_id='train_model',
        bash_command='cd ~/ids568-milestone3-khuzaimaalam2000 && python3 train.py'
    )

    # Task 3
    register = BashOperator(
        task_id='register_model',
        bash_command='cd ~/ids568-milestone3-khuzaimaalam2000 && python3 register.py'
    )

    # Dependencies
    preprocess >> train >> register