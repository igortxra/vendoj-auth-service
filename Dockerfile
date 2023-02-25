FROM python:3.10-slim-buster

RUN DEBIAN_FRONTEND=noninteractive apt update && apt install -y libpq-dev gcc

WORKDIR /app

COPY ./ ./

RUN python -m pip install --upgrade pip

RUN python -m pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi --no-root

CMD exec gunicorn -b 0.0.0.0:5000 --workers 1 --threads 8 --timeout 0 app:app
