"""API schemas module."""

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    """Base user schema."""

    email: EmailStr
    name: str


class UserCreate(UserBase):
    """User input schema for API payload."""


class UserOut(UserBase):
    """User schema for API responses."""

    model_config = ConfigDict(
        from_attributes=True,
    )
    id: int

