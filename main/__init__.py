from flask import Flask,Blueprint,request
import MySQLdb as SQL
import jwt
app = Flask(__name__)

from main.controller import login

app.register_blueprint(login.auth)