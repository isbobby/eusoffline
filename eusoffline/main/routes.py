from flask import Blueprint, render_template, flash, redirect, url_for

from flask_login import login_user, current_user, logout_user

from .forms import CheckMatricForm, LoginForm, CreatePasswordForm

from eusoffline.models import BaseUser
from eusoffline import db

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def mainHome():
    print(current_user)
    return render_template('/main/index.html')


@main.route("/login/matriccheck", methods=['GET', 'POST'])
def mainCheckMatric():
    matric_form = CheckMatricForm()

    # Matric form validation
    if matric_form.validate_on_submit():
        requesting_user = BaseUser.query.filter_by(
            matric=matric_form.matric.data).first()

        # if no such matric
        if (requesting_user is None):
            flash('Matric number not found.', 'danger')
        # matric exists
        elif (requesting_user is not None):
            # if firsttime user, redirect to set up page
            if(requesting_user.password is not None):

                return redirect(url_for('main.mainLogin',
                                        username=requesting_user.name,
                                        matric=requesting_user.matric))

            # if already registered
            elif(requesting_user.password is None):
                return redirect(url_for('main.mainCreatepassword',
                                        username=requesting_user.name,
                                        matric=requesting_user.matric))

            # errors
            else:
                print("Some error")
        else:
            flash('Some login error has occured.', 'danger')

    return render_template('/main/checkMatric.html',
                           form=matric_form)


@main.route("/login/createpassword/<username>/<matric>",
            methods=['GET', 'POST'])
def mainCreatepassword(username, matric):
    create_password_form = CreatePasswordForm()

    # Matric form validation
    if create_password_form.validate_on_submit():
        password1 = create_password_form.new_password.data
        password2 = create_password_form.re_password.data

        # check if two inputs are equal
        if (password1 != password2):
            flash('The passwords entered are not the same', 'danger')

        # not 6 digit
        elif (len(password1) != 6):
            flash('passwords have to be 6 digits', 'danger')

        # not pure numbers
        elif (not password1.isdigit()):
            flash('passwords have to contain only numbers', 'danger')

        # update databse
        else:
            db.session.query(BaseUser).filter_by(matric=matric).update(
                {BaseUser.password: password1}, synchronize_session=False)

            db.session.commit()
            return redirect(url_for('main.mainLogin', username=username,
                                    matric=matric))

    return render_template('/main/createPassword.html',
                           form=create_password_form,
                           username="meh")


@main.route("/login/<username>/<matric>", methods=['GET', 'POST'])
def mainLogin(username, matric):
    login_form = LoginForm()

    # Matric form validation
    if login_form.validate_on_submit():
        requesting_user = BaseUser.query.filter_by(
            matric=login_form.matric.data).first()

        # if no such matric
        if (requesting_user.password == login_form.password.data):
            login_user(requesting_user)
            return redirect(url_for('main.mainHome'))
        else:
            flash('Wrong password!', 'danger')

    return render_template('/main/login.html',
                           form=login_form)


@main.route("/logout", methods=['GET'])
def mainLogout():
    logout_user()
    return redirect(url_for('main.mainHome'))

