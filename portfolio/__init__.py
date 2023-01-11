from flask import Flask
app=Flask(__name__)
app.config['SECRET_KEY'] = '4f7139f0c16c908724a1d3085c9122ba763ccf775c5bd53f'

from portfolio import routes

