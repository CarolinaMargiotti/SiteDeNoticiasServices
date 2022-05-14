from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker
from db.api import engine

Base = declarative_base()

class Subjects(Base):
    __tablename__='subjects'
    id = Column(Integer, primary_key=True)
    subjectName = Column(String(50),nullable=False, unique=True )

    def __init__(self, subjectName=None):
        self.subjectName  =subjectName

    def __repr__(self):
        return (f'Subjects({self.subjectName})')


Base.metadata.create_all(engine)