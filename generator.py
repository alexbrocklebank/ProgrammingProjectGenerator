from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/idea/<idea_id>')
def show_idea(idea_id):
    # Get Idea from db
    return 'Idea'
