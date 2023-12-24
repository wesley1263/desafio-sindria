from src.core.abstracts import (CreateRepository, RetrieveAllRepository,
                                RetrieveByRepository)


class QuestionRepository(RetrieveAllRepository, CreateRepository, RetrieveByRepository):
    def __init__(self):
        super().__init__("questions")

    async def retrieve_question_by_id(self, id: str):
        return await self.retrieve_one_by_id(id)
