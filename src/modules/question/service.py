from bson.errors import InvalidId
from pydantic import BaseModel

from src.core.exceptions import ServiceException
from src.core.interfaces import IBaseRepository
from src.modules.question.schema import PaginateSchema, RetrieveDatasSchema


class QuestionRetrieveAllService:
    def __init__(self, repository: IBaseRepository, page: int = 1, limit: int = 10):
        self._repository = repository
        self._limit = limit
        self._page = page

    async def _paginate(self, data: RetrieveDatasSchema):
        _total = data.get("total")
        return PaginateSchema(
            page=self._page,
            limit=self._limit,
            total=_total,
            total_pages=_total // self._limit + 1,
            data=data.get("data"),
        )

    async def execute(self) -> PaginateSchema:
        _result = await self._repository.retrieve_all_paginated(self._page, self._limit)
        return await self._paginate(_result)


class QuestionCreateService:
    def __init__(self, repository: IBaseRepository, payload: BaseModel):
        self._repository = repository
        self._payload = payload
        self._valid_answer = ["A", "B", "C", "D"]

    async def _validate_title(self):
        _result = await self._repository.retrieve_by(title=self._payload.title)
        if _result:
            raise ServiceException("Questão já cadastrado!", 400)

    async def _validate_answer(self):
        if self._payload.answer not in self._valid_answer:
            raise ServiceException("Resposta inválida!", 400)

    async def _validate_options(self) -> None:
        _options = self._payload.options
        if len(_options) != 4:
            raise ServiceException("Número de opções inválido!", 400)
        for _option in _options:
            if "option" not in _option.dict() or "description" not in _option.dict():
                raise ServiceException("Opção inválida!", 400)
            if _option.option not in self._valid_answer:
                raise ServiceException("Opção inválida!", 400)

    async def _validate(self):
        await self._validate_answer()
        await self._validate_options()
        await self._validate_title()

    async def execute(self):
        await self._validate()
        await self._repository.create(self._payload.dict())
        return {"message": "Questão cadastrada com sucesso"}


class AnswerQuestionService:
    def __init__(self, repository: IBaseRepository, payload: BaseModel):
        self._repository = repository
        self._payload = payload

    async def execute(self) -> bool:
        try:
            _result = await self._repository.retrieve_question_by_id(
                self._payload.question_id
            )
            if not _result:
                raise ServiceException("Questão não encontrada!", 400)
            return _result.get("answer") == self._payload.answer
        except InvalidId:
            raise ServiceException("_id inválido", 400)
