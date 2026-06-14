# create_engine: builds the connection to PostgreSQL — created once when the app starts
# Session: represents one "conversation" with the DB for reading/writing data
# SQLModel: base class, imported here so its metadata is accessible if needed elsewhere
from sqlmodel import create_engine, Session, SQLModel

# Import settings to read DATABASE_URL from .env instead of hardcoding it
from app.core.config import settings

# Single engine instance shared across the entire app
# Reads the connection string from .env (e.g. postgresql+psycopg2://user:pass@localhost/db)
engine = create_engine(settings.DATABASE_URL)

# Generator function used as a FastAPI dependency
# yield (instead of return) pauses the function while the request is being handled,
# then resumes to close the session automatically when the request finishes
def get_session():
    with Session(engine) as session:
        yield session
