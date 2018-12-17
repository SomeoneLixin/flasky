# from flask import Flask
# from flask import request, make_response, redirect, abort, url_for, render_template
# from flask_script import Manager
# import config
#
#
# app = Flask(__name__)
# app.config.from_object(config)
# manager = Manager(app)
#
# @app.route('/')
# def index():
#     # user_agent = request.headers.get('User-Agent')
#     # return '<p>Your Browser is %s</p>' % user_agent
#     # response = make_response('<h1>This document carries a cookie!</h1>')
#     # response.set_cookie('answer', '42')
#     # return response
#     # print (url_for('get_user', id='1'))
#     # print (url_for('user', name='wanglixin'))
#     # return 'Hello world!'
#     # login_url = url_for('login')
#     # return redirect(login_url)
#     context = {
#         'username' : '知了课堂',
#         'gender' : '男',
#         'age' : '18',
#     }
#     return render_template('index.html', **context)
#
# @app.route('/login/')
# def login():
#     return 'This is login page.'
#
# @app.route('/question/<is_login>/')
# def question(is_login):
#     if is_login =='1':
#         return 'This is question page'
#     else:
#         login_url = url_for('login')
#         return redirect(login_url)
#
# @app.route('/user/<id>')
# def get_user(id):
#     # user = load_user(id)
#     # if not user:
#     #     abort(404)
#     return '<h1>Hello %s!</h1>' % id
#
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello %s!</h1>' % name
#
# if __name__ == '__main__':
#     manager.run()




"""

    按照章节顺序尝试

"""

from flask import Flask, render_template, session, redirect, url_for, flash
# from flask import request, make_response, redirect, abort
# from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)
# manager = Manager(app)

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    # return '<h1>Hello World!</h1>'

    # user_agent = request.headers.get('User-Agent')
    # return '<p>Your browser is %s</p>' % user_agent

    # response = make_response('<h1>This document carries a cookie!</h1>')
    # response.set_cookie('answer', '42')
    # return response

    # return redirect('http://www.example.com')

    # name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))

    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# @app.route('/user/<id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hello %s!</h1>' % user.name


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
    # manager.run()