from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class CheckMatricForm(FlaskForm):
    matric = StringField('Matric Number', validators=[DataRequired()])
    submit = SubmitField('Login')


class CreatePasswordForm(FlaskForm):
    new_password = PasswordField('6 digit pin', validators=[DataRequired()])
    re_password = PasswordField(
        'Re-enter 6 digit pin', validators=[DataRequired()])
    submit = SubmitField('Update')


class LoginForm(FlaskForm):
    matric = StringField('Matric Number', validators=[DataRequired()])
    password = PasswordField('6 digit pin', validators=[DataRequired()])
    submit = SubmitField('Login')
