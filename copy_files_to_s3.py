import boto3
import requests
import os
import zipfile
import io

# Configuration
GITHUB_REPO = 'https://github.com/username/repository/archive/refs/heads/main.zip'
S3_BUCKET = 'my-github-files-bucket'
AWS_ACCESS_KEY = 'YOUR_AWS_ACCESS_KEY'
AWS_SECRET_KEY = 'YOUR_AWS_SECRET_KEY'
AWS_REGION = 'YOUR_AWS_REGION'

def download_github_repo(repo_url):
    response = requests.get(repo_url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to download repository: {response.status_code}")

def upload_to_s3(file_data, bucket, key, aws_access_key, aws_secret_key, region):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=region
    )
    s3_client.put_object(Body=file_data, Bucket=bucket, Key=key)

def main():
    # Download GitHub repository
    repo_data = download_github_repo(GITHUB_REPO)
    
    # Extract and upload files to S3
    with zipfile.ZipFile(io.BytesIO(repo_data)) as z:
        for file_info in z.infolist():
            if not file_info.is_dir():
                file_data = z.read(file_info.filename)
                s3_key = os.path.basename(file_info.filename)
                upload_to_s3(file_data, S3_BUCKET, s3_key, AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION)
                print(f"Uploaded {s3_key} to {S3_BUCKET}")

if __name__ == "__main__":
    main()
