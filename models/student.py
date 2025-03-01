#student.py


# from enums.student import WeekDayEnum
from models.base import *
from typing import List, Optional
from sqlalchemy import ARRAY
from datetime import date


# Перечисления (остаются без изменений)
class PaymentType(PyEnum):
    TRANSFER = "Переводом"
    QR = "QR"
    CASH = "Наличные"

class SchoolShift(PyEnum):
    FIRST_SHIFT = "Первая смена"
    SECOND_SHIFT = "Вторая смена"
    WEEKEND_SHIFT = "Выходной день"

class PaymentStatus(PyEnum):
    PAID = "Оплачено"
    UNPAID = "Не оплачено"
    PARTIALLY_PAID = "Частично оплачено"

class LessonType(PyEnum):
    INDIVIDUAL = "Индивидуально"
    GROUP = "В группе"

class CourseType(PyEnum):
    GENERAL_ENGLISH = "General English"
    IELTS = "IELTS"

class TeacherType(PyEnum):
    NATIVE = "Носитель языка"
    LOCAL = "Местный преподаватель"

class LessonFormat(PyEnum):
    ONLINE = "Онлайн"
    OFFLINE = "Офлайн"
    BOTH = "Онлайн и офлайн"

class EnglishLevel(PyEnum):
    BEGINNER = "Beginner"
    BEGINNER_PLUS = "Beginner+"
    ELEMENTARY = "Elementary"
    ELEMENTARY_PLUS = "Elementary+"
    PRE_INTERMEDIATE = "Pre-Intermediate"
    PRE_INTERMEDIATE_PLUS = "Pre-Intermediate+"
    INTERMEDIATE = "Intermediate"
    INTERMEDIATE_PLUS = "Intermediate+"
    UPPER_INTERMEDIATE = "Upper-Intermediate"
    UPPER_INTERMEDIATE_PLUS = "Upper-Intermediate+"
    ADVANCED = "Advanced"

    # def __init__(self, id, description):
    #     self.id = id
    #     self.description = description

    @classmethod
    def get_by_id(cls, id):
        for level in cls:
            if level.id == id:
                return level
        raise ValueError(f"Invalid EnglishLevel ID: {id}")
    
class AgeGroup(PyEnum):
    KIDS = "Дети (6-12 лет)"
    TEENS = "Подростки (13-17 лет)"
    ADULTS = "Взрослые (18+ лет)"

class Student(Base):
    __tablename__ = "students"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, info={"verbose_name": "ID"})
    full_name: Mapped[str] = mapped_column(String, index=True, info={"verbose_name": "ФИО ученика"})
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"), nullable=True, info={"verbose_name": "Группа"})
    parent_name: Mapped[Optional[str]] = mapped_column(String, nullable=True, info={"verbose_name": "Имя родителя"})
    parent_contact: Mapped[Optional[str]] = mapped_column(String, nullable=True, info={"verbose_name": "Контакт родителя"})
    email: Mapped[Optional[str]] = mapped_column(String, nullable=True, info={"verbose_name": "Почта"})
    age: Mapped[Optional[int]] = mapped_column(Integer, nullable=True, info={"verbose_name": "Возраст"})
    school_shift: Mapped[SchoolShift] = mapped_column(Enum(SchoolShift), default=SchoolShift.FIRST_SHIFT, info={"verbose_name": "Смена занятий"})
    lesson_times: Mapped[List[str]] = mapped_column(JSON, default=[], info={"verbose_name": "Время занятий"})  # Используем JSON
    lesson_days: Mapped[List[str]] = mapped_column(JSON, default=[], info={"verbose_name": "Дни занятий"})  # Используем JSON
    lesson_format: Mapped[LessonFormat] = mapped_column(Enum(LessonFormat), default=LessonFormat.OFFLINE, info={"verbose_name": "Формат занятий"})
    teacher_type: Mapped[TeacherType] = mapped_column(Enum(TeacherType), default=TeacherType.LOCAL, info={"verbose_name": "Тип преподавателя"})
    course_type: Mapped[CourseType] = mapped_column(Enum(CourseType), default=CourseType.GENERAL_ENGLISH, info={"verbose_name": "Тип курса"})
    age_group: Mapped[AgeGroup] = mapped_column(Enum(AgeGroup), default=AgeGroup.ADULTS, info={"verbose_name": "Возрастная группа"})
    english_level: Mapped[EnglishLevel] = mapped_column(Enum(EnglishLevel), default=EnglishLevel.BEGINNER, info={"verbose_name": "Уровень английского"})
    start_date: Mapped[date] = mapped_column(Date, default=date.today, info={"verbose_name": "Дата начала обучения"})
    end_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True, info={"verbose_name": "Дата окончания обучения"})
    discount: Mapped[int] = mapped_column(Integer, default=0, info={"verbose_name": "Скидка"})
    cost: Mapped[int] = mapped_column(Integer, default=0, info={"verbose_name": "Стоимость обучения"})
    payment_type: Mapped[PaymentType] = mapped_column(Enum(PaymentType), default=PaymentType.TRANSFER, info={"verbose_name": "Тип оплаты"})
    payment_status: Mapped[PaymentStatus] = mapped_column(Enum(PaymentStatus), default=PaymentStatus.UNPAID, info={"verbose_name": "Статус оплаты"})
    lesson_type: Mapped[LessonType] = mapped_column(Enum(LessonType), default=LessonType.GROUP, info={"verbose_name": "Тип обучения"})
    payment_date: Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True, info={"verbose_name": "Дата оплаты"})
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True, info={"verbose_name": "Примечания"})

    group: Mapped["Group"] = relationship("Group", back_populates="students")