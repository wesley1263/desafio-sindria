from fastapi import APIRouter, HTTPException, Query, status

from src.core.exceptions import ServiceException
from src.modules.question.repository import QuestionRepository
from src.modules.question.schema import (PostAnswerQuestionSchema,
                                         PostQuestionSchema)
from src.modules.question.service import (AnswerQuestionService,
                                          QuestionCreateService,
                                          QuestionRetrieveAllService)
from src.modules.student.repository import StudentRepository
from src.modules.student.service import UpdateScoreStudentService

router = APIRouter(prefix="/questions")

repository = QuestionRepository()


@router.get("/", description="List questions", status_code=status.HTTP_200_OK)
async def retrieve_all(page: int = Query(1), limit: int = Query(10)):
    return await QuestionRetrieveAllService(repository, page, limit).execute()


@router.post(
    "/create",
    description="Create new question",
    status_code=status.HTTP_201_CREATED,
    response_model=dict,
)
async def create(payload: PostQuestionSchema):
    try:
        return await QuestionCreateService(repository, payload).execute()
    except ServiceException as err:
        raise HTTPException(status_code=err.status_code, detail=str(err))


@router.post(
    "/answer",
    description="Create new question",
    status_code=status.HTTP_201_CREATED,
    response_model=dict,
)
async def answer(payload: PostAnswerQuestionSchema):
    try:
        _score = 10
        _result = await AnswerQuestionService(repository, payload).execute()
        if not _result:
            _score = -5
        return await UpdateScoreStudentService(
            StudentRepository(), payload.student_rn, _score
        ).execute()
    except ServiceException as err:
        raise HTTPException(status_code=err.status_code, detail=str(err))
