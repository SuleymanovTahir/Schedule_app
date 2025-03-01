from sqlalchemy.orm import Session
from models.student import Student
from schemas.student import StudentCreate

def create_student(db: Session, student: StudentCreate):
    db_student = Student(**student.dict())  # Создаем объект ученика
    db.add(db_student)  # Добавляем в сессию
    db.commit()  # Сохраняем изменения
    db.refresh(db_student)  # Обновляем объект
    return db_student  # Возвращаем созданного ученика

def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()  # Получаем ученика по ID