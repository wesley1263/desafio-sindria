import pytest
from motor.motor_asyncio import AsyncIOMotorDatabase

from src.core.config import get_settings
from src.core.database import Database

settings = get_settings()


@pytest.mark.asyncio
async def test_get_connection():
    client = await Database.get_connection()
    assert isinstance(client, AsyncIOMotorDatabase)


async def test_close_connection():
    await Database.get_connection()
    await Database.close_connection()
    assert Database.client is None


@pytest.fixture(autouse=True)
async def reset():
    await Database.close_connection()
