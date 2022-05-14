from db.session import session
from sqlalchemy import select
from models.adm import Adm
from flask import make_response,jsonify

def login(user,password):
    try:
        statement = select(Adm.id,Adm.username,Adm.password).where(Adm.username==f'{user}')
        foundUser = session.execute(statement).first()
        session.rollback()
        if foundUser is None:
            return make_response({"mensagem":"Usuario não existe"},400)
        if foundUser.password == password:
            return make_response({"mensagem":"okay"},200)
        else:
            return make_response({"mensagem":"Senha incorreta"},400)

    except Exception:
        session.rollback()
        return make_response({"mensagem":"Ocorreu um erro"},400)


