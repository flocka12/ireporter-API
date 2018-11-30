from flask import Blueprint
from flask_restful import Api
from app.api.v1.views import *

api_blueprint = Blueprint("api", __name__)

api = Api(api_blueprint)

api.add_resource(RedFlagList, '/red-flags')