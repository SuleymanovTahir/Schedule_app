from pydantic import BaseModel
from datetime import datetime,time
from typing import Optional
# from enums.student import WeekDayEnum



class StudentBase(BaseModel):
    full_name: str  # ФИО ученика
    group_id: int  # Группа ученика
    parent_name: str  # Имя родителя
    parent_contact: str  # Контакт родителя
    email: str  # Почта
    lesson_start: time  # Время занятий (например, "10:00-11:00")
    lesson_end: time  # Время занятий (например, "10:00-11:00")
    lesson_days: str # Дни занятий (например, "пн,ср,пт")
    lesson_time: str  # Время занятий (например, "10:00-11:00")
    cost: int  # Стоимость обучения
    payment_date: datetime  # Дата оплаты
    notes: Optional[str] = None  # Примечания

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True