from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .db import SessionLocal, engine
from .models import Base, User, db_ping
import os

app = FastAPI(title="FastAPI + Neon (Minimal)")

# --- CORS ---
# Für Produktion FRONTEND_ORIGIN exakt setzen (z. B. https://ui-frontend.onrender.com)
origins = [os.getenv("FRONTEND_ORIGIN", "http://localhost:8501","*")]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- DB Setup (Tabellen anlegen, wenn nicht vorhanden) ---
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    try:
        v = db_ping(db)
        return {"db": "ok", "version": v}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).order_by(User.id).all()

@app.post("/users")
def create_user(name: str, db: Session = Depends(get_db)):
    if not name.strip():
        raise HTTPException(400, "name darf nicht leer sein")
    u = User(name=name.strip())
    db.add(u)
    db.commit()
    db.refresh(u)
    return u
