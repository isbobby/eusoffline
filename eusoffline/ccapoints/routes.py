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

    gender = "Male"

    if current_user.gender == "f":
        gender = "Female"

    return render_template('/ccapoints/checkccapoint.html', result=result,
                           totalPoints=totalPoints,
                           gender=gender)


@cca.route("/cca/checktopresidents", methods=['GET'])
def ccaCheckTopResidents():
    # contains matric, number of CCA and total points
    TotalPointSummary = db.session.query(CCAMap.matric,
                                         db.func.count(CCAMap.cca).label(
                                             'Number of CCA'),
                                         db.func.sum(CCAMap.points).label(
                                             'Total Points')).group_by(
        CCAMap.matric).all()

    TotalPointSummary.sort(reverse=True, key=lambda x: x[2])

    topMaleResidents = []
    topFemaleResidents = []
    MaleNumber = 1
    FemaleNumber = 1

    # resident 0 is the matric number
    for entry in TotalPointSummary:
        resident = BaseUser.query.filter_by(matric=entry[0]).first()
        newEntry = {
            'name': resident.name,
            'ccacount': entry[1],
            'totalpoints': entry[2],
            'index': 0
        }

        # Gender check
        if(resident.gender.lower() == "m" and MaleNumber < 110):
            newEntry['index'] = MaleNumber
            topMaleResidents.append(newEntry)
            MaleNumber += 1
        else:
            if (FemaleNumber < 110):
                newEntry['index'] = FemaleNumber
                topFemaleResidents.append(newEntry)
                FemaleNumber += 1

    return render_template('/ccapoints/checkTopResidents.html',
                           topMaleResidents=topMaleResidents,
                           topFemaleResidents=topFemaleResidents)
