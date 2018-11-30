from flask_restful import reqparse, Resource

from app.api.v1.models.models import IncidenceModel

parser = reqparse.RequestParser()
parser.add_argument('type', type=str, required=True, help='Type cannot be blank!')
parser.add_argument('location', type=str, required=True, help='Location cannot be blank!')
parser.add_argument('comment', type=str, required=True, help='Comment cannot be blank!')

class RedFlagList(Resource):
    """Allows a request on a list of RedFlag items"""
    def post(self):
        data = parser.parse_args()

        red_flag = IncidenceModel(
                createdBy = 1,
                _type = data['type'],
                comment = data['comment'],
                location = data['location']
            )

        IncidenceModel.insert_an_incidence(red_flag.incidence_as_dict())

        return {
            "status": 201,
            "data": [
                {
                    "id": red_flag.get_id(),
                    "message": "Create red-flag record"
                }
            ]
        }, 201
