#group.py


from models.base import *
from typing import List, Dict, Optional  # Импортируем типы
from datetime import datetime


class WeekDay(PyEnum):
    MONDAY = "Понедельник"
    TUESDAY = "Вторник"
    WEDNESDAY = "Среда"
    THURSDAY = "Четверг"
    FRIDAY = "Пятница"
    SATURDAY = "Суббота"
    SUNDAY = "Воскресенье"

class GroupType(PyEnum):
    GROUP = "Группа"
    INDIVIDUAL = "Индивидуально"

class LessonFormat(PyEnum):
    ONLINE = "Онлайн"
    OFFLINE = "Офлайн"

class Group(Base):
    __tablename__ = "groups"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True, unique=True, info={"verbose_name": "Название группы"})
    level_id: Mapped[int] = mapped_column(ForeignKey("levels.id"), index=True, info={"verbose_name": "Уровень группы"})
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"), index=True, info={"verbose_name": "Преподаватель"})
    group_type: Mapped[GroupType] = mapped_column(Enum(GroupType), default=GroupType.GROUP, info={"verbose_name": "Тип группы"})  # По умолчанию "Группа"
    lesson_format: Mapped[LessonFormat] = mapped_column(Enum(LessonFormat), default=LessonFormat.OFFLINE, info={"verbose_name": "Формат занятий"})  # По умолчанию "Офлайн"
    days: Mapped[List[str]] = mapped_column(JSON, default=[], info={"verbose_name": "Дни занятий"})  # Используем JSON вместо ARRAY
    materials: Mapped[Dict | None] = mapped_column(JSON, nullable=True, info={"verbose_name": "Учебные материалы"})  # Учебные материалы
    notes: Mapped[str | None] = mapped_column(Text, nullable=True, info={"verbose_name": "Примечания"})
    cost: Mapped[int] = mapped_column(Integer, default=0, info={"verbose_name": "Стоимость группы"})
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, info={"verbose_name": "Дата создания"})
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, info={"verbose_name": "Дата обновления"})
    
    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="groups")
    level: Mapped["Level"] = relationship("Level", back_populates="groups")
    students: Mapped[list["Student"]] = relationship("Student", back_populates="group")
    lessons: Mapped[list["Lesson"]] = relationship("Lesson", back_populates="group")
    
    def get_students(self):
        return [student.full_name for student in self.students]
    
    def get_schedule(self):
        return [lesson.date for lesson in self.lessons]