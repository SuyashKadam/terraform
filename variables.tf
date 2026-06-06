variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "raw_bucket_name" {
  description = "Bucket for raw CSV uploads"
  type        = string
  default     = "suyash-raw-csv-bucket-2026"
}

variable "processed_bucket_name" {
  description = "Bucket for cleaned CSV files"
  type        = string
  default     = "suyash-processed-csv-bucket-2026"
}

variable "lambda_function_name" {
  description = "Lambda function name"
  type        = string
  default     = "csv-cleaning-lambda"
}
