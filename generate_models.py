import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Database Setup
create_file('backend/app/db/database.py', """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Fallback to local postgres if ENV not provided
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/healthsphere")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
""")

# 2. Base Model
create_file('backend/app/models/base.py', """
import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base

class BaseModel(Base):
    __abstract__ = True
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
""")

# 3. User & Auth Models
create_file('backend/app/models/user.py', """
from sqlalchemy import Column, String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
import enum
from app.models.base import BaseModel

class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    DOCTOR = "DOCTOR"
    NURSE = "NURSE"
    RECEPTIONIST = "RECEPTIONIST"
    LAB_STAFF = "LAB_STAFF"
    PHARMACIST = "PHARMACIST"
    PATIENT = "PATIENT"

class User(BaseModel):
    __tablename__ = "users"

    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=True)
    role = Column(Enum(UserRole), default=UserRole.PATIENT, nullable=False)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    patient_profile = relationship("Patient", back_populates="user", uselist=False)
    doctor_profile = relationship("Doctor", back_populates="user", uselist=False)
    staff_profile = relationship("Staff", back_populates="user", uselist=False)
""")

# 4. Department & Core Models
create_file('backend/app/models/department.py', """
from sqlalchemy import Column, String, Text
from sqlalchemy.orm import relationship
from app.models.base import BaseModel

class Department(BaseModel):
    __tablename__ = "departments"

    name = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    contact_number = Column(String(20), nullable=True)
    location = Column(String(100), nullable=True)
    
    # Relationships
    doctors = relationship("Doctor", back_populates="department")
""")

# 5. Doctor & Patient Models
create_file('backend/app/models/doctor.py', """
from sqlalchemy import Column, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class Doctor(BaseModel):
    __tablename__ = "doctors"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)
    department_id = Column(UUID(as_uuid=True), ForeignKey("departments.id"), nullable=False)
    
    specialization = Column(String(100), nullable=False)
    license_number = Column(String(100), unique=True, nullable=False)
    consultation_fee = Column(Integer, default=0)
    bio = Column(Text, nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="doctor_profile")
    department = relationship("Department", back_populates="doctors")
""")

create_file('backend/app/models/patient.py', """
from sqlalchemy import Column, String, Date, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import enum
from app.models.base import BaseModel

class BloodGroup(str, enum.Enum):
    A_POS = "A+"
    A_NEG = "A-"
    B_POS = "B+"
    B_NEG = "B-"
    O_POS = "O+"
    O_NEG = "O-"
    AB_POS = "AB+"
    AB_NEG = "AB-"

class Patient(BaseModel):
    __tablename__ = "patients"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)
    
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(20), nullable=False)
    blood_group = Column(Enum(BloodGroup), nullable=True)
    address = Column(Text, nullable=True)
    emergency_contact_name = Column(String(100), nullable=True)
    emergency_contact_number = Column(String(20), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="patient_profile")
""")

create_file('backend/app/models/staff.py', """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class Staff(BaseModel):
    __tablename__ = "staff"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), unique=True, nullable=False)
    employee_id = Column(String(50), unique=True, nullable=False)
    designation = Column(String(100), nullable=False)
    
    # Relationships
    user = relationship("User", back_populates="staff_profile")
""")

create_file('backend/app/models/__init__.py', """
from app.models.base import BaseModel
from app.models.user import User, UserRole
from app.models.department import Department
from app.models.doctor import Doctor
from app.models.patient import Patient, BloodGroup
from app.models.staff import Staff
""")

print("Backend models generated successfully.")
