from db.session import session
from sqlalchemy import select
from models.adm import Adm

def login(user,password):
    try:
        statement = select(Adm.username, Adm.password).where(Adm.username==f'{user}')
        foundUser = session.execute(statement).first()
        if foundUser is None:
            return 'erro'
        if foundUser.password == password:
            return 'okay'
        else:
            return 'erro'
    except:
        return 'erro'


