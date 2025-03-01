#database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
from models.base import Base



DATABASE_URL = "sqlite:///./schedule.db"

engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()        

# Импортируем модели
from models.teacher import Teacher
from models.student import Student
from models.level import Level
from models.lesson import Lesson
from models.group import Group
from models.director import Director
# from models.model_admin import Model_Admin




# Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

