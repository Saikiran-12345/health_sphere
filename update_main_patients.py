path = "backend/app/main.py"
with open(path, "r") as f:
    content = f.read()

if "from app.api import patients" not in content:
    content = content.replace("from app.api import auth", "from app.api import auth, patients")
    content = content.replace("app.include_router(auth.router)", "app.include_router(auth.router)\napp.include_router(patients.router)")
    with open(path, "w") as f:
        f.write(content)
