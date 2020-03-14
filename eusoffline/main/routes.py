from flask import Blueprint, render_template, request

main = Blueprint('main',__name__)

@main.route("/")
def mainHome():
    return render_template('/main/index.html')