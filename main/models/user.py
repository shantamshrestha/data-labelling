from main import db

class User(db.model):
    __tablename__ = 'Users'
    id = db.Column('id',db.Interger, primary_key = True)
    username = db.Column('username',db.String)
    password = db.Column('password',db.String)