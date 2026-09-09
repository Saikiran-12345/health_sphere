provider "aws" {
  region = var.aws_region
}

resource "aws_vpc" "healthsphere_vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
  tags = { Name = "healthsphere-vpc" }
}

resource "aws_db_instance" "postgres_primary" {
  allocated_storage    = 100
  engine               = "postgres"
  engine_version       = "15.3"
  instance_class       = "db.t3.large"
  db_name              = "healthsphere_prod"
  username             = var.db_user
  password             = var.db_password
  parameter_group_name = "default.postgres15"
  skip_final_snapshot  = true
  multi_az             = true
}

resource "aws_ecs_cluster" "backend_cluster" {
  name = "healthsphere-backend-cluster"
}

resource "aws_s3_bucket" "medical_records" {
  bucket = "healthsphere-medical-records-prod"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "medical_records_crypto" {
  bucket = aws_s3_bucket.medical_records.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
