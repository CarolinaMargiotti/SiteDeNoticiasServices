from flask import Flask,request
from controllers import news_bp,adm_bp,subjects_bp
from db.session import session
from flask_cors import CORS, cross_origin
from models.adm import Adm;
from waitress import serve
from models.envVariables import port,host


def createAdm():
    try:
        userAdm = Adm(username="usuario",password="senha")
        session.add(userAdm)
        session.commit()
        session.rollback()
    except:
        session.rollback()


createAdm()

app = Flask(__name__)
CORS(app)
app.register_blueprint(news_bp)
app.register_blueprint(adm_bp)
app.register_blueprint(subjects_bp)


@app.after_request
def after_request(response):
    try:
        white_origin= ['http://www.dom.com:8000','http://localhost']
        if request.headers['Origin'] in white_origin:
            response.headers['Access-Control-Allow-Origin'] = request.headers['Origin']
            response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        return response
    except:
        return response

if __name__ == '__main__':
    # app.run(port=port)
    serve(app, host=host, port=port)
