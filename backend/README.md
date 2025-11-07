# Backend

This directory holds the backend data layer for the Gamify-HC project. The
SQLAlchemy models live in `database/database.py` and mirror the schema defined
in `database/backend_database.sql`.

## Local database setup

1. Create and activate a Python virtual environment (if you have not already):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. Configure any desired environment variables (see below). Defaults are
   provided so you can skip this step for a quick start.

3. Create or reset the local SQLite database:

   ```bash
   python backend/database/database.py
   ```

   The script will create `backend/database/test.db`, build all tables, and
   insert a sample `Course` record. Run it whenever you want a fresh test
   database before starting the frontend (`npm install && npm start`).

## Environment variables

The database utilities in `database.py` look for the following variables at
runtime:

- `DATABASE_URL` – SQLAlchemy connection string. Defaults to a bundled SQLite
  file (`sqlite:///backend/database/test.db`). Override this when you want to
  point the app at a different database (for example a temporary test database
  during CI or a local Postgres instance).
- `SQLALCHEMY_ECHO` – controls SQLAlchemy's query logging. Set to `1`,
  `true`, `yes`, etc. to enable verbose SQL logging. Defaults to `0` (disabled).

Example usage:

```bash
DATABASE_URL="sqlite:///backend/database/dev.db" \
SQLALCHEMY_ECHO=1 \
python backend/database/database.py
```

These same variables can be exported before running your frontend tooling so
that npm scripts and Python utilities share the exact same database settings.

## Next steps

- Integrate the database helpers into your web framework once the backend
  request/response layer is ready.
- Introduce a migration tool such as Alembic when the schema begins to evolve.
- Extend the seeding script with additional sample data as frontend features
  require it.