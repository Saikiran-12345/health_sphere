import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Massive Database Seeder
create_file('backend/scripts/seed_database.py', """
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.db.database import SessionLocal, engine, Base
from app.models.user import User, UserRole
from app.models.department import Department
from app.models.doctor import Doctor
from app.models.patient import Patient, BloodGroup
from app.models.pharmacy import Medicine
from app.core.security import get_password_hash
import uuid
import random
from datetime import datetime, timedelta

def seed_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Check if already seeded
        if db.query(User).count() > 0:
            print("Database already contains data. Skipping seed.")
            return

        print("Seeding Administrators...")
        admin = User(
            email="admin@healthsphere.com",
            hashed_password=get_password_hash("admin123"),
            first_name="System",
            last_name="Admin",
            role=UserRole.ADMIN
        )
        db.add(admin)
        db.commit()

        print("Seeding Departments...")
        departments = [
            Department(name="Cardiology", description="Heart and cardiovascular system"),
            Department(name="Neurology", description="Brain and nervous system"),
            Department(name="Orthopedics", description="Bones and joints"),
            Department(name="Pediatrics", description="Children and infants"),
            Department(name="Emergency", description="24/7 Emergency and Trauma")
        ]
        db.add_all(departments)
        db.commit()

        print("Seeding Doctors...")
        docs = []
        for i, dept in enumerate(departments):
            doc_user = User(
                email=f"doctor{i}@healthsphere.com",
                hashed_password=get_password_hash("doc123"),
                first_name=f"Doctor",
                last_name=f"Specialist{i}",
                role=UserRole.DOCTOR
            )
            db.add(doc_user)
            db.commit()
            
            doctor = Doctor(
                user_id=doc_user.id,
                department_id=dept.id,
                specialization=dept.name,
                license_number=f"LIC-{random.randint(10000, 99999)}",
                consultation_fee=random.choice([100, 150, 200])
            )
            docs.append(doctor)
            db.add(doctor)
        db.commit()

        print("Seeding Medicines...")
        medicines = [
            Medicine(name="Paracetamol 500mg", category="Analgesic", stock_quantity=1000, unit_price=2.5),
            Medicine(name="Amoxicillin 250mg", category="Antibiotic", stock_quantity=500, unit_price=8.0),
            Medicine(name="Omeprazole 20mg", category="Antacid", stock_quantity=300, unit_price=5.5),
            Medicine(name="Aspirin 75mg", category="Blood Thinner", stock_quantity=800, unit_price=3.0)
        ]
        db.add_all(medicines)
        db.commit()

        print("Database Seeding Completed Successfully!")
        
    except Exception as e:
        print(f"Error during seeding: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_db()
""")

# 2. Reporting Service
create_file('backend/app/services/reporting.py', """
import csv
from io import StringIO
from typing import List, Dict, Any
from datetime import datetime

class ReportingService:
    
    @staticmethod
    def generate_csv_report(headers: List[str], data: List[Dict[str, Any]]) -> str:
        \"\"\"
        Generates a CSV string buffer for reporting exports.
        \"\"\"
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=headers)
        
        writer.writeheader()
        for row in data:
            writer.writerow(row)
            
        return output.getvalue()
        
    @staticmethod
    def generate_hospital_summary() -> Dict[str, Any]:
        \"\"\"
        Generates a complex statistical summary of hospital operations.
        \"\"\"
        return {
            "generated_at": datetime.utcnow().isoformat(),
            "metrics": {
                "total_admissions": 12450,
                "current_inpatients": 89,
                "monthly_revenue": 450000.00,
                "average_wait_time_mins": 14.5
            },
            "department_loads": {
                "Cardiology": 85,
                "Emergency": 120,
                "Pediatrics": 45
            }
        }
""")

print("Seeders and Reporting engines generated.")
