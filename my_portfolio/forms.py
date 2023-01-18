from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, \
    TextAreaField
from wtforms.validators import DataRequired

class add_users(FlaskForm):
    name=StringField("NAME:", validators=[DataRequired()])
    email=EmailField("EMAIL:", validators=[DataRequired()])
    message=TextAreaField("MESSAGE:", validators=[DataRequired()])
    submit=SubmitField("Sumbit")

class Login(FlaskForm):
    user_name=StringField("NAME:", validators=[DataRequired()])
    password=PasswordField("PASSWORD:", validators=[DataRequired()])
    submit=SubmitField("Submit")


class Register(FlaskForm):
    user_name=StringField("NAME:", validators=[DataRequired()])
    password=PasswordField("PASSWORD:", validators=[DataRequired()])
    submit=SubmitField("Submit")