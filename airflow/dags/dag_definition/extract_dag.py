import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from utils.extract_s3 import extract_to_s3, retrieve_data
from utils.extract_data import extract_data
from airflow.providers.snowflake.transfers.copy_into_snowflake import CopyFromExternalStageToSnowflakeOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


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

extract_profile_to_s3 = PythonOperator(
    dag=dag,
    task_id='cde_travel_agency',
    python_callable=extract_to_s3
)

retrieve_data_from_s3 = PythonOperator(
    dag=dag,
    task_id='cde_travel',
    python_callable=retrieve_data
)

copy_into_table = CopyFromExternalStageToSnowflakeOperator(
    task_id="copy_into_table",
    snowflake_conn_id="snowflake-connection",
    table="TRAVELS",
    stage="TRAVEL_AGENCY_STAGING_TABLE",
    file_format="PARQUET_FILE_FORMAT",
    database="TRAVEL-AGENCY",
    schema="DBOO"
)

extract_profile_to_s3 >> retrieve_data_from_s3 >> copy_into_table