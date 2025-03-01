from pydantic import BaseModel

class TeacherBase(BaseModel):
    name: str
    is_active: bool
    working_days: str
    working_hours: str

class TeacherCreate(TeacherBase):
    pass

class Teacher(TeacherBase):
    id: int

    class Config:
        from_attributes = True