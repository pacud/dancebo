#!/usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
from flask import Flask
from student import Student
from misc import Misc
from lesson import Lesson


# init config
config = ConfigParser.SafeConfigParser()
config.read('config.ini')
app = Flask(config.get('dancebo', 'app_name'))
app.secret_key = config.get('dancebo', 'secret_key')
debug = bool(config.get('dancebo', 'debug'))
password = config.read('debug_pass')


# route config
app.add_url_rule('/', 'home_redirect', redirect_to='/login')
# misc endpoints
misc = Misc()
app.add_url_rule('/home', view_func=misc.show_home, methods=['GET'])
app.add_url_rule('/login', view_func=misc.login, methods=['GET', 'POST'])
# student related endpoints
student = Student()
app.add_url_rule(
    '/add_student', view_func=student.add_student, methods=['POST']
)
app.add_url_rule(
    '/inscription', view_func=student.view_inscription, methods=['GET']
)
app.add_url_rule('/search', view_func=student.search, methods=['POST'])
app.add_url_rule('/cartes', view_func=student.cartes, methods=['GET'])
app.add_url_rule(
    '/carte_detail/<int:student_id>', view_func=student.detail, methods=['GET']
)
# lesson related endpoints
lesson = Lesson()
app.add_url_rule('/presence', view_func=lesson.get_presence, methods=['GET'])
app.add_url_rule(
    '/add_lesson', view_func=lesson.add_one, methods=['GET', 'POST']
)
app.add_url_rule(
    '/chose_lesson', view_func=lesson.chose, methods=['GET', 'POST']
)
app.add_url_rule(
    '/edit_lesson/<int:lesson_id>',
    view_func=lesson.edit,
    methods=['GET', 'POST']
)
app.add_url_rule(
    '/add_presence/<int:lesson_id>',
    view_func=lesson.add_presence,
    methods=['GET', 'POST']
)
app.add_url_rule(
    '/remove_presence', view_func=lesson.remove_presence, methods=['POST']
)
app.add_url_rule(
    '/list_lessons', view_func=lesson.list_lessons, methods=['GET']
)


if __name__ == '__main__':
    app.run(debug=debug)
