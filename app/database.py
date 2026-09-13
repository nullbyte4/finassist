"""Database engine and session management for FinAssist.

Configures the SQLite connection used by the application and exposes a
FastAPI dependency that yields a database session per request.
"""

from sqlmodel import Session, SQLModel, create_engine

# Importing the models module registers Category, Income, and Expense on
# SQLModel's metadata, which create_db_and_tables() below relies on.
from app import models  # noqa: F401

DATABASE_URL = "sqlite:///./finassist.db"

# `check_same_thread=False` allows the SQLite connection to be shared
# across the worker threads FastAPI uses to handle requests.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def create_db_and_tables():
    """Create all tables defined by SQLModel models if they don't exist yet."""
    SQLModel.metadata.create_all(engine)


def get_session():
    """Yield a database session for use as a FastAPI dependency."""
    with Session(engine) as session:
        yield session
