from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker
from db.api import engine

Base = declarative_base()

class Adm(Base):
    __tablename__='adm'
    id = Column(Integer, primary_key=True)
    username = Column(String(255),nullable=False)
    password = Column(String(255),nullable=False)

    def __init__(self, username=None,password=None):
        self.titulo = titulo
        self.username = username
        self.password=password

    def __repr__(self):
        return "Adm(%r)" % (self.username)


Base.metadata.create_all(engine)