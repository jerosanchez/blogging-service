install:
	@echo "Installing application..."
	@python3.13 -m venv .venv
	@. .venv/bin/activate && \
		pip install -e .

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

build:
	@echo "Building application..."

deploy:
	@echo "Deploying application..."

all: install format lint test build deploy

start:
	@echo "Starting services with Docker Compose..."
	@docker compose up -d

stop:
	@echo "Stopping services with Docker Compose..."
	@docker compose down


db-reset: ## Reset Docker PostgreSQL volumes
	@echo "WARNING: This will delete all PostgreSQL data!"
	@read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ] || [ "$$confirm" = "Y" ]
	docker compose -f docker-compose.yml down -v
	docker volume prune -f

db-revision: ## Create a new migration
	@read -p "Enter migration message: " msg; \
	@. .venv/bin/activate && \
		alembic revision --autogenerate -m \"$$msg\""

db-migrate: ## Run database migrations
	@. .venv/bin/activate && \
		alembic upgrade head

precommit: format lint test
	@echo "Pre-commit checks passed."

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

.PHONY: install format lint test build deploy all start stop precommit clean