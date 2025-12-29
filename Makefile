install:
	@echo "Installing application..."
	@python3.13 -m venv .venv
	@. .venv/bin/activate && \
		pip install .

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