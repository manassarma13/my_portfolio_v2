from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class add_users(FlaskForm):
    name=StringField("name", validators=[DataRequired()])
    email=StringField("email", validators=[DataRequired()])
    message=StringField("message", validators=[DataRequired()])
    submit=SubmitField("Sumbit")

class Login(FlaskForm):
    user_name=StringField("name", validators=[DataRequired()])
    password=StringField("pass", validators=[DataRequired()])
    submit=SubmitField("Sumbit")
