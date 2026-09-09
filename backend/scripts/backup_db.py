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
