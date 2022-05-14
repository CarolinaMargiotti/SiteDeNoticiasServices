from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker
from db.api import engine

Base = declarative_base()

class News(Base):
    __tablename__='news'
    id = Column(Integer, primary_key=True)
    titulo= Column(String(255),nullable=False)
    resumo=Column(String(255),nullable=False)
    conteudo=Column(String(255),nullable=False)
    assunto=Column(Integer,nullable=False)

    def __init__(self, titulo=None,resumo=None,assunto=None,conteudo=None):
        self.titulo = titulo
        self.resumo = resumo
        self.conteudo = conteudo
        self.assunto = assunto

    def __repr__(self):
        return (f'News({self.id},{self.titulo},{self.resumo},{self.assunto})')



Base.metadata.create_all(engine)