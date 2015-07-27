# coding:utf8
from flask import render_template


class Student(object):

    profile = {}

    def __init__(self, profile):
        for k, v in profile.iteritems():
            self.profile[k] = v

    def show_profile(self):
        return render_template('profile.html', student=self.profile)
