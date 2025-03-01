from pydantic import BaseModel
from typing import Optional

class GroupBase(BaseModel):
    name: str  # Название группы
    level_id: int  # Уровень группы
    teacher_id: int  # Учитель группы
    is_individual: bool  # Индивидуальное занятие или групповое
    is_online: bool  # Онлайн или офлайн
    days: str  # Дни занятий (например, "пн,ср,пт")
    notes: Optional[str] = None  # Примечания

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int

    class Config:
        from_attributes = True