from main import *
from main.models.user import login

auth = Blueprint('Auth',__name__,url_prefix='/auth')

# @auth.route('/',methods=['GET'])
# def home():
#     return "Hello"

@auth.route('/',methods=['POST'])
def c_login():
    data = request.json
    # print(data)
    username = data['username']
    password = data['password']
    id = login(username,password)

    if not id:
        print("here")
        return "Invalid username or password",400
    token = jwt.encode({'user_id':id},app.config['SECRET_KEY'])

    print(token)
    return "%s" % token,200

@auth.route('/home/')
def home():
    return render_template("index.html")