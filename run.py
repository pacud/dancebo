#!/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect,
)
from werkzeug.exceptions import Forbidden


#init config
config = ConfigParser.SafeConfigParser()
config.read('config.ini')
app = Flask(config.get('dancebo', 'app_name'))
app.secret_key = config.get('dancebo', 'secret_key')
debug = bool(config.get('dancebo', 'debug'))
password = config.read('debug_pass')


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', user=session['name'])


@app.route('/inscription', methods=['GET'])
def inscription():
    return render_template('inscription.html', user=session['name'])


@app.route('/cartes', methods=['GET'])
def cartes():
    return render_template('cartes.html', user=session['name'])


@app.route('/trombi', methods=['GET'])
def trombi():
    return render_template('trombi.html', user=session['name'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print request.form
        # if not password == request.form['password']:
        #     raise Forbidden('You don\'t have access to this ressource')
        session['name'] = request.form['login']
        return redirect('/home')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=debug)
