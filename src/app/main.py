"""Main app module."""

from fastapi import FastAPI

from src.app.api import users

app = FastAPI()

app.include_router(users.router)
