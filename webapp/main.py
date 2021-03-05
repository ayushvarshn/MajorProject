import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template, url_for, request, make_response, flash, redirect

application = Flask(__name__)
random.seed()  # Initialize the random number generator
application.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@application.route('/', methods=['GET', 'POST'])
def index():
    username = request.cookies.get('username')
    if username:
        return render_template('main.html', username=username)
    return render_template('main.html')

@application.route('/login', methods=['GET', 'POST'])
def login():
    username = request.cookies.get('username')
    if username:
        return render_template('user.html', username=username)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043':
            flash("Successful login", "success")
            resp = make_response(redirect('/'))
            resp.set_cookie('username', username)
            return resp
        else:
            flash("Wrong username or password", "danger")
    return render_template('login.html')


@application.route('/home', methods=['GET', 'POST'])
def home():
    username = request.cookies.get('username')
    if username:
        return render_template('home.html', username=username)
    return redirect('/')

@application.route('/temperature', methods=['GET', 'POST'])
def temp():
    username = request.cookies.get('username')
    if username:
        return render_template('temp.html', username=username)
    return redirect('/')


@application.route('/voltage', methods=['GET', 'POST'])
def voltage():
    username = request.cookies.get('username')
    if username:
        return render_template('voltage.html', username=username)
    return redirect('/')


@application.route('/soc', methods=['GET', 'POST'])
def soc():
    username = request.cookies.get('username')
    if username:
        return render_template('soc.html', username=username)
    return redirect('/')


@application.route('/soh', methods=['GET', 'POST'])
def soh():
    username = request.cookies.get('username')
    if username:
        return render_template('soh.html', username=username)
    return redirect('/')


@application.route('/chart-data', methods=['GET', 'POST'])
def chart_data():
    def generate_random_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%M:%S'), 'temp': random.randint(290, 310)/10, 'voltage': random.randint(25, 35)/10, 'soc': random.randint(90, 100), 'soh': random.randint(90, 100)})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(generate_random_data(), mimetype='text/event-stream')


@application.route('/user', methods=['GET', 'POST'])
def user():
    username = request.cookies.get('username')
    if username:
        return render_template('user.html', username=username)
    return redirect('/')

@application.route('/logout', methods=['GET'])
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('username')
    return resp


if __name__ == '__main__':
    application.run(debug=True, threaded=True)
