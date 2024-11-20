import datetime

from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.transfers.copy_into_snowflake import \
    CopyFromExternalStageToSnowflakeOperator
from utils.s3_functions import s3_extract_transform_load, write_to_s3

from airflow import DAG

DAG_ID = 'a_travel_agency'

default_args = {
    'owner': 'blessing-cde-team',
    'start_date': datetime.datetime(2024, 11, 5),
    'retries': 1,
    'retry_delay': datetime.timedelta(seconds=5)
}


dag = DAG(
    DAG_ID,
    default_args=default_args,
    schedule_interval='0 0 * * *',
    catchup=False,
    description='hi',
    default_view="graph"
)

api_data_ingestion_to_s3 = PythonOperator(
    dag=dag,
    task_id='api_data_ingestion_to_s3',
    python_callable=write_to_s3
)

s3_extract_transform_load_ = PythonOperator(
    dag=dag,
    task_id='s3_extract_transform_load_task',
    python_callable=s3_extract_transform_load
)

copy_into_table = CopyFromExternalStageToSnowflakeOperator(
    task_id="s3_to_snowflake",
    snowflake_conn_id="snowflake-connection",
    table="TRAVELS",
    stage="TRAVEL_AGENCY_STAGING_TABLE",
    file_format="PARQUET_FILE_FORMAT",
    database="TRAVEL_AGENCY",
    schema="DBOO"
)

api_data_ingestion_to_s3 >> s3_extract_transform_load_ >> copy_into_table
