from sqlalchemy.orm import Session
from models.lesson import Lesson
from schemas.lesson import LessonCreate

def create_lesson(db: Session, lesson: LessonCreate):
    db_lesson = Lesson(**lesson.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson

def get_lesson(db: Session, lesson_id: int):
    return db.query(Lesson).filter(Lesson.id == lesson_id).first()