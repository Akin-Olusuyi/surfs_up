from flask import Flask
app = Flask(__name__)

# create flask routes


@app.route('/')
def hello_world():
    return 'Hello world'
