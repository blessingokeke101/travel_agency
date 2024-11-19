terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    snowflake = {
      source = "Snowflake-Labs/snowflake"
    }
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

# A simple configuration of the provider with a default authentication.
# A default value for `authenticator` is `snowflake`, enabling authentication with `user` and `password`.
provider "snowflake" {
  organization_name = "ZNJAYTZ"
  account_name      = "KL64802"
  user              = "blessingokeke"
  password          = "Blossom19."

  // optional
  role      = "ACCOUNTADMIN"
  warehouse = "compute_wh"
  params = {
    query_tag = "cde_project"
  }
}
