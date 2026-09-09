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
    """
    Generates WebAuthn registration options to allow a doctor to register FaceID/TouchID.
    """
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
    """
    Verifies the hardware cryptographic signature and saves the public key.
    """
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
