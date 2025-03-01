# base.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, String, Integer, DateTime, Time, Text,Enum, Boolean, Float, JSON,LargeBinary,Date
from sqlalchemy.orm import relationship, Mapped, mapped_column

from enum import Enum as PyEnum



Base = declarative_base()