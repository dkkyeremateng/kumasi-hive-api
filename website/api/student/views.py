from flask import Blueprint

from website.api.student.api import StudentAPI

student = Blueprint('student', __name__, url_prefix='/api')

student_view = StudentAPI.as_view('student_api')

student.add_url_rule('/students/',
                     defaults={'external_id': None},
                     view_func=student_view,
                     methods=['GET', 'OPTIONS'])

student.add_url_rule('/students/',
                     view_func=student_view,
                     methods=['POST'])

student.add_url_rule('/students/<external_id>',
                     view_func=student_view,
                     methods=['GET', 'DELETE', 'PUT'])
