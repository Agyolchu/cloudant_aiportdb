from cloudant_service import CloudantService
from connection_config import connection_credentials
from airport_data_processor import AirportDataProcessor
from upper_bounds_finder import UpperBoundsFinder
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
        arguments = {k: float(v) for k, v in arguments.items()}
        upper_bounds = UpperBoundsFinder(arguments)
        maximum_distance_cordinates = upper_bounds.generate_border_cordinates()
        airport_data = cloudant.get_airport_data(maximum_distance_cordinates, arguments)
        airport_processor_details = AirportDataProcessor(airport_data, arguments)
        output_data = airport_processor_details.distance_processor()
        data = {'result': output_data}
        return jsonify(data)


api.add_resource(HomeAPI, '/')
api.add_resource(AirportAPI, '/airport/')

if __name__ == '__main__':
    app.run(debug=True)
