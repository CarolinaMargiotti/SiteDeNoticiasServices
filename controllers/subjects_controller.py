from db.session import session
from flask import make_response,jsonify
from models.subjects import Subjects

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


def getSubjects():
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

def deleteSubject(subjectId):
    try:
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