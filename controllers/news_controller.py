from db.session import session
from sqlalchemy import select
from flask import make_response,jsonify
from models.news import News
from models.subjects import Subjects
from controllers.subjects_controller import createSubject

def getAllNews(startNumber:int, quantity:int):
    try:
        allNews = session.query(News).all()
        session.rollback()
        slicedNews = allNews[int(startNumber)-1:int(quantity)]

        treatedNews=[]
        for news in slicedNews:
            treatedNews.append({"id":news.id,"titulo":news.titulo,"assunto":news.assunto,"resumo":news.resumo,"conteudo":news.conteudo})
        return make_response(jsonify(treatedNews),200)
    except:
        session.rollback();
        return make_response({"mensagem":"Ocorreu um erro"},400)



def getNews(id:int):
    news = session.query(News).get(id)
    return {"id":id,"titulo":news.titulo,"assunto":news.assunto,"resumo":news.resumo,"conteudo":news.conteudo}

def getNewsFromASpecificSubject(assunto,startNumber:int, quantity:int):
    try:
        allNews = session.query(News).filter(News.assunto==assunto).all()
        session.rollback()
        slicedNews = allNews[int(startNumber)-1:int(quantity)]

        treatedNews=[]
        for news in slicedNews:
            treatedNews.append({"id":news.id,"titulo":news.titulo,"assunto":news.assunto,"resumo":news.resumo,"conteudo":news.conteudo})

        return treatedNews
    except:
        session.rollback();
        return []


def createNews(titulo,resumo,assunto,conteudo):
    try:
        createSubject(assunto)
        newNews = News(titulo=titulo,resumo=resumo,assunto=assunto,conteudo=conteudo)
        session.add(newNews)
        session.commit()
        createdNews={"id":1,"titulo":titulo,"assunto":assunto,"resumo":resumo,"conteudo":conteudo}
        session.rollback()
        return make_response(createdNews,200)
    except:
        session.rollback();
        return make_response({"mensagem":"ocorreu um erro"},400)

def editNews(id,titulo,resumo,assunto,conteudo):
    try:
        news = session.query(News).get(id)
        news.titulo = titulo
        news.resumo = resumo
        news.assunto = assunto
        news.conteudo=conteudo
        session.commit()
        session.rollback()
        return {"id":1,"titulo":titulo,"assunto":assunto,"resumo":resumo,"conteudo":conteudo}
    except:
        session.rollback();
        return {}

def deleteNews(id):
    try:
        session.query(News).filter(News.id == id).delete()
        session.commit()
        session.rollback()
        return id
    except:
        session.rollback();
        return 0
