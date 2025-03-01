#level.py

from models.base import *

# Перечисление для уровней
class LevelType(PyEnum):
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



class Level(Base):
    __tablename__ = "levels"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[LevelType] = mapped_column(Enum(LevelType), unique=True, index=True)  # Используем LevelType
    lessons: Mapped[list["Lesson"]] = relationship("Lesson", back_populates="level")
    groups: Mapped[list["Group"]] = relationship("Group", back_populates="level")
