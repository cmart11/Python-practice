from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index'


@app.route('/hello')
def hello_world():
    return f'Hello World!'
