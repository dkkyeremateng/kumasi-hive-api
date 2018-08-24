from flask import request, abort, jsonify
from flask.views import MethodView
from jsonschema import Draft4Validator
from jsonschema.exceptions import best_match
import uuid

from website.api.student.models import Student
from website.api.student.schema import student_schema
from website.api.student.templates import student_obj, students_objs


class StudentAPI(MethodView):

    def __init__(self):
        if (request.method != 'GET' and
                request.method != 'OPTIONS' and
                request.method != 'DELETE') and not request.json:
            abort(400)

    def get(self, external_id):

        if external_id:

            student = Student.find_by_external_id(external_id)

            if student:
                response = {
                    'result': 'ok',
                    'students': student_obj(student)
                }
                return jsonify(response), 200
            else:
                return jsonify({}), 404
        else:
            students = Student.find_by_status()

            response = {
                'result': 'ok',
                'students': students_objs(students)
            }
            return jsonify(response), 200

    def post(self):

        student_json = request.json

        error = best_match(Draft4Validator(
            student_schema).iter_errors(student_json))

        if error:
            return jsonify({"error": error.message}), 400
        else:
            hashed_password = Student.encrypt_password(student_json.get('password'))
            external_id = str(uuid.uuid4())

            params = {
                'email': student_json.get('email'),
                'first_name': student_json.get('first_name'),
                'last_name': student_json.get('last_name'),
                'display_pic': student_json.get('display_pic'),
                'interests': student_json.get('interests'),
                'gender': student_json.get('gender'),
                'telephone': student_json.get('telephone'),
                'password': hashed_password,
                'external_id': external_id,
            }

            if Student.objects.filter(email=params['email']).first():
                return jsonify({'error': "Email is already in use"}), 400

            student = Student(**params).save()

            response = {
                'result': 'ok',
                'student': student_obj(student)
            }
            return jsonify(response), 200

    def put(self, external_id):
        student = Student.find_by_external_id(external_id)

        student_json = request.json

        if not student:
            return jsonify({}), 404

        student.first_name = student_json.get('first_name')
        student.last_name = student_json.get('last_name')
        student.gender = student_json.get('gender')
        student.display_pic = student_json.get('display_pic')
        student.telephone = student_json.get('telephone')

        student.save()

    def delete(self, external_id):
        student = Student.find_by_external_id(external_id)

        if not student:
            return jsonify({}), 404

        student.is_active = False
        student.save()

        return jsonify({}), 204
