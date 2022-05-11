from flask import request, jsonify,Blueprint,make_response

from controllers.news_controller import getAllNews,getNews,createNews,editNews,deleteNews,getNewsFromASpecitifCategory
from controllers.adm_controller import login

news_bp = Blueprint("news",__name__)
adm_bp = Blueprint("adm",__name__)

@news_bp.route("/getallnews", methods=["GET"])
def getallnews():
    req = request.args

    startNumber = req.get("startNumber",None)
    quantity = req.get("quantity",None)

    if startNumber is None:
        res = make_response({"mensagem":'falta startNumber'},404)
        return res

    if quantity is None:
        res = make_response({"mensagem":'falta quantity'},404)
        return res

    allnews = getAllNews(startNumber,quantity)
    res = make_response(jsonify(allnews),200)
    return res

@news_bp.route("/getallnewsbycategory", methods=["GET"])
def getallnewsbycategory():
    req = request.args

    startNumber = req.get("startNumber",None)
    quantity = req.get("quantity",None)
    categoria = req.get("categoria",None)

    if startNumber is None:
        res = make_response({"mensagem":'falta startNumber'},404)
        return res

    if quantity is None:
        res = make_response({"mensagem":'falta quantity'},404)
        return res

    if categoria is None:
        res = make_response({"mensagem":'falta categoria'},404)
        return res

    allnews = getNewsFromASpecitifCategory(categoria,startNumber,quantity)
    res = make_response(jsonify(allnews),200)
    return res


@news_bp.route("/getnews", methods=["GET"])
def getnews():
    print(request.args)
    id = request.args.get("id",None)

    if id is None:
        res = make_response({"mensagem":'falta id'},404)
        return res

    news = getNews(id)
    res = make_response(jsonify(news),200)

    return res

@news_bp.route('/createnews/', methods=["POST"])
def createnews():
    req = request.args
    titulo = req.get("titulo",None)
    assunto = req.get("assunto",None)
    categoria = req.get('categoria',None)
    resumo = req.get("resumo",None)
    conteudo = req.get('conteudo',None)

    if titulo is None:
        res = make_response({"mensagem":'falta titulo'},404)
        return res

    if categoria is None:
        res = make_response({"mensagem":'falta categoria'},404)
        return res

    if resumo is None:
        res = make_response({"mensagem":'falta resumo'},404)
        return res

    if conteudo is None:
        res = make_response({"mensagem":'falta conteudo'},404)
        return res

    if assunto is None:
        res = make_response({"mensagem":'falta assunto'},404)
        return res

    newsCreated = createNews(titulo,categoria,resumo,assunto,conteudo)
    res = make_response(jsonify(newsCreated),200)

    return res

@news_bp.route('/editnews/', methods=["PUT"])
def editnews():
    req = request.args
    id = req.get("id",None)
    titulo = req.get("titulo",None)
    categoria = req.get('categoria',None)
    resumo = req.get("resumo",None)
    conteudo = req.get('conteudo',None)
    assunto = req.get("assunto",None)

    if id is None:
        res = make_response({"mensagem":'falta id'},404)
        return res

    if titulo is None:
        res = make_response({"mensagem":'falta titulo'},404)
        return res

    if categoria is None:
        res = make_response({"mensagem":'falta categoria'},404)
        return res

    if resumo is None:
        res = make_response({"mensagem":'falta resumo'},404)
        return res

    if conteudo is None:
        res = make_response({"mensagem":'falta conteudo'},404)
        return res

    if assunto is None:
        res = make_response({"mensagem":'falta assunto'},404)
        return res

    newsEdited = editNews(id,titulo,categoria,resumo,assunto,conteudo)
    res = make_response(jsonify(newsEdited),200)

    return res

@news_bp.route('/deletenews/', methods=["DELETE"])
def deletenews():
    id = request.args.get("id",None)

    if id is None:
        res = make_response({"mensagem":'falta id'},404)
        return res

    newsDeleted = deleteNews(id)
    res = make_response(jsonify(newsDeleted),200)
    return res

@adm_bp.route('/login/', methods=["POST"])
def loginADM():
    req = request.args
    user = req.get("user")
    password = req.get("password")

    if user is None:
        res = make_response({"mensagem":'falta nome do usuario'},404)

    if password is None:
        res = make_response({"mensagem":'falta senha'},404)

    loginUser = login(user,password)
    if loginUser == 'okay':
        res = make_response(jsonify(loginUser),200)
    else:
        res = make_response({"mensagem":'não foi possivel logar'},404)

    return res
