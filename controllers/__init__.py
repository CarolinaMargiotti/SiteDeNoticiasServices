from flask import request, jsonify,Blueprint,make_response

from controllers.news_controller import getAllNews,getNews,createNews,editNews,deleteNews,getNewsFromASpecificSubject
from controllers.adm_controller import login,checkUserDataIsValid
from controllers.subjects_controller import getSubjects,createSubject,deleteSubject,getSpecificId,editSubject,getAllSubjects

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
    req = request.form
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

@news_bp.route('/editnews', methods=["put"])
def editnews():
    req = request.form
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

@news_bp.route('/deletenews', methods=["delete"])
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

    respostaValidacao = checkUserDataIsValid(user,password)
    if(respostaValidacao['status_code']==400):
        return make_response(respostaValidacao['mensagem'],respostaValidacao['status_code'])

    res = login(user,password)
    return res


@subjects_bp.route("/getallsubjects",methods=['GET'])
def getAllOfTheSubjects():
    res = getAllSubjects()
    return res

@subjects_bp.route("/getsubjects",methods=['GET'])
def getSubjectsPaginated():
    req = request.args

    startNumber = req.get("startNumber",None)
    quantity = req.get("quantity",None)

    if startNumber is None:
        res = make_response({"mensagem":'falta startNumber'},400)
        return res

    if quantity is None:
        res = make_response({"mensagem":'falta quantity'},400)
        return res

    res = getSubjects(startNumber,quantity)
    return res

@subjects_bp.route("/createsubject",methods=['POST'])
def createNewSubject():
    req = request.form
    name = req.get("subjectName",None)

    if name is None:
        res = make_response({"mensagem":'falta nome do assunto'},400)
        return res

    res = createSubject(name)
    return res

@subjects_bp.route('/deletesubject', methods=["delete"])
def deleteSpecificSubject():
    id = request.args.get("id",None)

    if id is None:
        res = make_response({"mensagem":'falta id'},400)
        return res

    res = deleteSubject(id)
    return res

@subjects_bp.route('/getnewsbyid',methods=['get'])
def getSubjectById():
    id = request.args.get("id",None)

    if id is None:
        res = make_response({"mensagem":'falta id'},400)
        return res

    res = getSpecificId(id)
    return res

@subjects_bp.route("/editsubject",methods=['put'])
def editSpecificSubject():
    req = request.form
    id = req.get("id",None)
    nome = req.get("subjectName",None)

    if id is None:
        res = make_response({"mensagem":'falta id'},400)
        return res

    if nome is None:
        res = make_response({"mensagem":"falta nome do assunto"},400)
        return res

    res = editSubject(id,nome)
    return res

