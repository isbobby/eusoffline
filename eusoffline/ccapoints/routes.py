from flask import Blueprint, render_template

from flask_login import current_user

from eusoffline import db

from eusoffline.models import CCAMap, BaseUser

cca = Blueprint('cca', __name__)


@cca.route("/cca", methods=['GET'])
def ccaHome():
    return render_template('/ccapoints/ccaindex.html')


@cca.route("/cca/checkccapoint", methods=['GET'])
def ccaCheckPoint():
    result = CCAMap.query.filter_by(matric=current_user.matric).all()
    totalPoints = 0
    if result:
        for entries in result:
            totalPoints += entries.points

    return render_template('/ccapoints/checkccapoint.html', result=result,
                           totalPoints=totalPoints)


@cca.route("/cca/viewall", methods=['GET'])
def ccaViewAll():
    # contains matric, number of CCA and total points
    summary = db.session.query(CCAMap.matric,
                               db.func.count(CCAMap.cca).label(
                                   'Number of CCA'),
                               db.func.sum(CCAMap.points).label(
                                   'Total Points')).group_by(
        CCAMap.matric).all()

    summary.sort(key=lambda x: x[2], reverse=True)

    residentCount = 1
    residents = []
    for entry in summary:

        this_resident = BaseUser.query.filter_by(matric=entry[0]).first()

        newResident = {
            "index": residentCount,
            "matricno": entry[0],
            "name": this_resident.name,
            "ccacount": entry[1],
            "totalpoints": entry[2]
        }

        residents.append(newResident)
        residentCount += 1


    return render_template('/ccapoints/checkall.html',
                           residents=residents,
                           residentCount=residentCount)
