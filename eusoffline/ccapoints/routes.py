from flask import Blueprint, render_template

from flask_login import current_user

from eusoffline.models import CCAMap

ccapoints = Blueprint('ccapoints', __name__)


@ccapoints.route("/checkccapoint", methods=['GET'])
def mainCheckPoint():
    result = CCAMap.query.filter_by(matric=current_user.matric).all()
    totalPoints = 0
    if result:
        for entries in result:
            totalPoints += entries.points

    return render_template('/ccapoints/checkccapoint.html', result=result,
                           totalPoints=totalPoints)
