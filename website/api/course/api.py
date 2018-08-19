from flask.views import MethodView
from flask import jsonify, request, abort

from jsonschema import Draft4Validator
from jsonschema.exceptions import best_match
import datetime
import uuid

from website.api.course.models import Course
from website.api.course.templates import course_obj, courses_obj
from website.api.course.schema import schema


class CourseAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET' and
                request.method != 'OPTIONS' and
                request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self, course_id):

        if course_id:
            course = Course.find_by_id(course_id)

            if course:
                response = {
                    'result': 'ok',
                    'course': course_obj(course)
                }
                return jsonify(response), 200
            else:
                return jsonify({}), 404
        else:
            courses = Course.find_by_status(is_completed=False)

            response = {
                'result': 'ok',
                'courses': courses_obj(courses)
            }

            return jsonify(response), 200

    def post(self):
        course_json = request.json

        error = best_match(Draft4Validator(schema).iter_errors(course_json))

        if error:
            return jsonify({"error": error.message}), 400
        else:
            starting_date = datetime.datetime.strptime(
                course_json.get('starting_date'), "%Y-%m-%dT%H:%M:%SZ")

            ending_date = datetime.datetime.strptime(
                course_json.get('ending_date'), "%Y-%m-%dT%H:%M:%SZ")

            external_id = str(uuid.uuid4())

            params = {
                'title': course_json.get('title'),
                'description': course_json.get('description'),
                'duration': course_json.get('duration'),
                'starting_date': starting_date,
                'ending_date': ending_date,
                'user_id': course_json.get('user_id'),
                'display_picture': course_json.get('display_picture'),
                'requirements': course_json.get('requirements'),
                'what_you_will_learn': course_json.get('what_you_will_learn'),
                'curriculum': course_json.get('curriculum'),
                'target_audience': course_json.get('target_audience'),
                'external_id': external_id
            }

            try:
                course = Course(**params).save()
            except Exception as e:
                return jsonify({"error": e}), 400

            response = {
                'result': 'ok',
                'course': course_obj(course)
            }

            return jsonify(response)

    def put(self, course_id):

        course = Course.objects.filter(
            external_id=course_id, is_live=True).first()

        if not course:
            return jsonify({}), 404

        course_json = request.json

        error = best_match(Draft4Validator(schema).iter_errors(course_json))

        if error:
            return jsonify({"error": error.message}), 400
        else:
            starting_date = datetime.datetime.strptime(
                course_json.get('starting_date'), "%Y-%m-%dT%H:%M:%SZ")

            ending_date = datetime.datetime.strptime(
                course_json.get('ending_date'), "%Y-%m-%dT%H:%M:%SZ")

            course.title = course_json.get('title')
            course.description = course_json.get('description')
            course.duration = course_json.get('duration')
            course.starting_date = starting_date
            course.ending_date = ending_date
            course.user_id = course_json.get('user_id')
            course.display_picture = course_json.get('display_picture')
            course.requirements = course_json.get('requirements')
            course.what_you_will_learn = course_json.get('what_you_will_learn')
            course.curriculum = course_json.get('curriculum')
            course.target_audience = course_json.get('target_audience')

            course.save()

            response = {
                "result": "ok",
                "pet": course_obj(course)
            }
            return jsonify(response), 200

    def delete(self, course_id):
        course = Course.objects.filter(
            external_id=course_id, is_live=True).first()

        if not course:
            return jsonify({}), 404

        course.is_live = False
        course.save()

        return jsonify({}), 204
