#!/usr/bin/env bash
set -e
# optional: Alembic migrations
# [ -d "alembic" ] && alembic upgrade head || true
uvicorn app.main:app --host 0.0.0.0 --port "$PORT"
