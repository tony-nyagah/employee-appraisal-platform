# Variables
PYTHON := python
MANAGE_PY := src/staff_perfomance_evaluation_platform/manage.py
PORT := 8000

# Default target
.DEFAULT_GOAL := help

# Help target
help:
	@echo "Available targets:"
	@echo "   run-server                  Run the Django development server"
	@echo "   migrate                     Apply database migrations"
	@echo "   makemigrations              Create new database migrations"
	@echo "   shell                       Open Django shell"
	@echo "   createsuperuser             Create a superuser"
	@echo "   test                        Run tests"
	@echo "   collectstatic               Collect static files"
	@echo "   install-deps                Install project dependencies"
	@echo "   update-deps                 Update project dependencies"

# Django management commands
run-server:
	$(PYTHON) $(MANAGE_PY) runserver $(PORT)

migrate:
	$(PYTHON) $(MANAGE_PY) migrate

makemigrations:
	$(PYTHON) $(MANAGE_PY) makemigrations

shell:
	$(PYTHON) $(MANAGE_PY) shell

createsuperuser:
	$(PYTHON) $(MANAGE_PY) createsuperuser

test:
	$(PYTHON) $(MANAGE_PY) test

collectstatic:
	$(PYTHON) $(MANAGE_PY) collectstatic

# Dependency management
install-deps:
	pip install -r requirements.txt

update-deps:
	pip install --upgrade -r requirements.txt

# Ensure that command-line arguments are not interpreted as make targets
.PHONY: help run-server migrate makemigrations shell createsuperuser test collectstatic install-deps update-deps