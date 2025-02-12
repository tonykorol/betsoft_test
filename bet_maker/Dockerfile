FROM python:3.10

WORKDIR /app

COPY ../pyproject.toml ../poetry.lock ./

RUN pip install --no-cache-dir poetry && \
    poetry install --no-root

COPY . .
#
# RUN poetry run alembic upgrade head

CMD ["poetry", "run", "uvicorn", "bet_maker.main:app", "--host", "0.0.0.0", "--port", "8002"]
#CMD ["poetry", "run", "alembic", "upgrade", "head"]
#
COPY bet_maker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
