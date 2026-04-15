"""Crud module."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.app.schemas import UserCreate

from sqlalchemy import select

from src.app.models import User


async def create_user(db: AsyncSession, user: UserCreate) -> User:
    """Create and store a new user."""
    db_user = User(**user.model_dump())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_users(db: AsyncSession) -> list[User]:
    """Retrieve all users from the database."""
    result = await db.execute(select(User))
    return result.scalars.all()


async def get_user(db: AsyncSession, user_id: int) -> User | None:
    """Retrieve a specific user from the database."""
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()
