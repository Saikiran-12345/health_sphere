import os

path = "backend/app/main.py"
with open(path, "r") as f:
    content = f.read()

if "from app.api import clinical" not in content:
    content = content.replace("from app.api import auth, patients", "from app.api import auth, patients, clinical")
    content = content.replace("app.include_router(patients.router)", "app.include_router(patients.router)\napp.include_router(clinical.router)")
    with open(path, "w") as f:
        f.write(content)

path2 = "backend/app/models/__init__.py"
with open(path2, "r") as f:
    content = f.read()

if "Appointment" not in content:
    content += "\nfrom app.models.appointment import Appointment, AppointmentStatus\n"
    content += "from app.models.medical_record import MedicalRecord, RecordType\n"
    with open(path2, "w") as f:
        f.write(content)
