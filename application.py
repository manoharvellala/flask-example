from email.mime import application
from flask import Flask, jsonify, request, render_template
from flask import Flask
application=Flask(__name__)

@application.route('/')
def helloWorld():
    return "hello world"
@application.route('/test', methods=['GET', 'POST'])
def testfn():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'Sucesss', 200

@application.route('/index', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        jsonData = request.get_json()
        print(jsonData)
        return {
            'response' : 'I am the response'
        }
    return "hello"