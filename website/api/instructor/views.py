from flask import Blueprint

from website.api.instructor.api import InstructorAPI

instructor = Blueprint('instructor', __name__, url_prefix='/api')

instructor_view = InstructorAPI.as_view('student_api')

instructor.add_url_rule('/students/',
                        defaults={'external_id': None},
                        view_func=instructor_view,
                        methods=['GET', 'OPTIONS'])

instructor.add_url_rule('/students/',
                        view_func=instructor_view,
                        methods=['POST'])

instructor.add_url_rule('/students/<external_id>',
                        view_func=instructor_view,
                        methods=['GET', 'DELETE', 'PUT'])
