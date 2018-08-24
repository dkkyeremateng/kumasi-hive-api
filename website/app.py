from flask import Flask

from website.api.course.views import course
from website.api.user.views import user
from website.api.student.views import student

from website.extensions import db
from website.extensions import cors


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

    @app.route('/')
    def index_page():
        return 'Kumasi Hive Academy App API'

    app.register_blueprint(course)
    app.register_blueprint(user)
    app.register_blueprint(student)

    extensions(app)

    return app


def extensions(app):

    db.init_app(app)
    cors.init_app(app)

    return None
