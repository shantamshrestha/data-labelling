from flask import Flask

app = Flask(__name__)
# app.config['HOST'] = '0.0.0.0'

@app.route('/')
# @app.route('/home')
def hello():
    return "Hello"

@app.route('/home')
def home():
    return "Home"

if __name__ == '__main__':
    app.run(debug=True)