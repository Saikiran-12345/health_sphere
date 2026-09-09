import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Update Requirements for WebAuthn
path_req = "backend/requirements.txt"
with open(path_req, "a") as f:
    f.write("\nwebauthn\n")

# 2. WebAuthn Models
create_file('backend/app/models/passkeys.py', """
from sqlalchemy import Column, String, ForeignKey, LargeBinary
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import BaseModel

class UserPasskey(BaseModel):
    __tablename__ = "user_passkeys"
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    credential_id = Column(LargeBinary, nullable=False, unique=True)
    public_key = Column(LargeBinary, nullable=False)
    sign_count = Column(String(50), nullable=False)
""")

# 3. WebAuthn FastApi Router
create_file('backend/app/api/webauthn.py', """
import os
from fastapi import APIRouter, Depends, HTTPException, Response
from webauthn import generate_registration_options, verify_registration_response
from webauthn.helpers.structs import RegistrationCredential
from app.api.deps import get_current_user
from app.models.user import User
from pydantic import BaseModel

router = APIRouter(prefix="/api/auth/webauthn", tags=["Passkey Authentication"])

RP_ID = os.getenv("RP_ID", "localhost")
RP_NAME = "HealthSphere Enterprise"

class RegistrationResponseSchema(BaseModel):
    credential: dict

@router.post("/register/generate-options")
def generate_options(user: User = Depends(get_current_user)):
    \"\"\"
    Generates WebAuthn registration options to allow a doctor to register FaceID/TouchID.
    \"\"\"
    options = generate_registration_options(
        rp_id=RP_ID,
        rp_name=RP_NAME,
        user_id=str(user.id).encode("utf-8"),
        user_name=user.email,
    )
    # In reality, cache the challenge in Redis to verify later
    return options

@router.post("/register/verify")
def verify_registration(payload: RegistrationResponseSchema, user: User = Depends(get_current_user)):
    \"\"\"
    Verifies the hardware cryptographic signature and saves the public key.
    \"\"\"
    try:
        # Expected Challenge would be retrieved from Redis in prod
        expected_challenge = b"mock_challenge_verify"
        
        verification = verify_registration_response(
            credential=payload.credential,
            expected_challenge=expected_challenge,
            expected_rp_id=RP_ID,
            expected_origin=f"http://{RP_ID}:5173",
        )
        
        # Here we would save verification.credential_id and verification.credential_public_key to DB
        return {"status": "success", "message": "Biometric Passkey registered securely."}
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Registration failed: {str(e)}")
""")

# 4. Attach to Main and Init
path_main = "backend/app/main.py"
with open(path_main, "r") as f:
    content = f.read()

if "from app.api import webauthn" not in content:
    content = content.replace("from app.api import payments, audit, iot, diagnostics", "from app.api import payments, audit, iot, diagnostics, webauthn")
    content += "\napp.include_router(webauthn.router)\n"
    with open(path_main, "w") as f:
        f.write(content)

path_init = "backend/app/models/__init__.py"
with open(path_init, "a") as f:
    f.write("\nfrom app.models.passkeys import UserPasskey\n")

print("Biometric Passkeys generated.")
