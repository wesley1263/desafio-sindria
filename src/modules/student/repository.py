from src.core.abstracts import (CreateRepository, RetrieveByRepository,
                                UpdateRepository)


class StudentRepository(CreateRepository, RetrieveByRepository, UpdateRepository):
    def __init__(self):
        super().__init__("students")

    async def retrieve_by_email(self, email: str):
        return await self.retrieve_by(email=email)

    async def retrieve_by_name(self, name: str):
        return await self.retrieve_by(name=name)

    async def retrieve_by_rn(self, rn: str):
        pipeline = [
            {"$addFields": {"_id": {"$toString": "$_id"}}},
            {"$limit": 1},
            {"$match": {"rn": rn}},
        ]
        return await self.retrieve_with_pipeline(pipeline=pipeline)
