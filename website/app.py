from flask import Flask

from website.api.course.views import course
from website.api.user.views import user

from website.extensions import db


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

    extensions(app)

    return app


def extensions(app):

    db.init_app(app)

    return None
