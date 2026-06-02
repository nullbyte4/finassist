# BaseSettings is the Pydantic class for reading config from environment variables or .env files
# SettingsConfigDict lets us configure where to read those variables from
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Tell Pydantic to read variables from the .env file in the backend directory
    model_config = SettingsConfigDict(env_file=".env")

    # Each field must match the variable name in .env (case-insensitive)
    # Pydantic automatically validates that the value matches the declared type
    APP_NAME: str
    DEBUG: bool
    DATABASE_URL: str  # Connection string for SQLModel to reach PostgreSQL
    SECRET_KEY: str    # Used later to sign and verify JWT tokens

# Create a single instance — import this object anywhere in the app to access config
settings = Settings()
