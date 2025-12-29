<!-- markdownlint-disable MD041 -->

![CI/CD Pipeline](https://github.com/jerosanchez/blogging-service/actions/workflows/deploy.yaml/badge.svg)
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

### 4. Run

Start the FastAPI service locally:

```sh
make start
```

Once the server is running, open your browser and go to [http://localhost:8000/](http://localhost:8000/).

You can also check the interactive API docs at [http://localhost:8000/docs](http://localhost:8000/docs).

### 5. Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) file for guidelines on how to conbtribute to this project.
