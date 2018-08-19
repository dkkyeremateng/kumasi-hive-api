from flask import Blueprint

from website.api.category.api import CategoryAPI

category = Blueprint('category', __name__, url_prefix='/api')

category_view = CategoryAPI.as_view('course_api')

category.add_url_rule('/categories/',
                      view_func=category_view,
                      defaults={'category_id': None}
                      methods=['GET'])

category.add_url_rule('/categories/',
                      view_func=category_view,
                      methods=['POST'])

category.add_url_rule('/categories/<category_id>',
                      view_func=category_view,
                      methods=['GET', 'PUT', 'DELETE'])
