from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import text, Integer, String

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False)

# Nützlich fürs schnelle Connectivity-Testing
def db_ping(session) -> str:
    return session.execute(text("SELECT version()")).scalar_one()
