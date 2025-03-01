from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.teacher import TeacherCreate, Teacher
from crud.teacher import create_teacher, get_teacher
from database import get_db

router = APIRouter()

@router.post("/teachers/", response_model=Teacher)
def create_teacher_endpoint(teacher: TeacherCreate, db: Session = Depends(get_db)):
    return create_teacher(db, teacher)

@router.get("/teachers/{teacher_id}", response_model=Teacher)
def read_teacher(teacher_id: int, db: Session = Depends(get_db)):
    db_teacher = get_teacher(db, teacher_id)
    if db_teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher