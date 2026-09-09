import os
import subprocess
from datetime import datetime
import boto3
from botocore.exceptions import NoCredentialsError

# Configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "healthsphere")
DB_USER = os.getenv("DB_USER", "postgres")
S3_BUCKET = os.getenv("S3_BACKUP_BUCKET", "healthsphere-db-backups")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

def backup_postgres():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f"healthsphere_backup_{timestamp}.sql"
    
    print(f"Starting database backup to {backup_file}...")
    
    try:
        # Run pg_dump
        subprocess.run(
            ['pg_dump', '-h', DB_HOST, '-U', DB_USER, '-F', 'c', '-b', '-v', '-f', backup_file, DB_NAME],
            check=True,
            env=dict(os.environ, PGPASSWORD=os.getenv("DB_PASSWORD", "postgres"))
        )
        print("Backup created successfully.")
        return backup_file
    except subprocess.CalledProcessError as e:
        print(f"Error during backup: {e}")
        return None

def upload_to_s3(file_name):
    s3 = boto3.client('s3', region_name=AWS_REGION)
    try:
        print(f"Uploading {file_name} to S3 bucket {S3_BUCKET}...")
        s3.upload_file(file_name, S3_BUCKET, file_name)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available for AWS S3")
        return False

if __name__ == "__main__":
    file = backup_postgres()
    if file:
        success = upload_to_s3(file)
        if success:
            os.remove(file) # Clean up local file after S3 upload
            print("Backup process completely finished.")
