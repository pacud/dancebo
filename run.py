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
    return render_template('home.html')


@app.route('/inscription', methods=['GET'])
def inscription():
    return render_template('inscription.html')


@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.form
    student = {
        'firstname': data.get('firstname'),
        'lastname': data.get('lastname'),
        'profile_pic': '',
        'birth_date': data.get('birthdate'),
        'email': data.get('email'),
        'mobile': data.get('mobile'),
        'card_type': data.get('card_type'),
        'paiment_method': data.get('paiment_method'),
        'medical_certificate': data.get('medical_certificate', 0),
        'inscription_paid': data.get('inscription_paid', 0),
    }
    return render_template('profile.html', student=student)


@app.route('/cartes', methods=['GET'])
def cartes():
    return render_template('cartes.html')


@app.route('/trombi', methods=['GET'])
def trombi():
    tmp_profile_pic = 'file:///devel/dancebo/images/64184.jpg'
    user_list = [
        {
            'id': 1,
            'firstname': u'Coco',
            'lastname': u'Nut',
            'mobile': u'0612345789',
            'valid': 1,
            'lessons_left': 5,
            'profile_pic': tmp_profile_pic,
        },
        {
            'id': 2,
            'firstname': u'Pea',
            'lastname': u'Nut',
            'mobile': u'0123456789',
            'valid': 1,
            'lessons_left': 2,
            'profile_pic': tmp_profile_pic,
        },
        {
            'id': 3,
            'firstname': u'Wall',
            'lastname': u'Nut',
            'mobile': u'0033412356789',
            'valid': 1,
            'lessons_left': 1,
            'profile_pic': tmp_profile_pic,
        },
        {
            'id': 4,
            'firstname': u'Hairy',
            'lastname': u'Nut',
            'mobile': u'0712345689',
            'valid': 0,
            'lessons_left': 0,
            'profile_pic': tmp_profile_pic,
        },
    ]
    return render_template(
        'trombi.html',
        user_list=user_list
    )


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
