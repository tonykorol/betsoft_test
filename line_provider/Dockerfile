FROM python:3.10

WORKDIR /app

COPY ../pyproject.toml ../poetry.lock ./
RUN pip install --no-cache-dir poetry && \
    poetry install --no-root

COPY . .

CMD ["poetry", "run", "uvicorn", "line_provider.main:app", "--host", "0.0.0.0", "--port", "8001"]