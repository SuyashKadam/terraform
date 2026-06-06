import boto3
import csv
import os
from io import StringIO
from urllib.parse import unquote_plus

s3 = boto3.client("s3")

PROCESSED_BUCKET = os.environ["PROCESSED_BUCKET"]


def lambda_handler(event, context):
    print("Lambda started")
    print("Event received:", event)

    for record in event["Records"]:
        raw_bucket = record["s3"]["bucket"]["name"]
        raw_key = unquote_plus(record["s3"]["object"]["key"])

        print(f"Reading file from bucket: {raw_bucket}, key: {raw_key}")

        response = s3.get_object(Bucket=raw_bucket, Key=raw_key)
        csv_content = response["Body"].read().decode("utf-8")

        input_file = StringIO(csv_content)
        reader = csv.DictReader(input_file)

        cleaned_rows = []

        for row in reader:
            if all(row.values()):
                cleaned_rows.append(row)

        output_file = StringIO()

        if cleaned_rows:
            writer = csv.DictWriter(output_file, fieldnames=cleaned_rows[0].keys())
            writer.writeheader()
            writer.writerows(cleaned_rows)

        processed_key = f"cleaned/{raw_key}"

        s3.put_object(
            Bucket=PROCESSED_BUCKET,
            Key=processed_key,
            Body=output_file.getvalue()
        )

        print(f"Cleaned file written to {PROCESSED_BUCKET}/{processed_key}")

    return {
        "statusCode": 200,
        "body": "CSV processed successfully"
    }
