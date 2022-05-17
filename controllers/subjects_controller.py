from db.session import session
from flask import make_response,jsonify
from models.subjects import Subjects
import controllers.news_controller as news_controller

def createSubject(subject):
    try:
        subject = Subjects(subjectName=subject)
        session.add(subject)
        session.commit()
        session.rollback()
        return make_response({"subjectName":subject.subjectName},200)

    except:
        session.rollback();
        return make_response({"mensagem":"Assunto ja existe"},400)

def getAllSubjects():
    try:
        allSubjects = session.query(Subjects).all()
        session.rollback()

        treatedSubjects ={}
        for subject in allSubjects:
            treatedSubjects[subject.id]=subject.subjectName
        return make_response(jsonify(treatedSubjects),200)

    except:
        session.rollback();
        return make_response({"mensagem":"Ocorreu um erro"},400)

def getSubjects(startNumber:int, quantity:int):
    try:
        allSubjects = session.query(Subjects).all()
        session.rollback()
        endNumber = (int(startNumber)+int(quantity))-1
        slicedSubjects = allSubjects[int(startNumber)-1:endNumber]

        treatedSubjects ={}
        for subject in slicedSubjects:
            treatedSubjects[subject.id]=subject.subjectName
        return make_response(jsonify(treatedSubjects),200)

    except:
        session.rollback();
        return make_response({"mensagem":"Ocorreu um erro"},400)

def deleteSubject(subjectId):
    try:
        resNews = news_controller.getNewsFromASpecificSubject(subjectId,1,4)
        if len(resNews)>0:
            return make_response({"mensagem":"Existe noticias com esse assunto, as delete primeiro"},400)

        session.query(Subjects).filter(Subjects.id == subjectId).delete()
        session.commit()
        session.rollback()
        return make_response({"id":subjectId},200)
    except:
        session.rollback();
        return make_response({"mensagem":"Ocorreu um erro"},400)

def getSpecificId(id):
    try:
        subject = session.query(Subjects).get(id)
        session.rollback();
        chosenSubject = {"id":subject.id,"subjectName":subject.subjectName}
        return make_response(jsonify(chosenSubject),200)

    except:
        session.rollback();
        return make_response({"mensagem":"Ocorreu um erro"},400)

def editSubject(id,newname):
    try:
        subject = session.query(Subjects).get(id)
        subject.subjectName = newname
        session.commit()
        session.rollback()
        newSubject ={"id":id,"subjectName":newname};
        return make_response(jsonify(newSubject),200)
    except:
        session.rollback();
        return make_response({"mensagem":"Ocorreu um erro"},400)