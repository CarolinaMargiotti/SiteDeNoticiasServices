from flask import request, jsonify,Blueprint,make_response

from controllers.news_controller import getAllNews,getNews,createNews,editNews,deleteNews,getNewsFromASpecificSubject
from controllers.adm_controller import login
from controllers.subjects_controller import getSubjects,createSubject,deleteSubject

news_bp = Blueprint("news",__name__)
adm_bp = Blueprint("adm",__name__)
subjects_bp = Blueprint("subjects",__name__)

@news_bp.route("/getallnews", methods=["GET"])
def getallnews():
    req = request.args

    startNumber = req.get("startNumber",None)
    quantity = req.get("quantity",None)

    if startNumber is None:
        res = make_response({"mensagem":'falta startNumber'},400)
        return res

    if quantity is None:
        res = make_response({"mensagem":'falta quantity'},400)
        return res

    res = getAllNews(startNumber,quantity)
    return res

@news_bp.route("/getallnewsbysubject", methods=["GET"])
def getallnewsbysubject():
    req = request.args

    startNumber = req.get("startNumber",None)
    quantity = req.get("quantity",None)
    assunto = req.get("assunto",None)

    if startNumber is None:
        res = make_response({"mensagem":'falta startNumber'},400)
        return res

    if quantity is None:
        res = make_response({"mensagem":'falta quantity'},400)
        return res

    if assunto is None:
        res = make_response({"mensagem":'falta assunto'},400)
        return res

    allnews = getNewsFromASpecificSubject(assunto,startNumber,quantity)
    res = make_response(jsonify(allnews),200)
    return res


@news_bp.route("/getnews", methods=["GET"])
def getnews():
    id = request.args.get("id",None)

    if id is None:
        res = make_response({"mensagem":'falta id'},400)
        return res

    news = getNews(id)
    res = make_response(jsonify(news),200)

    return res

@news_bp.route('/createnews/', methods=["POST"])
def createnews():
    req = request.args
    titulo = req.get("titulo",None)
    assunto = req.get("assunto",None)
    resumo = req.get("resumo",None)
    conteudo = req.get('conteudo',None)

    if titulo is None:
        res = make_response({"mensagem":'falta titulo'},400)
        return res

    if resumo is None:
        res = make_response({"mensagem":'falta resumo'},400)
        return res

    if conteudo is None:
        res = make_response({"mensagem":'falta conteudo'},400)
        return res

    if assunto is None:
        res = make_response({"mensagem":'falta assunto'},400)
        return res

    res = createNews(titulo,resumo,assunto,conteudo)
    return res

@news_bp.route('/editnews/', methods=["POST"])
def editnews():
    req = request.args
    id = req.get("id",None)
    titulo = req.get("titulo",None)
    resumo = req.get("resumo",None)
    conteudo = req.get('conteudo',None)
    assunto = req.get("assunto",None)

    if id is None:
        res = make_response({"mensagem":'falta id'},400)
        return res

    if titulo is None:
        res = make_response({"mensagem":'falta titulo'},400)
        return res

    if resumo is None:
        res = make_response({"mensagem":'falta resumo'},400)
        return res

    if conteudo is None:
        res = make_response({"mensagem":'falta conteudo'},400)
        return res

    if assunto is None:
        res = make_response({"mensagem":'falta assunto'},400)
        return res

    res = editNews(id,titulo,resumo,assunto,conteudo)
    return res

@news_bp.route('/deletenews/', methods=["post"])
def deletenews():
    id = request.args.get("id",None)

    if id is None:
        res = make_response({"mensagem":'falta id'},400)
        return res

    newsDeleted = deleteNews(id)
    res = make_response(jsonify(newsDeleted),200)
    return res

@adm_bp.route('/login', methods=["POST"])
def loginADM():
    req = request.args
    user = req.get("user")
    password = req.get("password")

    if user is None:
        res = make_response({"mensagem":'falta nome do usuario'},400)
        return res


    if password is None:
        res = make_response({"mensagem":'falta senha'},400)
        return res

    res = login(user,password)
    return res


@subjects_bp.route("/getallsubjects",methods=['GET'])
def getAllSubjects():
    res = getSubjects()
    return res

@subjects_bp.route("/createsubject",methods=['POST'])
def createNewSubject():
    req = request.args
    name = req.get("subjectName",None)

    if name is None:
        res = make_response({"mensagem":'falta nome do assunto'},400)
        return res

    res = createSubject(name)
    return res

@news_bp.route('/deletesubject', methods=["post"])
def deleteSpecificSubject():
    id = request.args.get("id",None)

    if id is None:
        res = make_response({"mensagem":'falta id'},400)
        return res

    res = deleteSubject(id)
    return res