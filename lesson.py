# coding: utf8
import json
import datetime
from flask import (
    render_template,
    request,
    redirect,
    Response,
)
from flask.views import View
from validators import removal_validator
from cerberus import ValidationError
from models.lesson import LessonModel


class Lesson(View):

    def get_presence(self):
        return render_template('presence.html', current_page="presence")

    def list_lessons(self):
        start_filter = request.args.get('start')
        end_filter = request.args.get('end')
        start_filter = datetime.datetime.strptime(start_filter, '%Y-%m-%d')
        end_filter = datetime.datetime.strptime(end_filter, '%Y-%m-%d')
        lesson_list = LessonModel().list(
            start_filter, end_filter, json_ready=True
        )
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
        # LessonModel().set()
        return redirect('/presence')

    def chose(self):
        if request.method == 'GET':
            return render_template(
                'chose_lesson.html',
                current_page="presence",
                lesson_list=LessonModel().list()
            )
        # TODO: extraire l'id du cours du résultat du formulaire
        lesson_id = 1
        return redirect('/edit_lesson/{}'.format(lesson_id))

    def edit(self, lesson_id):
        lesson = LessonModel().get_by_id(lesson_id)
        # TODO: Gérer le cas où le cours n'est pas trouvé
        # LessonModel().set()
        return render_template(
            'edit_lesson.html',
            current_page='presence',
            lesson=lesson
        )

    def add_presence(self, lesson_id):
        student_list = LessonModel().list_student_in_lesson(lesson_id)
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
        # LessonModel().remove_presence()
        response = Response(
            json.dumps({'status': 'ok'}),
            status=200,
            mimetype='application/json'
        )
        return response
