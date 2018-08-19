from flask_script import Manager
from flask_mongoengine import MongoEngine
from flask_cors import CORS

manager = Manager()
db = MongoEngine()
cors = CORS()
