from flask import Blueprint
from flask_restful import Api

from core.view.message import Messages
from core.view.users import Users

api_bp = Blueprint('api', __name__)

api = Api(api_bp)
#api.add_resource(, '/todos/<int:id>')

api.add_resource(Messages, "/messages")
api.add_resource(Users, "/users")
