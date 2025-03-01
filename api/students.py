from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.student import StudentCreate, Student
from crud.student import create_student, get_student
from database import get_db

router = APIRouter()

@router.post("/students/", response_model=Student)
def create_student_endpoint(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)  # Создаем ученика

@router.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = get_student(db, student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Ученик не найден")
    return db_student