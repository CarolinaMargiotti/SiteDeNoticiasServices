from db.session import session
from sqlalchemy import select
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
