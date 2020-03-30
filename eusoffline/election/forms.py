from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import InputRequired


class TestForm(FlaskForm):
    votes = SelectField(label='Vote', validators=[
                        InputRequired()], choices=[('yes', 'yes'), ('no', 'no')])
    submit = SubmitField('Submit')
