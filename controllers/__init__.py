from flask import request,abort, jsonify,Blueprint,make_response

from controllers.news_controller import getAllNews,getNews,createNews,editNews,deleteNews
from controllers.adm_controller import login

news_bp = Blueprint("news",__name__)
adm_bp = Blueprint("adm",__name__)

@news_bp.route("/getallnews", methods=["GET"])
def getallnews():
    req = request.args

    startNumber = req.get("startNumber",None)
    quantity = req.get("quantity",None)

    if startNumber is None:
        abort(404,"falta startNumber")
    
    if quantity is None:
        abort(404,'falta quantity')

    allnews = getAllNews(startNumber,quantity)
    res = make_response(jsonify(allnews),200)
    return res

@news_bp.route("/getnews", methods=["GET"])
def getnews():
    print(request.args)
    id = request.args.get("id",None)

    if id is None:
        abort(404, "Falta id")

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
        abort(404,"falta titulo")

    if categoria is None:
        abort(404,"falta categoria")
    
    if resumo is None:
        abort(404,"falta resumo")
    
    if conteudo is None:
        abort(404,"falta conteudo")

    if assunto is None:
        abort(404,"falta assunto")

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
        abort(404,"falta id")

    if titulo is None:
        abort(404,"falta titulo")

    if categoria is None:
        abort(404,"falta categoria")
    
    if resumo is None:
        abort(404,"falta resumo")
    
    if conteudo is None:
        abort(404,"falta conteudo")

        
    if assunto is None:
        abort(404,"falta assunto")

    newsEdited = editNews(id,titulo,categoria,resumo,assunto,conteudo)
    res = make_response(jsonify(newsEdited),200)

    return res

@news_bp.route('/deletenews/', methods=["DELETE"])
def deletenews():
    id = request.args.get("id",None)

    if id is None:
        abort(404, "Falta id")

    newsDeleted = deleteNews(id)
    res = make_response(jsonify(newsDeleted),200)
    return res

@adm_bp.route('/login/', methods=["GET"])
def loginADM():
    req = request.args
    user = req.get("user")
    password = req.get("password")

    if user is None:
        abort(404,"falta nome do usuario")
    
    if password is None:
        abort(404, "falta senha")

    loginUser = login(user,password)
    res = make_response(jsonify(loginUser),200)

    return res