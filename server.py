from flask import Flask,Blueprint
from controllers import news_bp,adm_bp
from db.session import session


def createAdm():
    try:
        userAdm = Adm(username="usuario",password="senha")
        session.add(userAdm)
        session.commit()
    except:
        print("adm ja existe")

createAdm()

app = Flask(__name__)
app.register_blueprint(news_bp)
app.register_blueprint(adm_bp)

if __name__ == '__main__':
    app.run()
