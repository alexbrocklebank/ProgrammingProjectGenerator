from flask import Flask
app = Flask(__name__)

@app.route('/')
def initial():
    return 'Hello World!'