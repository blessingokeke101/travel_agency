resource "snowflake_database" "travel_agency_database" {
  name="TRAVEL-AGENCY"
  drop_public_schema_on_creation=true
}

resource "snowflake_schema" "travel_agency_schema" {
  name     = "DBOO"
  database = snowflake_database.travel_agency_database.name
}

resource "snowflake_file_format" "database_format" {
  name        = "PARQUET_FILE_FORMAT"
  database    = snowflake_database.travel_agency_database.name
  schema      = snowflake_schema.travel_agency_schema.name
  format_type = "PARQUET"
}

resource "snowflake_stage" "travel_agency_staging_table" {
  name        = "TRAVEL_AGENCY_STAGING_TABLE"
  url         = "s3://dev-cde-travel-agency/transformed-data"
  database    = snowflake_database.travel_agency_database.name
  schema      = snowflake_schema.travel_agency_schema.name
  credentials = "AWS_KEY_ID='${aws_iam_access_key.airflow_access_key.id}' AWS_SECRET_KEY='${aws_iam_access_key.airflow_access_key.secret}'"
}

resource "snowflake_table" "travel_agency_table" {
  database                    = snowflake_database.travel_agency_database.name
  schema                      = snowflake_schema.travel_agency_schema.name
  name                        = "TRAVELS"
  comment                     = "TRAVEL AGENCY TABLE."


   column {
    name     = "DATA"
    type     = "VARIANT"
    nullable = false
  }
}
