from email.mime import application
from flask import Flask, jsonify, request, render_template
from flask import Flask
application=Flask(__name__)
from OpenSSL import SSL
context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
context.use_privatekey_file('server.key')
context.use_certificate_file('server.crt')   

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
        return jsonData
    hello="world"
    return hello
application.run(ssl_context=("cert.pem", "key.pem"))

