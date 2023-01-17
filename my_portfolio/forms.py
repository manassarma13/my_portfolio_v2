from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired

class add_users(FlaskForm):
    name=StringField("NAME", validators=[DataRequired()])
    email=EmailField("EMAIL", validators=[DataRequired()])
    message=StringField("MESSAGE", validators=[DataRequired()])
    submit=SubmitField("Sumbit")

class Login(FlaskForm):
    user_name=StringField("NAME", validators=[DataRequired()])
    password=PasswordField("PASSWORD", validators=[DataRequired()])
    submit=SubmitField("Sumbit")
