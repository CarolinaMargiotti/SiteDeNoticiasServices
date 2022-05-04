from flask import Flask,Blueprint
from controllers import news_bp,adm_bp

app = Flask(__name__)
app.register_blueprint(news_bp)
app.register_blueprint(adm_bp)

if __name__ == '__main__':
    app.run()
