###########
# BUILDER #
###########
FROM python:3.11-slim-bullseye AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true

WORKDIR /app

RUN apt-get update && apt-get install -y python3-dev

COPY pyproject.toml poetry.lock ./


RUN python -m pip install --no-cache-dir poetry==2.2.1 \
    && poetry config virtualenvs.in-project true \
    && poetry install --no-interaction --no-ansi --no-root \
    && rm -rf $(poetry config cache-dir)/{cache,artifacts}

###########
## IMAGE ##
###########
FROM python:3.11-slim-bullseye AS prod

COPY --from=builder /app /app

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app

COPY src ./src
COPY main.py .
COPY .env .
