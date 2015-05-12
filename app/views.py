from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'nickname': 'Gabriela'}
#     posts = [
#         {
#             'author': {'nickname': 'bragerson'},
#             'body': 'Beautiful day in the beach babies'
#         },
#         {
#             'author': {'nickname': 'andersonsss'},
#             'body': 'The magic things of the big trick'
#         }
#     ]
#     return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('You are in man!! OpenId=%s, remember_me=%s' %
            (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')

    return render_template('login.html',
                            title='Sign in',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])
