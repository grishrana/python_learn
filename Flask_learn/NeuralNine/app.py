from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

@app.route('/hello', methods=['POST','GET'])
def hello():
    if request.method=='GET':
        return 'You made a GET request'
    elif request.method=="POST":
        return "You Made a POST request"
    else:
        return "You will never see this message.\n"

@app.route('/statusCode')
def statusCode():
    response = make_response("Hello world")
    response.status_code = 200
    response.headers['content-type']="text/plain"
    return response

@app.route('/greet/<name>', methods=['POST','GET'])
def greet(name):
    return (f"Hello {name}")

@app.route('/add/<int:n1>/<int:n2>')
def add(n1,n2):
    return f"{n1}+{n2}={n1+n2}"

@app.route('/handle_url_params')
def handle_params():
    if('greeting' in request.args.keys()) & ('name' in request.args.keys()):
        greeting = request.args['greeting']
        name = request.args['name']
        return f"Hello {name}"

    else:
        return "Some parameters are missing."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555,debug=True)
