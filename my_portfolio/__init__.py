from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, redirect, request, flash
from flask_login import LoginManager, login_user, login_required, \
    logout_user, current_user

db=SQLAlchemy()

from my_portfolio.forms import add_users, Login, Register
from my_portfolio.models import Users, SuperUser
# App

app=Flask(__name__)
app.config["SECRET_KEY"]='Y5Gj8iT"NxpU(My8'

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://c22107670:UwDXDVR+Ky0T@csmysql.cs.cf.ac.uk:3306/c22107670_flask_cw2"



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
    ################
    temp = SuperUser('sauronil','darkfire')
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
            return redirect(url_for('messages'))
    return render_template('login.html',form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form=Register()
    if form.validate_on_submit():
        temp = SuperUser(form.user_name.data,form.password.data)
        db.session.add(temp)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html',form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("./404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("./500.html"), 500

@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    form=add_users()
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
    message_data=Users.query.all()
    return render_template('messages.html', messages=message_data)

@app.route('/delete/<id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    del_id=Users.query.get(id)
    db.session.delete(del_id)
    db.session.commit()
    flash("Message Details Deleted Successfully")
    return redirect(url_for('messages'))
    


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))