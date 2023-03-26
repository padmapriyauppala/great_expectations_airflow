from airflow import DAG
from airflow.operators.python import PythonOperator
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
from great_expectations.core.batch import BatchRequest
from great_expectations.data_context.types.base import (
    DataContextConfig,
    CheckpointConfig
)


sample_dag = DAG(dag_id="sample",
                         description="A sample DAG",
                         catchup=False)


ge_data_context_root_dir_with_checkpoint_name_pass = GreatExpectationsOperator(
    task_id="ge_data_context_root_dir_with_checkpoint_name_pass",
    data_context_root_dir="./great_expectations",
    checkpoint_name="puppala_chkpt_taxi",
)

ge_data_context_root_dir_with_checkpoint_name_pass
