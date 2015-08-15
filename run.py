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
from student import Student


tmp_profile_pic = 'http://img15.hostingpics.net/pics/811484defaultavatar.png'
USER_LIST = [
    {
        'id': 1,
        'firstname': u'Coco',
        'lastname': u'Nut',
        'mobile': u'0612345789',
        'cart_paid': 1,
        'lessons_left': 5,
        'profile_pic': tmp_profile_pic,
        'medical_certificate': 0,
    },
    {
        'id': 2,
        'firstname': u'Pea',
        'lastname': u'Nut',
        'mobile': u'0123456789',
        'cart_paid': 1,
        'lessons_left': 2,
        'profile_pic': tmp_profile_pic,
        'medical_certificate': 1,
    },
    {
        'id': 3,
        'firstname': u'Wall',
        'lastname': u'Nut',
        'mobile': u'0033412356789',
        'cart_paid': 1,
        'lessons_left': 1,
        'profile_pic': tmp_profile_pic,
        'medical_certificate': 1,
    },
    {
        'id': 4,
        'firstname': u'Hairy',
        'lastname': u'Nut',
        'mobile': u'0712345689',
        'cart_paid': 0,
        'lessons_left': 0,
        'profile_pic': tmp_profile_pic,
        'medical_certificate': 1,
    },
]


# init config
config = ConfigParser.SafeConfigParser()
config.read('config.ini')
app = Flask(config.get('dancebo', 'app_name'))
app.secret_key = config.get('dancebo', 'secret_key')
debug = bool(config.get('dancebo', 'debug'))
password = config.read('debug_pass')


@app.route('/', methods=['GET', 'POST'])
def root():
    return redirect('/login')


@app.route('/home', methods=['GET'])
def home():
    return render_template('home.html', current_page="home")


@app.route('/inscription', methods=['GET'])
def inscription():
    return render_template('inscription.html', current_page="inscription")


@app.route('/search', methods=['POST'])
def search():
    search_terms = request.form
    user_list = USER_LIST
    matches = []
    for user in user_list:
        if search_terms['lastname'] == user['lastname']\
                and search_terms['firstname'] == user['firstname']:
            matches.append(user)
    return render_template(
        'search_results.html',
        matches=matches,
        current_page="cartes"
    )


@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.form
    profile = {
        'title': data.get('title'),
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
        'amount': data.get('amount', 0),
        'origin': data.get('origin', '').split(','),
        'origin_other_social': data.get('origin_other_social'),
        'origin_hearsay': data.get('origin_hearsay'),
        'origin_other': data.get('origin_other'),
        'favorite_chanel': data.get('favorite_chanel', '').split(','),
    }
    student = Student(profile)
    return student.show_profile()


@app.route('/presence', methods=['GET'])
def presence():
    return render_template('presence.html', current_page="presence")


@app.route('/cartes', methods=['GET'])
def cartes():
    user_list = USER_LIST
    return render_template(
        'cartes.html',
        user_list=user_list,
        current_page="cartes"
    )


@app.route('/carte_detail/<int:student_id>', methods=['GET'])
def carte_detail(student_id):
    profile = {}
    for student in USER_LIST:
        if student['id'] == student_id:
            profile = student
            break
    student = Student(profile)
    return student.show_profile()


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('name'):
        return redirect('/home')
    if request.method == 'POST':
        print request.form
        # if not password == request.form['password']:
        #     raise Forbidden('You don\'t have access to this ressource')
        session['name'] = request.form['login']
        return redirect('/home')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=debug)
