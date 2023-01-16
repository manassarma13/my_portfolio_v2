from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired

class add_users(FlaskForm):
    name=wtforms.StringField("name", validators=[DataRequired()])
    email=wtforms.StringField("email", validators=[DataRequired()])
    message=wtforms.StringField("message", validators=[DataRequired()])
    sumbit=wtforms.SubmitField("Sumbit")