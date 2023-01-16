from my_portfolio import db
from datetime import datetime

# Create Model
class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    message =db.Column(db.String(200), nullable=False, unique=True)
    date_added=db.Column(db.DateTime, default=datetime.utcnow)
