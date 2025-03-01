#teacher.py

from models.base import *
from datetime import time,date
from typing import Dict, Optional, List



# Перечисление для типов расписаний
class ScheduleType(PyEnum):
    FIVE_DAY_WEEK = "Пятидневка с 9:00 до 18:00 (с обедом в 13:00)"
    FIVE_DAY_WEEK_NO_LUNCH = "Пятидневка с 9:00 до 13:00"
    EVENING_SHIFT = "Вечерняя смена с 14:00 до 19:00"
    WEEKENDS_ONLY = "Только выходные с 9:00 до 16:00"
    FIVE_DAY_WEEK_PLUS_SATURDAY = "Пятидневка с 9:00 до 19:00 и суббота до 14:00"

# Функции для получения расписания по типу
def get_schedule(schedule_type: ScheduleType) -> Dict[str, Dict[str, Optional[str]]]:
    schedules = {
        ScheduleType.FIVE_DAY_WEEK: {
            "Monday": {"start_time": "09:00", "end_time": "18:00", "lunch_start": "13:00", "lunch_end": "14:00"},
            "Tuesday": {"start_time": "09:00", "end_time": "18:00", "lunch_start": "13:00", "lunch_end": "14:00"},
            "Wednesday": {"start_time": "09:00", "end_time": "18:00", "lunch_start": "13:00", "lunch_end": "14:00"},
            "Thursday": {"start_time": "09:00", "end_time": "18:00", "lunch_start": "13:00", "lunch_end": "14:00"},
            "Friday": {"start_time": "09:00", "end_time": "18:00", "lunch_start": "13:00", "lunch_end": "14:00"},
            "Saturday": None,
            "Sunday": None
        },
        ScheduleType.MORNING_SHIFT: {
            "Monday": {"start_time": "09:00", "end_time": "13:00", "lunch_start": None, "lunch_end": None},
            "Tuesday": {"start_time": "09:00", "end_time": "13:00", "lunch_start": None, "lunch_end": None},
            "Wednesday": {"start_time": "09:00", "end_time": "13:00", "lunch_start": None, "lunch_end": None},
            "Thursday": {"start_time": "09:00", "end_time": "13:00", "lunch_start": None, "lunch_end": None},
            "Friday": {"start_time": "09:00", "end_time": "13:00", "lunch_start": None, "lunch_end": None},
            "Saturday": None,
            "Sunday": None
        },
        ScheduleType.EVENING_SHIFT: {
            "Monday": {"start_time": "14:00", "end_time": "19:00", "lunch_start": None, "lunch_end": None},
            "Tuesday": {"start_time": "14:00", "end_time": "19:00", "lunch_start": None, "lunch_end": None},
            "Wednesday": {"start_time": "14:00", "end_time": "19:00", "lunch_start": None, "lunch_end": None},
            "Thursday": {"start_time": "14:00", "end_time": "19:00", "lunch_start": None, "lunch_end": None},
            "Friday": {"start_time": "14:00", "end_time": "19:00", "lunch_start": None, "lunch_end": None},
            "Saturday": None,
            "Sunday": None
        },
        ScheduleType.WEEKENDS_ONLY: {
            "Monday": None,
            "Tuesday": None,
            "Wednesday": None,
            "Thursday": None,
            "Friday": None,
            "Saturday": {"start_time": "09:00", "end_time": "16:00", "lunch_start": "13:00", "lunch_end": "14:00"},
            "Sunday": {"start_time": "09:00", "end_time": "16:00", "lunch_start": "13:00", "lunch_end": "14:00"}
        },
        ScheduleType.FIVE_DAY_WEEK_PLUS_SATURDAY: {
            "Monday": {"start_time": "09:00", "end_time": "19:00", "lunch_start": "13:00", "lunch_end": "14:00"},
            "Tuesday": {"start_time": "09:00", "end_time": "19:00", "lunch_start": "13:00", "lunch_end": "14:00"},
            "Wednesday": {"start_time": "09:00", "end_time": "19:00", "lunch_start": "13:00", "lunch_end": "14:00"},
            "Thursday": {"start_time": "09:00", "end_time": "19:00", "lunch_start": "13:00", "lunch_end": "14:00"},
            "Friday": {"start_time": "09:00", "end_time": "19:00", "lunch_start": "13:00", "lunch_end": "14:00"},
            "Saturday": {"start_time": "09:00", "end_time": "14:00", "lunch_start": None, "lunch_end": None},
            "Sunday": None
        }
    }
    return schedules[schedule_type]

# Перечисление для режима работы
class WorkMode(PyEnum):
    ONLINE = "Онлайн"
    OFFLINE = "Офлайн"
    BOTH = "Онлайн и офлайн"

# Перечисление для уровня английского
class Teacher_Level(PyEnum):
    BEGINNER = "Beginner"
    ELEMENTARY = "Elementary"
    PRE_INTERMEDIATE = "Pre-Intermediate"
    INTERMEDIATE = "Intermediate"
    UPPER_INTERMEDIATE = "Upper-Intermediate"
    ADVANCED = "Advanced"


# Функция для создания расписания по умолчанию
def default_working_schedule() -> Dict[str, Dict[str, Optional[str]]]:
    return {
        "Monday": {
            "start_time": "09:00",
            "end_time": "18:00",
            "lunch_start": "13:00",
            "lunch_end": "14:00"
        },
        "Tuesday": {
            "start_time": "09:00",
            "end_time": "18:00",
            "lunch_start": "13:00",
            "lunch_end": "14:00"
        },
        "Wednesday": {
            "start_time": "09:00",
            "end_time": "18:00",
            "lunch_start": "13:00",
            "lunch_end": "14:00"
        },
        "Thursday": {
            "start_time": "09:00",
            "end_time": "18:00",
            "lunch_start": "13:00",
            "lunch_end": "14:00"
        },
        "Friday": {
            "start_time": "09:00",
            "end_time": "18:00",
            "lunch_start": "13:00",
            "lunch_end": "14:00"
        },
        "Saturday": None,  # Не рабочий день
        "Sunday": None     # Не рабочий день
    }

class Teacher(Base):
    __tablename__ = "teachers"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)  # Имя
    surname: Mapped[str] = mapped_column(String, index=True, nullable=True)  # Фамилия
    patronymic: Mapped[str | None] = mapped_column(String, nullable=True)  # Отчество
    date_of_birth: Mapped[date | None] = mapped_column(Date, nullable=True)  # Дата рождения
    resume: Mapped[bytes | None] = mapped_column(LargeBinary, nullable=True)  # Резюме (файл)
    english_level: Mapped[Teacher_Level] = mapped_column(Enum(Teacher_Level), default=Teacher_Level.ADVANCED)  # Уровень английского
    can_teach_ielts: Mapped[bool] = mapped_column(Boolean, default=False)  # Может ли преподавать IELTS
    ielts_score: Mapped[float | None] = mapped_column(Float, nullable=True)  # Результат по IELTS
    work_mode: Mapped[WorkMode] = mapped_column(Enum(WorkMode))  # Режим работы
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    hourly_rate: Mapped[float | None] = mapped_column(Float, nullable=True)
    fixed_salary: Mapped[float | None] = mapped_column(Float, nullable=True)
    group_payment_rules: Mapped[str | None] = mapped_column(String, nullable=True)
    individual_payment_rules: Mapped[str | None] = mapped_column(String, nullable=True)
    working_schedule: Mapped[ScheduleType] = mapped_column(Enum(ScheduleType), default=ScheduleType.FIVE_DAY_WEEK)  # Тип расписания

    groups: Mapped[list["Group"]] = relationship("Group", back_populates="teacher")
    lessons: Mapped[list['Lesson']] = relationship('Lesson', back_populates='teacher')