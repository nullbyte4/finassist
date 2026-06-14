from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# SQLModel.metadata holds the table definitions from all imported models
# Alembic reads this to know what tables exist and detect changes
from sqlmodel import SQLModel

# Import User so SQLModel registers the table in its metadata
# Without this import, Alembic wouldn't know the User table exists
from app.models.user import User

# Import settings to read DATABASE_URL from .env instead of alembic.ini
from app.core.config import settings

# Alembic Config object — provides access to values in alembic.ini
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Point Alembic to our models so --autogenerate can detect schema changes
target_metadata = SQLModel.metadata


def run_migrations_offline() -> None:
    """Run migrations without a live DB connection — generates raw SQL instead."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations against a live DB connection."""
    # Override the URL from alembic.ini with the one from .env
    # This keeps the real credentials out of version-controlled config files
    config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
