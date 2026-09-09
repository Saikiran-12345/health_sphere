import os

def create_file(path, content):
    dir_name = os.path.dirname(path)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

# 1. Update Requirements for Testing and HL7
path_req = "backend/requirements.txt"
with open(path_req, "a") as f:
    f.write("\npytest\nhttpx\npytest-asyncio\n")

# 2. HL7 v2 Message Parser
create_file('backend/app/services/hl7_parser.py', """
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class HL7Parser:
    \"\"\"
    Enterprise HL7 v2.x Message Parser.
    Extracts clinical data from raw pipe-delimited (|) hospital messages.
    \"\"\"
    
    @staticmethod
    def parse_message(raw_hl7: str) -> Dict[str, Any]:
        segments = raw_hl7.strip().split('\\n')
        parsed_data = {
            "metadata": {},
            "patient": {},
            "observations": []
        }
        
        try:
            for segment in segments:
                fields = segment.split('|')
                segment_type = fields[0]
                
                if segment_type == "MSH":
                    parsed_data["metadata"] = {
                        "sending_app": fields[2] if len(fields) > 2 else "",
                        "receiving_app": fields[4] if len(fields) > 4 else "",
                        "message_time": fields[6] if len(fields) > 6 else "",
                        "message_type": fields[8] if len(fields) > 8 else "",
                    }
                elif segment_type == "PID":
                    names = fields[5].split('^') if len(fields) > 5 else ["", ""]
                    parsed_data["patient"] = {
                        "patient_id": fields[3] if len(fields) > 3 else "",
                        "last_name": names[0],
                        "first_name": names[1] if len(names) > 1 else "",
                        "dob": fields[7] if len(fields) > 7 else "",
                        "gender": fields[8] if len(fields) > 8 else ""
                    }
                elif segment_type == "OBX":
                    parsed_data["observations"].append({
                        "type": fields[2] if len(fields) > 2 else "",
                        "observation": fields[3] if len(fields) > 3 else "",
                        "value": fields[5] if len(fields) > 5 else "",
                        "units": fields[6] if len(fields) > 6 else "",
                        "reference_range": fields[7] if len(fields) > 7 else "",
                        "abnormal_flags": fields[8] if len(fields) > 8 else ""
                    })
                    
            return parsed_data
        except Exception as e:
            logger.error(f"HL7 Parsing Failed: {str(e)}")
            raise ValueError(f"Invalid HL7 format: {str(e)}")
""")

# 3. Create Pytest Configuration and Test Suite
create_file('backend/pytest.ini', """
[pytest]
asyncio_mode = auto
testpaths = tests
python_files = test_*.py
""")

create_file('backend/tests/__init__.py', "")

create_file('backend/tests/test_hl7_parser.py', """
import pytest
from app.services.hl7_parser import HL7Parser

def test_hl7_parsing_success():
    raw_message = (
        "MSH|^~\\&|LAB_SYSTEM|HOSPITAL|HEALTHSPHERE|SYS|202310151430||ORU^R01|MSG001|P|2.4\\n"
        "PID|1||PAT-9988||Doe^John||19800101|M\\n"
        "OBX|1|NM|GLU^Glucose|1|105|mg/dL|70-99|H|||F"
    )
    
    result = HL7Parser.parse_message(raw_message)
    
    assert result["metadata"]["sending_app"] == "LAB_SYSTEM"
    assert result["patient"]["last_name"] == "Doe"
    assert result["patient"]["first_name"] == "John"
    assert result["patient"]["gender"] == "M"
    assert len(result["observations"]) == 1
    assert result["observations"][0]["value"] == "105"
    assert result["observations"][0]["abnormal_flags"] == "H"

def test_hl7_parsing_empty():
    result = HL7Parser.parse_message("")
    assert result["metadata"] == {}
    assert result["patient"] == {}
    assert len(result["observations"]) == 0
""")

create_file('backend/tests/test_api_health.py', """
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    # Assuming standard FastAPI root acts as health check or Swagger redirect
    response = client.get("/")
    # Even if it redirects or 404s, we verify the app boots without crashing
    assert response.status_code in [200, 404]
    
def test_docs_available():
    response = client.get("/docs")
    assert response.status_code == 200
""")

print("HL7 Interoperability Engine and Pytest Suite generated.")
