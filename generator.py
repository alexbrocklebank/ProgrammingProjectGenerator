from flask import Flask, request, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='Random Programming Project Generator')

@app.route('/idea/<idea_id>')
def show_idea(idea_id):
    # Get Idea from db
    return 'Idea'

if __name__ == "__main__":
    app.run(debug=True)