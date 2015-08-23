# coding: utf8
import datetime
from user import UserModel


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


class LessonModel(object):

    def list(self, start_filter=None, end_filter=None, json_ready=False):
        lesson_list = LESSON_LIST
        if json_ready is True:
            original_lesson_list = lesson_list
            lesson_list = []
            for lesson in original_lesson_list:
                lesson_ready = lesson
                lesson_ready['start'] = str(lesson_ready['start'])
                lesson_ready['end'] = str(lesson_ready['end'])
                lesson_list.append(lesson_ready)
        return lesson_list

    def get_by_id(self, lesson_id):
        lesson = None
        for lesson in self.list():
            if lesson['id'] == lesson_id:
                break
        return lesson

    def list_student_in_lesson(self, lesson_id):
        student_list = UserModel().list()
        i = 0
        for student in student_list:
            student['participated'] = True if i % 2 == 1 else False
            i += 1
        return student_list
