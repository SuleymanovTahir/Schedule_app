from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.lesson import LessonCreate, Lesson
from crud.lesson import create_lesson, get_lesson
from database import get_db

router = APIRouter()

@router.post("/lessons/", response_model=Lesson)
def create_lesson_endpoint(lesson: LessonCreate, db: Session = Depends(get_db)):
    return create_lesson(db, lesson)

@router.get("/lessons/{lesson_id}", response_model=Lesson)
def read_lesson(lesson_id: int, db: Session = Depends(get_db)):
    db_lesson = get_lesson(db, lesson_id)
    if db_lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return db_lesson