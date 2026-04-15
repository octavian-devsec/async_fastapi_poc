from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.models import User
from src.app.schemas import UserCreate


async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars.all()


async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()
