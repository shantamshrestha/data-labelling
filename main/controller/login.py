from main import *
from main.models.user import login

auth = Blueprint('Auth',__name__,url_prefix='/auth')

@auth.route('/',methods=['POST'])
def c_login():
    print("Here")
    print("Here")
    data = request.json()
    username = data['username']
    password = data['password']
    id = login(username,password)
    if not id:
        return "Invalid username or password"
    return "%s" % id

@auth.route('/home')
def home():
    return "Home"