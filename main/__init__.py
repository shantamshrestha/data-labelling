from flask import Flask,Blueprint,request
import MySQLdb as SQL

app = Flask(__name__)

db = SQL.connect(host="localhost",user="shantam",passwd="password",db="Project1")

cursor = db.cursor()
