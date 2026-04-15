"""Test module for users."""

from collections.abc import AsyncGenerator

import pytest
from httpx import AsyncClient

STATUS_OK: int = 200


@pytest.mark.asyncio
async def test_create_user(client: AsyncGenerator[AsyncClient]) -> None:
    """Test create user endpoint."""
    result = await client.post(
        url="/users/",
        json={
            "email": "test@test.com",
            "name": "Test"
        }
    )
    assert result.status_code == STATUS_OK
    assert result.json()["email"] == "test@test.com"
    assert result.json()["name"] == "Test"
