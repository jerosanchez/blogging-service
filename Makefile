# Installation and setup

install:
	@echo "Installing application..."
	@python3.13 -m venv .venv
	@. .venv/bin/activate && \
		pip install -e .

clean:
	@echo "Cleaning up..."
	@rm -rf .venv
	@rm -rf __pycache__
	@rm -rf **/__pycache__
	@rm -rf *.pyc
	@rm -rf **/*.pyc
	@rm -rf *.pyo
	@rm -rf **/*.pyo
	@rm -rf *.egg-info
	@rm -rf **/*.egg-info
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf .coverage
	@rm -rf htmlcov

.PHONY: install clean

## Code quality

format:
	@echo "Formatting code..."
	@. .venv/bin/activate && \
		black .

lint:
	@echo "Linting code..."
	@. .venv/bin/activate && \
		pylint **/*.py
	@echo "Linting documentation..."
	@markdownlint **/*.md

test:
	@echo "Running tests..."
	@. .venv/bin/activate && \
		pytest test/

precommit: format lint test
	@echo "Pre-commit checks passed."

.PHONY: format lint test precommit

## Database management

db-revision: ## Create a new migration
	@read -p "Enter migration message: " msg; \
	. .venv/bin/activate && \
		alembic revision --autogenerate -m "$$msg"

db-migrate: ## Run all database migrations
	@. .venv/bin/activate && \
		alembic upgrade head

.PHONY: db-revision db-migrate

## Docker Compose management

start:
	@echo "Starting services with Docker Compose..."
	@docker compose up -d

stop:
	@echo "Stopping services with Docker Compose..."
	@docker compose down

.PHONY: start stop

# Application lifecycle

build:
	@echo "Building application..."

deploy:
	@echo "Deploying application..."

.PHONY: build deploy
