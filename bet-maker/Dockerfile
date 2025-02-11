FROM python:3.10

WORKDIR /app

COPY pyproect.toml poetry.lock ./
RUN pip install --no-cache-dir poetry && \
    poetry install --no-root

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8002"]