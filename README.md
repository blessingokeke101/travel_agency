
# Travel Agency Data Platform

## Problem Statement
The Travel Agency requires a scalable data platform to process and store information from the [REST Countries API](https://restcountries.com/v3.1/all) for predictive analytics. The raw API data needs to be stored in AWS S3 as Parquet files, ensuring efficient storage and future flexibility. Specific attributes, such as country name, population, region, and currency details, must be extracted and loaded into Snowflake for downstream analytics. The platform uses Apache Airflow for orchestration, Terraform for cloud resource provisioning, and GitHub Actions for CI/CD pipelines. Data modeling with DBT organizes data into fact and dimension tables to enable actionable insights for the Data Science team.

---

## Architecture Overview
The system is designed to efficiently process and store data while ensuring scalability and ease of use.

### Components:
1. **Data Ingestion:**
   - Extracts raw data from the [REST Countries API](https://restcountries.com/v3.1/all).
   - Stores the raw data in AWS S3 as Parquet files to serve as the Data Lake.

2. **Data Transformation:**
   - Apache Airflow orchestrates workflows to extract and transform specific attributes from the raw data.

3. **Data Storage:**
   - Stores the final transformed data in Snowflake, enabling efficient querying and analytics.

4. **Infrastructure as Code:**
   - Terraform provisions all required cloud infrastructure, with state management stored in AWS S3.

5. **CI/CD Pipeline:**
   - GitHub Actions automates linting, testing, and deployment of Dockerized workflows to AWS ECR.

6. **Data Modeling:**
   - DBT organizes data into fact and dimension tables for predictive analytics.

### Architecture Diagram
![Architecture Diagram](https://github.com/blessingokeke101/travel_agency/blob/main/data_architecture.jpg)

---

## Data Description

The data is organized into the following tables:

•⁠  ⁠*dimCountry*: Stores country details such as country name, country code, official name, population, and language information.
•⁠  ⁠*dimLocation*: Contains geographic details like region, subregion, and continent information.
•⁠  ⁠*dimCurrency*: Stores currency details like currency name, code, and symbol.
•⁠  ⁠*factTable*: The fact table contains key metrics, including country population, area, region, and currency information, linked to the ⁠ dimCountry ⁠, ⁠ dimLocation ⁠, and ⁠ dimCurrency ⁠ tables.

### Entity Relationship Diagram (ERD)
![ERD Diagram](https://github.com/blessingokeke101/travel_agency/blob/main/erd_travel_agency.png)

---


## Directions to Run the Code/Project

### Prerequisites
- **Required Tools:**
  - Docker
  - Terraform
  - AWS CLI
  - DBT
  - Apache Airflow
  - Python with dependencies in `requirements.txt` and `requirements-ci.txt`
- **Accounts/Access:**
  - AWS Account (S3, ECR, Snowflake permissions).
  - GitHub repository: [Travel Agency Data Platform](https://github.com/blessingokeke101/travel_agency).

---

### Steps to Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/blessingokeke101/travel_agency.git
   cd travel_agency
   ```

2. **Set Up Infrastructure:**
   - Navigate to the Terraform directory:
     ```bash
     cd terraform
     terraform init
     terraform apply
     ```
   - Verify all resources (S3 bucket, Snowflake, IAM roles) are provisioned.

3. **Build and Push Docker Image:**
   - Build the Docker image:
     ```bash
     docker build -t travel-agency-extractor .
     ```
   - Push the image to AWS ECR:
     ```bash
     aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <ecr_url>
     docker tag travel-agency-extractor:latest <ecr_url>/travel-agency-extractor:latest
     docker push <ecr_url>/travel-agency-extractor:latest
     ```

4. **Run Apache Airflow:**
   - Start Airflow to orchestrate the workflows:
     ```bash
     cd airflow
     docker-compose up
     ```
   - Monitor and trigger workflows through the Airflow web UI.

5. **Run DBT Models:**
   - Navigate to the DBT project directory:
     ```bash
     cd dbt_project
     dbt run
     ```
   - Verify that fact and dimension tables are created in Snowflake.

6. **CI/CD with GitHub Actions:**
   - GitHub Actions are pre-configured for code linting, testing, and Docker image deployment.
   - Push any changes to the repository to trigger the CI/CD pipeline:
     ```bash
     git add .
     git commit -m "Your commit message"
     git push origin main
     ```

7. **Validate the Pipeline:**
   - Verify raw data is stored in S3, transformed data is in Snowflake, and workflows are orchestrated in Airflow.

---

## Repository Links
- **Repository URL:** [Travel Agency Data Platform Repository](https://github.com/blessingokeke101/travel_agency)
- **Clone URL:** `https://github.com/blessingokeke101/travel_agency.git`
- **Data API:** [REST Countries API](https://restcountries.com/v3.1/all)

---
