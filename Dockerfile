FROM python:3.12-slim

WORKDIR /app

COPY airflow/dags/utils /app/dags/utils

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8080

# Run extract_to_s3.py when the container launches
CMD ["bash", "-c", "python /app/dags/utils/data_extraction.py && \
        python /app/dags/utils/data_transformation.py && \
        python /app/dags/utils/s3_functions.py"]


    
