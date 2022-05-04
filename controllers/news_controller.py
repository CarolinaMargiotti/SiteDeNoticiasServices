from db.session import session
from models.news import News

def getAllNews(startNumber:int, quantity:int):
    # allNews = session.query.paginate(startNumber,False,quantity)
    # print(allNews)
    return ["noticia1",'noticia2','noticia3']

def getNews(id:int):
    news = session.query(News).get(id)

    return {"id":id,"titulo":news.titulo,"assunto":news.assunto,"categoria":news.categoria,"resumo":news.resumo,"conteudo":news.conteudo}

def createNews(titulo,categoria,resumo,assunto,conteudo):
    newNews = News(titulo=titulo,categoria=categoria,resumo=resumo,assunto=assunto,conteudo=conteudo)
    session.add(newNews)
    session.commit()
    return {"id":1,"titulo":titulo,"assunto":assunto,"categoria":categoria,"resumo":resumo,"conteudo":conteudo}

def editNews(id,titulo,categoria,resumo,assunto,conteudo):
    news = session.query(News).get(id)
    news.titulo = titulo
    news.categoria=categoria
    news.resumo = resumo
    news.assunto = assunto
    news.conteudo=conteudo
    session.commit()
    return {"id":1,"titulo":titulo,"categoria":categoria,"assunto":assunto,"resumo":resumo,"conteudo":conteudo}

def deleteNews(id):
    session.query(News).filter(News.id == id).delete()
    session.commit()
    return id
