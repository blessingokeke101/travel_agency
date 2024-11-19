import boto3
from airflow.models import Variable
from .extract_data import extract_data
import awswrangler as wr
import pandas as pd
from .travel_trans import transform_data
import logging
# Establish connection with AWS and Extract files to AWS S3

logging.basicConfig(format='%(asctime)s %(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(20)

def aws_session():
    session = boto3.Session(
                aws_access_key_id=Variable.get('aws_access_key'),
                aws_secret_access_key=Variable.get('aws_secret_key'),
                region_name="eu-north-1"
    )
    return session

def extract_to_s3():
    data = extract_data()
    wr.s3.to_parquet(
        df=data,
        path="s3://dev-cde-travel-agency/raw-data",
        boto3_session=aws_session(),
        mode='overwrite',
        dataset=True
    )
    return ("Data successfully written to the all all_profiles S3 bucket")


def retrieve_data():
    col=['name','independent', 'continents', 'unMember', 'startOfWeek','region', 'subregion',
            'population', 'area', 'currencies','languages', 'idd', 'capital']
    logging.info("fetching parquet file")
    df = wr.s3.read_parquet(
        path="s3://dev-cde-travel-agency/raw-data",
        boto3_session=aws_session(),
        columns=col,
        dataset=True
    )
    logging.info("finish reading parquet file")
    df = pd.DataFrame(df)
    logging.info("finished conversion to pandas dataframe")
    data = transform_data(df)
    logging.info("transforming data")
    if data is not None:
        extract_transformed_to_s3(data)


def extract_transformed_to_s3(data):
    wr.s3.to_parquet(
        df=data,
        path="s3://dev-cde-travel-agency/transformed-data",
        boto3_session=aws_session(),
        mode='overwrite',
        dataset=True
    )
    return ("Transformed data successfully written to the all all_profiles S3 bucket")

