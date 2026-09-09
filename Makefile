.PHONY: up down build logs seed test shell-backend shell-frontend

up:
	docker-compose up -d

down:
	docker-compose down

build:
	docker-compose build

logs:
	docker-compose logs -f

seed:
	docker-compose exec backend python scripts/seed_database.py

test:
	docker-compose exec backend pytest

shell-backend:
	docker-compose exec backend /bin/bash

shell-frontend:
	docker-compose exec frontend /bin/sh
