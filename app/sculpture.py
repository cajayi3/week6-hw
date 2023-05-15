from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class SealsixStructure(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sealsix')

class MajorStructure(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sealsix')

class PostStructure(FlaskForm):
    body = StringField('body', validators=[DataRequired()])
    submit = SubmitField('Publish')

class OverSearchStructure(FlaskForm):
    user = StringField('user', validators=[DataRequired()])
    submit = SubmitField('Search')