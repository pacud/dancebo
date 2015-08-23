# coding: utf8
from cerberus import Validator


removal_schema = {
    'student_id': {'required': True, 'type': 'integer'},
    'lesson_id': {'required': True, 'type': 'integer'},
}
removal_validator = Validator(removal_schema)
