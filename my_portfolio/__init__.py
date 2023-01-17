from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, Flask, render_template, url_for, redirect, request
from flask_login import LoginManager, login_user, login_required, \
    logout_user, current_user

db=SQLAlchemy()

from my_portfolio.forms import add_users, Login
from my_portfolio.models import Users, SuperUser
# App

app=Flask(__name__)
app.config["SECRET_KEY"]='DSFCDSF'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"


db.init_app(app)
login_manager=LoginManager()
login_manager.login_view='login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return SuperUser.query.get(int(user_id))

with app.app_context():
    db.create_all()
    temp = SuperUser('s@s.c','qwerty')
    db.session.add(temp)
    db.session.commit()
    
@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=Login()
    if form.validate_on_submit():
        su=SuperUser.query.filter_by(user_name=form.user_name.data).first()
        if su and su.check_pass(form.password.data):
            login_user(su,remember=False)
            return 'fghdjfk'
    return render_template('login.html',form=form)



@app.errorhandler(404)
def page_not_found(e):
    return render_template("./404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("./500.html"), 500

@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    form=add_users()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        users=Users(form.name.data, form.email.data, form.message.data)
        db.session.add(users)
        db.session.commit()
        return render_template('/submit.html',name=form.name.data)

    return render_template('contact.html',form=form)

@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')

@app.route('/messages')
@login_required
def messages():
    return render_template('messages.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))