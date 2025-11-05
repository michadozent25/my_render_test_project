import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Erwartet z. B.:
# postgresql+psycopg://USER:PASSWORD@HOST:5432/DBNAME?sslmode=require
DATABASE_URL = os.getenv("DB_URL_PYTEST")

if not DATABASE_URL:
    raise RuntimeError("Env DATABASE_URL (Neon) fehlt.")

# Echo=True nur zum Debuggen
engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
