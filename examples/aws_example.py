import boto3

# AWS Access Key and Secret
aws_access_key_id = 'YOUR_AWS_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_AWS_SECRET_ACCESS_KEY'

# Create a session using the provided AWS credentials
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
)

# Create an S3 client using the session
s3_client = session.client('s3')

# List all buckets in the S3 account
buckets = s3_client.list_buckets()

# Print the names of the buckets
print("S3 Buckets:")
for bucket in buckets['Buckets']:
    print(f"  {bucket['Name']}")
