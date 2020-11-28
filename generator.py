from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Page'

@app.route('/idea/<idea_id>')
def show_idea(idea_id):
    # Get Idea from db
    return 'Idea'
