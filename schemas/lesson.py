from pydantic import BaseModel
from datetime import datetime

class LessonBase(BaseModel):
    time_start: datetime
    time_end: datetime
    teacher_id: int
    group_id: int
    level_id: int

class LessonCreate(LessonBase):
    pass

class Lesson(LessonBase):
    id: int

    class Config:
        from_attributes = True