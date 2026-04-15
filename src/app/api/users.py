"""Users endpoints module."""

from typing import TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

    from src.app.models import User

from fastapi import APIRouter, Depends, HTTPException

from src.app import crud, schemas
from src.app.db import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post("/", response_model=schemas.UserOut)
async def create_user(
    user: schemas.UserCreate,
    db: Annotated[AsyncSession, Depends(get_db)]
) -> User:
    """POST / endpoint.

    Create a new user in the database and
    return the created record with generated fields.
    """
    return await crud.create_user(db, user)


@router.get("/", response_model=list[schemas.UserOut])
async def get_users(
    db: Annotated[AsyncSession, Depends(get_db)]
) -> list[User]:
    """GET / endpoint.

    Return a list of all users stored in the database.
    """
    return await crud.get_users(db)


@router.get("/{user_id}", response_model=schemas.UserOut)
async def get_user(
    user_id: int,
    db: Annotated[AsyncSession, Depends(get_db)]
) -> User:
    """GET /{user_id} endpoint.

    Retrieve a single user by ID.

    Raises:
        HTTPException: If the user does not exist (404).
    """
    user = await crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404)
    return user
