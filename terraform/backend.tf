# Create a backend state file
terraform {
  backend "s3" {
    bucket         = "travel-agency-terraform-state-bucket"
    key            = "terraform.tfstate" # Path within the bucket
    region         = "eu-north-1"
    encrypt        = true
  }
}
