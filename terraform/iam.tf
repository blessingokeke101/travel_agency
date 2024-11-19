# Create a user for Airflow to access AWS
resource "aws_iam_user" "airflow_user" {
  name = "airflow_user_cde_project"

  tags = {
    Name        = "Airflow User"
    Environment = "Dev"
    owner       = "Blessing"
    team        = "CDE"
    managed_by  = "Blessing"
    service     = "airflow"
  }
}


# Create access key and secret key for airflow_user to access AWS
resource "aws_iam_access_key" "airflow_access_key" {
  user = aws_iam_user.airflow_user.name
}


# Store access and secret keys using AWS SSM parameters
resource "aws_ssm_parameter" "airflow_access_key" {
  name        = "/dev/airflow/cde_project/access_key"
  description = "The access key for Airflow user"
  type        = "String"
  value       = aws_iam_access_key.airflow_access_key.id

  tags = {
    Name        = "Airflow Access Key"
    Environment = "Dev"
    owner       = "Blessing"
    team        = "CDE"
    managed_by  = "Blessing"
    service     = "airflow"
  }
}

resource "aws_ssm_parameter" "airflow_secret_key" {
  name        = "/dev/airflow/cde_project/secret_key"
  description = "The secret key for Airflow user"
  type        = "String"
  value       = aws_iam_access_key.airflow_access_key.secret

  tags = {
    Name        = "Airflow Secret Key"
    Environment = "Dev"
    owner       = "Blessing"
    team        = "CDE"
    managed_by  = "Blessing"
    service     = "airflow"
  }
}


# Create IAM policy to be used by Airflow user to read and write to AWS S3
resource "aws_iam_policy" "airflow_policy" {
  name        = "dev-airflow-cde-project-policy"
  description = "IAM policy used by Airflow to access AWS"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "s3:ListBucket",
          "s3:*Object*",
        ]
        Resource = [
          "arn:aws:s3:::dev-cde-travel-agency",
          "arn:aws:s3:::dev-cde-travel-agency/*"
        ]
      }
    ]
  })
}


# Attach the Airflow policy and Airflow user above together
resource "aws_iam_user_policy_attachment" "airflow_policy_attach" {
  user       = aws_iam_user.airflow_user.name
  policy_arn = aws_iam_policy.airflow_policy.arn
}
