from flask import request, abort, jsonify
from flask.views import MethodView
from jsonschema import Draft4Validator
from jsonschema.exceptions import best_match
import uuid

from website.api.instructor.models import Instructor
from website.api.instructor.schema import instructor_schema
from website.api.instructor.templates import instructor_obj, instructors_objs


class InstructorAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET' and
                request.method != 'OPTIONS' and
                request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self, external_id):

        if external_id:

            instructor = Instructor.find_by_external_id(external_id)

            if instructor:
                response = {
                    'result': 'ok',
                    'instructors': instructor_obj(instructor)
                }
                return jsonify(response), 200
            else:
                return jsonify({}), 404
        else:
            instructors = Instructor.find_by_status()

            response = {
                'result': 'ok',
                'instructors': instructors_objs(instructors)
            }
            return jsonify(response), 200

    def post(self):

        instructor_json = request.json

        error = best_match(Draft4Validator(
            instructor_schema).iter_errors(instructor_json))

        if error:
            return jsonify({"error": error.message}), 400
        else:
            hashed_password = Instructor.encrypt_password(instructor_json.get('password'))
            external_id = str(uuid.uuid4())

            params = {
                'email': instructor_json.get('email'),
                'first_name': instructor_json.get('first_name'),
                'last_name': instructor_json.get('last_name'),
                'display_pic': instructor_json.get('display_pic'),
                'interests': instructor_json.get('interests'),
                'gender': instructor_json.get('gender'),
                'telephone': instructor_json.get('telephone'),
                'password': hashed_password,
                'external_id': external_id,
            }

            if Instructor.objects.filter(email=params['email']).first():
                return jsonify({'error': "Email is already in use"}), 400

            instructor = Instructor(**params).save()

            response = {
                'result': 'ok',
                'instructor': instructor_obj(instructor)
            }
            return jsonify(response), 200

    def put(self, external_id):
        instructor = Instructor.find_by_external_id(external_id)

        instructor_json = request.json

        if not instructor:
            return jsonify({}), 404

        instructor.first_name = instructor_json.get('first_name')
        instructor.last_name = instructor_json.get('last_name')
        instructor.gender = instructor_json.get('gender')
        instructor.display_pic = instructor_json.get('display_pic')
        instructor.telephone = instructor_json.get('telephone')

        instructor.save()

    def delete(self, external_id):
        instructor = Instructor.find_by_external_id(external_id)

        if not instructor:
            return jsonify({}), 404

        instructor.is_active = False
        instructor.save()

        return jsonify({}), 204
