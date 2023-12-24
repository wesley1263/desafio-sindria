from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient

from src.core.config import get_settings

settings = get_settings()


class Database:
    client: AsyncIOMotorClient = None

    @classmethod
    async def get_connection(cls) -> AsyncIOMotorClient:
        _mongo_uri = settings.MONGO_URI if not settings.TESTING else "mongodb://localhost:27017/test_db"
        _mongo_db = settings.MONGO_DB if not settings.TESTING else "test_db"
        if cls.client is None:
            cls.client = AsyncIOMotorClient(
                _mongo_uri, serverSelectionTimeoutMS=2000, maxPoolSize=10
            )
            logger.info("Database connected")
        return cls.client[_mongo_db]

    @classmethod
    async def close_connection(cls):
        if cls.client is not None:
            cls.client.close()
            logger.info("Database disconnected")
            cls.client = None
