from app.models.patient import Patient
from typing import Dict, Any

class FHIRMapper:
    @staticmethod
    def patient_to_fhir(patient: Patient) -> Dict[str, Any]:
        """
        Maps internal SQLAlchemy Patient model to standard FHIR R4 Patient Resource.
        """
        return {
            "resourceType": "Patient",
            "id": str(patient.id),
            "identifier": [
                {
                    "use": "usual",
                    "value": f"PAT-{str(patient.id).split('-')[0]}"
                }
            ],
            "active": True,
            "name": [
                {
                    "use": "official",
                    "family": patient.user.last_name if patient.user else "Unknown",
                    "given": [patient.user.first_name if patient.user else "Unknown"]
                }
            ],
            "telecom": [
                {
                    "system": "phone",
                    "value": patient.user.phone_number if patient.user else "",
                    "use": "mobile"
                }
            ],
            "gender": patient.gender.lower() if patient.gender else "unknown",
            "birthDate": patient.date_of_birth.isoformat() if patient.date_of_birth else None,
            "address": [
                {
                    "use": "home",
                    "text": patient.address
                }
            ]
        }
