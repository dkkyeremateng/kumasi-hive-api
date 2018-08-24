from flask import Flask, jsonify

from website.api.course.views import course
from website.api.user.views import user
from website.api.student.views import student
from website.api.instructor.views import instructor

from website.extensions import db
from website.extensions import cors

from website.api.course.schema import schema as course_schema
from website.api.student.schema import student_schema
from website.api.instructor.schema import instructor_schema
from website.api.user.schema import register_schema


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(course)
    app.register_blueprint(user)
    app.register_blueprint(student)
    app.register_blueprint(instructor)

    @app.route('/')
    def index_page():
        return 'Kumasi Hive Academy API'

    @app.route('/spec/courses')
    def courses_schema():
        return jsonify(course_schema)

    @app.route('/spec/students')
    def students_schema():
        return jsonify(student_schema)

    @app.route('/spec/users')
    def users_schema():
        return jsonify(register_schema)

    @app.route('/spec/instructors')
    def instructors_schema():
        return jsonify(instructor_schema)

    extensions(app)

    return app


def extensions(app):

    db.init_app(app)
    cors.init_app(app)

    return None
