from flask import Flask,Blueprint,request
import MySQLdb as SQL
import jwt
app = Flask(__name__)
app.config['SECRET_KEY'] = 'letitbe'

from main.controller.login import auth

app.register_blueprint(auth)