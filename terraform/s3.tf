# Create an S3 Bucket
resource "aws_s3_bucket" "dev_travel_agency" {
  bucket = "dev-cde-travel-agency"

  tags = {
    Name        = "CDE bucket"
    Environment = "Dev"
    owner       = "Blessing"
    team        = "CDE"
    managed_by  = "Blessing"
    service     = "airflow"
  }
}


# Enable bucket versioning
resource "aws_s3_bucket_versioning" "dev_travel_agency_versioning" {
  bucket = aws_s3_bucket.dev_travel_agency.id
  versioning_configuration {
    status = "Enabled"
  }
}
