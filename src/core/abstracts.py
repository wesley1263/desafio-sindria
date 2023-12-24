from abc import ABC
from typing import Dict, List

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from src.core.database import Database
from src.core.interfaces import IBaseRepository, ICreateRepository


class BaseRepository(IBaseRepository, ABC):
    def __init__(self, collection_name: str):
        self._collection = None
        self._name = collection_name

    async def collection(self) -> AsyncIOMotorClient:
        _client = await Database.get_connection()
        self._collection = _client[self._name]
        return self._collection


class CreateRepository(ICreateRepository, BaseRepository, ABC):
    async def create(self, payload: dict):
        _collection = await self.collection()
        _result = await _collection.insert_one(payload)
        return _result


class RetrieveAllRepository(BaseRepository, ABC):
    async def retrieve_all(self) -> List:
        _collection = await self.collection()
        pipeline = [{"$addFields": {"_id": {"$toString": "$_id"}}}]
        _result = await self._collection.aggregate(pipeline).to_list(length=None)
        if not _result:
            return []
        return _result

    async def count_documents(self):
        _collection = await self.collection()
        pipeline = [{"$count": "total"}]
        total = await _collection.aggregate(pipeline).to_list(length=1)
        return total[0]["total"] if total else 0

    async def retrieve_all_paginated(self, skip: int = 0, limit: int = 10) -> Dict:
        _collection = await self.collection()
        total_count = await self.count_documents()
        pipeline = [
            {"$addFields": {"_id": {"$toString": "$_id"}}},
            {"$skip": skip},
            {"$limit": limit},
        ]
        _result = await _collection.aggregate(pipeline).to_list(length=limit)
        if not _result:
            return {"total": total_count, "data": []}
        return {"total": total_count, "data": _result}


class RetrieveByRepository(BaseRepository, ABC):
    async def retrieve_by(self, **kwargs):
        _collection = await self.collection()
        _result = await _collection.find_one(kwargs)
        if not _result:
            return None
        return _result

    async def retrieve_with_pipeline(self, pipeline: list):
        _collection = await self.collection()
        _result = await _collection.aggregate(pipeline).to_list(length=None)
        if not _result:
            return None
        return _result

    async def retrieve_one_by_id(self, _id: str):
        _collection = await self.collection()
        _result = await _collection.find_one({"_id": ObjectId(_id)})
        if not _result:
            return None
        return _result


class UpdateRepository(BaseRepository, ABC):
    async def update_one(self, query: dict, new_value: dict):
        _collection = await self.collection()
        _result = await _collection.update_one(query, {"$set": new_value})
        return _result
