import re

from pydantic import BaseModel

from src.core.exceptions import ServiceException
from src.core.interfaces import IBaseRepository
from src.modules.student.enum import Ranking
from src.modules.student.schema import GetRankingStudent, GetStudentSchema


class StudentCreateService:
    def __init__(self, repository: IBaseRepository, payload: BaseModel):
        self._repository = repository
        self._payload = payload

    async def _validate_name(self):
        _result = await self._repository.retrieve_by_name(self._payload.name)
        if _result:
            raise ServiceException("Nome já cadastrado!", 400)

    async def _validate_email(self):
        _result = await self._repository.retrieve_by_email(self._payload.email)
        if _result:
            raise ServiceException("E-mail já cadastrado!", 400)

    async def _validate_rn_exists(self):
        _result = await self._repository.retrieve_by(rn=self._payload.rn)
        if _result:
            raise ServiceException("RN já cadastrado!", 400)

    async def _validate_rn_pattern(self):
        if not re.match(r"^[A-Z]{2}[0-9]{3}$", self._payload.rn):
            raise ServiceException("RN inválido!", 400)
        return True

    async def _validate(self):
        await self._validate_name()
        await self._validate_email()
        await self._validate_rn_pattern()
        await self._validate_rn_exists()

    async def execute(self):
        await self._validate()
        _payload = self._payload.dict()
        _payload["score"] = 0
        await self._repository.create(_payload)
        return {"message": "Aluno Criado com sucesso"}


class StudentGetByRNService:
    def __init__(self, repository: IBaseRepository, rn: str):
        self._repository = repository
        self._rn = rn

    async def execute(self):
        _result = await self._repository.retrieve_by_rn(self._rn)
        if not _result:
            raise ServiceException("Aluno não encontrado!", 404)
        return GetStudentSchema(
            id=_result[0].get("_id"),
            name=_result[0].get("name"),
            email=_result[0].get("email"),
            rn=_result[0].get("rn"),
        )


class UpdateScoreStudentService:
    def __init__(self, repository: IBaseRepository, rn: str, score: int):
        self._repository = repository
        self._rn = rn
        self._score = score

    async def _ranking(self, score):
        if score <= 50:
            return Ranking.NOVATO
        elif 51 <= score <= 100:
            return Ranking.CONHECEDOR
        elif 101 <= score <= 200:
            return Ranking.EXPERT
        else:
            return Ranking.MESTRE_DO_ENEM

    async def _get_student(self):
        _result = await self._repository.retrieve_by_rn(self._rn)
        if not _result:
            raise ServiceException("Aluno não encontrado!", 404)
        _student = _result[0]
        _student["score"] += self._score
        if _student["score"] < 0:
            _student["score"] = 0
        return _student

    async def execute(self):
        _student = await self._get_student()
        _result_score = await self._repository.update_one(
            {"rn": self._rn}, {"score": _student["score"]}
        )
        _ranking = await self._ranking(_student["score"])
        print(_ranking)
        return GetRankingStudent(
            name=_student.get("name"),
            rn=_student.get("rn"),
            score=_student.get("score"),
            ranking=_ranking.value,
        )
