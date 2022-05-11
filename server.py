from flask import Flask,request
from controllers import news_bp,adm_bp
from db.session import session
from flask_cors import CORS, cross_origin


def createAdm():
    try:
        userAdm = Adm(username="usuario",password="senha")
        session.add(userAdm)
        session.commit()
    except:
        print("adm ja existe")

createAdm()

app = Flask(__name__)
CORS(app)
app.register_blueprint(news_bp)
app.register_blueprint(adm_bp)


@app.after_request
def after_request(response):
    white_origin= ['http://www.dom.com:8000','http://localhost']
    if request.headers['Origin'] in white_origin:
        response.headers['Access-Control-Allow-Origin'] = request.headers['Origin'] 
        response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

if __name__ == '__main__':
    app.run(port=8080)
