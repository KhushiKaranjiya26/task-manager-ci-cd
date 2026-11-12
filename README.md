
# Task Manager API

A simple FastAPI project created to learn CI/CD.

## Features

- Create tasks
- Get all tasks
- Get task by ID
- Update tasks
- Delete tasks
- Health check endpoint

## Technologies

- Python
- FastAPI
- Pytest
- Docker
- GitHub Actions

## Installation

```bash
py -m venv .venv
```

Activate the virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

## Run application

```bash
uvicorn main:app --reload
```

## Run tests

```bash
pytest -v
```
