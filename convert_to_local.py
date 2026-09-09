import os
import re

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Rewrite backup_db.py to strictly use Local Storage (NO AWS)
create_file('backend/scripts/backup_db.py', """
import os
import subprocess
from datetime import datetime

# Local Configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "healthsphere")
DB_USER = os.getenv("DB_USER", "postgres")
BACKUP_DIR = os.getenv("BACKUP_DIR", os.path.join(os.path.dirname(__file__), "..", "backups"))

def backup_postgres_locally():
    # Ensure local backup directory exists
    os.makedirs(BACKUP_DIR, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(BACKUP_DIR, f"healthsphere_local_backup_{timestamp}.sql")
    
    print(f"Starting database backup to Local Storage: {backup_file}...")
    
    try:
        # Run pg_dump
        subprocess.run(
            ['pg_dump', '-h', DB_HOST, '-U', DB_USER, '-F', 'c', '-b', '-v', '-f', backup_file, DB_NAME],
            check=True,
            env=dict(os.environ, PGPASSWORD=os.getenv("DB_PASSWORD", "postgres"))
        )
        print(f"SUCCESS: Local backup secured at {backup_file}.")
        return backup_file
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Backup failed: {e}")
        return None

if __name__ == "__main__":
    print("HealthSphere Local Offline Backup Utility Initiated...")
    backup_postgres_locally()
""")

# 2. Remove AWS dependencies from requirements
path_req = "backend/requirements.txt"
if os.path.exists(path_req):
    with open(path_req, "r") as f:
        reqs = f.read()
    
    # Remove boto3
    reqs = re.sub(r'\\bboto3\\b', '', reqs)
    
    with open(path_req, "w") as f:
        f.write(reqs.strip())

# 3. Update docker-compose to persist backups locally
path_docker = "docker-compose.yml"
if os.path.exists(path_docker):
    with open(path_docker, "r") as f:
        docker_content = f.read()
    
    if "backups_data:" not in docker_content:
        # Add backups volume mapping to db
        docker_content = docker_content.replace(
            "- postgres_data:/var/lib/postgresql/data",
            "- postgres_data:/var/lib/postgresql/data\\n      - backups_data:/backups"
        )
        # Declare volume
        docker_content = docker_content.replace(
            "volumes:\\n  postgres_data:",
            "volumes:\\n  postgres_data:\\n  backups_data:"
        )
        
        with open(path_docker, "w") as f:
            f.write(docker_content)

print("AWS dependencies removed. Fully converted to Local Database backups.")
