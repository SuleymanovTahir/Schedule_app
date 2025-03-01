from sqlalchemy.orm import Session
from models.teacher import Teacher
from schemas.teacher import TeacherCreate

def create_teacher(db: Session, teacher: TeacherCreate):
    db_teacher = Teacher(**teacher.dict())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def get_teacher(db: Session, teacher_id: int):
    return db.query(Teacher).filter(Teacher.id == teacher_id).first()