from email.mime import application
from flask import Flask
application=Flask(__name__)

@application.route('/')
def helloWorld():
    return "hello world"