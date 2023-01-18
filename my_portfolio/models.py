from my_portfolio import db
from sqlalchemy.dialects.mysql import LONGTEXT
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import check_password_hash,generate_password_hash

# Create Model
class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message =db.Column(db.String(200), nullable=False)
    date_added=db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, email, message):
        self.name=name
        self.email=email
        self.message=message


class SuperUser(UserMixin, db.Model):
    __tablename__="super_user"

    id=db.Column(db.Integer, primary_key=True)
    user_name=db.Column(db.String(10), nullable=False)
    #password=db.Column(LONGTEXT, nullable=False)
    password=db.Column(db.String(100), nullable=False)
    

    def __init__(self, user_name, password):
        self.user_name=user_name
        self.password=generate_password_hash(password)

    def check_pass(self,password):
        return check_password_hash(self.password,password) 