from cloudant_service import CloudantService
from connection_config import connection_credentials
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
cloudant = CloudantService(**connection_credentials)


class HomeAPI(Resource):
    def get(self):
        return "Hello Airport"


class AirportAPI(Resource):
    def get(self):
        arguments = request.args.to_dict()
        dd = cloudant.get_airport_data(**arguments)
        data = {'result':dd}
        return jsonify(data)


api.add_resource(HomeAPI, '/')
api.add_resource(AirportAPI, '/airport/')

if __name__ == '__main__':
    app.run(debug=True)

