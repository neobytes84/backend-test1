from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

# Base para modelos
Base = declarative_base()

# Engine de SQLAlchemy
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# Sesión para FastAPI
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Dependencia que FastAPI usará vía Depends()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
