from db.session import session
from sqlalchemy import select
from flask import make_response,jsonify
from models.news import News
from controllers.subjects_controller import getSpecificId

def getAllNews(startNumber:int, quantity:int):
    try:
        allNews = session.query(News).all()
        session.rollback()
        endNumber = (int(startNumber)+int(quantity))-1
        slicedNews = allNews[int(startNumber)-1:endNumber]

        treatedNews=[]
        for news in slicedNews:
            treatedNews.append({"id":news.id,"titulo":news.titulo,"assunto":str(news.assunto),"resumo":news.resumo,"conteudo":news.conteudo})
        return make_response(jsonify(treatedNews),200)
    except:
        session.rollback();
        return make_response({"mensagem":"Ocorreu um erro"},400)



def getNews(id:int):
    news = session.query(News).get(id)
    return {"id":id,"titulo":news.titulo,"assunto":str(news.assunto),"resumo":news.resumo,"conteudo":news.conteudo}

def getNewsFromASpecificSubject(assunto,startNumber:int, quantity:int):
    try:
        allNews = session.query(News).filter(News.assunto==assunto).all()
        session.rollback()
        slicedNews = allNews[int(startNumber)-1:int(quantity)]

        treatedNews=[]
        for news in slicedNews:
            treatedNews.append({"id":news.id,"titulo":news.titulo,"assunto":str(news.assunto),"resumo":news.resumo,"conteudo":news.conteudo})

        return treatedNews
    except:
        session.rollback();
        return []


def createNews(titulo,resumo,assunto,conteudo):
    try:
        resSubject = getSpecificId(assunto)
        if(resSubject.status_code!=200):
            return make_response({"mensagem":"assunto não existe"},400)

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
        editedNews={"id":1,"titulo":titulo,"assunto":assunto,"resumo":resumo,"conteudo":conteudo}

        return make_response(editedNews,200)
    except:
        session.rollback();
        return make_response({"mensagem":"Ocorreu um erro"},400)

def deleteNews(id):
    try:
        session.query(News).filter(News.id == id).delete()
        session.commit()
        session.rollback()
        return id
    except:
        session.rollback();
        return 0
