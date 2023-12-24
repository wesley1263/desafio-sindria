from typing import List

from pydantic import BaseModel, Field, validator


class OptionSchema(BaseModel):
    option: str
    description: str


class CategorySchema(BaseModel):
    title: str


class PostQuestionSchema(BaseModel):
    title: str
    question: str
    answer: str = Field(min_length=1, max_length=1)
    options: List[OptionSchema]
    area: CategorySchema


class PostAnswerQuestionSchema(BaseModel):
    question_id: str
    answer: str = Field(min_length=1, max_length=1)
    student_rn: str


class GetQuestionSchema(BaseModel):
    _id: str
    title: str
    question: str
    options: List[OptionSchema]
    area: CategorySchema


class PaginateSchema(BaseModel):
    page: int
    limit: int
    total: int
    total_pages: int
    data: List[GetQuestionSchema]


class RetrieveDatasSchema(BaseModel):
    total: int
    data: List[GetQuestionSchema]
