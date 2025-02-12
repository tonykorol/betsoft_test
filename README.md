# Проект BetSoft Test Work

## Описание
Этот проект представляет собой сервис для работы со ставками, разработанный с использованием Python, FastAPI и PostgreSQL. Контейнеризация обеспечивается с помощью Docker и Docker Compose.

## Требования
- Docker
- Docker Compose

## Установка и запуск

### 1. Клонирование репозитория
```sh
git clone https://github.com/tonykorol/betsoft_test.git
cd betsoft_test_work
```

### 2. Создание файлов переменных окружения

#### `.env` для `bet-maker`
Создайте файл `bet_maker/.env` и добавьте туда нужные переменные окружения:
```sh
DB_NAME=betsoft
DB_HOST=postgres-bet
DB_PORT=5432
DB_USER=betsoft_user
DB_PASS=securepassword
```

#### `.env` для `line-provider`
Создайте файл `line_provider/.env`, если необходимо.

#### `.env_db` для базы данных
Создайте файл `postgres.env` в корне проекта и добавьте:
```sh
POSTGRES_DB=betsoft
POSTGRES_USER=betsoft_user
POSTGRES_PASSWORD=securepassword
```
Добавьте этот файл в `.gitignore`, чтобы не коммитить пароли:
```sh
echo '.env_db' >> .gitignore
```

### 3. Сборка и запуск контейнеров
```sh
docker compose up --build
```

### 4. Проверка работы
Открыть в браузере:
- API `bet-maker`: [http://localhost:8002/docs](http://localhost:8002/docs)
- API `line-provider`: [http://localhost:8001/docs](http://localhost:8001/docs)

## Остановка контейнеров
```sh
docker compose down -v
```

