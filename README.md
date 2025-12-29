<!-- markdownlint-disable MD041 -->

![CI/CD Pipeline](https://github.com/jerosanchez/fastapi-service/actions/workflows/deploy.yaml/badge.svg)
![Beta](https://img.shields.io/badge/status-beta-yellow)
![Python Version](https://img.shields.io/badge/python-3.13-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Docs](https://img.shields.io/badge/docs-available-brightgreen)

# README

## Getting Started

Follow these steps to set up your development environment:

### 1. Clone the repository

```sh
git clone git@github.com:jerosanchez/fastapi-service.git
cd post-service
```

### 2. Install markdownlint (for Markdown linting)

You need to install `markdownlint` globally to enable linting for Markdown files:

```sh
sudo apt update && sudo apt install nodejs npm
npm install -g markdownlint-cli
```

### 3. Install Python dependencies

Before using any other make target, run:

```sh
make install
```

This will create a virtual environment (if it doesn't exist) and install all Python dependencies listed in `requirements.txt`.

### 4. Customize the template for your project

Since this repository was created from a template, you'll need to customize several files for your specific project. Here's a checklist of what to update:

#### 4.1 Project Metadata

- **[pyproject.toml](pyproject.toml)**:
  - Update `name` (currently `fastapi-service`) to your project name
  - Update `description` to describe your service
  - Update `authors` with your name and email

- **[LICENSE](LICENSE)**:
  - Update the copyright holder name if needed

- **README.md** (this file):
  - Update the CI/CD badge URL to point to your repository
  - Update the repository URL in the clone command (step 1)
  - Customize the project description and any service-specific instructions

- **[CONTRIBUTING.md](CONTRIBUTING.md)**:
  - Review and customize development workflow guidelines for your team
  - Update project-specific folder structure details if you add new directories

#### 4.2 Application Configuration

- **[app/core/config.py](app/core/config.py)**:
  - Change `app_name` from `"MyApp"` to your application name
  - Add any additional configuration variables your service needs

- **[.env.example](.env.example)**:
  - Update `APP_NAME` to match your application name
  - Update `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB` with your preferred defaults
  - Add any additional environment variables your service requires
  - Copy to `.env` for local development: `cp .env.example .env`

- **[.env.production](.env.production)**:
  - Update `APP_NAME` to match your application name
  - Review and adjust production settings (ports, log levels, workers)
  - Document any additional environment variables needed in production

#### 4.3 Docker Configuration

- **[docker-compose.yml](docker-compose.yml)**:
  - Update `container_name` values (`app-db`, `fastapi-service`) to match your project
  - Review and adjust default values in environment variable fallbacks
  - Adjust port mappings if your service uses different ports

- **[Dockerfile](Dockerfile)**:
  - Review if the Python version (3.13) matches your requirements
  - Adjust worker count in the CMD line if needed for production

#### 4.4 GitHub Actions and CI/CD

If you're using GitHub Actions for CI/CD:

- Update workflow files in `.github/workflows/` to reference your repository
- Add required secrets in GitHub repository settings (e.g., `POSTGRES_PASSWORD`, API keys)
- Update deployment targets and environment configurations

#### Quick Start Checklist

After customizing, verify your changes:

- Search for `fastapi-service`, `MyApp`, and `jerosanchez` across the codebase
- Ensure all references point to your new project name

### 5. Run and test the basic service

Start the FastAPI service:

```sh
make start
```

Once the server is running, open your browser and go to [http://localhost:8000/](http://localhost:8000/).

You should see a welcome message indicating the service is working.

You can also check the interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs).

### 6. Start building your FastAPI service

This project provides a foundation for new FastAPI services. To begin building your own service:

1. Create new API routes in the `app/api/` directory (e.g., add modules under `app/api/v1/`).
2. Define your data models in `app/models/`.
3. Add business logic and reusable functions in `app/services/`.
4. Update configuration as needed in `app/core/config.py`.
5. Register your new routes in `app/main.py`.

See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.
