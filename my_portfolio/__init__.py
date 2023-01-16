from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, redirect, request

from my_portfolio.forms import add_users

# App

app=Flask(__name__)
app.config["SECRET_KEY"]='DSFCDSF'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"

db=SQLAlchemy(app)

with app.app_context():
    db.create_all()
    



@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/contact.html')
def contact():
    form = add_users()
    return render_template('contact.html',form=form)

@app.route('/submit_form', methods= ['GET', 'POST'])
def submit():
    return "form submitted"

@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')

# from my_portfolio import server