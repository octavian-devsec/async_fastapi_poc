"""Db module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from sqlalchemy.ext.asyncio import AsyncEngine

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@db:5432/app"


engine: AsyncEngine = create_async_engine(
    url=DATABASE_URL,
    echo=True,
)


AsyncSessionLocal: async_sessionmaker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db() -> AsyncGenerator:
    """Get a database session with every call."""
    async with AsyncSessionLocal() as session:
        yield session
