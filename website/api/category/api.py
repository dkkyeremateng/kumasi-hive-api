from flask.views import MethodView
from flask import jsonify, request, abort
import datetime

from website.api.category.models import Category
from website.api.category.templates import course_obj, courses_obj


class CategoryAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET' and
                request.method != 'OPTIONS' and
                request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self):
        category = Category.find_by_status()

        response = {
            'result': 'ok',
            'categories': courses_obj(courses)
        }

        return jsonify(response)

    def post(self):
        category_json = request.json

        params = {
            'category_name': category_json.get('category_name')
        }

        category = Category(**params).save()

        response = {
            'result': 'ok',
            'category': course_obj(course)
        }

        return jsonify(response)
