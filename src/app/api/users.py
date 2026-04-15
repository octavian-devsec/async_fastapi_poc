from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.db import get_db
from src.app import schemas
from src.app import crud

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/", response_model=schemas.UserOut)
async def create_user(
    user: schemas.UserCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.create_user(db, user)


@router.get("/", response_model=list[schemas.UserOut])
async def get_users(
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_users(db)


@router.get("/{user_id}", response_model=schemas.UserOut)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    user = await crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404)
    return user
