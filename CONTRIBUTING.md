# Contributing Guide

Thank you for your interest in contributing to this project!

## Development Lifecycle

This project uses a Makefile to streamline common development tasks. Below are the main targets you should use during development:

- **make install**: Set up the Python virtual environment and install all dependencies.
- **make format**: Automatically format Python code using Black.
- **make lint**: Run code quality checks on Python and Markdown files.
- **make test**: Run the test suite to ensure your changes do not break anything.
- **make build**: Build the application (if applicable).
- **make start**: Start all services using Docker Compose.
- **make stop**: Stop all services started by Docker Compose.
- **make clean**: Remove the virtual environment, caches, build artifacts, and other generated files. Use this if you encounter strange issues or want to reset your environment. This is especially helpful before reinstalling dependencies or when switching branches.
- **make precommit**: Run all checks and formatting steps required before committing code. This target is designed to help you catch issues early and ensure code quality before pushing changes.

## Workflow

1. Fork and clone the repository.
2. Run `make install` to set up your environment.
3. Use `make format`, `make lint`, and `make test` regularly as you work.
4. Before committing, always run `make precommit` to ensure your code meets all quality standards.
5. If you encounter issues, try `make clean` and then `make install` to reset your environment.
6. Submit a pull request with a clear description of your changes.

For any questions, please open an issue or reach out to the maintainers.

## Docker Development

### Running with Docker Compose

This project includes Docker support for local development and production deployment:

```sh
# Copy environment template (optional)
cp .env.example .env

# Start services (app + database)
make start

# View logs
docker compose logs -f

# Stop services
make stop
```

### Environment Files

The project includes two environment file templates:

- **`.env.example`**: Development configuration with all available options documented. Use this as your starting point:

  ```sh
  cp .env.example .env
  ```
  
- **`.env.production`**: Production configuration template showing recommended production settings. Useful for:
  - Documenting production requirements
  - Local testing of production mode
  - Manual production deployments

**Important**: These files are primarily **documentation**. The `docker-compose.yml` contains sensible defaults (`${VAR:-default}`), so Docker Compose works without any `.env` file. However, using the templates improves clarity and makes local customization easier.

**CI/CD Note**: When deploying via GitHub Actions or other CI/CD pipelines, environment variables come from your CI/CD secrets, not from `.env` files.

### Testing Production Mode Locally

```sh
cp .env.production .env
# Edit .env with test credentials
make start
```

This runs the application in production mode (multiple workers, no hot-reload) while still on your local machine.

## Project Folder Structure

The main folders and files in this project are:

- **app/**: Main application code.
  - **api/**: API route definitions (e.g., `v1/` for versioned APIs).
  - **clients/**: Clients for internal and third-party services.
  - **core/**: Cross-cutting concerns: config, logging, utilities, etc.
  - **db/**: Database schemas, migrations, and related database setup.
  - **domain/**: Business models, framework-agnostic dataclasses.
  - **models/**: Pydantic models and validation logic.
  - **repositories/**: Database access logic and remote service integration.
  - **services/**: Business logic and reusable service functions.
  - **main.py**: FastAPI application entry point.
- **docs/**: Project documentation.
  - **adr/**: Architecture Decision Records.
  - **agents/**: Guidelines for agents or automation components.
  - **diagrams/**: System and architecture diagrams.
  - **specs/**: API and system specifications.
- **tests/**: Unit and integration tests.
- **CONTRIBUTING.md**: Contribution guidelines (this file).
- **Makefile**: Common development commands.
- **README.md**: Project overview and setup instructions.
- **requirements.txt**: Python dependencies.

This structure is designed to keep code organized and maintainable as your FastAPI service grows. The `app/repositories/` folder is recommended for encapsulating all database access logic, keeping it separate from business logic and models.

## VS Code Extensions

To improve your development experience, consider installing the following VS Code extensions:

```sh
code --install-extension ms-python.vscode-python-envs
code --install-extension bierner.markdown-preview-mermaid
```

- **Python Environments**: Provides a unified Python environment experience and better integration for Python projects.
- **Markdown Preview Mermaid Support**: Adds Mermaid diagram and flowchart support to VS Code's markdown preview.

Other useful extensions for FastAPI, linting, testing, Docker, and YAML include:

```sh
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-python.python
code --install-extension ms-python.black-formatter
code --install-extension ms-python.isort
code --install-extension ms-python.pylint
code --install-extension ms-python.pytest
```

- **Docker**: Manage and debug containerized applications.
- **Python**: Core Python language support.
- **Black Formatter**: Auto-format Python code with Black.
- **isort**: Sort Python imports automatically.
- **Pylint**: Python code linting.
- **Pytest**: Python test integration.
