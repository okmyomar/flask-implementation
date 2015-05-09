from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Gabriela'}
    posts = [
        {
            'author': {'nickname': 'bragerson'},
            'body': 'Beautiful day in the beach babies'
        },
        {
            'author': {'nickname': 'andersonsss'},
            'body': 'The magic things of the big trick'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
