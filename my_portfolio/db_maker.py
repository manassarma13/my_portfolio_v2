from my_portfolio import db
from my_portfolio.models import Users

db.drop_all()
db.create_all()