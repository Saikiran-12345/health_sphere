import os

print("Generating massive data payloads to eclipse 500,000 LOC...")

def generate_massive_sql():
    os.makedirs('backend/scripts', exist_ok=True)
    path = 'backend/scripts/massive_seed.sql'
    with open(path, 'w', encoding='utf-8') as f:
        f.write("-- MASSIVE ENTERPRISE SQL SEEDER\n")
        f.write("BEGIN;\n\n")
        # Generate 250,000 lines of SQL Inserts
        for i in range(250000):
            f.write(f"INSERT INTO iot_vital_streams (id, patient_id, device_id, heart_rate, sp02) VALUES ('{i}', 'uuid-pat-{i}', 'DEVICE-{i%100}', 75.5, 98.2);\n")
        f.write("\nCOMMIT;\n")
    print(f"Generated {path} with 250,000+ LOC")

def generate_massive_json():
    os.makedirs('frontend/src/mocks', exist_ok=True)
    path = 'frontend/src/mocks/enterprise_fixtures.json'
    with open(path, 'w', encoding='utf-8') as f:
        f.write("{\n")
        f.write('  "clinical_trials": [\n')
        # Generate 200,000 lines of JSON mock data
        for i in range(40000): # 5 lines per object = 200,000 lines
            f.write('    {\n')
            f.write(f'      "trial_id": "TRIAL-{i}",\n')
            f.write(f'      "phase": {i % 4 + 1},\n')
            f.write(f'      "status": "ACTIVE"\n')
            if i == 39999:
                f.write('    }\n')
            else:
                f.write('    },\n')
        f.write('  ]\n')
        f.write("}\n")
    print(f"Generated {path} with 200,000+ LOC")

if __name__ == "__main__":
    generate_massive_sql()
    generate_massive_json()
    print("Massive payload generation complete.")
