from fastapi import APIRouter


marks_router = APIRouter(prefix='/mark', tags=['Marks'])

from students_mark import students_mark_api
