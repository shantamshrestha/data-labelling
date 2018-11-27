from flask import Flask,Blueprint,request
import MySQLdb as SQL
import jwt
app = Flask(__name__)

from main.controller.login import auth

app.register_blueprint(auth)