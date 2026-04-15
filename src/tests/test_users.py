"""Test module for users."""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from httpx import AsyncClient

import pytest

STATUS_OK: int = 200


@pytest.mark.asyncio
async def test_create_user(client: AsyncGenerator[AsyncClient]) -> None:
    """Test create user endpoint."""
    result = await client.post(
        url="/users/", json={"email": "test@test.com", "name": "Test"}
    )
    assert result.status_code == STATUS_OK
    assert result.json()["email"] == "test@test.com"
    assert result.json()["name"] == "Test"
