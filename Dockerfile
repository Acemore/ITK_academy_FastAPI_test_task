FROM python:3.13-slim

WORKDIR /project

RUN pip install uv

ADD pyproject.toml uv.lock ./
RUN uv sync --no-install-project

ADD . .

CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0"]
