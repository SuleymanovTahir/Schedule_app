#lesson.py

from models.base import *




class Lesson(Base):
    __tablename__ = "lessons"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    time_start: Mapped[DateTime] = mapped_column(DateTime)
    time_end: Mapped[DateTime] = mapped_column(DateTime)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    level_id: Mapped[int] = mapped_column(ForeignKey("levels.id"))
    # Используем строковые ссылки для relationship
    teacher: Mapped["Teacher"] = relationship("Teacher", back_populates="lessons")
    group: Mapped["Group"] = relationship("Group", back_populates="lessons")
    level: Mapped["Level"] = relationship("Level", back_populates="lessons")

