from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker
from db.api import engine

Base = declarative_base()

class categories(Base):
    __tablename__='categoriess'
    id = Column(Integer, primary_key=True)
    categoriesName = Column(String(255),nullable=False, unique=True )

    def __init__(self, categoriesName=None):
        self.categoriesName  =categoriesName

    def __repr__(self):
        return "Categoriess(%r)" % (self.categoriesName)


Base.metadata.create_all(engine)