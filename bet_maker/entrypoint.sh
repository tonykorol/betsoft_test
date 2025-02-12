#!/bin/bash

echo "⏳ Ожидание доступности базы данных..."
until poetry run alembic upgrade head; do
  echo "❗ База данных ещё не готова. Повторяем попытку..."
  sleep 2
done

echo "✅ База данных готова. Запускаем приложение..."
exec "$@"
