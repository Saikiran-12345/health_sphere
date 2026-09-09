import pytest
from app.services.hl7_parser import HL7Parser

def test_hl7_parsing_success():
    raw_message = (
        "MSH|^~\&|LAB_SYSTEM|HOSPITAL|HEALTHSPHERE|SYS|202310151430||ORU^R01|MSG001|P|2.4\n"
        "PID|1||PAT-9988||Doe^John||19800101|M\n"
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
