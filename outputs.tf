output "raw_bucket_name" {
  value = aws_s3_bucket.raw_bucket.bucket
}

output "processed_bucket_name" {
  value = aws_s3_bucket.processed_bucket.bucket
}

output "lambda_function_name" {
  value = aws_lambda_function.csv_lambda.function_name
}
