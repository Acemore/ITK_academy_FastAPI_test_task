# ITK academy FastAPI test task

[![docker-ci](https://github.com/Acemore/ITK_academy_FastAPI_test_task/actions/workflows/docker-ci.yml/badge.svg)](https://github.com/Acemore/ITK_academy_FastAPI_test_task/actions/workflows/docker-ci.yml)

This program is web app that provides REST API CRUD operations to work with items.

## To run this app locally

Clone repo:

```bash
git clone git@github.com:Acemore/ITK_academy_FastAPI_test_task.git
```

Create .env file from .env-sample

Install dependencies:

```bash
uv sync
```

Run app:

```bash
uv run uvicorn app.main:app --reload
```

Run tests:

```bash
uv run pytest tests/item_tests.py
```

Run linter check:

```bash
uv run flake8 app tests
```

## To run this app from dockerfile

Build the app image

```bash
docker build --tag <tag_name> .
```

Run container with this app

```bash
docker run -p 8000:8000 -d <tag_name>
```

## To run this app using docker compose

Run app

```bash
docker compose up -d
```

Run tests and linter check

```bash
docker compose -f docker-compose-tests.yml up
```

Remove containers

```bash
docker compose rm -fs
```
