# coding: utf8
import json
import datetime
from flask import (
    render_template,
    request,
    redirect,
    Response,
    current_app,
)
from flask.views import View
from validators import removal_validator
from cerberus import ValidationError

LESSON_LIST = [
    {
        'id': 1,
        'title': u"Cours débutant",
        'start': datetime.datetime(year=2015, month=8, day=13, hour=19, minute=30),
        'end': datetime.datetime(year=2015, month=8, day=13, hour=21, minute=0),
        'allDay': False,
        'url': u"/add_presence/1",
        'recurring': 1,
    },
    {
        'id': 2,
        'title': u"Cours intermédiaire",
        'start': datetime.datetime(year=2015, month=8, day=13, hour=21, minute=0),
        'end': datetime.datetime(year=2015, month=8, day=13, hour=22, minute=30),
        'allDay': False,
        'url': u"/add_presence/2",
        'recurring': 2,
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
        response = Response(
            json.dumps(lesson_list),
            status=200,
            mimetype='application/json'
        )
        return response

    def add_one(self):
        if request.method == 'GET':
            return render_template(
                'edit_lesson.html',
                current_page='presence'
            )
        return redirect('/presence')

    def chose(self):
        if request.method == 'GET':
            return render_template(
                'chose_lesson.html',
                current_page="presence",
                lesson_list=LESSON_LIST
            )
        # TODO: extraire l'id du cours du résultat du formulaire
        lesson_id = 1
        return redirect('/edit_lesson/{}'.format(lesson_id))

    def edit(self, lesson_id):
        lesson_list = LESSON_LIST
        lesson = None
        for lesson in lesson_list:
            if lesson['id'] == lesson_id:
                break
        # TODO: Gérer le cas où le cours n'est pas trouvé
        return render_template(
            'edit_lesson.html',
            current_page='presence',
            lesson=lesson
        )

    def add_presence(self, lesson_id):
        from student import USER_LIST
        student_list = USER_LIST
        i = 0
        for student in student_list:
            student['participated'] = True if i % 2 == 1 else False
            i += 1
        return render_template(
            'add_presence.html',
            current_page='presence',
            lesson_id=lesson_id,
            students=student_list
        )

    def remove_presence(self):
        data = request.get_json(force=True)
        try:
            removal_validator.validate(data)
        except ValidationError as e:
            response = Response(
                json.dumps({'status': e.message}),
                status=400,
                mimetype='application/json'
            )
            return response
        # TODO: handle the actual remove
        response = Response(
            json.dumps({'status': 'ok'}),
            status=200,
            mimetype='application/json'
        )
        return response
