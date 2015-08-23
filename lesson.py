# coding: utf8
from flask import render_template
from flask.views import View


class Lesson(View):

    def get_presence(self):
        return render_template('presence.html', current_page="presence")

    def add_one(self):
        return render_template(
            'add_lesson.html',
            current_page='presence'
        )

    def add_presence(self, lesson_id):
        return render_template(
            'add_presence.html',
            current_page='presence',
            lesson_id=lesson_id
        )
