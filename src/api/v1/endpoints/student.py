from fastapi import APIRouter, HTTPException, status

from src.core.exceptions import ServiceException
from src.modules.student.repository import StudentRepository
from src.modules.student.schema import GetStudentSchema, PostStudentSchema
from src.modules.student.service import (StudentCreateService,
                                         StudentGetByRNService)

router = APIRouter(prefix="/students")

repository = StudentRepository()


@router.post(
    "/",
    description="Create new Student",
    status_code=status.HTTP_201_CREATED,
    response_model=dict,
)
async def create(payload: PostStudentSchema):
    try:
        return await StudentCreateService(repository, payload).execute()
    except ServiceException as err:
        raise HTTPException(status_code=err.status_code, detail=str(err))


@router.get("/{rn}", description="Get Student by rn", response_model=GetStudentSchema)
async def retrieve_by_rn(rn: str):
    try:
        return await StudentGetByRNService(repository, rn).execute()
    except ServiceException as err:
        raise HTTPException(status_code=err.status_code, detail=str(err))
