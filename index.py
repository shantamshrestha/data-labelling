from main import *

# app.config['HOST'] = '0.0.0.0'
data = []
def dataRequest():
    global data
    print("Here")
    data = request.json
    print(data['email'])

@app.route('/',methods=['GET'])
def home():
    return "homes"
    
@app.route('/',methods=['POST'])
def login():
    try:
        dataRequest()
        print(data)
        return "data",200
    except :
        return "Something went wrong"
if __name__ == '__main__':
    app.run(debug=True)

