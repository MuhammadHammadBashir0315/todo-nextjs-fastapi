from sqlalchemy import Boolean, Column, Integer, String
from db import Base

class Task(Base):
    __tablename__ = 'task'

    id=Column(Integer, primary_key=True)
    title=Column(String)
    description=Column(String)