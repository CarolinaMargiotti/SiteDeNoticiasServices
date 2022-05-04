from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker
from db.api import engine

Base = declarative_base()

class News(Base):
    __tablename__='news'
    id = Column(Integer, primary_key=True)
    titulo= Column(String(255),nullable=False)
    categoria= Column(String(255),nullable=False)
    resumo=Column(String(255),nullable=False)
    conteudo=Column(String(255),nullable=False)
    assunto=Column(String(255),nullable=False)

    def __init__(self, titulo=None,categoria=None,resumo=None,assunto=None,conteudo=None):
        self.titulo = titulo
        self.resumo = resumo
        self.categoria=categoria
        self.conteudo = conteudo
        self.assunto = assunto

    def __repr__(self):
        return "News(%r, %r, %r, %r)" % (self.titulo,self.categoria, self.assunto, self.resumo,self.conteudo)


Base.metadata.create_all(engine)