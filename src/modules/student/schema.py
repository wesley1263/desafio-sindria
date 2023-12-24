from pydantic import BaseModel


class PostStudentSchema(BaseModel):
    name: str
    email: str
    rn: str = "AB321"


class GetStudentSchema(BaseModel):
    id: str
    name: str
    email: str
    rn: str = "AB321"
    score: int


class GetRankingStudent(BaseModel):
    name: str
    rn: str = "AB321"
    score: int
    ranking: str
