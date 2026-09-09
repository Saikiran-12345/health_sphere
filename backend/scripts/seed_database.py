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
