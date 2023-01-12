from flask import Flask, render_template, url_for, redirect, request

app=Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')