import boto3

# Your S3 bucket name
bucket_name = "your-bucket-name"

# Create S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY'
)

# File to upload
file_name = "index.html"

try:
    s3.upload_file(file_name, bucket_name, file_name)
    print("File uploaded successfully to S3")
except Exception as e:
    print("Error uploading file:", e)
