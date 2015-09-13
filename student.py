# coding: utf8
from flask import (
    render_template,
    request,
)
from flask.views import View
from models.user import UserModel


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
        amounts = [int(amount) for amount in data.get('amount').split(',')]
        profile = UserModel().add(
            title=data.get('title'),
            firstname=data.get('firstname'),
            lastname=data.get('lastname'),
            profile_pic='',
            birth_date=data.get('birthdate'),
            email=data.get('email'),
            mobile=data.get('mobile'),
            card_type=data.get('card_type'),
            paiment_method=data.get('paiment_method'),
            medical_certificate=data.get('medical_certificate', 0),
            inscription_paid=data.get('inscription_paid', 0),
            amount=amounts,
            origin=data.get('origin', '').split(','),
            origin_other_social=data.get('origin_other_social'),
            origin_hearsay=data.get('origin_hearsay'),
            origin_other=data.get('origin_other'),
            favorite_chanel=data.get('favorite_chanel', '').split(',')
        )
        self.load(profile)
        return self.show_profile()

    def view_inscription(self):
        return render_template('inscription.html', current_page="inscription")

    def search(self):
        search_terms = request.form
        lastname = search_terms['lastname']
        firstname = search_terms['firstname']
        matches = UserModel().search(firstname, lastname)
        return render_template(
            'cartes.html',
            user_list=matches,
            current_page="cartes"
        )

    def cartes(self):
        user_list = UserModel().list()
        return render_template(
            'cartes.html',
            user_list=user_list,
            current_page="cartes"
        )

    def detail(self, student_id):
        profile = UserModel().get_by_id(student_id)
        student = Student(profile)
        return student.show_profile()
