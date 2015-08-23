# coding:utf8
from flask import (
    render_template,
    request,
)
from flask.views import View
from slugify import slugify


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


class Student(View):

    profile = {}

    def __init__(self, profile=None):
        if profile:
            self.load(profile)

    def load(self, profile):
        for k, v in profile.iteritems():
            self.profile[k] = v

    def show_profile(self):
        return render_template(
            'profile.html', student=self.profile, current_page='cartes'
        )

    def add_student(self):
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
            'lessons_left': 0,
        }
        self.load(profile)
        return self.show_profile()

    def view_inscription(self):
        return render_template('inscription.html', current_page="inscription")

    def search(self):
        search_terms = request.form
        user_list = USER_LIST
        matches = []
        search_last = slugify(search_terms['lastname'])
        search_first = slugify(search_terms['firstname'])
        for user in user_list:
            user_last = slugify(user['lastname'])
            user_first = slugify(user['firstname'])
            if search_last == user_last and search_first == user_first:
                matches.append(user)
        return render_template(
            'cartes.html',
            user_list=matches,
            current_page="cartes"
        )

    def cartes(self):
        user_list = USER_LIST
        return render_template(
            'cartes.html',
            user_list=user_list,
            current_page="cartes"
        )

    def detail(self, student_id):
        profile = {}
        for student in USER_LIST:
            if student['id'] == student_id:
                profile = student
                break
        student = Student(profile)
        return student.show_profile()
