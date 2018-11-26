from main import app

# app.config['HOST'] = '0.0.0.0'
app.config['SQLALCHEMY_DATABASE_URI'] = mysql://root:password@localhost/Project1
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)