import boto3

bucket_name = "shankar-bucket-21-4"

s3 = boto3.client('s3')

file_name = "index.html"

try:
    s3.upload_file(file_name, bucket_name, file_name)
    print("File uploaded successfully")
except Exception as e:
    print("Error:", e)
