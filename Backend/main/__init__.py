from flask import Flask,Blueprint,request
from flask_cors import CORS
import MySQLdb as SQL
import jwt
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'letitbe'

from main.controller.login import auth

app.register_blueprint(auth)