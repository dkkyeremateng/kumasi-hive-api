from flask import Blueprint

from website.api.course.api import CourseAPI

course = Blueprint('course', __name__, url_prefix='/api')

course_view = CourseAPI.as_view('course_api')

course.add_url_rule('/courses/',
                    defaults={'course_id': None},
                    view_func=course_view,
                    methods=['GET'])

course.add_url_rule('/courses/',
                    view_func=course_view,
                    methods=['POST'])

course.add_url_rule('/courses/<course_id>',
                    view_func=course_view,
                    methods=['GET', 'PUT', 'DELETE'])
