# Gamify-HC Backend

Flask + PostgreSQL API that powers Gamify-HC. Features JWT authentication, modular blueprints, auto-seeded SQLAlchemy models, and Swagger-based API docs.

## Quick Start (Docker, Recommended)

```bash
docker compose up --build
```

What you get:
- PostgreSQL 16 on `5432`
- Backend API on `http://localhost:5001`
- Frontend on `http://localhost:3000`
- Docs at `http://localhost:5001/api/docs` (spec served from `docs/swagger.json`)
- Health at `http://localhost:5001/api/health` → `{"status": "ok", "message": "Gamify-HC API is running"}`

`docker-compose.yml` wires all environment variables (including `DATABASE_URL`) for you.

## Local Development (without Docker)

1) **Copy env defaults**
```bash
cp .env.example .env   # adjust values as needed
```

2) **Start PostgreSQL**
```bash
docker compose up postgres -d
```
Uses the `gamify_hc` database defined in `docker-compose.yml`. You can also point `DATABASE_URL` at your own Postgres instance.

3) **Install Python deps**
```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

4) **Run the API from repo root**
```bash
python run.py
```
The server starts on `http://localhost:5001` using the config in `backend/config.py`.

5) **Smoke test**
```bash
curl http://localhost:5001/api/health
```

## Project Structure

```
backend/
├── app.py                  # Flask app factory + blueprint registration + Swagger + health
├── config.py               # Env-driven configuration (DB, Flask, JWT)
├── database/
│   ├── models.py           # SQLAlchemy ORM models
│   ├── setup.py            # Engine/session creation + auto-seeding
│   └── seed_data/          # Initial seed data
├── routes/                 # Flask blueprints (prefixed with /api)
│   ├── auth.py             # Register/login/me, JWT issuance
│   ├── courses.py          # Course endpoints
│   ├── units.py            # Unit endpoints
│   ├── concepts.py         # Concept endpoints
│   ├── quiz.py             # Quiz submission + cards
│   └── users.py            # User profile/progress
├── services/               # Business logic / DB helpers
│   ├── auth/               # AuthService (passwords, JWT)
│   ├── course/             # CourseService, etc.
│   ├── quiz/               # QuizService
│   ├── user/               # UserService, progress calculations
│   ├── base_service.py     # Shared CRUD and transaction helpers
│   └── serializers.py      # Serialization helpers
├── utils/
│   └── database_manager.py # Database session lifecycle for Flask
└── tests/                  # Pytest suite (routes + services + fixtures)
```

## Architecture at a Glance

```
Client (Frontend)
    │ REST/JSON
    ▼
Flask Blueprints (/api/*)          ← CORS enabled
    │ delegates
    ▼
Service Layer (backend/services)   ← validation, querying, transactions
    │ uses
    ▼
SQLAlchemy Models                  ← PostgreSQL 16
    │ auto-seeds on empty DB
    ▼
database/seed_data/*
```

- `create_app()` wires CORS, blueprints, Swagger UI, and a per-request DB session via `DatabaseManager`.
- `database/setup.py` creates the engine, tables, and seeds on first run (controlled by `AUTO_SEED_DATABASE`).
- `docs/swagger.json` is served verbatim at `/api/swagger.json` for Swagger UI and client generation.

## API Surface

- **Auth**: `POST /api/auth/register`, `POST /api/auth/login`, `GET /api/auth/me`
- **Courses**: `GET /api/courses`, `GET /api/courses/:id`, `GET /api/courses/:id/units`
- **Units**: `GET /api/units/:id`, `GET /api/units/:id/concepts`
- **Concepts**: `GET /api/concepts/:id`, `GET /api/concepts/:id/quiz-cards`
- **Quiz**: `GET /api/quiz-cards/:id`, `POST /api/quiz-submit`
- **Users**: `GET /api/users/:id`, `GET /api/users/:id/progress`
- **Health**: `GET /api/health`

## Authentication

- JWT-based; tokens issued on register/login.
- Send on every protected request: `Authorization: Bearer <access_token>`.
- Expiration set by `JWT_EXPIRATION_HOURS` (default 24h). Secret configured via `JWT_SECRET_KEY`.

## Configuration

Key environment variables (see `.env.example` for all options):
- `DATABASE_URL` – PostgreSQL connection string (required outside Docker).
- `POSTGRES_PASSWORD` – Used by Docker Compose Postgres service; defaults to `gamify_secret`.
- `FLASK_HOST` / `FLASK_PORT` / `FLASK_DEBUG` – Server config.
- `JWT_SECRET_KEY`, `JWT_ALGORITHM`, `JWT_EXPIRATION_HOURS` – Auth settings.
- `SQLALCHEMY_ECHO`, `SQLALCHEMY_POOL_*`, `AUTO_SEED_DATABASE` – Database tuning and seeding.

Example local run with explicit settings:
```bash
DATABASE_URL="postgresql://gamify:gamify_secret@localhost:5432/gamify_hc" \
SQLALCHEMY_ECHO=1 \
JWT_SECRET_KEY="change-me" \
python run.py
```

## Testing

- Runner: `pytest backend/tests`
- Infra: `testcontainers` spins up PostgreSQL automatically; no manual DB prep.
- Coverage: route integration tests + service unit tests with rich fixtures (`backend/tests/README.md`).

Common commands:
```bash
pytest backend/tests          # full suite
pytest backend/tests -q       # quieter output
pytest backend/tests/routes   # only API surface
```

## Database Notes

- PostgreSQL 16 only (dev, test, prod).
- Tables auto-create from SQLAlchemy models; initial data seeds from `database/seed_data/` when empty.
- For production migrations, consider adding Alembic; current dev setup relies on `database/setup.py`.

## API Docs & Health

- Swagger UI: `http://localhost:5001/api/docs`
- Raw OpenAPI spec: `http://localhost:5001/api/swagger.json` (source: `docs/swagger.json`)
- Health: `GET /api/health` (used by Docker healthchecks)

## Troubleshooting

- **Port already in use**: stop other Postgres/Flask processes or change `FLASK_PORT`/`DATABASE_URL`.
- **Database URL missing**: set `DATABASE_URL` (see `.env.example`) or run through Docker Compose.
- **Seed data not loading**: ensure `AUTO_SEED_DATABASE=True` or run `database/seed_data/seed.py` manually against your DB.
- **Swagger spec 404**: confirm `docs/swagger.json` exists and is copied into the container (not ignored by `.dockerignore`).
