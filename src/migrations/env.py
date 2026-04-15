"""Alembic environment configuration."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from alembic.config import Config
    from sqlalchemy.engine import Connection
    from sqlalchemy.ext.asyncio import AsyncEngine
    from sqlalchemy.sql.schema import MetaData

import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config

from src.app.models import Base

config: Config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata: MetaData = Base.metadata


def run_migrations_offline() -> None:
    """Run Alembic migrations in an offline context."""
    url: str | None = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """Run Alembic migrations.

    This is used in running the migrations in an online context
    """
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run Alembic migrations in an online context."""
    section: dict[str, Any] = config.get_section(config.config_ini_section) or {}
    connectable: AsyncEngine = async_engine_from_config(
        configuration=section,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run() -> None:
    """Run the Alembic migrations online or offline, depending on context."""
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        asyncio.run(run_migrations_online())


if __name__ == "__main__":
    run()
