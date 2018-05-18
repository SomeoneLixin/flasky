from flask import Flask
from flask import request, make_response, redirect, abort, url_for, render_template
from flask_script import Manager
import config


app = Flask(__name__)
app.config.from_object(config)
manager = Manager(app)

@app.route('/')
def index():
    # user_agent = request.headers.get('User-Agent')
    # return '<p>Your Browser is %s</p>' % user_agent
    # response = make_response('<h1>This document carries a cookie!</h1>')
    # response.set_cookie('answer', '42')
    # return response
    # print (url_for('get_user', id='1'))
    # print (url_for('user', name='wanglixin'))
    # return 'Hello world!'
    # login_url = url_for('login')
    # return redirect(login_url)
    context = {
        'username' : '知了课堂',
        'gender' : '男',
        'age' : '18',
    }
    return render_template('index.html', **context)

@app.route('/login/')
def login():
    return 'This is login page.'

@app.route('/question/<is_login>/')
def question(is_login):
    if is_login =='1':
        return 'This is question page'
    else:
        login_url = url_for('login')
        return redirect(login_url)

@app.route('/user/<id>')
def get_user(id):
    # user = load_user(id)
    # if not user:
    #     abort(404)
    return '<h1>Hello %s!</h1>' % id

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name

if __name__ == '__main__':
    manager.run()