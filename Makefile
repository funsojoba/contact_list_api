COMPOSE = docker compose
SERVICE = django


build:
	$(COMPOSE) build

up:
	$(COMPOSE) up

up-d:
	$(COMPOSE) up -d

enter:
	$(COMPOSE) exec $(SERVICE) bash

createsuperuser:
	$(COMPOSE) exec $(SERVICE) python manage.py createsuperuser

pre-commit:
	pre-commit run --all-files

populate-history:
	$(COMPOSE) exec $(SERVICE) python manage.py populate_history --auto

shell:
	$(COMPOSE) exec $(SERVICE) python manage.py shell

test:
	$(COMPOSE) run --rm $(SERVICE) pytest -vv

down:
	$(COMPOSE) down

migrate:
	$(COMPOSE) exec $(SERVICE) python manage.py migrate

migrations:
	$(COMPOSE) exec $(SERVICE) python manage.py makemigrations

showmigrations:
	$(COMPOSE) exec $(SERVICE) python manage.py showmigrations
