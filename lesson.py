# coding: utf8
import json
import datetime
from flask import (
    render_template,
    request,
)
from flask.views import View

LESSON_LIST = [
    {
        'id': 1,
        'title': u"Cours débutant",
        'start': datetime.datetime(year=2015, month=8, day=13, hour=19, minute=30),
        'end': datetime.datetime(year=2015, month=8, day=13, hour=21, minute=0),
        'allDay': False,
        'url': u"/add_presence/1"
    },
    {
        'id': 2,
        'title': u"Cours intermédiaire",
        'start': datetime.datetime(year=2015, month=8, day=13, hour=21, minute=0),
        'end': datetime.datetime(year=2015, month=8, day=13, hour=22, minute=30),
        'allDay': False,
        'url': u"/add_presence/2"
    },
]


class Lesson(View):

    def get_presence(self):
        return render_template('presence.html', current_page="presence")

    def list_lessons(self):
        start_filter = request.args.get('start')
        end_filter = request.args.get('end')
        start_filter = datetime.datetime.strptime(start_filter, '%Y-%m-%d')
        end_filter = datetime.datetime.strptime(end_filter, '%Y-%m-%d')
        lesson_list = []
        for lesson in LESSON_LIST:
            lesson_ready = lesson
            lesson_ready['start'] = str(lesson_ready['start'])
            lesson_ready['end'] = str(lesson_ready['end'])
            lesson_list.append(lesson_ready)
        return json.dumps(lesson_list)

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
