import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from db.api import engine

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()
